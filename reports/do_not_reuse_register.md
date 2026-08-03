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
2026-08-03 | Saudi Arabia/Regional | The Philadelphia Inquirer | Trump says he will order halt to Iran strikes after parameters reached for deal to end war | https://www.inquirer.com/news/nation-world/trump-iron-pause-strikes-negotiations-strait-hormuz-mohammed-bin-salman-20260802.html
2026-08-03 | Saudi Arabia/Regional | Middle East Eye | Saudi, Iranian foreign ministers discuss efforts to reduce regional tensions | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-iranian-foreign-ministers-discuss-efforts-reduce-regional-tensions
2026-08-03 | Saudi Arabia/Regional | Al Jazeera | No breakthrough on Strait of Hormuz as Trump halts attack on Iran | https://www.aljazeera.com/news/2026/8/2/no-breakthrough-on-strait-of-hormuz-as-trump-halts-attack-on-iran
2026-08-03 | Negative Articles | Press TV | Persian Gulf states handed over their sovereignty for illegal war: Analyst | https://www.presstv.co.uk/Detail/2026/08/02/773592/Persian-Gulf-states-sovereignty-Iran-war-US-Israel-aggression-
2026-08-03 | Global | CNBC | 'Spider-Man: Brand New Day' box office $355 million domestic opening | https://www.cnbc.com/2026/08/02/spider-man-brand-new-day-box-office-355-million-domestic-opening.html
2026-08-03 | Global | Chicago Sun-Times | Review: Tate McRae closes out Lollapalooza with surprisingly subdued set | https://chicago.suntimes.com/lollapalooza/2026/08/02/review-tate-mcrae-closes-out-lollapalooza-with-surprisingly-subdued-set
