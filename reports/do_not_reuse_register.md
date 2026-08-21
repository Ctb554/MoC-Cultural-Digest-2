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

2026-08-21 | Saudi Arabia/Regional | Middle East Report | 'Women at Work'—Challenging the Art/Craft Divide | https://merip.org/2026/08/women-at-work-challenging-the-art-craft-divide/
2026-08-21 | Saudi Arabia/Regional | WWD | Saudi Arabia's Beauty Market Booms With Young, Trend-savvy Consumers | https://wwd.com/beauty-industry-news/beauty-features/saudi-arabia-beauty-market-booms-young-savvy-consumers-1239081751/
2026-08-21 | Negative Articles | Middle East Eye | US vows to 'collapse' Iran with new sanctions as energy prices spike | https://www.middleeasteye.net/news/us-vows-collapse-iran-new-sanctions-energy-prices-spike
2026-08-21 | Global | ArtReview | Gwangju Biennale accused of censoring pavilion title | https://artreview.com/gwangju-biennale-accused-of-censoring-pavilion-title/
2026-08-21 | Global | The Art Newspaper | New documentary focuses on traditional crafts around the world and the pressures facing artisans | https://www.theartnewspaper.com/2026/08/20/handmade-future-documentary-craft-traditions-artisans-underpressure
