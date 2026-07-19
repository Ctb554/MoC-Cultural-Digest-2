# Tests

Two markdown fixtures used to verify `scripts/build_docx.py` and
`scripts/audit_report.py` against the format confirmed against a real
delivered edition (2026-07-19) -- see SKILL.md's "FORMAT CONFIRMED AGAINST
REAL PRODUCTION" note. Not real digest editions; content is generic/
paraphrased, not copied from any real client deliverable.

- `sample_test_digest.md` -- a clean digest following the confirmed format:
  headline bullets first, bilingual commission labels, free-form analytical
  bullets, no subheadings in Negative Articles, multi-item Risks/
  Opportunities with restarting numbering. Should build without errors and
  pass the audit with zero hard failures.
- `sample_broken_digest.md` -- deliberately broken in ten ways: full-summary
  section appearing before the headline block, an invented commission label,
  a non-bilingual commission label, an excluded Saudi-owned outlet, a
  commission subheading incorrectly placed under Negative Articles, a Risks
  item missing its Source and Consideration lines, an Opportunities item
  missing its Consideration line, and two banned inflated phrases (plus an
  American-spelling warning). Should fail the audit and list all ten
  problems.

Run them:

```bash
# Should build cleanly and pass
python3 scripts/build_docx.py tests/sample_test_digest.md --output /tmp/clean.docx
python3 scripts/audit_report.py tests/sample_test_digest.md --docx /tmp/clean.docx --register /dev/null

# Should fail with a list of caught problems
python3 scripts/audit_report.py tests/sample_broken_digest.md --register /dev/null
```

(Both were run during development after the format was corrected against a
real delivered edition; the audit correctly caught all ten injected problems
in the broken fixture, and the clean fixture built and passed with zero
failures -- verified by rendering to PDF and round-tripping through pandoc to
confirm the bilingual labels and hyperlinks render correctly.)
