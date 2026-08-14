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
2026-08-14 | Saudi Arabia/Regional | Gulf News | Saudi defence minister calls Iraq 'cherished neighbour' after strikes | https://gulfnews.com/world/gulf/saudi/saudi-defence-minister-calls-iraq-cherished-neighbour-after-strikes-1.500640250
2026-08-14 | Saudi Arabia/Regional | The National | Turkey, Saudi Arabia and Pakistan to establish political and military mechanisms under defence pact | https://www.thenationalnews.com/news/gulf/2026/08/13/turkey-saudi-arabia-and-pakistan-to-establish-political-and-military-mechanisms-under-defence-pact/
2026-08-14 | Saudi Arabia/Regional | AGBI | PIF's new strategy focuses on returns and attracting investment | https://www.agbi.com/giga-projects/2026/08/pifs-new-strategy-focuses-on-returns-and-attracting-investment/
2026-08-14 | Global | Archaeology Magazine | Fourth-Century B.C. Graves Found at Hattusha | https://archaeology.org/news/2026/08/13/fourth-century-b-c-graves-found-at-hattusha/
2026-08-14 | Global | Archaeology Magazine | Homo antecessor Skull Fragments Examined | https://archaeology.org/news/2026/08/13/homo-antecessor-skull-fragments-examined/
2026-08-14 | Global | The Hollywood Reporter | NY Film Festival Sets Currents Lineup Led by 'Bardi' World Premiere | https://www.hollywoodreporter.com/movies/movie-news/ny-film-festival-2026-currents-lineup-1236673366/
2026-08-14 | Global | Deadline | 'Spider-Man: Brand New Day' Fastest To $700 Million At U.S. Box Office | https://deadline.com/2026/08/box-office-spider-man-brand-new-day-700m-record-fastest-1237032881/
2026-08-14 | Global | The Hollywood Reporter | The War Over Warner Bros. Is Splintering Hollywood's Labor World | https://www.hollywoodreporter.com/business/business-news/paramount-warner-bros-labor-world-1236673223/
2026-08-14 | Global | WWD | Jemima Kirke, Rowan Blanchard Front Marc Jacobs Fall 2026 Campaign | https://wwd.com/fashion-news/fashion-scoops/marc-jacobs-fall-2026-jemima-kirke-rowan-blanchard-campaign-1239117952/
