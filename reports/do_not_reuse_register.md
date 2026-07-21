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

2026-07-21 | Saudi Arabia/Regional | Al-Monitor | As Houthis declare Red Sea blockade on Saudi Arabia, oil markets brace for impact | https://www.al-monitor.com/originals/2026/07/houthis-declare-red-sea-blockade-saudi-arabia-oil-markets-brace-impact
2026-07-21 | Saudi Arabia/Regional | Bloomberg | Saudi Arabia's Riyadh Air Locks in Options for Boeing, Airbus Jets | https://www.bloomberg.com/news/articles/2026-07-20/riyadh-locks-in-options-for-boeing-airbus-jets-amid-growth-push
2026-07-21 | Saudi Arabia/Regional | AGBI | Saudi producers offer US defence a way around supply bottleneck | https://www.agbi.com/analysis/industry/2026/07/us-defence-manufacturers-eye-saudi-as-supply-chains-tighten/
2026-07-21 | Global | The Korea Times | UNESCO adopts Busan Declaration for global heritage preservation | https://www.koreatimes.co.kr/lifestyle/koreanheritage/20260720/unesco-adopts-busan-declaration-for-global-heritage-preservation
2026-07-21 | Global | The Art Newspaper | Union threatens strike action over working conditions in Venice museums due to extreme temperatures | https://www.theartnewspaper.com/2026/07/20/union-threatens-strike-action-over-working-conditions-in-venice-museums-due-to-extreme-temperatures
2026-07-21 | Global | Artforum | David Zwirner Exits New York's Upper East Side | https://www.artforum.com/news/david-zwirner-leaves-the-upper-east-side-in-new-york-1234755116/
2026-07-21 | Global | Deadline | Toronto Film Festival Unveils First 2026 Lineups | https://deadline.com/2026/07/toronto-film-festival-2026-line-up-1236998190/
2026-07-21 | Global | Billboard | Ella Langley's 'Choosin' Texas' Makes More History With 14th Week at No. 1 on Billboard Hot 100 | https://www.billboard.com/lists/ella-langley-choosin-texas-hot-100-number-one-14th-week/
2026-07-21 | Global | WWD | EXCLUSIVE: Le Bon Marché and Tagwalk Founder Alexandra Van Houtte Return for Second Capsule | https://wwd.com/fashion-news/fashion-scoops/le-bon-marche-alexandra-van-houtte-collaboration-fall-2026-1239075990/
