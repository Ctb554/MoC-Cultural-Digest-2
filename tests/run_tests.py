#!/usr/bin/env python3
"""
Automated regression suite for scripts/audit_report.py and scripts/build_docx.py.

Pure stdlib, no test framework dependency (matches the rest of this repo).
Covers every hardening change made against the fixtures in this directory,
plus regression checks that the original clean/broken fixture behavior
still holds. Run:

    python3 tests/run_tests.py

Exit code 0 = every check passed. Exit code 1 = at least one failed; the
failure list is printed at the end either way.
"""

import argparse
import json
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = REPO_ROOT / "tests"
SCRIPTS_DIR = REPO_ROOT / "scripts"
CONFIRMED_LOG = str(TESTS_DIR / "sample_search_log_confirmed.json")
NOT_RUN_LOG = str(TESTS_DIR / "sample_search_log_not_run.json")

sys.path.insert(0, str(SCRIPTS_DIR))
import audit_report as ar  # noqa: E402

FAILURES = []


def check(name, condition, detail=""):
    if condition:
        print(f"  [ok] {name}")
    else:
        FAILURES.append(f"{name}: {detail}")
        print(f"  [FAIL] {name}: {detail}")


def run_audit_on(md_path, search_log_path=CONFIRMED_LOG, register_path="/dev/null",
                  as_of_date=None, skip_url_check=True):
    return ar.run_audit(str(md_path), None, register_path, skip_url_check=skip_url_check,
                         search_log_path=search_log_path, as_of_date=as_of_date)


# --- Item 2: fixture safety --------------------------------------------------

def test_clean_fixture_fails_only_on_fixture_safety():
    print("\n== Fixture safety: sample_test_digest.md ==")
    result = run_audit_on(TESTS_DIR / "sample_test_digest.md")
    fixture_markers = ["/example", "test-fixture headline", "identical to test fixture", "DO-NOT-SHIP"]
    non_fixture_failures = [f for f in result.hard_failures if not any(m in f for m in fixture_markers)]
    check("fails for fixture-safety reasons only (no structural failures)",
          len(non_fixture_failures) == 0, non_fixture_failures)
    check("all four fixture-safety tripwires fire",
          len(result.hard_failures) >= 4, result.hard_failures)


def test_realistic_fixture_passes_cleanly():
    print("\n== Fixture safety: sample_realistic_digest.md (no false positive) ==")
    result = run_audit_on(TESTS_DIR / "sample_realistic_digest.md")
    check("zero hard failures", result.ok(), result.hard_failures)


def test_fixture_safety_does_not_false_positive_on_unrelated_content():
    print("\n== Fixture safety: unrelated digest with no fixture overlap ==")
    md = """# Headlines, 4 April 2028

## Saudi Arabia/Regional
- Placeholder headline unrelated to any fixture

## Negative Articles
- Another unrelated placeholder headline

## Global
- Yet another unrelated placeholder headline

# Saudi Arabia/Regional

## General (عام)
- Fully unrelated bullet text. ([Wire](https://www.unrelatedwire.invalid/a))

# Negative Articles
- Fully unrelated negative bullet text. ([Wire](https://www.unrelatedwire.invalid/b))

# Global

## Music (الموسيقى)
- Fully unrelated global bullet text. ([Wire](https://www.unrelatedwire.invalid/c))

# Risks and Opportunities

## Risks

1. **A risk**
Paragraph.
Source: [Wire](https://www.unrelatedwire.invalid/a)
Consideration: Something.

## Opportunities

1. **An opportunity**
Paragraph.
Source: [Wire](https://www.unrelatedwire.invalid/c)
Consideration: Something.
"""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
        path = f.name
    try:
        result = run_audit_on(path)
        check("no fixture-safety false positive", result.ok(), result.hard_failures)
    finally:
        Path(path).unlink()


# --- Regression: original broken-fixture defects -----------------------------

