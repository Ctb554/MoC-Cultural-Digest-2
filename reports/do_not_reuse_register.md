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

2026-08-15 | Saudi Arabia/Regional | Reuters via BOE Report | Houthis say they targeted Aramco in Saudi Arabia's Najran with drone | https://boereport.com/2026/08/14/houthis-say-they-targeted-aramco-in-saudi-arabias-najran-with-drone/
2026-08-15 | Saudi Arabia/Regional | Al Jazeera | Yemen's government says Houthi attack on al-Makha kills at least four | https://www.aljazeera.com/news/2026/8/14/yemens-government-says-houthi-attack-on-al-makha-kills-at-least-four
2026-08-15 | Saudi Arabia/Regional | Al-Monitor | Saudi Arabia bets on defensive alliances to deter slide into war | https://www.al-monitor.com/originals/2026/08/analysis-saudi-arabia-bets-defensive-alliances-deter-slide-war
2026-08-15 | Saudi Arabia/Regional | AGBI | Saudi Arabia replaces head of capital markets regulator | https://www.agbi.com/finance/2026/08/saudi-arabia-replaces-head-of-capital-markets-regulator/
2026-08-15 | Negative Articles | Press TV | Saudi-linked targets come under fresh heavy strikes by Yemen's Armed Forces | https://www.presstv.co.uk/Detail/2026/08/14/774366/Yemen-strikes-Saudi-Arabia-targets-mercenaries
2026-08-15 | Global | The Art Newspaper | Stolen Cezanne, Matisse and Renoir paintings recovered in Italy | https://www.theartnewspaper.com/2026/08/14/stolen-cezanne-matisse-renoir-paintings-recovered-in-italy
2026-08-15 | Global | The Art Newspaper | Camden Art Centre director Martin Clark to step down and lead Towner Eastbourne | https://www.theartnewspaper.com/2026/08/14/camden-art-centre-director-martin-clark-to-step-down-and-lead-towner-eastbourne
2026-08-15 | Global | The Art Newspaper | Chinese museums ordered to strengthen emergency protocols following blackouts and incidents of overcrowding | https://www.theartnewspaper.com/2026/08/14/chinese-museums-ordered-to-strengthen-emergency-protocols-following-blackouts-and-incidents-of-overcrowding
2026-08-15 | Global | FAD Magazine | British Museum to explore 2,000 years of Korean art as K-culture goes global | https://fadmagazine.com/2026/08/14/korean-art-british-museum-2026/
2026-08-15 | Global | Arkeonews | Rare 2,000-year-old Kushan royal seal discovered in Tajikistan | https://arkeonews.net/rare-2000-year-old-kushan-royal-seal-discovered-in-tajikistan/
2026-08-15 | Global | Arkeonews | Older Bronze Age burial found beneath Viking ship grave in Norway | https://arkeonews.net/older-bronze-age-burial-found-beneath-viking-ship-grave-in-norway/
2026-08-15 | Global | UPI via Yahoo News | Phoebe Bridgers releases 'Lost Weekend' album featuring 'I Can't Wait' | https://ca.news.yahoo.com/phoebe-bridgers-releases-lost-weekend-132853127.html
