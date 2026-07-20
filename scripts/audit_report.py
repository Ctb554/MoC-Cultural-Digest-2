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
import json
import re
import socket
import sys
import time
import urllib.error
import urllib.request
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

# --- URL resolution (item 1: dead/fabricated links must hard-fail) ----------
#
# A bot wall or rate limit on the LIVE site still proves the URL exists; only
# a genuinely dead link (404, DNS/connection failure, timeout) means the link
# is fabricated or stale. 401/403/429 are treated as "exists" for this reason
# -- the same "bot wall is normal, not a policy problem" principle SKILL.md's
# Stage 0 capability check already applies to WebFetch.
SOFT_BLOCK_STATUSES = {401, 403, 429}
URL_CHECK_USER_AGENT = "Mozilla/5.0 (compatible; MoC-Digest-Audit/1.0)"
DEFAULT_URL_TIMEOUT = 10
DEFAULT_URL_DELAY = 0.5  # seconds between checks -- polite rate limiting

# --- Fixture safety (item 2: a confused run must never ship test content) --
#
# tests/*.md live inside the cloned repo and use placeholder "/example" URLs
# and generic headlines. Without a defensive check, a confused run that
# accidentally builds a digest FROM a fixture (or copies its content) would
# pass every other check -- the fixture is deliberately well-formed. This
# marker must appear in every fixture under tests/ and nowhere else; its
# presence in a digest being audited is always a hard failure.
DO_NOT_SHIP_MARKER = "DO-NOT-SHIP: FIXTURE CONTENT -- NEVER DELIVER THIS DIGEST"
FIXTURE_FILENAMES = ["sample_test_digest.md", "sample_broken_digest.md"]


class AuditResult:
    def __init__(self):
        self.hard_failures = []
        self.warnings = []
        # Populated by check_minimum_coverage: {section: {"count": int,
        # "minimum_required": int, "met": bool, "rung": str}}. Exposed here
        # (rather than only as pass/fail messages) so a run-status writer can
        # report "which ladder rungs were used" without re-deriving it.
        self.coverage_ladder = {}

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


def _count_section_bullets(h1_name, h1_lines):
    if h1_name in SECTIONS_WITH_SUBHEADINGS:
        return sum(len(bullets) for bullets in get_h2_bullets(h1_lines).values())
    return len(get_direct_bullets(h1_lines))


