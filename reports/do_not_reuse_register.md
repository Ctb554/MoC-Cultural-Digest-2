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
2026-09-27 | Saudi Arabia/Regional | Masrawy | 7Dogs becomes the first Arab film to sell one million tickets in Saudi cinemas | https://www.masrawy.com/arts/zoom/details/2026/9/26/3054191/
2026-09-27 | Saudi Arabia/Regional | ANTARA News | Indonesia eyes expanding fashion market share in Saudi Arabia | https://en.antaranews.com/news/432947/indonesia-eyes-expanding-fashion-market-share-in-saudi-arabia
2026-09-27 | Saudi Arabia/Regional | Youm7 | Saudi Embassy in Cairo celebrates Saudi coffee for the 96th National Day | https://www.youm7.com/story/2026/9/26/%D8%B3%D9%81%D8%A7%D8%B1%D8%A9-%D8%A7%D9%84%D9%85%D9%85%D9%84%D9%83%D8%A9-%D8%AA%D8%AD%D8%AA%D9%81%D9%89-%D8%A8%D8%A7%D9%84%D9%82%D9%87%D9%88%D8%A9-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9/7558232
2026-09-27 | Saudi Arabia/Regional | Business Today Middle East | Riyadh Season 2026 Launches October 21, GEA Chairman Announces | https://businesstoday.me/news/riyadh-season-2026-launches-october-21-gea-chairman-announces/
2026-09-27 | Negative Articles | Press TV | Yemeni military spokesman: Saudi warplanes carry out 27 airstrikes across Yemen | https://www.presstv.co.uk/Detail/2026/09/26/777077/Yemen-Yahya-Saree-Saudi-warplanes-launch-airstrikes-target-bridges-civilian-infrastructure
2026-09-27 | Global | Arkeonews | A Planned Roman City With an 8,000-Seat Amphitheater Discovered in Austria | https://arkeonews.net/a-planned-roman-city-with-an-8000-seat-amphitheater-discovered-in-austria/
2026-09-27 | Global | Arkeonews | 16 New Rock Art Panels Discovered at Sweden's Tanum World Heritage Site, Including a Huge One | https://arkeonews.net/16-new-rock-art-panels-discovered-at-swedens-tanum-world-heritage-site-including-a-huge-one/
2026-09-27 | Global | Arkeonews | Meet Apollo, the First AI That Reads Ancient Greek | https://arkeonews.net/meet-apollo-the-first-ai-that-reads-ancient-greek/
2026-09-27 | Global | Arkeonews | Europe's Earliest Beer? 6,500-Year-Old Malt Found at Solnitsata | https://arkeonews.net/europes-earliest-beer-6500-year-old-malt-found-at-solnitsata/
2026-09-27 | Global | Business of Fashion | Milan Day Five: Identity Matters | https://www.businessoffashion.com/reviews/fashion-week/ferragamo-dolce-gabbana-bottega-veneta-act-n1-autumn-winter-2026/
2026-09-27 | Risks and Opportunities | CNBC | Trump rejects Iran's conditional ceasefire proposal, WSJ reports | https://www.cnbc.com/2026/09/26/trump-rejects-irans-conditional-ceasefire-proposal-wsj-reports.html
