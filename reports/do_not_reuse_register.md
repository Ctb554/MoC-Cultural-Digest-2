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

2026-09-07 | Saudi Arabia/Regional | UA.NEWS | King Abdulaziz Foundation takes part in book fair in Moscow | https://ua.news/en/culture/fond-korolia-abdul-aziza-bere-uchast-u-knizhkovomu-iarmarku-v-moskvi
2026-09-07 | Negative Articles | AGBI | Saudi construction push hit by costly detour around Hormuz | https://www.agbi.com/analysis/construction/2026/09/saudi-construction-push-hit-by-costly-detour-around-hormuz/
2026-09-07 | Negative Articles | AGBI | Saudi-Turkish electricity corridor likely to be costly and complex | https://www.agbi.com/analysis/energy/2026/09/saudi-turkish-electricity-corridor-likely-to-be-costly-and-complex/
2026-09-07 | Negative Articles | Middle East Eye | Yemen's Houthis say Saudi CH-4 drone downed over al-Jawf | https://www.middleeasteye.net/live-blog/live-blog-update/yemens-houthis-say-it-downed-saudi-ch-4-drone-over-al-jawf
2026-09-07 | Global | Arkeonews | 430,000-Year-Old Wooden Tools Found in Greece Are the Oldest Handheld Examples Known | https://arkeonews.net/430000-year-old-wooden-tools-found-in-greece-are-the-oldest-handheld-examples-known/
2026-09-07 | Global | Arkeonews | Could Gobekli Tepe's 'Handbag' Symbols Be the World's Oldest Architectural Drawings? | https://arkeonews.net/could-gobekli-tepes-handbag-symbols-be-the-worlds-oldest-architectural-drawings/
2026-09-07 | Global | Variety | 'Possible Love' From Lee Chang-dong Earns 6-Minute Ovation at Venice | https://variety.com/2026/film/festivals/possible-love-lee-chang-dong-venice-premiere-1236838135/
2026-09-07 | Global | Deadline | 'Primetime' Review: Lance Oppenheim's Dark TV Morality Tale | https://deadline.com/2026/09/primetime-review-robert-pattinson-lance-oppenheim-venice-1237068867/
