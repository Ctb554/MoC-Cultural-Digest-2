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

2026-09-02 | Saudi Arabia/Regional | FashionUnited | Saudi Arabia expands fashion education and industry pathways | https://fashionunited.uk/news/fashion/saudi-arabia-expands-fashion-education-and-industry-pathways/2026090190067
2026-09-02 | Saudi Arabia/Regional | Business of Fashion | What's Driving Saudi Arabia's Beauty Transformation | https://www.businessoffashion.com/articles/beauty/whats-driving-saudi-arabias-beauty-transformation/
2026-09-02 | Saudi Arabia/Regional | Campaign Middle East | Stop exporting your UAE strategy to Saudi | https://campaignme.com/stop-exporting-your-uae-strategy-to-saudi/
2026-09-02 | Negative Articles | Bloomberg | Saudi Arabia Returns to Markets With Dollar-Bond Offering | https://www.bloomberg.com/news/articles/2026-09-01/saudi-arabia-returns-to-markets-with-dollar-bond-offering
2026-09-02 | Global | The Art Newspaper | The art world's billionaire problem is getting worse | https://www.theartnewspaper.com/2026/09/01/the-art-worlds-billionaire-problem-is-getting-worse
2026-09-02 | Global | Arkeonews | Gardener Unearths Denmark's Largest Viking Silver Hoard — 18.5 Kilograms Hidden in a Clay Pot | https://arkeonews.net/gardener-unearths-denmarks-largest-viking-silver-hoard-18-5-kilograms-hidden-in-a-clay-pot/
2026-09-02 | Global | Deadline | 'Avengers: Secret Wars' Adds Noah Jupe To Cast In Key Role | https://deadline.com/2026/09/avengers-secret-wars-noah-jupe-cast-marvel-1237064363/
2026-09-02 | Global | Dezeen | Kengo Kuma awarded Andrée Putman Lifetime Achievement Award by CDA | https://www.dezeen.com/2026/09/01/kengo-kuma-andree-putman-lifetime-achievement-award-cda/
