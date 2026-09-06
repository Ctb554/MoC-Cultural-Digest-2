# Do-Not-Reuse Register

Append-only ledger of every article link and headline used in a delivered
edition of the MoC Daily Cultural Digest. Nothing is ever removed, including
entries from superseded drafts. Each run's Stage 1 reads this in full and
Stage 5 audits against it before delivery.

Format per entry: `<date> | <section> | <outlet> | <headline> | <url>`, where
`<date>` is ISO `YYYY-MM-DD` (the edition's date, not the article's
publication date) -- `scripts/audit_report.py` parses this to enforce a
rolling 60-day reuse window (see SKILL.md's Stage 6): entries within the
window block reuse (hard failure), older entries stay here for the
permanent record but no longer block (warning only). A line that doesn't
match this exact format is treated as fail-safe -- always enforced,
never expiring -- so malformed entries never silently lose protection.

<!-- Entries begin below. First real edition appends here. -->
2026-09-06 | Saudi Arabia/Regional | Mid-East.info | "Shalimar Harmony" Takes Center Stage at the Venice Biennale with 15 New Paintings, a New Sculpture, and Invitations to International Art Events | https://mid-east.info/shalimar-harmony-takes-center-stage-at-the-venice-biennale-with-15-new-paintings-a-new-sculpture-and-invitations-to-international-art-events/
2026-09-06 | Saudi Arabia/Regional | Variety | Mad Solutions and Haitham Dabbour's Irth Platform Announce Strategic Pan-Arab Content Partnership in Venice | https://variety.com/2026/film/festivals/mad-solutions-haitham-dabbours-irth-pan-arab-partnership-1236852377/
2026-09-06 | Negative Articles | Gulf News | US approves $5b sale of bombs to Saudi Arabia | https://gulfnews.com/world/americas/us-approves-5b-sale-of-bombs-to-saudi-arabia-1.500663730
2026-09-06 | Negative Articles | The Guardian | Civilians among at least 60 killed in Yemen as ground fighting escalates | https://www.theguardian.com/world/2026/sep/05/yemen-ground-fighting-escalates-houthi-rebels-government-forces
2026-09-06 | Global | The Playlist | 'Primetime' Review: Robert Pattinson Is Monomaniacal, Magnetic & Completely Unhinged In Lance Oppenheim's Terrific Drama | https://theplaylist.net/primetime-review-robert-pattinson-lance-oppenheim-20260905/
2026-09-06 | Global | Billboard | Ella Langley's 'Choosin' Texas' No. 1 on Hot 100 for 20th Week | https://www.billboard.com/lists/ella-langley-choosin-texas-hot-100-number-one-20-weeks/
