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
2026-07-31 | Saudi Arabia/Regional | The New York Times | Saudi Arabia Aims to Deter Red Sea Attacks With New Coalition | https://www.nytimes.com/2026/07/30/world/middleeast/saudi-arabia-red-sea-houthis.html
2026-07-31 | Saudi Arabia/Regional | The Guardian | Saudi Arabia prepares sea and possible land offensive against Houthis | https://www.theguardian.com/world/2026/jul/30/saudi-forces-planning-major-offensive-against-houthis-central-yemen
2026-07-31 | Saudi Arabia/Regional | AGBI | Saudi economy shrinks for first time in three years | https://www.agbi.com/analysis/economy/2026/07/saudi-economy-shrinks-first-time-in-three-years-as-oil-output-drops/
2026-07-31 | Saudi Arabia/Regional | Bloomberg | Saudi Budget Deficit Narrows Three-Quarters on Wartime Oil Spike | https://www.bloomberg.com/news/articles/2026-07-30/saudi-budget-deficit-narrows-three-quarters-on-wartime-oil-spike
2026-07-31 | Saudi Arabia/Regional | Al-Monitor | The Red Sea's shared history comes alive in Jeddah | https://www.al-monitor.com/newsletter/2026-07-30/red-seas-shared-history-comes-alive-jeddah
2026-07-31 | Negative Articles | BBC | 'End this nightmare': Wife of ailing Briton jailed in Saudi Arabia appeals for release | https://www.bbc.co.uk/news/articles/ckg4jxxn4ggo
2026-07-31 | Negative Articles | Antiwar.com | Al-Houthi Says There Are Indications Saudi Arabia Is Planning Major Escalation in Yemen | https://news.antiwar.com/2026/07/30/al-houthi-says-there-are-indications-saudi-arabia-is-planning-major-escalation-in-yemen/
2026-07-31 | Global | Arkeonews | LiDAR Reveals Up to 30,000 Earthworks Built by a Lost Amazonian Civilization | https://arkeonews.net/lidar-reveals-up-to-30000-earthworks-built-by-a-lost-amazonian-civilization/
2026-07-31 | Global | Arkeonews | Archaeologists Unearth Two Miniature Mammoth Ivory Birds Carved 40,000 Years Ago | https://arkeonews.net/archaeologists-unearth-two-miniature-mammoth-ivory-birds-carved-40000-years-ago/
2026-07-31 | Global | Archaeology Magazine | Possible Marks of Cannibalism Detected on Adult Homo Antecessor Fossils | https://archaeology.org/news/2026/07/30/possible-marks-of-cannibalism-detected-on-adult-homo-antecessor-fossils/
2026-07-31 | Global | The Art Newspaper | Treasures from Ancient Egypt's 'Golden City', and the stories of the people who made them, revealed in San Francisco show | https://www.theartnewspaper.com/2026/07/30/life-and-treasure-from-ancient-egypts-golden-city-revealed-in-san-francisco-show
2026-07-31 | Global | The Art Newspaper | 'Amazon-style' conditions: Prospect union members overwhelmingly vote to strike at London's V&A museums | https://www.theartnewspaper.com/2026/07/30/amazon-style-conditions-va-east-storehouse-officers-overwhelmingly-vote-to-strike-as-other-museum-workers-also-consider-industrial-action
2026-07-31 | Global | Artnet News | Will Tariff Tensions Ebb for the Art Trade? And Other Art World Matters | https://news.artnet.com/artnet-bulletin/new-tariffs-july-30-2790904
2026-07-31 | Global | The Art Newspaper | The Obama Presidential Center aims high, like a Gothic cathedral | https://www.theartnewspaper.com/2026/07/30/comment-obama-presidential-center-art-architecture-gothic-cathedral
2026-07-31 | Global | The Hollywood Reporter | 'Clueless' Sequel Series Moving Forward at Paramount+ | https://www.hollywoodreporter.com/tv/tv-news/clueless-sequel-series-paramount-1236659500/
2026-07-31 | Global | Deadline | 'Wicker' Trailer: Olivia Colman & Alexander Skarsgård Upend Quiet Village | https://deadline.com/2026/07/wicker-trailer-olivia-colman-alexander-skarsgard-1237013463/
