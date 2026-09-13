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
2026-09-13 | Saudi Arabia/Regional | Emirates 24/7 | 35th Abu Dhabi International Book Fair opens on Sunday | https://www.emirates247.com/uae/35th-abu-dhabi-international-book-fair-opens-tomorrow-with-1500-events-and-exhibitors-from-95-countries/5564
2026-09-13 | Negative Articles | NBC News | Saudi Arabia's shutdown of key pipeline limits oil flow as Yemen hits back against Houthis | https://www.nbcnews.com/world/middle-east/saudi-arabia-shutdown-key-pipeline-limits-oil-flow-yemen-houthis-rcna597362
2026-09-13 | Negative Articles | Al Jazeera | Iraq probes drone strikes on Saudi Arabia, shuts three crossings to Iran | https://www.aljazeera.com/news/2026/9/12/iraq-probes-drone-strikes-on-saudi-arabia-shuts-three-crossings-to-iran
2026-09-13 | Negative Articles | Vanguard | Houthi in Yemen bombs Saudi Arabia | https://www.vanguardngr.com/2026/09/houthi-in-yemen-bombs-saudi-arabia/
2026-09-13 | Negative Articles | Press TV | Iraqi resistance denies involvement in attacks on Saudi oil infrastructure | https://www.presstv.co.uk/Detail/2026/09/12/776155/Iraqi-resistance-denies-involvement-attacks-Saudi-oil-infrastructure
2026-09-13 | Global | Archaeology News Online Magazine | Huge Iron Age salt-mining complex found beneath Hallstatt in Austria | https://archaeologymag.com/2026/09/iron-age-salt-mining-complex-beneath-hallstatt/
2026-09-13 | Global | Archaeology News Online Magazine | Massive limestone blocks hint at a monumental Etruscan building at ancient port in Italy | https://archaeologymag.com/2026/09/limestone-blocks-hint-at-a-etruscan-building-in-italy/
2026-09-13 | Global | Variety | Andrew Scott Gets Candid About Gay Actors Playing Straight Roles at TIFF | https://variety.com/2026/film/news/andrew-scott-tiff-elsinore-gay-actors-prejudice-fleabag-1236859840/
2026-09-13 | Global | The Hollywood Reporter | John Cho on Playing the Villain in Action Movie Your Mother Your Mother Your Mother | https://www.hollywoodreporter.com/movies/movie-features/your-mother-your-mother-your-mother-john-cho-interview-1236698846/
2026-09-13 | Global | Deadline | Huge Job Losses & Economic Pain If Paramount Exits LA, County Report Says | https://deadline.com/2026/09/paramount-job-losses-california-exit-antitrust-lawsuit-1237099942/
2026-09-13 | Global | Billboard | Stray Kids Drives Fans Wild in Historic Rock in Rio Debut | https://www.billboard.com/music/music-news/stray-kids-rock-in-rio-brazil-debut-review-recap-1236338948/
