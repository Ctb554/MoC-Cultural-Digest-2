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

2026-07-26 | Saudi Arabia/Regional | Bloomberg | Houthi Claim Missile Strikes on Southern Saudi Arabia | https://www.bloomberg.com/news/articles/2026-07-25/houthi-claim-missile-strikes-on-southern-saudi-arabia
2026-07-26 | Saudi Arabia/Regional | CNBC | Saudi military strikes Houthi targets in Yemen after Iran-backed militia attacked Red Sea shipping | https://www.cnbc.com/2026/07/25/saudi-military-strikes-iran-backed-houthi-targets-yemen.html
2026-07-26 | Saudi Arabia/Regional | Bloomberg | Iran War: US Pauses Strikes as Houthi Attacks Threaten Saudi Oil Routes | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-26 | Negative Articles | Middle East Eye | Houthis say Saudi attack on Hodeidah will lead to 'escalation for escalation' | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-26 | Negative Articles | Fox News | 'Weird Al' Yankovic says he walked away from a seven-figure comedy festival offer in Saudi Arabia | https://www.foxnews.com/media/weird-al-yankovic-says-he-walked-away-from-seven-figure-comedy-festival-offer-saudi-arabia
2026-07-26 | Global | Arkeonews | Roman Gold, Barracks and Surgical Tools Unearthed at Vindonissa's First Military Camp in Switzerland | https://arkeonews.net/roman-gold-barracks-and-surgical-tools-unearthed-at-vindonissas-first-military-camp-in-switzerland/
2026-07-26 | Global | Arkeonews | 5,000-Year-Old Bronze Age Temple with Altars and Sacred Hearths Discovered in Eastern Türkiye | https://arkeonews.net/5000-year-old-bronze-age-temple-with-altars-and-sacred-hearths-discovered-in-eastern-turkiye/
2026-07-26 | Global | HeritageDaily | Heatwave reveals lost Welsh landscapes | https://www.heritagedaily.com/2026/07/heatwave-reveals-lost-welsh-landscapes/158718
2026-07-26 | Global | The Stage | RSC cancels Game of Thrones play preview hours before curtain up | https://www.thestage.co.uk/news/rsc-cancels-game-of-thrones-play-preview-performances
2026-07-26 | Global | The Hollywood Reporter | 'Black Panther 3': David Jonsson to Star as T'Challa's Son, Sequel Set for 2028 | https://www.hollywoodreporter.com/movies/movie-news/black-panther-3-marvel-ryan-coogler-comic-con-1236656570/
2026-07-26 | Global | Deadline | Ryan Gosling Unveiled As Next Ghost Rider at Marvel's Comic-Con Panel | https://deadline.com/2026/07/ryan-gosling-ghost-rider-marvel-comic-con-1237003726/
2026-07-26 | Global | WWD | Michelle Yeoh and Hunter Schafer Go Designer at Comic-Con | https://wwd.com/pop-culture/celebrity-news/michelle-yeoh-hunter-schafer-comic-con-outfits-1239081924/
