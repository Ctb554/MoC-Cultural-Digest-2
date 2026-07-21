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
        --register reports/do_not_reuse_register.md \\
        --search-log reports/search_log.json \\
        --reader-used tavily --delivery-result success

Exit code 0 = all hard checks pass (warnings may still be printed).
Exit code 1 = at least one hard check failed, or the audit itself crashed;
the digest must not be delivered either way.

Notable flags (see full --help for all of them): --skip-url-check disables
the live URL-resolution check for offline testing ONLY (on by default, never
skip for a real run); --search-log points at the evidence file that allows
an empty Negative Articles section; --register-window-days controls the
do-not-reuse register's rolling reuse window (default 60); --status-out
controls where the machine-readable run summary is written (default
reports/last_run_status.json, written reliably even if this script crashes).

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
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# --- Structure constants (must match SKILL.md exactly) ----------------------

REQUIRED_SECTIONS = ["Saudi Arabia/Regional", "Negative Articles", "Global"]

# Sections that use commission subheadings in the full-summary block.
# Negative Articles deliberately has none, per confirmed real production.
SECTIONS_WITH_SUBHEADINGS = {"Saudi Arabia/Regional", "Global"}

# Approved commission labels. Changed 2026-07-21: previously bilingual
# "English (Arabic)" pairs, reverse-engineered from the 19/20/21 July real
# editions. A separately-reviewed real edition (16 July) showed plain
# English-only labels ("General:", not "General (عام)"), and the user
# confirmed this directly: the digest gets fully translated into Arabic as
# a separate downstream step, so the English edition's own labels don't
# need to carry Arabic at all. Plain English labels, colon-terminated, are
# now the standard -- see SKILL.md's Stage 3 for the full rationale.
APPROVED_COMMISSIONS = [
    "General",
    "Heritage",
    "Museums",
    "Visual Arts",
    "Film",
    "Fashion",
    "Music",
    "Theatre and Performing Arts",
    "Literature, Publishing, and Translation",
    "Libraries",
    "Culinary Arts",
    "Architecture and Design",
]
# Build the exact "Label:" strings expected in the markdown
APPROVED_LABEL_STRINGS = {f"{label}:" for label in APPROVED_COMMISSIONS}

# Domains excluded per the source-eligibility rule (Saudi-owned outlets).
EXCLUDED_SAUDI_DOMAINS = [
    "arabnews.com", "saudigazette.com.sa", "spa.gov.sa", "aleqt.com",
    "okaz.com.sa", "sabq.org", "argaam.com", "asharq.com", "aawsat.com",
]

# Israeli-outlet posture (item 5, deliberate reputational-caution decision,
# separate from the Saudi-ownership rule above): for a Saudi government
# client, the reputational risk of citing Israeli media exists regardless of
# whether the outlet is itself credible or the citation is neutral -- this is
# a client-specific sensitivity call, not a factual-accuracy judgment about
# these outlets. ALL are hard-fails, not warnings; jpost.com was previously
# the only one treated this strictly while Times of Israel/Haaretz/Ynet/i24/
# TheMarker were warn-only, which was an inconsistency this closes. This is
# overridable ONLY by a human editing the digest directly (e.g. the team
# deciding a specific citation is warranted) -- no automated logic in this
# pipeline should ever add one of these domains to ALLOWED_OVERRIDE_DOMAINS
# or otherwise bypass this list.
EXCLUDED_ISRAELI_DOMAINS = [
    "jpost.com", "timesofisrael.com", "haaretz.com", "haaretz.co.il",
    "ynetnews.com", "ynet.co.il", "i24news.tv", "themarker.com",
]

# Combined lookup: domain -> human-readable reason, used in failure messages.
EXCLUDED_DOMAINS = {
    **{d: "Saudi-owned" for d in EXCLUDED_SAUDI_DOMAINS},
    **{d: "Israeli outlet -- reputational-caution policy" for d in EXCLUDED_ISRAELI_DOMAINS},
}

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