def test_broken_fixture_still_catches_original_defects():
    print("\n== Regression: sample_broken_digest.md still catches its 10 original defects ==")
    result = run_audit_on(TESTS_DIR / "sample_broken_digest.md")
    expected_substrings = [
        "headline bullets must come first",
        "Invalid/invented or non-bilingual commission label 'Tourism and Hospitality'",
        "Invalid/invented or non-bilingual commission label 'Heritage'",
        "commission subheading(s)",
        "Excluded outlet used (Saudi-owned)",
        "'Risks' item 1 missing a 'Source:' line",
        "'Risks' item 1 missing a 'Consideration:' line",
        "'Opportunities' item 1 missing a 'Consideration:' line",
        "Banned inflated phrase found: 'groundbreaking'",
        "Banned inflated phrase found: 'unprecedented'",
    ]
    for substr in expected_substrings:
        check(f"catches: {substr}", any(substr in f for f in result.hard_failures), "not found")
    check("also catches fixture-safety (this fixture uses /example too)",
          any("/example" in f for f in result.hard_failures), "not found")


# --- Item 1: URL resolution ---------------------------------------------------

def test_url_resolution_pass_and_fail_logic():
    print("\n== URL resolution logic (monkeypatched resolver, no real network) ==")
    md = (TESTS_DIR / "sample_realistic_digest.md").read_text(encoding="utf-8")
    blocks = ar.split_h1_blocks(md)

    result = ar.AuditResult()
    ar.check_url_resolution(blocks, result, skip=False, resolver=lambda url, timeout: (True, "HTTP 200 (fake)"))
    check("all-2xx resolver -> no failures", result.ok(), result.hard_failures)

    result = ar.AuditResult()
    ar.check_url_resolution(blocks, result, skip=False, resolver=lambda url, timeout: (False, "HTTP 404 (fake)"))
    check("all-404 resolver -> hard failures", not result.ok(), "expected failures, got none")
    check("dead-link failure message format",
          all("Dead or unreachable link" in f for f in result.hard_failures), result.hard_failures)

    for code in (401, 403, 429):
        result = ar.AuditResult()
        ar.check_url_resolution(blocks, result, skip=False,
                                 resolver=lambda url, timeout, c=code: (True, f"HTTP {c} (fake bot wall)"))
        check(f"bot-wall/rate-limit ({code}) resolver -> treated as exists, no failure",
              result.ok(), result.hard_failures)

    result = ar.AuditResult()
    ar.check_url_resolution(blocks, result, skip=True, resolver=lambda url, timeout: (False, "HTTP 404 (fake)"))
    check("skip=True bypasses even a dead-everything resolver", result.ok(), result.hard_failures)
    check("skip=True still emits a warning", any("skipped" in w for w in result.warnings), result.warnings)


def test_cli_crash_path_writes_status_and_exits_nonzero():
    print("\n== URL/status wiring: real CLI crash path (subprocess) ==")
    with tempfile.TemporaryDirectory() as tmpdir:
        bad_path = Path(tmpdir)  # a directory, not a file -- triggers IsADirectoryError
        status_path = Path(tmpdir) / "status.json"
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "audit_report.py"), str(bad_path),
             "--register", "/dev/null", "--skip-url-check", "--status-out", str(status_path)],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        check("CLI exits nonzero on crash", proc.returncode != 0, proc.returncode)
        check("status file written despite crash", status_path.exists(), "missing")
        if status_path.exists():
            loaded = json.loads(status_path.read_text(encoding="utf-8"))
            check("status shows audit.result == error", loaded.get("audit", {}).get("result") == "error", loaded)
            check("status run_error captured", bool(loaded.get("run_error")), loaded)


# --- Item 3: minimum-coverage ladder ------------------------------------------

def test_empty_negative_ladder():
    print("\n== Minimum-coverage ladder: empty Negative Articles ==")
    md_path = TESTS_DIR / "sample_empty_negative_digest.md"

    result = run_audit_on(md_path, search_log_path=CONFIRMED_LOG)
    check("confirmed search log -> passes", result.ok(), result.hard_failures)
    check("coverage_ladder marks Negative Articles empty-justified",
          result.coverage_ladder.get("Negative Articles", {}).get("rung") == "empty-justified",
          result.coverage_ladder)

    result = run_audit_on(md_path, search_log_path=NOT_RUN_LOG)
    check("'not run' search log -> fails", not result.ok(), "expected failure")
    check("failure message names the missing evidence",
          any("no search-log evidence" in f for f in result.hard_failures), result.hard_failures)

    result = run_audit_on(md_path, search_log_path="/tmp/this-search-log-does-not-exist.json")
    check("missing search log entirely -> fails (fail-closed default)", not result.ok(), "expected failure")