def load_search_log(search_log_path):
    """
    Returns the parsed reports/search_log.json dict, or None if it's
    missing/unreadable/invalid JSON. None is treated as "no evidence" by
    check_minimum_coverage -- fail-closed, not fail-open: an empty Negative
    Articles section is only excused when the log positively confirms the
    negative/watchdog searches were run.
    """
    if not search_log_path:
        return None
    path = Path(search_log_path)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def check_minimum_coverage(blocks, result, search_log_path=None):
    """
    Minimum-coverage ladder (item 3 of the hardening pass):
      - Saudi Arabia/Regional and Global must have at least one article --
        hard-fail if empty, no exceptions.
      - Negative Articles may legitimately be empty (a culture digest should
        never manufacture criticism of the client to fill a quota), but ONLY
        if reports/search_log.json confirms the negative/watchdog searches
        were actually run this cycle. Absence of that evidence is a hard
        failure, not a free pass -- fail-closed by design.
    """
    bullet_counts = {}
    for h1_name, h1_lines in blocks:
        if h1_name in REQUIRED_SECTIONS:
            bullet_counts[h1_name] = _count_section_bullets(h1_name, h1_lines)

    for section in ["Saudi Arabia/Regional", "Global"]:
        count = bullet_counts.get(section, 0)
        met = count >= 1
        result.coverage_ladder[section] = {
            "count": count, "minimum_required": 1, "met": met,
            "rung": "has-content" if met else "empty-FAIL",
        }
        if not met:
            result.fail(
                f"'{section}' has zero articles -- minimum coverage requires "
                f"at least one; a short section is fine, an empty one is not "
                f"(unlike Negative Articles, this section has no legitimate-"
                f"empty exception)"
            )

    negative_count = bullet_counts.get("Negative Articles", 0)
    if negative_count >= 1:
        result.coverage_ladder["Negative Articles"] = {
            "count": negative_count, "minimum_required": 0, "met": True,
            "rung": "has-content",
        }
    else:
        search_log = load_search_log(search_log_path)
        searches_confirmed_run = bool(search_log and search_log.get("negative_searches_run") is True)
        result.coverage_ladder["Negative Articles"] = {
            "count": 0, "minimum_required": 0, "met": searches_confirmed_run,
            "rung": "empty-justified" if searches_confirmed_run else "empty-unjustified-FAIL",
        }
        if searches_confirmed_run:
            result.warn(
                "'Negative Articles' is empty; justified by "
                f"{search_log_path} confirming the negative/watchdog "
                f"searches were run and returned nothing in-window -- this "
                f"is a legitimate outcome, not a sourcing failure"
            )
        else:
            result.fail(
                "'Negative Articles' is empty but no search-log evidence "
                f"(expected at {search_log_path}) confirms the negative/"
                f"watchdog searches were actually run this cycle -- an "
                f"empty section is only excused with that evidence; "
                f"otherwise this looks like a skipped search, not a quiet "
                f"news day"
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


def collect_all_urls(blocks):
    """
    Returns {url: [context_str, ...]} for every article link (in the three
    required sections) and every Risks/Opportunities Source-line link in the
    digest. Used by check_url_resolution so every citation the digest makes
    -- not just article bullets -- gets checked.
    """
    urls = {}

    def add(url, context):
        urls.setdefault(url, []).append(context)

    for h1_name, h1_lines in blocks:
        if h1_name in REQUIRED_SECTIONS:
            if h1_name in SECTIONS_WITH_SUBHEADINGS:
                bullets_by_label = get_h2_bullets(h1_lines)
            else:
                bullets_by_label = {"(no subheading)": get_direct_bullets(h1_lines)}
            for label, bullets in bullets_by_label.items():
                for bullet in bullets:
                    for _, url in MD_LINK_RE.findall(bullet):
                        add(url, f"{h1_name} / {label}")
        elif h1_name == "Risks and Opportunities":
            current_h2 = None
            for line in h1_lines:
                if line.startswith("## "):
                    current_h2 = line[3:].strip()
                elif line.strip().startswith("Source:"):
                    for _, url in MD_LINK_RE.findall(line):
                        add(url, f"Risks and Opportunities / {current_h2 or '?'}")

    return urls


def _resolve_url_status(url, timeout):
    """
    Returns (ok: bool, detail: str). ok=True covers a live 2xx/3xx response
    AND a bot-wall/rate-limit response (401/403/429) -- both prove the URL
    exists. ok=False covers a real dead link: 404 and other 4xx/5xx, DNS/
    connection failure, or a timeout.

    Tries HEAD first (cheap, no body download); a site that rejects HEAD
    (405) is retried once with a ranged GET.
    """
    headers = {"User-Agent": URL_CHECK_USER_AGENT}
    try:
        req = urllib.request.Request(url, method="HEAD", headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.getcode()
    except urllib.error.HTTPError as exc:
        if exc.code == 405:
            return _resolve_url_status_get(url, timeout)
        code = exc.code
    except urllib.error.URLError as exc:
        return False, f"unreachable ({exc.reason})"
    except (TimeoutError, socket.timeout):
        return False, "timeout"
    except Exception as exc:  # noqa: BLE001 -- any other network failure is a hard fail
        return False, f"error ({exc})"

    if code < 400:
        return True, f"HTTP {code}"
    if code in SOFT_BLOCK_STATUSES:
        return True, f"HTTP {code} (bot wall/rate limit, treated as exists)"
    return False, f"HTTP {code}"


def _resolve_url_status_get(url, timeout):
    """GET fallback for sites that reject HEAD (405). Range header keeps the
    download to a single byte so this stays cheap even for large pages."""
    headers = {"User-Agent": URL_CHECK_USER_AGENT, "Range": "bytes=0-0"}
    try:
        req = urllib.request.Request(url, method="GET", headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.getcode()
    except urllib.error.HTTPError as exc:
        code = exc.code
    except urllib.error.URLError as exc:
        return False, f"unreachable ({exc.reason})"
    except (TimeoutError, socket.timeout):
        return False, "timeout"
    except Exception as exc:  # noqa: BLE001
        return False, f"error ({exc})"

    if code < 400:
        return True, f"HTTP {code}"
    if code in SOFT_BLOCK_STATUSES:
        return True, f"HTTP {code} (bot wall/rate limit, treated as exists)"
    return False, f"HTTP {code}"


def check_url_resolution(blocks, result, skip=False, timeout=DEFAULT_URL_TIMEOUT,
                          delay=DEFAULT_URL_DELAY, resolver=_resolve_url_status):
    """
    Hard-fails on any dead or unreachable link. ON by default -- callers pass
    skip=True (--skip-url-check) only for offline testing. `resolver` is
    injectable so tests can verify the pass/fail logic without real network
    calls; production always uses the default `_resolve_url_status`.
    """
    if skip:
        result.warn("URL-resolution check skipped (--skip-url-check) -- "
                     "links were NOT verified to be live; do not use this "
                     "for a real delivery run")
        return

    urls = collect_all_urls(blocks)
    for i, (url, contexts) in enumerate(sorted(urls.items())):
        if i > 0 and delay:
            time.sleep(delay)
        ok, detail = resolver(url, timeout)
        if not ok:
            ctx = "; ".join(sorted(set(contexts)))
            result.fail(f"Dead or unreachable link ({detail}): {url} [{ctx}]")


def load_fixture_guard_data(tests_dir=None):
    """
    Reads tests/*.md (if present) to build the comparison data
    check_fixture_content_leak needs: each fixture's full text (for an
    exact-content match) and every headline string from its headline-bullet
    block (for a literal-headline match). Missing fixture files degrade
    gracefully -- those specific sub-checks are skipped, not a hard failure,
    since some deployments may not ship tests/ at all.
    """
    if tests_dir is None:
        tests_dir = Path(__file__).resolve().parent.parent / "tests"
    else:
        tests_dir = Path(tests_dir)

    fixture_texts = {}
    fixture_headlines = set()

    for filename in FIXTURE_FILENAMES:
        path = tests_dir / filename
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        fixture_texts[filename] = text
        blocks = split_h1_blocks(text)
        for h1_name, h1_lines in blocks:
            if not h1_name.startswith("Headlines,"):
                continue
            for h2_name, headlines in get_h2_bullets(h1_lines).items():
                fixture_headlines.update(headlines)

    return {"texts": fixture_texts, "headlines": fixture_headlines}


def check_fixture_content_leak(md_text, result, fixture_data=None):
    """
    Defends against a confused run building a real digest from (or matching)
    the test fixtures in tests/, which would otherwise pass every other
    check since the fixtures are deliberately well-formed. Four independent
    tripwires, any one of which is a hard failure on its own:
      (a) any URL containing "/example" (the fixtures' placeholder pattern)
      (b) any exact fixture headline appearing verbatim in the digest
      (c) the digest's content being identical to a known fixture file
      (d) the DO-NOT-SHIP marker appearing anywhere in the digest
    """
    if fixture_data is None:
        fixture_data = load_fixture_guard_data()

    if "/example" in md_text.lower():
        count = md_text.lower().count("/example")
        result.fail(
            f"Found {count} URL(s) containing '/example' -- this is the "
            f"tests/ fixtures' placeholder pattern; this digest looks like "
            f"it was built from (or copied) test fixture content, not a "
            f"real sourced edition"
        )

    for headline in fixture_data["headlines"]:
        if headline and headline in md_text:
            result.fail(
                f"Digest contains a known test-fixture headline verbatim: "
                f"'{headline}' -- this looks like fixture content, not a "
                f"real sourced edition"
            )

    normalized_md = md_text.strip()
    for filename, fixture_text in fixture_data["texts"].items():
        if normalized_md == fixture_text.strip():
            result.fail(
                f"Digest content is identical to test fixture "
                f"'tests/{filename}' -- this is fixture content and must "
                f"never be delivered"
            )

    if DO_NOT_SHIP_MARKER in md_text:
        result.fail(
            f"Found the DO-NOT-SHIP marker in the digest -- this text only "
            f"exists in tests/ fixtures and must never appear in a real "
            f"edition"
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


def run_audit(md_path, docx_path, register_path, skip_url_check=False,
              url_timeout=DEFAULT_URL_TIMEOUT, url_delay=DEFAULT_URL_DELAY,
              search_log_path=None):
    result = AuditResult()
    md_text = Path(md_path).read_text(encoding="utf-8")
    blocks = split_h1_blocks(md_text)
    register_urls = load_register_urls(register_path)

    check_required_blocks(blocks, result)
    check_headline_block_ordering(blocks, result)
    check_commission_labels(blocks, result)
    check_negative_articles_no_subheadings(blocks, result)
    check_minimum_coverage(blocks, result, search_log_path=search_log_path)
    check_links_and_sources(blocks, result, register_urls)
    check_risks_and_opportunities(blocks, result)
    check_banned_phrases(md_text, result)
    check_american_spellings(md_text, result)
    check_arabic_only_in_labels(md_text, blocks, result)
    check_docx_parity(docx_path, result)
    check_url_resolution(blocks, result, skip=skip_url_check,
                          timeout=url_timeout, delay=url_delay)
    check_fixture_content_leak(md_text, result)

    return result


def main():
    parser = argparse.ArgumentParser(description="Stage 5 audit for the MoC Daily Cultural Digest")
    parser.add_argument("markdown_path", help="Path to the canonical markdown digest")
    parser.add_argument("--docx", default=None, help="Path to the built .docx (optional parity check)")
    parser.add_argument("--register", default="reports/do_not_reuse_register.md",
                         help="Path to the do-not-reuse register")
    parser.add_argument("--skip-url-check", action="store_true",
                         help="Skip live URL-resolution checks (offline testing only -- "
                              "ON by default in real runs; never skip for a real delivery)")
    parser.add_argument("--url-timeout", type=float, default=DEFAULT_URL_TIMEOUT,
                         help=f"Per-URL request timeout in seconds (default {DEFAULT_URL_TIMEOUT})")
    parser.add_argument("--url-delay", type=float, default=DEFAULT_URL_DELAY,
                         help=f"Delay between URL checks in seconds, for polite rate-limiting "
                              f"(default {DEFAULT_URL_DELAY})")
    parser.add_argument("--search-log", default="reports/search_log.json",
                         help="Path to the search-log JSON confirming which searches ran this "
                              "cycle (default reports/search_log.json) -- required evidence for "
                              "an empty Negative Articles section to be allowed")
    args = parser.parse_args()

    result = run_audit(args.markdown_path, args.docx, args.register,
                        skip_url_check=args.skip_url_check,
                        url_timeout=args.url_timeout, url_delay=args.url_delay,
                        search_log_path=args.search_log)

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
