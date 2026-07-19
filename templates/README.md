# Templates

There is no real branded MoC Word template in this repo yet. `scripts/build_docx.py`
currently builds a clean, professionally formatted document from scratch
(headings, bullets, section structure) matching the reference digests'
visual style, rather than editing a pre-branded template.

## When a real branded template is available

Once the Ministry has an actual `.docx` letterhead/template (logo, house
colors, fonts, header/footer), switch to the pinned-template approach used by
the conflict-monitoring repo this project was adapted from:

1. Place the template at `templates/template.docx`.
2. Compute its SHA-256: `sha256sum templates/template.docx`.
3. Record the hash in `SKILL.md`'s Stage 0 capability check, so every run
   verifies it before building (a mismatch means someone hand-edited the
   template, which should stop the run rather than build from a modified copy).
4. Rewrite `scripts/build_docx.py` to do direct XML editing of the pinned
   template instead of building from scratch: unzip the template, insert the
   digest content into a placeholder paragraph in `word/document.xml`
   (reusing the template's existing heading/hyperlink styles), and re-zip.
   The conflict-monitoring repo's `scripts/build_docx.py` is a working
   reference for this pattern (direct XML, Python stdlib only, no external
   library needed).
5. Never hand-edit the template afterward — to change the brand chrome,
   produce a new template file and update the pinned hash in the same change.
