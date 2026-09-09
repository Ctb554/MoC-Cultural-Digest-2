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

2026-09-09 | Saudi Arabia/Regional | Muslim Network TV | Saudi experts explore how geography shaped cultural identity | https://www.muslimnetwork.tv/saudi-experts-explore-how-geography-shaped-cultural-identity/
2026-09-09 | Saudi Arabia/Regional | Design Middle East | Ithra Opens Registration for 2026 Design Challenges | https://design-middleeast.com/ithra-opens-registration-for-2026-design-challenges/
2026-09-09 | Saudi Arabia/Regional | eHotelier | Red Sea Global unveils Nammos Resort AMAALA, introducing Nammos' first resort hotel globally | https://insights.ehotelier.com/properties/2026/09/09/red-sea-global-unveils-nammos-resort-amaala-introducing-nammos-first-resort-hotel-globally/
2026-09-09 | Negative Articles | BBC | Saudi Arabia vows to respond after Houthis attack cities and energy facilities | https://www.bbc.co.uk/news/articles/cp849n2nz01o
2026-09-09 | Negative Articles | Bloomberg | Saudi Arabia Says Several Energy Sites Halted After Attacks | https://www.bloomberg.com/news/articles/2026-09-08/saudi-arabia-says-several-energy-sites-halted-after-attacks
2026-09-09 | Negative Articles | The Guardian | British family of man abducted by Saudi Arabia speak out over nine-year ordeal | https://www.theguardian.com/world/2026/sep/08/rami-naimi-abducted-saudi-arabia-mira-lozi
2026-09-09 | Negative Articles | Middle East Eye | Houthis target Saudi Arabia following air strikes as Yemeni forces push towards Sanaa | https://www.middleeasteye.net/news/yemen-forces-push-toward-sanaa-fighting-houthis-intensifies
2026-09-09 | Negative Articles | Semafor | Saudi wealth fund takes its capital pitch to Wall Street | https://www.semafor.com/article/09/08/2026/saudi-wealth-fund-takes-its-capital-pitch-to-wall-street
2026-09-09 | Global | Al Jazeera | Renoir paintings stolen from museum in southern France | https://www.aljazeera.com/news/2026/9/8/three-paintings-worth-10m-stolen-from-renoir-museum-in-southern-france
2026-09-09 | Global | ARTnews | Jenny Holzer and Andy Goldsworthy Win $95,000 Praemium Imperiale Award | https://www.artnews.com/art-news/news/jenny-holzer-and-andy-goldsworthy-win-95000-praemium-imperiale-1234797291/
2026-09-09 | Global | Arkeonews | 4,400-Year-Old Tomb of an Egyptian Judge Found at Saqqara with Colors Still on the Walls | https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/
2026-09-09 | Global | Archaeology Magazine | Lavish Roman Bath Excavated in Eastern Serbia | https://archaeology.org/news/2026/09/08/lavish-roman-bath-excavated-in-eastern-serbia/
2026-09-09 | Global | WWD | Milan Fashion Week September 2026 Edition: What to Know | https://wwd.com/fashion-news/fashion-features/milan-fashion-week-september-2026-schedule-shows-presentations-1239201148/
2026-09-09 | Global | ArchDaily | IXCAMPUS / Baumschlager Eberle Architekten | https://www.archdaily.com/1184644/ixcampus-baumschlager-eberle-architekten
2026-09-09 | Global | TheWrap | The Summer Box Office Blew Past Records. But Can Theaters Sustain the Momentum? | https://www.thewrap.com/creative-content/movies/summer-box-office-2026-success-explained-spider-man-odyssey/
