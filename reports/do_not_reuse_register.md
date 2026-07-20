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
2026-07-20 | Saudi Arabia/Regional | AGBI | Saudi Arabia launches multiple-entry Umrah visa | https://www.agbi.com/tourism/2026/07/saudi-arabia-launches-multiple-entry-umrah-visa/
2026-07-20 | Saudi Arabia/Regional | AGBI | Riyadh Air adds 34 Boeing and Airbus jets to fleet plans | https://www.agbi.com/aviation/2026/07/riyadh-air-adds-34-boeing-and-airbus-jets-to-fleet-plans/
2026-07-20 | Saudi Arabia/Regional | The National | Houthis say they will impose 'maritime embargo' against Saudi Arabia in retaliation for Yemen blockade | https://www.thenationalnews.com/news/2026/07/20/houthis-announce-maritime-ban-on-saudi-arabia-citing-blockade-of-yemen/
2026-07-20 | Global | The Korea Herald | UNESCO World Heritage Committee opens in Busan, a first for Korea | https://www.koreaherald.com/article/10812733
2026-07-20 | Global | Taipei Times | UNESCO to list sites 'under threat' of war, climate change | https://www.taipeitimes.com/News/world/archives/2026/07/19/2003861013
2026-07-20 | Global | The Art Newspaper | Union threatens strike action over working conditions in Venice museums due to extreme temperatures | https://www.theartnewspaper.com/2026/07/20/union-threatens-strike-action-over-working-conditions-in-venice-museums-due-to-extreme-temperatures
2026-07-20 | Global | South China Morning Post | Hong Kong jewellery artist Wallace Chan brings his 'Vessels of Other Worlds' exhibition from Venice to Shanghai | https://www.scmp.com/magazines/style/lifestyle/design/article/3361161/hong-kong-jewellery-artist-wallace-chan-brings-his-vessels-other-worlds-exhibition-venice-shanghai
2026-07-20 | Global | The Hollywood Reporter | 'The Odyssey' Smashes 'Star Wars' Record Over London's BFI Imax Opening Weekend | https://www.hollywoodreporter.com/movies/movie-news/the-odyssey-bfi-imax-record-screening-film-nolan-tickets-1236652045/
2026-07-20 | Global | The Korea Herald | Will 'A Shop for Killers' 2 find room to shine amid K-action drama boom? | https://www.koreaherald.com/article/10813838
2026-07-20 | Global | The Art Newspaper | As Andy Burnham becomes the new UK prime minister, here are five key challenges facing his culture ministry | https://www.theartnewspaper.com/2026/07/20/as-andy-burnham-becomes-the-new-uk-prime-minister-here-are-five-key-challenges-facing-his-culture-ministry
