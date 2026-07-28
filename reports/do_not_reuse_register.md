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

2026-07-28 | Saudi Arabia/Regional | The New York Times | How the Houthis Cornered Saudi Arabia Into a New Battle | https://www.nytimes.com/2026/07/27/world/middleeast/houthis-saudi-arabia-iran-war.html
2026-07-28 | Saudi Arabia/Regional | The Guardian | Asia 'scraping the bottom of the barrel' as Red Sea oil blockade worsens energy crisis | https://www.theguardian.com/world/2026/jul/28/asia-energy-oil-crisis-red-sea-blockade-houthis
2026-07-28 | Saudi Arabia/Regional | CNBC | Iran hosts Hormuz calls with Saudi Arabia, Oman as Trump hails 'good talks' | https://www.cnbc.com/2026/07/28/us-iran-war-trump-hormuz.html
2026-07-28 | Negative Articles | Foreign Policy | Trump's Saudi Nuclear Deal Is Diplomatic Malpractice | https://foreignpolicy.com/2026/07/27/trump-nuclear-saudi-arabia-deal-iran-israel/
2026-07-28 | Global | Tech Times | D-Day Beaches, Okefenokee Swamp, Mount Olympus Join UNESCO World Heritage List | https://www.techtimes.com/articles/321672/20260727/d-day-beaches-okefenokee-swamp-mount-olympus-join-unesco-world-heritage-list.htm
2026-07-28 | Global | Archaeology News | First Roman camp at Vindonissa revealed through new excavation of walls, barracks, and artifacts | https://archaeologymag.com/2026/07/first-roman-camp-at-vindonissa-revealed/
2026-07-28 | Global | Archaeology Magazine | Roman Battle Camp Found in Spain | https://archaeology.org/news/2026/07/27/roman-battle-camp-found-in-spain/
2026-07-28 | Global | ARTnews | Betye Saar, Pioneering Assemblage Artist Who Powerfully Tackled Racism, Dies at 99 | https://www.artnews.com/art-news/news/betye-saar-dead-1234793560/
2026-07-28 | Global | Dezeen | RSHP unveils tripartite Shanghai skyscraper informed by historical laneways | https://www.dezeen.com/2026/07/27/rshps-one-shanghai-tower/
