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
2026-07-20 | Saudi Arabia/Regional | Bloomberg | What Wall Street Never Understood About Gulf Investors | https://www.bloomberg.com/opinion/articles/2026-07-20/what-wall-street-never-understood-about-gulf-investors
2026-07-20 | Saudi Arabia/Regional | CNBC | CEO of new airline Riyadh Air on the state of the aviation market | https://www.cnbc.com/video/2026/07/20/ceo-of-new-airline-riyadh-air-on-the-state-of-the-aviation-market.html
2026-07-20 | Negative Articles | Reuters | Yemen's Houthis declare naval blockade against Saudi Arabia | https://www.reuters.com/world/middle-east/yemens-houthis-declare-naval-blockade-against-saudi-arabia-statement-2026-07-20/
2026-07-20 | Global | The Art Newspaper | As Andy Burnham becomes the new UK prime minister, here are five key challenges facing his culture ministry | https://www.theartnewspaper.com/2026/07/20/as-andy-burnham-becomes-the-new-uk-prime-minister-here-are-five-key-challenges-facing-his-culture-ministry
2026-07-20 | Global | The Art Newspaper | Union threatens strike action over working conditions in Venice museums due to extreme temperatures | https://www.theartnewspaper.com/2026/07/20/union-threatens-strike-action-over-working-conditions-in-venice-museums-due-to-extreme-temperatures
2026-07-20 | Global | The Atlanta Journal-Constitution | What World Heritage honor will and won't mean for Georgia's Okefenokee Swamp | https://www.ajc.com/business/2026/07/what-world-heritage-honor-will-and-wont-mean-for-georgias-okefenokee-swamp/
