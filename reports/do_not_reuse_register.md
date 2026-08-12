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
2026-08-12 | Saudi Arabia/Regional | Nikkei Asia | Turkey-Pakistan-Saudi pact a 'Muslim NATO'?: 5 things to know | https://asia.nikkei.com/politics/defense/turkey-pakistan-saudi-pact-a-muslim-nato-5-things-to-know
2026-08-12 | Saudi Arabia/Regional | The New York Times | Four Killed in Houthi Strike on Red Sea Ship, Yemeni Government Says | https://www.nytimes.com/2026/08/11/world/middleeast/deadly-houthi-strike-red-sea.html
2026-08-12 | Saudi Arabia/Regional | Semafor | Saudi data center capacity projected to boom, but financing a challenge | https://www.semafor.com/article/08/11/2026/saudi-data-center-capacity-projected-to-boom-but-financing-a-challenge
2026-08-12 | Saudi Arabia/Regional | AGBI | Ades confirms all offshore rigs in Saudi Arabia are operational | https://www.agbi.com/oil-and-gas/2026/08/ades-confirms-all-offshore-rigs-in-saudi-arabia-are-operational/
2026-08-12 | Negative Articles | Al Jazeera | Six killed in Houthi attack on Bab al-Mandeb ship, Yemen's government says | https://www.aljazeera.com/news/2026/8/12/six-killed-in-houthi-attack-on-bab-al-mandeb-ship-yemens-government-says
2026-08-12 | Negative Articles | Middle East Eye | Saudi defence pact with Turkey and Pakistan sparks UAE backlash | https://www.middleeasteye.net/trending/saudi-arabia-defence-pact-turkey-pakistan-sparks-uae-backlash
2026-08-12 | Global | The Art Newspaper | Bottoms up: vast Roman shipwreck filled with ancient wine amphoras discovered near Sicily | https://www.theartnewspaper.com/2026/08/11/bottoms-up-vast-roman-shipwreck-filled-with-ancient-wine-amphoras-discovered-near-sicily
2026-08-12 | Global | The Art Newspaper | Earthquake damages Colombia's tallest church | https://www.theartnewspaper.com/2026/08/11/colombia-earthquake-damages-manizales-cathedral
2026-08-12 | Global | Hyperallergic | Russia Has Damaged or Destroyed Over 4,500 Cultural Sites in Ukraine | https://hyperallergic.com/russia-has-damaged-or-destroyed-over-4-500-cultural-sites-in-ukraine/
2026-08-12 | Global | Hyperallergic | San Diego Museum of Art Lays Off 11 Workers | https://hyperallergic.com/san-diego-museum-of-art-lays-off-11-workers/
2026-08-12 | Global | The Art Newspaper | 'Stopping while we're ahead': London gallery Sid Motion to shut after a decade | https://www.theartnewspaper.com/2026/08/11/stopping-while-were-ahead-london-gallery-sid-motion-to-shut-after-a-decade
2026-08-12 | Global | Hyperallergic | Maori Karmael Holmes Looks Back on 15 Years of BlackStar | https://hyperallergic.com/maori-karmael-holmes-looks-back-on-15-years-of-blackstar/
2026-08-12 | Global | ArchDaily | Peter Zumthor's Architecture Takes Center Stage in Wim Wenders' New Film "From Inside Out" | https://www.archdaily.com/1183086/peter-zumthors-architecture-takes-center-stage-in-wim-wenders-new-film-from-inside-out
2026-08-12 | Global | The Stage | ATG Entertainment agrees sale to global events firm Mari | https://www.thestage.co.uk/news/atg-entertainment-sold-to-global-events-firm-mari
