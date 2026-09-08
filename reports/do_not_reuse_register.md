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
2026-09-08 | Saudi Arabia/Regional | A&E Magazine | Diriyah Art Futures launches CONTINUUM '26 exhibition in Riyadh | https://aeworld.com/lifestyle/art/diriyah-art-futures-launches-continuum-26-exhibition-in-riyadh
2026-09-08 | Negative Articles | BBC | Did the FBI bury evidence of alleged Saudi agent's role in 9/11? | https://www.bbc.co.uk/news/articles/cr4vn1e207go
2026-09-08 | Negative Articles | Al-Monitor | Saudi-led coalition in Yemen says 73 injured in Houthi attacks on the kingdom | https://www.al-monitor.com/originals/2026/09/saudi-led-coalition-yemen-says-73-injured-houthi-attacks-kingdom
2026-09-08 | Negative Articles | Middle East Eye | Yemen's Houthis accuse Saudi Arabia of air raids, missile strikes | https://www.middleeasteye.net/live-blog/live-blog-update/yemens-houthis-accuse-saudi-arabia-air-raids-missile-strikes
2026-09-08 | Global | Dezeen | Design overtakes retail as biggest contributor to UK economy | https://www.dezeen.com/2026/09/07/design-council-economy-report/
2026-09-08 | Global | ArchDaily | Madrid Region and the City of Leganes launch open urban design contest | https://www.archdaily.com/1184667/madrid-region-and-the-city-of-leganes-launch-an-open-call-urban-design-contest-for-the-new-puerta-de-madrid-sustainable-district-in-leganes-madrid
2026-09-08 | Global | Deadline | MPA signs two declarations at Lumiere Summit, attends roundtables with Macron and Lee Jae Myung | https://deadline.com/2026/09/mpa-signs-declarations-lumiere-summit-1237070415/
2026-09-08 | Global | Variety | Prada Foundation Film Fund chief Paolo Moretti on first-year journey | https://variety.com/2026/film/global/prada-film-fund-paolo-moretti-rubaiyat-venice-bride-1236853486/
2026-09-08 | Global | Variety | Korea box office: The Odyssey overwhelms Spider-Man Brand New Day as admissions top 10 million | https://variety.com/2026/film/box-office/korea-box-office-the-odyssey-spider-man-brand-new-day-the-intern-1236854398/
2026-09-08 | Global | Billboard | Radiohead announce first Australian tour in 15 years with 16 arena shows | https://www.billboard.com/music/music-news/radiohead-announce-australia-tour-2027-1236335276/
2026-09-08 | Global | Billboard | ARIA Award for Best Music Festival returns for second year | https://www.billboard.com/pro/aria-award-best-music-festival-returns/
2026-09-08 | Global | WWD | Sofia Bertolli Balestra launches global call to rediscover Renato Balestra couture | https://wwd.com/fashion-news/designer-luxury/sofia-bertolli-balestra-global-call-rediscover-couture-1239194640/
