# Tests

Automated suite plus a set of markdown/JSON fixtures used to verify
`scripts/build_docx.py` and `scripts/audit_report.py`. None of this is a
real digest edition; content is generic/paraphrased, not copied from any
real client deliverable.

## Running everything

```bash
python3 tests/run_tests.py
```

This is the primary way to verify the repo — it imports `scripts/audit_report.py`
directly (no real network calls; URL-resolution logic is tested via a
monkeypatched resolver, never live HTTP) and runs every check below in one
pass. Exit code 0 = everything passed; a nonzero exit prints the failure
list. Run it after any change to `scripts/audit_report.py` or the fixtures
in this directory.

## Fixtures

- **`sample_test_digest.md`** — a structurally clean digest following the
  confirmed format: headline bullets first, bilingual commission labels,
  free-form analytical bullets, no subheadings in Negative Articles,
  multi-item Risks/Opportunities with restarting numbering, `/example`
  placeholder URLs, and a `DO-NOT-SHIP: FIXTURE CONTENT` marker.
  **Deliberately fails the audit** — that's the point, not a bug: the
  fixture-safety guard (see below) is designed to catch exactly a digest
  that looks like this. It fails on fixture-safety grounds *only*; every
  original structural check still passes cleanly underneath.
- **`sample_broken_digest.md`** — deliberately broken in ten structural ways
  (full-summary section before the headline block, an invented commission
  label, a non-bilingual commission label, an excluded Saudi-owned outlet, a
  commission subheading incorrectly placed under Negative Articles, a Risks
  item missing its Source and Consideration lines, an Opportunities item
  missing its Consideration line, two banned inflated phrases, plus an
  American-spelling warning) **on top of** the same fixture-safety failures
  as above (it also uses `/example` URLs and the marker).
- **`sample_realistic_digest.md`** — a genuinely clean fixture with
  non-`/example` `.invalid`-domain URLs and original headlines, added so
  there's still a way to regression-test "does structurally correct content
  pass every check" without tripping the fixture-safety guard. Its
  `.invalid` URLs are intentionally non-resolving (RFC 2606 reserved TLD) —
  always test it with `--skip-url-check`.
- **`sample_empty_negative_digest.md`** — Saudi Arabia/Regional and Global
  populated, Negative Articles deliberately empty. Demonstrates the
  minimum-coverage ladder: passes when paired with
  `sample_search_log_confirmed.json`, fails when paired with
  `sample_search_log_not_run.json` or no `--search-log` at all.
- **`sample_search_log_confirmed.json`** / **`sample_search_log_not_run.json`**
  — paired fixtures for `--search-log`, confirming vs. denying that the
  negative/watchdog searches were actually run this cycle.
- **`sample_israeli_outlet_digest.md`** — a digest citing Times of Israel.
  Demonstrates the Israeli-outlet hard-fail posture (all Israeli outlets,
  not just jpost.com, are treated identically to Saudi-owned exclusions).

## Manual spot-checks

```bash
# sample_test_digest.md: builds fine, but the audit correctly refuses to
# treat it as real -- fails on fixture-safety grounds only.
python3 scripts/build_docx.py tests/sample_test_digest.md --output /tmp/clean.docx
python3 scripts/audit_report.py tests/sample_test_digest.md --docx /tmp/clean.docx --register /dev/null --skip-url-check --no-status-out

# sample_broken_digest.md: fails with all ten original problems, plus fixture-safety.
python3 scripts/audit_report.py tests/sample_broken_digest.md --register /dev/null --skip-url-check --no-status-out

# sample_realistic_digest.md: builds and passes cleanly (0 hard failures).
python3 scripts/build_docx.py tests/sample_realistic_digest.md --output /tmp/realistic.docx
python3 scripts/audit_report.py tests/sample_realistic_digest.md --docx /tmp/realistic.docx --register /dev/null --skip-url-check --no-status-out

# sample_empty_negative_digest.md: passes only with a confirming search log.
python3 scripts/audit_report.py tests/sample_empty_negative_digest.md --register /dev/null --skip-url-check --search-log tests/sample_search_log_confirmed.json --no-status-out   # PASS
python3 scripts/audit_report.py tests/sample_empty_negative_digest.md --register /dev/null --skip-url-check --search-log tests/sample_search_log_not_run.json --no-status-out       # FAIL
python3 scripts/audit_report.py tests/sample_empty_negative_digest.md --register /dev/null --skip-url-check --no-status-out --search-log /tmp/does-not-exist.json                  # FAIL (fail-closed default)

# sample_israeli_outlet_digest.md: fails on the Times of Israel citation.
python3 scripts/audit_report.py tests/sample_israeli_outlet_digest.md --register /dev/null --skip-url-check --search-log tests/sample_search_log_confirmed.json --no-status-out
```

`--no-status-out` above is only to avoid littering `reports/` with a status
file while spot-checking by hand; a real run should never pass it (see
SKILL.md Stage 5/6).

## What's NOT covered by fixtures alone (covered by `tests/run_tests.py` instead)

- **Live URL resolution** (item 1) — testing this against real URLs would be
  flaky (sites go up/down, rate-limit, or change over time) and slow. The
  pass/fail/bot-wall classification logic is unit-tested in
  `tests/run_tests.py` via a monkeypatched resolver instead; only the CLI
  wiring (crash-safety, exit codes) is exercised end-to-end via a real
  subprocess call, deliberately pointed at a directory (not a URL) to force
  a real, deterministic crash.
- **Do-not-reuse register rolling window** (item 4a) — needs a register with
  entries at specific ages relative to "today", which would silently break
  every 60 days if committed as a static fixture. `tests/run_tests.py`
  builds this synthetically with a fixed `--as-of-date`, so it's
  deterministic regardless of when the suite runs.
- **Run-status file** (item 6) — pass/crash payload shapes are checked
  directly against `build_run_status`/`write_status_file`; the full crash
  path (a real crash inside a real subprocess still leaving a status file
  behind) is checked via the same subprocess call as the URL-resolution
  CLI-wiring check above.

(The original two fixtures were run during development after the format was
corrected against a real delivered edition; the audit correctly caught all
ten injected problems in the broken fixture, and the clean fixture built and
rendered correctly — verified by rendering to PDF and round-tripping through
pandoc to confirm the bilingual labels and hyperlinks render. That step
predates the fixture-safety guard in this hardening pass, which is why the
audit's verdict on `sample_test_digest.md` changed without its actual
document content changing.)
