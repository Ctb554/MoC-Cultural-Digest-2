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

2026-09-22 | Saudi Arabia/Regional | Gulf Daily News | Desert Rock becomes Saudi Arabia's first Three MICHELIN Key resort | https://www.gdnonline.com/Details/1407172/Desert-Rock-becomes-Saudi-Arabia%E2%80%99s-first-Three-MICHELIN-Key-resort
2026-09-22 | Negative Articles | The National | Red Sea Film Festival cancels 2026 event | https://www.thenationalnews.com/arts-culture/2026/09/21/red-sea-film-festival-cancels-2026-event/
2026-09-22 | Negative Articles | The New York Times | Why the Iran-Backed Houthis in Yemen and Saudi Arabia Are Back at War | https://www.nytimes.com/2026/09/21/world/middleeast/yemen-houthis-saudi-war.html
2026-09-22 | Negative Articles | AGBI | Protracted Houthi war risks squeezing Saudi economy | https://www.agbi.com/analysis/economy/2026/09/protracted-houthi-war-risks-squeezing-saudi-economy/
2026-09-22 | Negative Articles | Middle East Eye | Saudi air strike targets a local market in a village near Bab al-Mandeb in Yemen | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-air-strike-targets-local-market-village-near-bab-al-mandeb-yemen
2026-09-22 | Global | Blooloop | Lucas Museum launches in LA with star-studded opening gala | https://blooloop.com/news/lucas-museum-opening-gala
2026-09-22 | Global | Arkeonews | 8,000-Year-Old 'Guardians of Grain' Discovered in a Neolithic House | https://arkeonews.net/8000-year-old-guardians-of-grain-discovered-in-a-neolithic-house/
2026-09-22 | Global | The Irish News | Burberry celebrates 170 years of the trench coat with playful London Fashion Week show | https://www.irishnews.com/life/burberry-celebrates-170-years-of-the-trench-coat-with-playful-london-fashion-week-show-K5F3Y4CEIBLX5KGYKGAIOTRAJ4/
2026-09-22 | Global | ABC News | Taylor Swift to be honored at 2026 MTV Video Music Awards: What to know about the awards show | https://abcnews.go.com/GMA/Culture/taylor-swift-honored-2026-mtv-video-music-awards/story?id=136625459
2026-09-22 | Global | Dezeen | Dezeen Awards 2026 architecture shortlist announced | https://www.dezeen.com/2026/09/21/dezeen-awards-2026-architecture-shortlist/
2026-09-22 | Global | ArchDaily | On the International Day of Peace: Architecture Between Conflict and Coexistence | https://www.archdaily.com/1185438/on-the-international-day-of-peace-architecture-between-conflict-and-coexistence
2026-09-22 | Global | Al Jazeera | Paramount settles with US states, union to win Warner Bros takeover | https://www.aljazeera.com/economy/2026/9/21/paramount-settles-with-us-states-in-step-towards-merger-with-warner-bros
