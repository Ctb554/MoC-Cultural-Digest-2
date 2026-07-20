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

Format checked here is the one confirmed against a real delivered edition
(2026-07-19), NOT either of the two original written specs -- see SKILL.md's
"FORMAT CONFIRMED AGAINST REAL PRODUCTION" note for what changed and why.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path

# --- Structure constants (must match SKILL.md exactly) ----------------------

REQUIRED_SECTIONS = ["Saudi Arabia/Regional", "Negative Articles", "Global"]

# Sections that use commission subheadings in the full-summary block.
# Negative Articles deliberately has none, per confirmed real production.
SECTIONS_WITH_SUBHEADINGS = {"Saudi Arabia/Regional", "Global"}

# Approved bilingual commission labels: English -> Arabic, confirmed against
# real production. A label must match one of these pairs exactly.
APPROVED_COMMISSIONS = {
    "General": "عام",
    "Heritage": "التراث",
    "Museums": "المتاحف",
    "Visual Arts": "الفنون البصرية",
    "Film": "الأفلام",
    "Fashion": "الأزياء",
    "Music": "الموسيقى",
    "Theatre and Performing Arts": "المسرح والفنون الأدائية",
    "Literature, Publishing, and Translation": "الأدب والنشر والترجمة",
    "Libraries": "المكتبات",
    "Culinary Arts": "فنون الطهي",
    "Architecture and Design": "فنون العمارة والتصميم",
}
# Build the exact "English (Arabic)" strings expected in the markdown
APPROVED_LABEL_STRINGS = {
    f"{en} ({ar})" for en, ar in APPROVED_COMMISSIONS.items()
}

# Domains excluded per the source-eligibility rule (Saudi-owned outlets)
EXCLUDED_DOMAINS = [
    "arabnews.com", "saudigazette.com.sa", "spa.gov.sa", "aleqt.com",
    "okaz.com.sa", "sabq.org", "argaam.com", "asharq.com", "aawsat.com",
]
ALLOWED_OVERRIDE_DOMAINS = [
    "alarabiya.net", "thenationalnews.com", "campaignme.com",
]

BANNED_PHRASES = [
    "groundbreaking", "world-leading", "landmark", "unprecedented",
    "unusually broad pickup",
]

AMERICAN_SPELLING_WARNINGS = [
    r"\bcolor\b", r"\bfavorite\b", r"\bcenter\b", r"\btheater\b",
    r"\bdefense\b", r"\boffense\b", r"\btraveled\b", r"\bcanceled\b",
    r"\bfueled\b", r"\bgray\b", r"\banalyze\b",
]

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://\S+")
ARABIC_RE = re.compile(r"[\u0600-\u06FF]")
NUMBERED_ITEM_RE = re.compile(r"^\s*(\d+)\.\s*(.*)$")


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
    """Returns {h2_name: [bullet_text, ...]} for one H1 block (## subheadings)."""
    result = {}
    current_h2 = None
    for line in h1_lines:
        if line.startswith("## "):
            current_h2 = line[3:].strip()
            result.setdefault(current_h2, [])
        elif line.strip().startswith("- ") and current_h2:
            result[current_h2].append(line.strip()[2:].strip())
    return result


def get_direct_bullets(h1_lines):
    """Returns bullets sitting directly under an H1, with no ## subheading."""
    return [
        line.strip()[2:].strip()
        for line in h1_lines
        if line.strip().startswith("- ")
    ]


def check_required_blocks(blocks, result):
    h1_names = [name for name, _ in blocks]

    headline_block_names = [n for n in h1_names if n.startswith("Headlines,")]
    if not headline_block_names:
        result.fail("No 'Headlines, <date>' block found")
    elif len(headline_block_names) > 1:
        result.warn(f"Multiple 'Headlines,' blocks found: {headline_block_names}")

    for section in REQUIRED_SECTIONS:
        if section not in h1_names:
            result.fail(f"Required full-summary section missing: '{section}'")

    if "Risks and Opportunities" not in h1_names:
        result.fail("'Risks and Opportunities' section missing")


def check_headline_block_ordering(blocks, result):
    """
    Headline block must appear BEFORE the full-summary sections, per
    confirmed real production (not after, as the handoff note assumed).
    """
    h1_names = [name for name, _ in blocks]
    headline_idx = next(
        (i for i, n in enumerate(h1_names) if n.startswith("Headlines,")), None
    )
    if headline_idx is None:
        return  # already flagged as a hard failure elsewhere

    for section in REQUIRED_SECTIONS:
        if section in h1_names:
            section_idx = h1_names.index(section)
            if section_idx < headline_idx:
                result.fail(
                    f"Full-summary section '{section}' appears before the "
                    f"headline-bullet block -- headline bullets must come first"
                )


def check_commission_labels(blocks, result):
    for h1_name, h1_lines in blocks:
        if h1_name not in SECTIONS_WITH_SUBHEADINGS:
            continue
        h2_names = [line[3:].strip() for line in h1_lines if line.startswith("## ")]
        for h2 in h2_names:
            if h2 not in APPROVED_LABEL_STRINGS:
                result.fail(
                    f"Invalid/invented or non-bilingual commission label "
                    f"'{h2}' under section '{h1_name}' -- must be an approved "
                    f"'English (Arabic)' pair"
                )


def check_negative_articles_no_subheadings(blocks, result):
    for h1_name, h1_lines in blocks:
        if h1_name != "Negative Articles":
            continue
        h2_count = sum(1 for line in h1_lines if line.startswith("## "))
        if h2_count > 0:
            result.fail(
                f"'Negative Articles' full-summary section has {h2_count} "
                f"commission subheading(s) -- this section must have none, "
                f"per confirmed real production"
            )


