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
2026-07-27 | Saudi Arabia/Regional | The Guardian | The Guardian view on a US-Saudi nuclear agreement: an offer that further erodes international safeguards | https://www.theguardian.com/commentisfree/2026/jul/26/the-guardian-view-on-a-us-saudi-nuclear-agreement-an-offer-that-further-erodes-international-safeguards
2026-07-27 | Saudi Arabia/Regional | Bloomberg | Iran War: US Pauses Strikes as Houthi Attacks Threaten Saudi Oil Routes | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-27 | Saudi Arabia/Regional | WWD | EXCLUSIVE: Saudi Arabia to Showcase Fashion, Food in 'Immersive' Display at Selfridges' Corner Shop | https://wwd.com/business-news/retail/saudi-arabia-fashion-food-design-selfridges-corner-shop-1239081869/
2026-07-27 | Negative Articles | Al Jazeera | New front in US-Iran war escalates as Houthis fire at Saudi oil facilities | https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities
2026-07-27 | Global | Associated Press | UNESCO adds France's D-Day landing beaches, Greece's Mount Olympus to World Heritage List | https://apnews.com/article/unesco-mount-olympus-japan-ancient-capitals-1d3fabaa482d9384b1cb0b5c917ce5d5
2026-07-27 | Global | The Art Newspaper | Earthquake damages 16th-century church in Peru | https://www.theartnewspaper.com/2026/07/27/peru-earthquake-damages-16th-century-church-iglesia-apostol-santiago
2026-07-27 | Global | CNN | Fungi fashion: Could mushrooms and seaweed be on tomorrow's catwalk? | https://www.cnn.com/2026/07/26/world/video/fungi-leather-farm-indonesia-transformers-hkn-spc
2026-07-27 | Global | Fashionista | See the Provisional Schedule for Paris Fashion Week Spring 2027 | https://fashionista.com/2026/07/paris-fashion-week-september-2026-schedule
2026-07-27 | Global | Newsweek | 118-Year-Old NYC Skyscraper's Interiors Finally Visualised | https://www.newsweek.com/antoni-gaudi-118-year-old-lost-nyc-skyscraper-design-interiors-unveiled-12240546