def test_minimum_coverage_cannot_be_waived_for_saudi_or_global():
    print("\n== Minimum coverage: Saudi/Regional and Global can never be waived ==")
    md = """# Headlines, 1 January 2028

## Saudi Arabia/Regional

## Negative Articles

## Global
- Some global item

# Saudi Arabia/Regional

# Negative Articles

# Global

## Museums (المتاحف)
- Placeholder bullet with a link. ([Wire](https://www.placeholderwire.invalid/x))

# Risks and Opportunities

## Risks

1. **A risk**
Paragraph.
Source: [Wire](https://www.placeholderwire.invalid/x)
Consideration: Something.

## Opportunities

1. **An opportunity**
Paragraph.
Source: [Wire](https://www.placeholderwire.invalid/x)
Consideration: Something.
"""
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(md)
        path = f.name
    try:
        # Even with a confirming search log, an empty Saudi Arabia/Regional
        # must still hard-fail -- only Negative Articles gets that exception.
        result = run_audit_on(path, search_log_path=CONFIRMED_LOG)
        check("empty Saudi Arabia/Regional hard-fails despite confirmed search log",
              any("'Saudi Arabia/Regional' has zero articles" in f for f in result.hard_failures),
              result.hard_failures)
    finally:
        Path(path).unlink()


# --- Item 5: Israeli-outlet posture -------------------------------------------

def test_israeli_outlet_hard_fail():
    print("\n== Israeli-outlet hard-fail posture ==")
    result = run_audit_on(TESTS_DIR / "sample_israeli_outlet_digest.md")
    check("Times of Israel citation hard-fails",
          any("Israeli outlet" in f and "timesofisrael.com" in f for f in result.hard_failures),
          result.hard_failures)


# --- Item 4a: register rolling window -----------------------------------------

