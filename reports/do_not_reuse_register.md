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

2026-07-20 | Saudi Arabia/Regional | Al-Monitor | Houthis impose Saudi naval blockade, opening new front in US-Iran war | https://www.al-monitor.com/originals/2026/07/houthis-impose-saudi-naval-blockade-opening-new-front-us-iran-war
2026-07-20 | Saudi Arabia/Regional | Business Standard | What Wall Street never understood about Gulf investors and their priorities | https://www.business-standard.com/world-news/what-wall-street-never-understood-about-gulf-investors-and-their-priorities-126072000259_1.html
2026-07-20 | Risks and Opportunities | CNBC | Iran's Houthi allies declare maritime embargo against Saudi Arabia, escalating threat to oil market | https://www.cnbc.com/2026/07/20/iran-houthi-yemen-saudi-arabia.html
2026-07-20 | Global | The Korea Herald | UNESCO World Heritage Committee opens in Busan, a first for Korea | https://www.koreaherald.com/article/10812733
2026-07-20 | Global | The Japan Times | U.N. to list more sites as 'in danger' from conflict or climate change | https://www.japantimes.co.jp/environment/2026/07/20/climate-change/un-danger-conflict-climate-change/
2026-07-20 | Global | Arkeonews | World's Oldest Nearly Complete Roman Armor May Preserve the Fate of a Captured Legionary | https://arkeonews.net/worlds-oldest-nearly-complete-roman-armor-may-preserve-the-fate-of-a-captured-legionary/
2026-07-20 | Global | Arkeonews | 1,000-Year-Old Scandinavian-Style Houses Discovered in Poland's Viking-Age Wolin | https://arkeonews.net/1000-year-old-scandinavian-style-houses-discovered-in-polands-viking-age-wolin/
2026-07-20 | Global | Deadline | Box Office Global: 'The Odyssey' $257M Bow A Record for Christopher Nolan | https://deadline.com/2026/07/box-office-global-the-odyssey-1236996979/
2026-07-20 | Global | Variety | Future Debuts at No. 1 With 'The Real Me,' as Rolling Stones and 'Heated Rivalry' Soundtrack Also Bow in Top 10 | https://variety.com/2026/music/news/future-album-billbord-chart-number-one-rolling-stones-1236816201/
2026-07-20 | Global | Publishing Perspectives | Around the Book World: Monday, July 20th, 2026 | https://publishingperspectives.com/2026/07/around-the-book-world-monday-july-20th-2026/
