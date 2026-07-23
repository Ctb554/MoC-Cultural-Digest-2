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

2026-07-23 | Saudi Arabia/Regional | AP via PBS NewsHour | Trump approves nuclear agreement that may allow Saudi Arabia to enrich uranium | https://www.pbs.org/newshour/world/ap-report-trump-approves-nuclear-agreement-that-may-allow-saudi-arabia-to-enrich-uranium
2026-07-23 | Saudi Arabia/Regional | The New York Times | Houthis Claim Strikes on 2 Saudi Oil Tankers in Red Sea | https://www.nytimes.com/2026/07/22/world/middleeast/houthis-saudi-oil-tankers-red-sea.html
2026-07-23 | Saudi Arabia/Regional | Al-Monitor | Saudi nuclear deal delivers strategic economic prizes as Trump boosts Gulf allies | https://www.al-monitor.com/originals/2026/07/saudi-nuclear-deal-delivers-strategic-economic-prizes-trump-boosts-gulf-allies
2026-07-23 | Negative Articles | Middle East Eye | Trump to approve nuclear deal with Saudi Arabia despite regional proliferation risks | https://www.middleeasteye.net/news/trump-to-approve-nuclear-deal-saudi-arabia-despite-regional-proliferation-risks
2026-07-23 | Negative Articles | Press TV | Yemen says retaliatory naval operations against Saudi targets to continue under 'siege for a siege' policy | https://www.presstv.co.uk/Detail/2026/07/22/772814/Yemen-Saudi-Arabia-ships-blockade-warning
2026-07-23 | Negative Articles | AGBI | Deserted island: what happened at Sindalah and what's next | https://www.agbi.com/giga-projects/2026/07/deserted-island-what-happened-at-neom-sindalah-and-whats-next/
2026-07-23 | Global | ARTnews | The Louvre's Apollo Gallery Reopens, This Time Without Any Crown Jewels | https://www.artnews.com/art-news/news/louvre-apollo-gallery-reopens-without-crown-jewels-1234793182/
2026-07-23 | Global | The Art Newspaper | Jessica Morgan named new Tate director | https://www.theartnewspaper.com/2026/07/22/jessica-morgan-named-new-tate-director
2026-07-23 | Global | The Art Newspaper | European Union officially pulls €2m Venice Biennale funding over Russian participation | https://www.theartnewspaper.com/2026/07/22/european-union-officially-pull-2m-venice-biennale-funding-over-russian-participation
2026-07-23 | Global | The Art Newspaper | Artforum bids farewell to back-cover star in style | https://www.theartnewspaper.com/2026/07/22/artforum-bids-farewell-to-back-cover-star-in-style
2026-07-23 | Global | Deadline | BAFTA Expands Outstanding British Film Longlist & Adds AI Clause To Submission Rules | https://deadline.com/2026/07/bafta-ai-clause-submission-rules-2027-1237000067/
2026-07-23 | Global | The Hollywood Reporter | 'The Odyssey' Proves It: Audiences Want Movies Made the Hard Way | https://www.hollywoodreporter.com/movies/movie-news/odyssey-box-office-2026-practical-effects-1236652219/
2026-07-23 | Global | The Korea Herald | Hyolyn channels Y2K nostalgia on 'OriginaLyn' | https://www.koreaherald.com/article/10815414
2026-07-23 | Global | Publishers Weekly | How Holt Crashed Mahmoud Khalil's Memoir in Six Months | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/100890-how-holt-finished-mahmoud-khalil-s-no-land-to-stand-on-in-just-six-months.html
2026-07-23 | Global | HeritageDaily | New study reveals how Cypriot goldsmiths united four ancient cultures | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-23 | Global | Designboom | SANAA-led team wins Ecuador national museum competition after revised selection process | https://www.designboom.com/architecture/sanaa-team-ecuador-national-museum-muna-competition-revised-selection-process-estudioa0-caaporarq-jeromehaferdstudio/