def test_register_rolling_window():
    print("\n== Do-not-reuse register: rolling 60-day window ==")
    as_of = date(2027, 11, 15)
    register_text = (
        "2027-11-01 | Global | Wire | Recent entry | https://www.recentwire.invalid/recent\n"
        "2027-08-01 | Global | Wire | Stale entry | https://www.stalewire.invalid/stale\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(register_text)
        register_path = f.name

    try:
        recent, stale = ar.load_register_urls(register_path, window_days=60, as_of=as_of)
        check("14-day-old entry bucketed as recent",
              "https://www.recentwire.invalid/recent" in recent, recent)
        check("~106-day-old entry bucketed as stale",
              "https://www.stalewire.invalid/stale" in stale, stale)

        md = """# Headlines, 15 November 2027

## Saudi Arabia/Regional
- Placeholder

## Negative Articles

## Global
- Placeholder

# Saudi Arabia/Regional

## General (عام)
- Placeholder bullet reusing a stale link. ([Wire](https://www.stalewire.invalid/stale))

# Negative Articles

# Global

## Museums (المتاحف)
- Placeholder bullet reusing a recent link. ([Wire](https://www.recentwire.invalid/recent))

# Risks and Opportunities

## Risks

1. **A risk**
Paragraph.
Source: [Wire](https://www.recentwire.invalid/recent)
Consideration: Something.

## Opportunities

1. **An opportunity**
Paragraph.
Source: [Wire](https://www.stalewire.invalid/stale)
Consideration: Something.
"""
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f2:
            f2.write(md)
            digest_path = f2.name
        try:
            result = ar.run_audit(digest_path, None, register_path, skip_url_check=True,
                                   search_log_path=CONFIRMED_LOG, as_of_date=as_of)
            check("reusing the recent link hard-fails",
                  any("recentwire.invalid" in f and "within the last" in f for f in result.hard_failures),
                  result.hard_failures)
            check("reusing the stale link does NOT hard-fail",
                  not any("stalewire.invalid" in f for f in result.hard_failures),
                  result.hard_failures)
            check("reusing the stale link produces a warning instead",
                  any("stalewire.invalid" in w for w in result.warnings), result.warnings)
        finally:
            Path(digest_path).unlink()
    finally:
        Path(register_path).unlink()


# --- Item 6: run-status file ---------------------------------------------------

def test_run_status_file_pass_and_crash_shapes():
    print("\n== Run-status file: pass and crash payload shapes ==")

    result = run_audit_on(TESTS_DIR / "sample_realistic_digest.md")
    args = argparse.Namespace(
        markdown_path=str(TESTS_DIR / "sample_realistic_digest.md"),
        reader_used="tavily", delivery_result="not_attempted",
        skip_url_check=True, register_window_days=60,
    )
    status = ar.build_run_status(args, result=result, run_error=None)
    check("pass status has audit.result == pass", status["audit"]["result"] == "pass", status)
    check("pass status has section_item_counts", "section_item_counts" in status, status)
    check("pass status has minimum_coverage_ladder", "minimum_coverage_ladder" in status, status)
    check("pass status auto-detects named_entity_lists_last_verified",
          status.get("named_entity_lists_last_verified") is not None, status)

    args_crash = argparse.Namespace(
        markdown_path="/some/path", reader_used="none",
        delivery_result="not_attempted", skip_url_check=True, register_window_days=60,
    )
    crash_status = ar.build_run_status(args_crash, result=None, run_error="Simulated crash: boom")
    check("crash status has audit.result == error", crash_status["audit"]["result"] == "error", crash_status)
    check("crash status captures run_error", crash_status["run_error"] == "Simulated crash: boom", crash_status)

    with tempfile.TemporaryDirectory() as tmpdir:
        out_path = Path(tmpdir) / "nested" / "status.json"
        ar.write_status_file(out_path, status)
        check("write_status_file creates parent dirs and writes valid JSON",
              json.loads(out_path.read_text(encoding="utf-8"))["audit"]["result"] == "pass", "")


# --- build_docx.py regression --------------------------------------------------

def test_build_docx_still_works():
    print("\n== build_docx.py regression ==")
    with tempfile.TemporaryDirectory() as tmpdir:
        out = Path(tmpdir) / "out.docx"
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "build_docx.py"),
             str(TESTS_DIR / "sample_realistic_digest.md"), "--output", str(out)],
            capture_output=True, text=True, cwd=str(REPO_ROOT),
        )
        check("build_docx.py exits 0", proc.returncode == 0, proc.stderr)
        check("docx file created", out.exists(), "missing")


TESTS = [
    test_clean_fixture_fails_only_on_fixture_safety,
    test_realistic_fixture_passes_cleanly,
    test_fixture_safety_does_not_false_positive_on_unrelated_content,
    test_broken_fixture_still_catches_original_defects,
    test_url_resolution_pass_and_fail_logic,
    test_cli_crash_path_writes_status_and_exits_nonzero,
    test_empty_negative_ladder,
    test_minimum_coverage_cannot_be_waived_for_saudi_or_global,
    test_israeli_outlet_hard_fail,
    test_register_rolling_window,
    test_run_status_file_pass_and_crash_shapes,
    test_build_docx_still_works,
]


def main():
    print("=== MoC Digest Hardening Test Suite ===")
    for test_fn in TESTS:
        try:
            test_fn()
        except Exception as exc:  # noqa: BLE001 -- a test raising is itself a failure to report
            FAILURES.append(f"{test_fn.__name__} raised {type(exc).__name__}: {exc}")
            print(f"  [FAIL] {test_fn.__name__} raised {type(exc).__name__}: {exc}")

    print()
    if FAILURES:
        print(f"=== {len(FAILURES)} FAILURE(S) ===")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print("=== ALL TESTS PASSED ===")
        sys.exit(0)


if __name__ == "__main__":
    main()
