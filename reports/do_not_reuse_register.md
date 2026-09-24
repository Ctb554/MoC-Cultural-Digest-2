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
2026-09-24 | Saudi Arabia/Regional | Lifestyle & Tech | Saudi Film Nights brings contemporary Saudi cinema to South Africa this October | https://lifestyleandtech.co.za/just-life/article/2026-09-23/saudi-film-nights-brings-contemporary-saudi-cinema-to-south-africa-this-october
2026-09-24 | Saudi Arabia/Regional | Emirates Woman | 4 Saudi princesses shaping the kingdom's fashion landscape | https://emirateswoman.com/4-saudi-arabian-princesses-shaping-the-kingdoms-fashion-landscape/
2026-09-24 | Saudi Arabia/Regional | Khaleej Times | From fighter jets to cultural shows: How Saudi Arabia is celebrating its 96th National Day | https://www.khaleejtimes.com/world/mena/from-fighter-jets-to-fireworks-how-saudi-arabia-is-celebrating-its-96th-national-day
2026-09-24 | Saudi Arabia/Regional | Emirates Woman | Saudi National Day: 5 experiences to discover across the Kingdom | https://emirateswoman.com/saudi-national-day-5-experiences-to-discover-across-the-kingdom/
2026-09-24 | Negative Articles | The Manila Times | Riyadh attacks key port city - Houthis | https://www.manilatimes.net/2026/09/23/world/americas-emea/riyadh-attacks-key-port-city-houthis/2430315
2026-09-24 | Negative Articles | Al Jazeera | How much is UK supporting Saudi Arabia in its war with Iran-backed Houthis? | https://www.aljazeera.com/news/2026/9/23/how-much-is-uk-supporting-saudi-arabia-in-its-war-with-iran-backed-houthis
2026-09-24 | Global | The Art Newspaper | British Museum bans visitors from photographing Bayeux Tapestry | https://www.theartnewspaper.com/2026/09/23/british-museum-bans-visitors-from-photographing-bayeux-tapestry
2026-09-24 | Global | The Art Newspaper | AI can strengthen human connections to museums, report suggests | https://www.theartnewspaper.com/2026/09/23/ai-can-strengthen-human-connections-to-museums-report-suggests
2026-09-24 | Global | Archaeology Magazine | U.S. Repatriates Looted Objects to Greece | https://archaeology.org/news/2026/09/23/u-s-repatriates-looted-objects-to-greece/
2026-09-24 | Global | HeritageDaily | Intact burials at Gobeklitepe reveal new clues to 11,000-year-old burial rituals | https://www.heritagedaily.com/2026/09/intact-burials-at-gobeklitepe-reveal-new-clues-to-11000-year-old-burial-rituals/159391
2026-09-24 | Global | The Hollywood Reporter | Phil Lord and Chris Miller Tapped as Guest Artistic Directors for AFI Fest 2026 | https://www.hollywoodreporter.com/movies/movie-news/phil-lord-chris-miller-guest-artistic-directors-afi-fest-1236708523/
2026-09-24 | Global | Billboard | Taylor Swift Announces 'The Life of a Showgirl: The Encore' Album Featuring Newly Recorded Tracks | https://www.billboard.com/music/pop/taylor-swift-life-of-a-showgirl-the-encore-album-new-songs-1236345267/
2026-09-24 | Global | The Business of Fashion | Chanel Plans to Keep Investing in China Despite Demand Downturn | https://www.businessoffashion.com/news/global-markets/chanel-plans-to-keep-investing-in-china-despite-demand-downturn/
2026-09-24 | Global | ArchDaily | BIG's Macondo Park Opens as a Temporary Cultural Landscape for Shakira's Madrid Residency | https://www.archdaily.com/1185625/bigs-macondo-park-opens-as-a-temporary-cultural-landscape-for-shakiras-madrid-residency
2026-09-24 | Global | The Stage | Oldham Coliseum and Bolton Octagon among £15m Manchester culture fund recipients | https://www.thestage.co.uk/news/oldham-coliseum-and-bolton-octagon-among-15m-manchester-culture-fund-recipients
2026-09-24 | Global | Publishers Weekly | YALLFest Adds Adult Romance Programming | https://www.publishersweekly.com/pw/by-topic/industry-news/trade-shows-events/article/101323-yallfest-adds-adult-romance-programming.html
