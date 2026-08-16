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
2026-08-16 | Saudi Arabia/Regional | The National | Why the Gulf's economy has defied early war predictions | https://www.thenationalnews.com/business/economy/2026/08/15/why-the-gulfs-economy-has-defied-early-war-predictions/
2026-08-16 | Saudi Arabia/Regional | The National | UAE to defend Strait of Hormuz rights after attack on Adnoc vessel, Dr Gargash says | https://www.thenationalnews.com/news/mena/2026/08/15/uae-to-defend-strait-of-hormuz-rights-after-attack-on-adnoc-vessel-dr-gargash-says/
2026-08-16 | Saudi Arabia/Regional | Middle East Eye | How a pragmatic axis could reshape the Middle East | https://www.middleeasteye.net/live-blog/live-blog-update/how-pragmatic-axis-could-reshape-middle-east
2026-08-16 | Global | Dezeen | NUA Arquitectures renovates Catalan textile warehouse with timber office block | https://www.dezeen.com/2026/08/16/nua-arquitectures-tuvatextil-office/
2026-08-16 | Global | Dezeen | Helen & Hard uses uprooted spruce trees to shape Norwegian cabin | https://www.dezeen.com/2026/08/15/cabin-sande-spruce-trees-norway-atlanic-ocean-helen-hard-architects/