# --- Do-not-reuse register rolling window (item 4a) -------------------------
#
# Entry format: "<YYYY-MM-DD> | <section> | <outlet> | <headline> | <url>".
# Only entries dated within the last N days are enforced for reuse-blocking;
# older entries stay in the file for record (append-only, nothing removed)
# but no longer block a new edition from citing the same outlet again.
REGISTER_ENTRY_RE = re.compile(
    r"^\s*(\d{4}-\d{2}-\d{2})\s*\|[^|]*\|[^|]*\|[^|]*\|\s*(\S+)\s*$"
)
DEFAULT_REGISTER_WINDOW_DAYS = 60


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
                    f"Invalid/invented commission label '{h2}' under section "
                    f"'{h1_name}' -- must be an approved label from "
                    f"APPROVED_COMMISSIONS, written as 'Label:'"
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

        # Added 2026-07-21, closing a real regression: themed negative
        # searches alone can legitimately find nothing while the day's own
        # top Regional story still carries adversarial framing from a
        # different outlet (e.g. Al Jazeera framing a Houthi-blockade story
        # as Saudi Arabia besieging Yemen) -- a case the themed searches are
        # not built to catch. When the log says this check was applicable,
        # it must also say it was run, or the empty-Negative justification
        # does not hold, same fail-closed principle as negative_searches_run.
        framing_applicable = bool(search_log and search_log.get("adversarial_framing_check_applicable") is True)
        framing_run = bool(search_log and search_log.get("adversarial_framing_check_run") is True)
        framing_check_satisfied = (not framing_applicable) or framing_run

        searches_confirmed_run = searches_confirmed_run and framing_check_satisfied
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
        elif framing_applicable and not framing_run:
            result.fail(
                "'Negative Articles' is empty and the search log flags "
                f"adversarial_framing_check_applicable=true (today's lead "
                f"Regional story names Saudi Arabia in a geopolitical/"
                f"security context) but adversarial_framing_check_run is "
                f"not true -- this is the exact gap that produced a real "
                f"regression on 2026-07-21 (a Houthi-blockade story with "
                f"adversarial Al Jazeera framing was missed); run the check "
                f"described in Stage 2's 'Adversarial-framing check' before "
                f"treating this section as legitimately empty"
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


def check_links_and_sources(blocks, result, recent_register_urls, stale_register_urls,
                             register_window_days=DEFAULT_REGISTER_WINDOW_DAYS):
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
                    for excluded_domain, reason in EXCLUDED_DOMAINS.items():
                        if excluded_domain in url_lower:
                            result.fail(
                                f"[{h1_name} / {label}] Excluded outlet used "
                                f"({reason}): {url}"
                            )
                            break

                for _, url in links:
                    if url in recent_register_urls:
                        result.fail(
                            f"[{h1_name} / {label}] Reused link from a prior "
                            f"edition's do-not-reuse register (within the "
                            f"last {register_window_days} days): {url}"
                        )
                    elif url in stale_register_urls:
                        result.warn(
                            f"[{h1_name} / {label}] Link appears in the "
                            f"do-not-reuse register, but from an entry older "
                            f"than the {register_window_days}-day reuse "
                            f"window -- not blocking, flagged for awareness: "
                            f"{url}"
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


def check_no_arabic_anywhere(md_text, result):
    """
    Changed 2026-07-21: labels are no longer bilingual (see APPROVED_COMMISSIONS
    docstring), so Arabic is not expected ANYWHERE in this pipeline's English
    edition -- the full document gets translated into Arabic as a separate
    downstream step, and that translation is out of scope for this repo (see
    SKILL.md's routine run constants). Any Arabic character in the English
    digest is a hard failure.
    """
    if ARABIC_RE.search(md_text):
        result.fail(
            "Arabic characters found in the English digest -- this pipeline "
            "produces the English edition only (full Arabic translation is a "
            "separate downstream step, not part of this repo's output); "
            "Arabic should not appear anywhere in this document"
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


def load_register_urls(register_path, window_days=DEFAULT_REGISTER_WINDOW_DAYS, as_of=None):
    """
    Returns (recent_urls, stale_urls). recent_urls are from entries dated
    within the last `window_days` days of `as_of` (defaults to real today)
    -- reusing one of these is a hard failure. stale_urls are older entries,
    kept in the register for record (it's append-only, nothing is ever
    removed) but no longer enforced -- reusing one of these is a warning
    only. A line that can't be parsed as "<date> | ... | ... | ... | <url>",
    or whose date is malformed, falls back to being treated as always-recent
    (never expires) -- fail-safe, since we can't confirm it's actually old.
    """
    if not register_path or not Path(register_path).exists():
        return set(), set()
    if as_of is None:
        as_of = date.today()
    cutoff = as_of - timedelta(days=window_days)

    recent, stale = set(), set()
    text = Path(register_path).read_text(encoding="utf-8")
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("<!--"):
            continue

        m = REGISTER_ENTRY_RE.match(stripped)
        if not m:
            # Malformed/unstructured line -- fail-safe: enforce any URL on it.
            recent.update(URL_RE.findall(stripped))
            continue

        entry_date_str, url = m.groups()
        try:
            entry_date = date.fromisoformat(entry_date_str)
        except ValueError:
            recent.add(url)  # can't confirm age -- fail-safe, always enforce
            continue

        if entry_date >= cutoff:
            recent.add(url)
        else:
            stale.add(url)

    return recent, stale


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
              search_log_path=None, register_window_days=DEFAULT_REGISTER_WINDOW_DAYS,
              as_of_date=None):
    result = AuditResult()
    md_text = Path(md_path).read_text(encoding="utf-8")
    blocks = split_h1_blocks(md_text)
    recent_register_urls, stale_register_urls = load_register_urls(
        register_path, window_days=register_window_days, as_of=as_of_date
    )

    check_required_blocks(blocks, result)
    check_headline_block_ordering(blocks, result)
    check_commission_labels(blocks, result)
    check_negative_articles_no_subheadings(blocks, result)
    check_minimum_coverage(blocks, result, search_log_path=search_log_path)
    check_links_and_sources(blocks, result, recent_register_urls, stale_register_urls,
                             register_window_days=register_window_days)
    check_risks_and_opportunities(blocks, result)
    check_banned_phrases(md_text, result)
    check_american_spellings(md_text, result)
    check_no_arabic_anywhere(md_text, result)
    check_docx_parity(docx_path, result)
    check_url_resolution(blocks, result, skip=skip_url_check,
                          timeout=url_timeout, delay=url_delay)
    check_fixture_content_leak(md_text, result)

    return result


# --- Run-status reporting (item 6: reliable machine-readable run summary) --

DEFAULT_SKILL_MD_PATH = Path(__file__).resolve().parent.parent / ".claude" / "skills" / "cultural-digest" / "SKILL.md"
DEFAULT_STATUS_OUT_PATH = "reports/last_run_status.json"
NAMED_ENTITY_STALE_AFTER_DAYS = 180
LAST_VERIFIED_RE = re.compile(r"LAST VERIFIED:\s*(\d{4}-\d{2}-\d{2})")


def check_named_entity_freshness(skill_md_path=None, max_age_days=NAMED_ENTITY_STALE_AFTER_DAYS, as_of=None):
    """
    Parses SKILL.md's "LAST VERIFIED: YYYY-MM-DD" header for the Named
    Entity People/Places lists (item 4b) and flags staleness -- non-blocking,
    just a signal in the run status that those lists need re-verification.
    Returns {"last_verified": "YYYY-MM-DD" or None, "days_old": int or None,
    "stale": bool or None}; None values mean the date couldn't be found (not
    an error -- some deployments may not ship SKILL.md at this path).
    """
    if skill_md_path is None:
        skill_md_path = DEFAULT_SKILL_MD_PATH
    path = Path(skill_md_path)
    if not path.exists():
        return {"last_verified": None, "days_old": None, "stale": None}

    match = LAST_VERIFIED_RE.search(path.read_text(encoding="utf-8"))
    if not match:
        return {"last_verified": None, "days_old": None, "stale": None}

    last_verified = date.fromisoformat(match.group(1))
    today = as_of if as_of is not None else date.today()
    days_old = (today - last_verified).days
    return {
        "last_verified": last_verified.isoformat(),
        "days_old": days_old,
        "stale": days_old > max_age_days,
    }


def build_run_status(args, result=None, run_error=None, as_of=None):
    """
    Builds the reports/last_run_status.json payload. Called from main()'s
    `finally` block so a status file is written whether the audit passed,
    failed, or crashed with an exception -- result=None + run_error set
    covers the crash path.
    """
    status = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "markdown_path": args.markdown_path,
        "reader_used": args.reader_used,
        "delivery_result": args.delivery_result,
        "url_resolution_check": "skipped" if args.skip_url_check else "enabled",
        "register_window_days": args.register_window_days,
        "run_error": run_error,
    }

    if result is not None:
        status["section_item_counts"] = {
            section: data["count"] for section, data in result.coverage_ladder.items()
        }
        status["minimum_coverage_ladder"] = result.coverage_ladder
        status["audit"] = {
            "result": "pass" if result.ok() else "fail",
            "hard_failures": result.hard_failures,
            "warnings": result.warnings,
        }
    else:
        status["section_item_counts"] = {}
        status["minimum_coverage_ladder"] = {}
        status["audit"] = {"result": "error", "hard_failures": [], "warnings": []}

    freshness = check_named_entity_freshness(as_of=as_of)
    status["named_entity_lists_last_verified"] = freshness["last_verified"]
    status["named_entity_lists_days_old"] = freshness["days_old"]
    status["stale_named_entity_lists"] = freshness["stale"]

    return status


def write_status_file(path, status):
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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
    parser.add_argument("--register-window-days", type=int, default=DEFAULT_REGISTER_WINDOW_DAYS,
                         help=f"Rolling window in days for do-not-reuse register enforcement "
                              f"(default {DEFAULT_REGISTER_WINDOW_DAYS}); older register entries "
                              f"stay on file but no longer block reuse")
    parser.add_argument("--as-of-date", default=None,
                         help="Override 'today' (YYYY-MM-DD) for register-window calculations -- "
                              "testing only, defaults to the real current date")
    parser.add_argument("--reader-used", choices=["tavily", "connector", "none"], default="none",
                         help="Which reader path this run actually used for bot-walled premium "
                              "wires -- informational, recorded verbatim in the run-status file")
    parser.add_argument("--delivery-result", default="not_attempted",
                         help="Free-form delivery outcome for this run (e.g. 'success', "
                              "'failed: <reason>', 'skipped: no credentials', 'not_attempted') -- "
                              "informational, recorded verbatim in the run-status file")
    parser.add_argument("--status-out", default=DEFAULT_STATUS_OUT_PATH,
                         help=f"Where to write the machine-readable run-status JSON "
                              f"(default {DEFAULT_STATUS_OUT_PATH}). Written reliably even if the "
                              f"audit itself crashes -- see --no-status-out to disable for testing")
    parser.add_argument("--no-status-out", action="store_true",
                         help="Do not write the run-status file (testing convenience only -- "
                              "a real run should always leave a status file behind)")
    args = parser.parse_args()

    as_of = date.fromisoformat(args.as_of_date) if args.as_of_date else None

    # Wrapped so a crash anywhere in run_audit still leaves a failure status
    # behind (item 6) -- reports/last_run_status.json is written in `finally`
    # regardless of whether the audit passed, failed, or raised.
    result = None
    run_error = None
    try:
        result = run_audit(args.markdown_path, args.docx, args.register,
                            skip_url_check=args.skip_url_check,
                            url_timeout=args.url_timeout, url_delay=args.url_delay,
                            search_log_path=args.search_log,
                            register_window_days=args.register_window_days,
                            as_of_date=as_of)
    except Exception as exc:  # noqa: BLE001 -- any crash must still write a status file
        run_error = f"{type(exc).__name__}: {exc}"
    finally:
        if not args.no_status_out:
            status = build_run_status(args, result=result, run_error=run_error, as_of=as_of)
            write_status_file(args.status_out, status)

    print("=== MoC Digest Audit ===")

    if result is None:
        print(f"\nRESULT: ERROR -- {run_error}")
        print("A failure status was recorded; this digest must not be delivered.")
        sys.exit(1)

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