def check_links_and_sources(blocks, result, register_urls):
    for h1_name, h1_lines in blocks:
        if h1_name not in REQUIRED_SECTIONS:
            continue

        if h1_name in SECTIONS_WITH_SUBHEADINGS:
            bullets_by_label = get_h2_bullets(h1_lines)
        else:
            bullets_by_label = {"(no subheading)": get_direct_bullets(h1_lines)}

        for label, bullets in bullets_by_label.items():
            for bullet in bullets:
                links = MD_LINK_RE.findall(bullet)
                if not links:
                    result.fail(
                        f"[{h1_name} / {label}] Bullet has no link at all: "
                        f"'{bullet[:80]}...'"
                    )
                    continue

                last_link = links[-1]
                last_link_pos = bullet.rfind(f"[{last_link[0]}]({last_link[1]})")
                trailing_text = bullet[
                    last_link_pos + len(f"[{last_link[0]}]({last_link[1]})") :
                ].strip()
                if trailing_text not in ("", ")", "."):
                    result.warn(
                        f"[{h1_name} / {label}] Link may not be the trailing "
                        f"element in bullet: '{bullet[:80]}...'"
                    )

                text_without_md_links = MD_LINK_RE.sub("", bullet)
                if URL_RE.search(text_without_md_links):
                    result.fail(
                        f"[{h1_name} / {label}] Raw URL found outside the "
                        f"outlet-name link: '{bullet[:80]}...'"
                    )

                for _, url in links:
                    url_lower = url.lower()
                    if any(allowed in url_lower for allowed in ALLOWED_OVERRIDE_DOMAINS):
                        continue
                    if any(excluded in url_lower for excluded in EXCLUDED_DOMAINS):
                        result.fail(
                            f"[{h1_name} / {label}] Excluded (Saudi-owned) "
                            f"outlet used: {url}"
                        )

                for _, url in links:
                    if url in register_urls:
                        result.fail(
                            f"[{h1_name} / {label}] Reused link from a prior "
                            f"edition's do-not-reuse register: {url}"
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


def check_arabic_only_in_labels(md_text, blocks, result):
    """
    Arabic is allowed ONLY inside the approved bilingual commission label
    strings. Any Arabic text elsewhere in the document body is a failure.
    """
    text_without_labels = md_text
    for label in APPROVED_LABEL_STRINGS:
        text_without_labels = text_without_labels.replace(label, "")

    if ARABIC_RE.search(text_without_labels):
        result.fail(
            "Arabic characters found outside the approved bilingual "
            "commission labels -- Arabic is only allowed inside "
            "'English (Arabic)' subheadings"
        )


def check_risks_and_opportunities(blocks, result):
    ro_block = None
    for name, lines in blocks:
        if name == "Risks and Opportunities":
            ro_block = lines
            break
    if ro_block is None:
        return  # already flagged as a hard failure

    h2_sections = {}
    current_h2 = None
    current_lines = []
    for line in ro_block:
        if line.startswith("## "):
            if current_h2:
                h2_sections[current_h2] = current_lines
            current_h2 = line[3:].strip()
            current_lines = []
        else:
            current_lines.append(line)
    if current_h2:
        h2_sections[current_h2] = current_lines

    for expected in ["Risks", "Opportunities"]:
        if expected not in h2_sections:
            result.fail(f"'Risks and Opportunities' missing the '{expected}' subsection")
            continue

        body_lines = h2_sections[expected]
        item_starts = [
            i for i, line in enumerate(body_lines)
            if NUMBERED_ITEM_RE.match(line.strip())
        ]
        if not item_starts:
            result.fail(f"'{expected}' subsection has no numbered item")
            continue

        # Check each item individually has a headline, Source, and Consideration
        for idx, start in enumerate(item_starts):
            end = item_starts[idx + 1] if idx + 1 < len(item_starts) else len(body_lines)
            item_text = "\n".join(body_lines[start:end])
            item_number = NUMBERED_ITEM_RE.match(body_lines[start].strip()).group(1)

            if "Source:" not in item_text:
                result.fail(
                    f"'{expected}' item {item_number} missing a 'Source:' line"
                )
            if "Consideration:" not in item_text:
                result.fail(
                    f"'{expected}' item {item_number} missing a "
                    f"'Consideration:' line"
                )

        # Numbering should restart at 1 for each subsection
        first_number = NUMBERED_ITEM_RE.match(body_lines[item_starts[0]].strip()).group(1)
        if first_number != "1":
            result.warn(
                f"'{expected}' subsection's first item is numbered "
                f"{first_number}, expected to restart at 1"
            )


def load_register_urls(register_path):
    if not register_path or not Path(register_path).exists():
        return set()
    text = Path(register_path).read_text(encoding="utf-8")
    return set(URL_RE.findall(text))


def check_docx_parity(docx_path, result):
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

    check_required_blocks(blocks, result)
    check_headline_block_ordering(blocks, result)
    check_commission_labels(blocks, result)
    check_negative_articles_no_subheadings(blocks, result)
    check_links_and_sources(blocks, result, register_urls)
    check_risks_and_opportunities(blocks, result)
    check_banned_phrases(md_text, result)
    check_american_spellings(md_text, result)
    check_arabic_only_in_labels(md_text, blocks, result)
    check_docx_parity(docx_path, result)

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
# GitHub App write-access test
