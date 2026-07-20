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
2026-07-20 | Saudi Arabia/Regional | FlightGlobal | Riyadh Air to take 787-10s as it firms up Dreamliner and A350-1000 options | https://www.flightglobal.com/archive/2026/07/riyadh-air-to-take-787-10s-as-it-firms-up-dreamliner-and-a350-1000-options/
2026-07-20 | Saudi Arabia/Regional | FashionUnited | Arab Fashion Council names new chairwoman | https://fashionunited.com/news/people/arab-fashion-council-names-new-chairwoman/2026072073591
2026-07-20 | Negative Articles | NBC News | Yemen's Houthis declare naval blockade on Saudi Arabia, widening threat to global oil supplies | https://www.nbcnews.com/world/middle-east/yemen-houthis-maritime-embargo-saudi-arabia-oil-rcna588345
2026-07-20 | Negative Articles | Reuters | Gulf bourses retreat as US–Iran hostilities intensify | https://www.reuters.com/world/middle-east/gulf-bourses-retreat-usiran-hostilities-intensify-2026-07-19/
2026-07-20 | Global | Associated Press | Nolan's 'The Odyssey' storms the box office with a $264.1 million global debut | https://apnews.com/article/odyssey-box-office-christopher-nolan-923bf602d99b1c9c4aeb462d377b59c4
2026-07-20 | Global | The Art Newspaper | Union threatens strike action over working conditions in Venice museums due to extreme temperatures | https://www.theartnewspaper.com/2026/07/20/union-threatens-strike-action-over-working-conditions-in-venice-museums-due-to-extreme-temperatures
2026-07-20 | Global | The Art Newspaper | As Andy Burnham becomes the new UK prime minister, here are five key challenges facing his culture ministry | https://www.theartnewspaper.com/2026/07/20/as-andy-burnham-becomes-the-new-uk-prime-minister-here-are-five-key-challenges-facing-his-culture-ministry
