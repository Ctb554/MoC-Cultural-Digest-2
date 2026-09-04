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
2026-09-04 | Saudi Arabia/Regional | BroadcastPro ME | Saudi Arabia promotes film production ecosystem at 83rd Venice Film Festival | https://www.broadcastprome.com/news/saudi-arabia-promotes-film-production-ecosystem-at-83rd-venice-film-festival/
2026-09-04 | Saudi Arabia/Regional | WWD | What to Watch: Despite Conflict, Design Companies Remain Committed to the Middle East | https://ca.finance.yahoo.com/news/watch-despite-conflict-design-companies-050000524.html
2026-09-04 | Negative Articles | The Philippine Star | Two Filipino seafarers killed as Saudi tanker attacked in Hormuz | https://www.philstar.com/headlines/2026/09/03/2553745/two-filipino-seafarers-killed-saudi-tanker-attacked-hormuz
2026-09-04 | Negative Articles | AGBI | Saudi-UAE payment delays demand costly workarounds | https://www.agbi.com/analysis/banking-finance/2026/09/saudi-uae-payment-delays-demand-costly-workarounds/
2026-09-04 | Global | ArtReview | Chinese Pavilion to boycott Gwangju Biennale | https://artreview.com/chinese-pavilion-to-boycott-gwangju-biennale/
2026-09-04 | Global | designboom | designboom's guide to Paris Design Week 2026: highlights in and out of Maison&Objet | https://www.designboom.com/design/designboom-guide-paris-design-week-2026-highlights-maisonobjet/
2026-09-04 | Global | Reuters | New York Fashion Week leans into American legacy brand revival | https://www.investing.com/news/stock-market-news/new-york-fashion-week-leans-into-american-legacy-brand-revival-4888390
2026-09-04 | Global | The Hollywood Reporter | 'Wild Horse Nine' Gets Venice's First Rapturous Reception of 2026 | https://www.hollywoodreporter.com/movies/movie-news/wild-horse-nine-venice-first-rapturous-reception-2026-1236689493/
2026-09-04 | Global | IndieWire | 'Everest: The Other Side' Review: Everest Climbing Doc About Grief | https://www.indiewire.com/criticism/movies/everest-the-other-side-review-everest-climbing-doc-1235214536/
