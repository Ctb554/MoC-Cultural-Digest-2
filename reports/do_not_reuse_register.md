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
2026-09-10 | Saudi Arabia/Regional | MEED | Why global capital is committing to Saudi Arabia's birthplace | https://www.meed.com/why-global-capital-is-committing-to-saudi-arabias-birthplace
2026-09-10 | Saudi Arabia/Regional | Khaleej Times | Saudi Arabia's National Day: Public holiday announced in the kingdom | https://www.khaleejtimes.com/world/gulf/saudi-arabia-national-day-2026-public-holiday
2026-09-10 | Saudi Arabia/Regional | Khaleej Times | 2,000-year-old Sharjah coastal network moves closer to UNESCO World Heritage status | https://www.khaleejtimes.com/uae/2000-year-old-sharjah-coastal-network-added-unesco-tentative-list
2026-09-10 | Negative Articles | Associated Press | Yemen's Houthi rebels say Saudi-backed forces launched airstrikes | https://www.wsls.com/news/world/2026/09/09/yemens-houthi-rebels-say-saudi-backed-forces-launched-airstrikes-and-other-key-mideast-news/
2026-09-10 | Negative Articles | Al Jazeera | Houthi attacks on Saudi Arabia could activate defence pact, Pakistan says | https://www.aljazeera.com/news/2026/9/9/pakistan-warns-mecca-defense-pact-will-activate-after-houthi-attacks
2026-09-10 | Negative Articles | Semafor | Saudi Arabia could give UN nuclear watchdog greater inspection powers | https://www.semafor.com/article/09/09/2026/saudi-arabia-could-give-un-nuclear-watchdog-greater-inspection-powers
2026-09-10 | Global | The Art Newspaper | Jenny Holzer and Andy Goldsworthy win art world's Nobel Prizes | https://www.theartnewspaper.com/2026/09/09/artists-jenny-holzer-and-andy-goldsworthy-among-winners-of-2026-praemium-imperiale-awards
2026-09-10 | Global | ARTnews | Leilah Babirye Joins Salon 94 and More: Industry Moves for September 9, 2026 | https://www.artnews.com/art-news/market/leilah-babirye-joins-salon-94-industry-moves-september-9-2026-1234797601/
2026-09-10 | Global | Artnet News | Less Is More: Inside the Art World's New Season of Recalibration | https://news.artnet.com/market/art-world-new-season-recalibration-2806419
2026-09-10 | Global | Archaeology Magazine | Roman-Era Mosaic Floor Unearthed in Northern Turkey | https://archaeology.org/news/2026/09/09/roman-era-mosaic-floor-unearthed-in-northern-turkey/
2026-09-10 | Global | Variety | Primetime, Victorian Psycho and Wicker Join Beyond Fest's 2026 Lineup | https://variety.com/2026/film/festivals/beyond-fest-2026-primtetime-victorian-pscyho-1236855248/
2026-09-10 | Global | Deadline | Wildwood To Open AFI Fest 2026 | https://deadline.com/2026/09/wildwood-afi-fest-2026-opening-film-1237072469/
2026-09-10 | Global | WWD | CFDA Unveils 2026 CFDA Fashion Award Nominees and Honorees | https://wwd.com/fashion-news/fashion-features/cfda-fashion-award-nominees-honorees-2026-1239203108/
2026-09-10 | Global | Dezeen | Fifty Europe, Middle East and Africa projects selected for Dezeen Awards 2026 Regional Showcases | https://www.dezeen.com/2026/09/09/emea-regional-showcases-dezeen-awards/
