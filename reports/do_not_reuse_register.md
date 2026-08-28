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

2026-08-28 | Saudi Arabia/Regional | Al-Monitor | AlUla brings Saudi creativity to Paris | https://www.al-monitor.com/newsletter/2026-08-27/alula-brings-saudi-creativity-paris
2026-08-28 | Negative Articles | New York Times | Saudi Response to Houthis' Attacks on Ships May Be a New War | https://www.nytimes.com/2026/08/27/world/middleeast/saudi-arabia-yemen-houthis-war.html
2026-08-28 | Negative Articles | TASS | Saudi Arabia preparing for new war with Houthis in Yemen — media | https://tass.com/world/2178491
2026-08-28 | Negative Articles | Al Jazeera | World Cup 2034 hosts Saudi Arabia back Infantino amid FIFA crisis | https://www.aljazeera.com/sports/2026/8/27/world-cup-2034-hosts-saudi-arabia-back-infantino-amid-fifa-crisis
2026-08-28 | Global | Al Jazeera | Yayoi Kusama, Japan's 'queen of polka dots', dies at 97 | https://www.aljazeera.com/news/2026/8/27/yayoi-kusama-japans-queen-of-polka-dots-dies-at-97
2026-08-28 | Global | The Art Newspaper | Founders of alternative art fair Basel Social Club to launch new event in Tokyo | https://www.theartnewspaper.com/2026/08/27/alternative-art-fair-basel-social-club-to-launch-new-event-tokyo
2026-08-28 | Global | ARTnews | $1.98 M. Worth of Gold Pieces Stolen From the Treasure of Villena | https://www.artnews.com/art-news/news/gold-pieces-stolen-from-the-treasure-of-villena-1234796080/
2026-08-28 | Global | Arkeonews | Monumental Herakles Gate with 1,800-Year-Old Reliefs Unearthed at Ancient Side | https://arkeonews.net/monumental-herakles-gate-with-1800-year-old-reliefs-unearthed-at-ancient-side/
2026-08-28 | Global | Arkeonews | Russia's Largest Intact Medieval Coin Hoard Found with 2,600 Silver Coins | https://arkeonews.net/russias-largest-intact-medieval-coin-hoard-found-with-2600-silver-coins/
2026-08-28 | Global | The Art Newspaper | Monumental Noguchi sculpture donated to the New Orleans Museum of Art | https://www.theartnewspaper.com/2026/08/27/monumental-isamu-noguchi-sculpture-donated-moving-new-orleans-museum-art-mississippi-fountain
2026-08-28 | Global | The Art Newspaper | Chief executive of Sydney's anticipated Parramatta Powerhouse museum steps down two months before grand opening | https://www.theartnewspaper.com/2026/08/27/chief-executive-of-sydneys-anticipated-parramatta-powerhouse-museum-steps-down-two-months-before-grand-opening
2026-08-28 | Global | WWD | CFDA Releases Preliminary Official New York Fashion Week Schedule for Spring 2027 Season | https://wwd.com/fashion-news/designer-luxury/cfda-official-new-york-fashion-week-schedule-1239047705/
