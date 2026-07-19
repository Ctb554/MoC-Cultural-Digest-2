# Tests

Two markdown fixtures used to verify `scripts/build_docx.py` and
`scripts/audit_report.py` work correctly. Not real digest editions.

- `sample_test_digest.md` — a clean digest following the spec exactly.
  Should build without errors and pass the audit with zero hard failures.
- `sample_broken_digest.md` — deliberately broken in ten different ways
  (invented commission label, raw URL in a bullet, an excluded Saudi-owned
  outlet, a reused link, a headline bullet with a link embedded, a doubled
  numbered Risks paragraph, missing Consideration lines, banned inflated
  phrases). Should fail the audit and list all ten problems.

Run them:

```bash
# Should build cleanly and pass
python3 scripts/build_docx.py tests/sample_test_digest.md --output /tmp/clean.docx
python3 scripts/audit_report.py tests/sample_test_digest.md --docx /tmp/clean.docx --register /dev/null

# Should fail with a list of caught problems
python3 scripts/audit_report.py tests/sample_broken_digest.md --register /dev/null
```

(Both were run during development; the audit correctly caught all ten
injected problems in the broken fixture and passed the clean one cleanly.)
