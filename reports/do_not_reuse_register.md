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
2026-09-23 | Saudi Arabia/Regional | Variety | Red Sea Film Festival Cancels 2026 Edition, Will Return Next Year | https://variety.com/2026/film/festivals/red-sea-film-festival-cancels-2026-edition-1236865126/
2026-09-23 | Saudi Arabia/Regional | The National | Frieze fuelled London's art boom and now the stage is set for Abu Dhabi | https://www.thenationalnews.com/arts-culture/art-design/2026/09/23/frieze-fuelled-londons-art-boom-and-now-the-stage-is-set-for-abu-dhabi/
2026-09-23 | Negative Articles | Bloomberg | Saudi Arabia Running Tests to Resume East-West Oil Pipeline | https://www.bloomberg.com/news/articles/2026-09-22/saudi-arabia-running-tests-to-resume-east-west-oil-pipeline
2026-09-23 | Negative Articles | Semafor | Saudi issues new warnings, as Houthi attacks intensify | https://www.semafor.com/article/09/22/2026/saudi-issues-new-warnings-as-houthi-attacks-intensify
2026-09-23 | Global | ARTnews | A Fragment of a Peace Treaty Between the Hittite and Egyptian Empires Discovered in Hattusa, Turkey | https://www.artnews.com/art-news/news/cuneiform-peace-treaty-fragment-discovered-hattusa-turkey-1234799042/
2026-09-23 | Global | ARTnews | Met Museum Repatriates Five Pieces of Looted Cretan Armor to Greece | https://www.artnews.com/art-news/news/met-museum-repatriates-looted-cretan-armor-to-greece-1234799035/
2026-09-23 | Global | Blooloop | Pokémon coming to Science Museum for space-themed experience | https://blooloop.com/news/pokemon-space-experience-science-museum
2026-09-23 | Global | ArchDaily | MAD Architects' Lucas Museum of Narrative Art Opens to the Public in Los Angeles | https://www.archdaily.com/1184508/first-look-at-the-completed-lucas-museum-of-narrative-art-opening-september-22-2026
2026-09-23 | Global | Dezeen | Dezeen Awards 2026 interiors shortlist revealed | https://www.dezeen.com/2026/09/22/dezeen-awards-2026-interiors-shortlist/
2026-09-23 | Global | CP24 | The 2026 Michelin Guide Toronto & Region has been released. Here are the restaurants that got a star | https://www.cp24.com/local/toronto/2026/09/23/here-are-the-toronto-and-ontario-restaurants-awarded-with-michelin-star/
