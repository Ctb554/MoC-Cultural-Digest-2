#!/usr/bin/env python3
"""
Deterministic Stage 5 audit for the MoC Daily Cultural Digest.

This is the committed implementation of the cultural-digest skill's Stage 5
programmatic audit. It is an INDEPENDENT gate: the routine runs it against
the canonical markdown (and, if given, the built .docx for a parity spot
check) after generation, and fails the run on any hard failure, so a
clean-but-wrong digest can never ship green.

Usage:
    python3 scripts/audit_report.py reports/MoC_Digest_2026-07-19.md \\
        --docx reports/MoC_Digest_2026-07-19.docx \\
        --register reports/do_not_reuse_register.md

Exit code 0 = all hard checks pass (warnings may still be printed).
Exit code 1 = at least one hard check failed; the digest must not be delivered.

Design notes:
- The canonical markdown is the primary audit target, since it's the
  structured source of truth the build script renders from. The --docx flag
  adds a lightweight text-parity spot check (headings present in both), not
  a full re-audit of the docx, since the markdown already IS what generated it.
- This mirrors the conflict-monitoring skill's audit_report.py in spirit,
  adapted for this digest's rules: source exclusion (Saudi-owned outlets
  banned, UAE-based allowed), link-only-in-outlet-name, GB English, no
  invented commission labels, and the numbered one-paragraph Risks/
  Opportunities structure.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

# --- Structure constants (must match SKILL.md exactly) ----------------------

REQUIRED_SECTIONS = ["Saudi Arabia/Regional", "Negative Articles", "Global"]

APPROVED_COMMISSIONS = {
    "General", "Heritage", "Museums", "Visual Arts", "Film", "Fashion",
    "Music", "Theatre and Performing Arts", "Literature, Publishing, and Translation",
    "Literature, Publishing and Translation",  # tolerate missing Oxford comma
    "Libraries", "Culinary Arts", "Architecture and Design",
}

# Domains excluded per the source-eligibility rule (Saudi-owned outlets)
EXCLUDED_DOMAINS = [
    "arabnews.com", "saudigazette.com.sa", "spa.gov.sa", "aleqt.com",
    "okaz.com.sa", "sabq.org", "argaam.com", "asharq.com", "aawsat.com",
]
# Explicit brief overrides -- allowed even though regionally adjacent
ALLOWED_OVERRIDE_DOMAINS = [
    "alarabiya.net", "thenationalnews.com", "campaignme.com",
]

BANNED_PHRASES = [
    "groundbreaking", "world-leading", "landmark", "unprecedented",
    "unusually broad pickup",
]

# Unambiguous Americanisms -- flagged as warnings (not hard fails, to avoid
# false positives on genuinely ambiguous forms like -ize/-ise, which are
# valid in both Oxford British and American spelling).
AMERICAN_SPELLING_WARNINGS = [
    r"\bcolor\b", r"\bfavorite\b", r"\bcenter\b", r"\btheater\b",
    r"\bdefense\b", r"\boffense\b", r"\btraveled\b", r"\bcanceled\b",
    r"\bfueled\b", r"\bgray\b", r"\banalyze\b",
]

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://\S+")
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")


class AuditResult:
    def __init__(self):
        self.hard_failures = []
        self.warnings = []

    def fail(self, msg):
        self.hard_failures.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def ok(self):
        return not self.hard_failures


def split_h1_blocks(md_text):
    """Splits markdown into (h1_name, h1_body_lines) blocks, in order."""
    blocks = []
    current_name = None
    current_lines = []
    for line in md_text.split("\n"):
        if line.startswith("# ") and not line.startswith("## "):
            if current_name is not None:
                blocks.append((current_name, current_lines))
            current_name = line[2:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_name is not None:
        blocks.append((current_name, current_lines))
    return blocks


def get_h2_bullets(h1_lines):
    """Returns {h2_name: [bullet_text, ...]} for one H1 block."""
    result = {}
    current_h2 = None
    for line in h1_lines:
        if line.startswith("## "):
            current_h2 = line[3:].strip()
            result.setdefault(current_h2, [])
        elif line.strip().startswith("- ") and current_h2:
            result[current_h2].append(line.strip()[2:].strip())
    return result


def check_required_sections(blocks, result):
    """Check both the headline-bullet block and full-summary blocks exist."""
    h1_names = [name for name, _ in blocks]

    headline_block_names = [n for n in h1_names if n.startswith("Headlines,")]
    if not headline_block_names:
        result.fail("No 'Headlines, <date>' block found")
    elif len(headline_block_names) > 1:
        result.warn(f"Multiple 'Headlines,' blocks found: {headline_block_names}")

    for section in REQUIRED_SECTIONS:
        occurrences = [i for i, n in enumerate(h1_names) if n == section]
        if not occurrences:
            result.fail(f"Required section missing entirely: '{section}'")
        elif len(occurrences) < 1:
            result.fail(f"Required full-summary section missing: '{section}'")

    if "Risks and Opportunities" not in h1_names:
        result.fail("'Risks and Opportunities' section missing")


def check_section_order(blocks, result):
    """Sections should appear in the fixed order after the headline block."""
    h1_names = [name for name in [b[0] for b in blocks] if name in REQUIRED_SECTIONS]
    if h1_names != REQUIRED_SECTIONS[: len(h1_names)] and set(h1_names) == set(REQUIRED_SECTIONS):
        result.warn(f"Sections present but not in expected order: {h1_names}")


def check_commission_labels(blocks, result):
    for h1_name, h1_lines in blocks:
        if h1_name not in REQUIRED_SECTIONS:
            continue
        h2_names = [line[3:].strip() for line in h1_lines if line.startswith("## ")]
        for h2 in h2_names:
            if h2 not in APPROVED_COMMISSIONS:
                result.fail(
                    f"Invalid/invented commission label '{h2}' under section '{h1_name}' "
                    f"-- not in the approved list"
                )


def check_links_and_sources(blocks, result, register_urls):
    for h1_name, h1_lines in blocks:
        if h1_name not in REQUIRED_SECTIONS:
            continue
        bullets_by_h2 = get_h2_bullets(h1_lines)
        for h2, bullets in bullets_by_h2.items():
            for bullet in bullets:
                links = MD_LINK_RE.findall(bullet)
                if not links:
                    result.fail(
                        f"[{h1_name} / {h2}] Bullet has no link at all: "
                        f"'{bullet[:80]}...'"
                    )
                    continue

                # Link-only-in-outlet-name rule: the markdown link should be
                # the LAST thing in the bullet (the trailing "(Outlet)").
                last_link = links[-1]
                last_link_pos = bullet.rfind(f"[{last_link[0]}]({last_link[1]})")
                trailing_text = bullet[last_link_pos + len(f"[{last_link[0]}]({last_link[1]})"):].strip()
                if trailing_text not in ("", ")", "."):
                    result.warn(
                        f"[{h1_name} / {h2}] Link may not be the trailing element "
                        f"in bullet: '{bullet[:80]}...'"
                    )

                # No raw/bare URLs outside the markdown link syntax
                text_without_md_links = MD_LINK_RE.sub("", bullet)
                if URL_RE.search(text_without_md_links):
                    result.fail(
                        f"[{h1_name} / {h2}] Raw URL found outside the outlet-name "
                        f"link: '{bullet[:80]}...'"
                    )

                # Source-exclusion check on every link URL in the bullet
                for _, url in links:
                    url_lower = url.lower()
                    if any(allowed in url_lower for allowed in ALLOWED_OVERRIDE_DOMAINS):
                        continue
                    if any(excluded in url_lower for excluded in EXCLUDED_DOMAINS):
                        result.fail(
                            f"[{h1_name} / {h2}] Excluded (Saudi-owned) outlet used: "
                            f"{url}"
                        )

                # Do-not-reuse register check
                for _, url in links:
                    if url in register_urls:
                        result.fail(
                            f"[{h1_name} / {h2}] Reused link from a prior edition's "
                            f"do-not-reuse register: {url}"
                        )


def check_banned_phrases(md_text, result):
    text_lower = md_text.lower()
    for phrase in BANNED_PHRASES:
        if phrase in text_lower:
            result.fail(f"Banned inflated phrase found: '{phrase}'")


def check_american_spellings(md_text, result):
    for pattern in AMERICAN_SPELLING_WARNINGS:
        matches = re.findall(pattern, md_text, re.IGNORECASE)
        if matches:
            result.warn(
                f"Possible American spelling found ({len(matches)}x): "
                f"pattern '{pattern}' -- digest should be GB English"
            )


def check_no_arabic(md_text, result):
    if ARABIC_RE.search(md_text):
        result.fail("Arabic characters found in the produced digest -- output must be English only")


def check_risks_and_opportunities(blocks, result):
    ro_block = None
    for name, lines in blocks:
        if name == "Risks and Opportunities":
            ro_block = lines
            break
    if ro_block is None:
        return  # already flagged as a hard failure in check_required_sections

    text = "\n".join(ro_block)
    h2_sections = {}
    current_h2 = None
    current_lines = []
    for line in ro_block:
        if line.startswith("## "):
            if current_h2:
                h2_sections[current_h2] = "\n".join(current_lines)
            current_h2 = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_h2:
        h2_sections[current_h2] = "\n".join(current_lines)

    for expected, number in [("Risks", "1."), ("Opportunities", "2.")]:
        if expected not in h2_sections:
            result.fail(f"'Risks and Opportunities' missing the '{expected}' subsection")
            continue
        body = h2_sections[expected]
        numbered_paragraphs = re.findall(r"^\s*\d+\.\s", body, re.MULTILINE)
        if len(numbered_paragraphs) == 0:
            result.fail(f"'{expected}' subsection has no numbered paragraph")
        elif len(numbered_paragraphs) > 1:
            result.fail(
                f"'{expected}' subsection has {len(numbered_paragraphs)} numbered "
                f"paragraphs -- spec requires exactly one"
            )
        if "Source:" not in body:
            result.fail(f"'{expected}' subsection missing a 'Source:' line")
        if "Consideration:" not in body:
            result.fail(f"'{expected}' subsection missing a 'Consideration:' line")


def check_headline_bullets_present(blocks, result):
    headline_block = None
    for name, lines in blocks:
        if name.startswith("Headlines,"):
            headline_block = lines
            break
    if headline_block is None:
        return  # already a hard failure

    headline_bullets = get_h2_bullets(headline_block)
    for section in REQUIRED_SECTIONS:
        if section not in headline_bullets:
            result.fail(f"Headline-bullet block missing '{section}' subsection")
        elif not headline_bullets[section]:
            result.warn(f"Headline-bullet block has an empty '{section}' subsection")

        # Cross-check count against the full-summary section's article count
        full_section = None
        for name, lines in blocks:
            if name == section:
                full_section = get_h2_bullets(lines)
                break
        if full_section is not None:
            full_count = sum(len(v) for v in full_section.values())
            headline_count = len(headline_bullets.get(section, []))
            if full_count != headline_count:
                result.warn(
                    f"'{section}': {headline_count} headline bullets but "
                    f"{full_count} full-summary articles -- counts should match"
                )

        # Headline bullets must contain no links at all (no raw URLs, no md links)
        for bullet in headline_bullets.get(section, []):
            if URL_RE.search(bullet) or MD_LINK_RE.search(bullet):
                result.fail(
                    f"Headline bullet contains a link (should be plain headline "
                    f"text only): '{bullet[:80]}...'"
                )


def load_register_urls(register_path):
    if not register_path or not Path(register_path).exists():
        return set()
    text = Path(register_path).read_text(encoding="utf-8")
    return set(url for url in URL_RE.findall(text))


def check_docx_parity(md_text, docx_path, result):
    """Lightweight spot check: key headings from the markdown also appear as
    text somewhere in the built docx. Not a full re-audit -- the markdown IS
    the source of truth the docx was built from."""
    if not docx_path or not Path(docx_path).exists():
        return

    try:
        with zipfile.ZipFile(docx_path) as z:
            xml = z.read("word/document.xml").decode("utf-8", errors="ignore")
    except (KeyError, zipfile.BadZipFile) as exc:
        result.fail(f"Could not read built .docx for parity check: {exc}")
        return

    docx_text = re.sub(r"<[^>]+>", "", xml)

    for section in REQUIRED_SECTIONS + ["Risks and Opportunities"]:
        if section not in docx_text:
            result.fail(f"Section heading '{section}' missing from built .docx text")


def run_audit(md_path, docx_path, register_path):
    result = AuditResult()
    md_text = Path(md_path).read_text(encoding="utf-8")
    blocks = split_h1_blocks(md_text)
    register_urls = load_register_urls(register_path)

    check_required_sections(blocks, result)
    check_section_order(blocks, result)
    check_commission_labels(blocks, result)
    check_links_and_sources(blocks, result, register_urls)
    check_headline_bullets_present(blocks, result)
    check_risks_and_opportunities(blocks, result)
    check_banned_phrases(md_text, result)
    check_american_spellings(md_text, result)
    check_no_arabic(md_text, result)
    check_docx_parity(md_text, docx_path, result)

    return result


def main():
    parser = argparse.ArgumentParser(description="Stage 5 audit for the MoC Daily Cultural Digest")
    parser.add_argument("markdown_path", help="Path to the canonical markdown digest")
    parser.add_argument("--docx", default=None, help="Path to the built .docx (optional parity check)")
    parser.add_argument("--register", default="reports/do_not_reuse_register.md",
                         help="Path to the do-not-reuse register")
    args = parser.parse_args()

    result = run_audit(args.markdown_path, args.docx, args.register)

    print("=== MoC Digest Audit ===")
    if result.warnings:
        print(f"\n{len(result.warnings)} WARNING(S):")
        for w in result.warnings:
            print(f"  [WARN] {w}")

    if result.hard_failures:
        print(f"\n{len(result.hard_failures)} HARD FAILURE(S):")
        for f in result.hard_failures:
            print(f"  [FAIL] {f}")
        print("\nRESULT: FAIL -- do not deliver this digest.")
        sys.exit(1)
    else:
        print("\nRESULT: PASS -- all hard checks passed.")
        sys.exit(0)


if __name__ == "__main__":
    main()
