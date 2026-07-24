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

2026-07-24 | Saudi Arabia/Regional | The New York Times | Oil-Rich Saudi Arabia Isn't Short on Energy. Here's Why It Wants to Go Nuclear. | https://www.nytimes.com/2026/07/23/world/middleeast/saudi-arabia-nuclear.html
2026-07-24 | Saudi Arabia/Regional | CNBC | Oil prices: WTI, Brent rise after attacks on Saudi tankers | https://www.cnbc.com/2026/07/23/oil-prices-today-wti-brent-trump-iran-hormuz.html
2026-07-24 | Saudi Arabia/Regional | The Guardian | How the Bab al-Mandab blockade threat helped push oil back above $100 | https://www.theguardian.com/business/2026/jul/23/bab-al-mandab-blockade-push-oil-100-houthi-ships
2026-07-24 | Saudi Arabia/Regional | The New York Times | Trump's New Demand for Nuclear Deal Puts Saudis in a Bind | https://www.nytimes.com/2026/07/23/world/middleeast/trump-saudi-arabia-palestinian-state.html
2026-07-24 | Saudi Arabia/Regional | UNESCO | The World Heritage Committee will examine new nominations and the state of conservation of inscribed sites | https://www.unesco.org/en/articles/world-heritage-committee-will-examine-new-nominations-and-state-conservation-inscribed-sites
2026-07-24 | Negative Articles | The Guardian | Why would Trump agree to the Saudi nuclear deal? | https://www.theguardian.com/commentisfree/2026/jul/23/trump-saudi-nuclear-deal
2026-07-24 | Negative Articles | Foreign Policy | Trump Is Triggering a Middle East Nuclear Arms Race | https://foreignpolicy.com/2026/07/23/trump-us-saudi-nuclear-deal-weapons-iran-israel-arms-race/
2026-07-24 | Global | IndieWire | Venice Film Festival Reveals 2026 Lineup | https://www.indiewire.com/news/festivals/venice-film-festival-reveals-2026-lineup-1235206616/
2026-07-24 | Global | Variety | Vijay's 'Jana Nayagan' Finally Gets a Release Date | https://variety.com/2026/film/news/vijay-jana-nayagan-release-date-2-1236811540/
2026-07-24 | Global | The Hollywood Reporter | Comic-Con 2026 Hall H Preview | https://www.hollywoodreporter.com/movies/movie-news/comic-con-2026-hall-h-preview-1236653276/
2026-07-24 | Global | Reporter Gourmet | Michelin Guide Italy adds 15 new restaurants in July | https://reportergourmet.com/en/news/10512-michelin-guide-italy-15-new-entries-in-july-from-pascuccis-bistro-to-the-boom-in-basilicata-the-restaurants
