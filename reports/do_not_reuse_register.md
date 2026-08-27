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

2026-08-27 | Saudi Arabia/Regional | CairoScene | Saudi Architecture and Design Commission launches a national professional learning platform for the design sector | https://cairoscene.com/Home/New-Professional-Learning-Platform-Launched-for-Saudi-Designers
2026-08-27 | Saudi Arabia/Regional | Youm7 | Dalia Mubarak, one of the Kingdom's most prominent female singers, announces her retirement from music | https://www.youm7.com/story/2026/8/26/%D8%A7%D8%B9%D8%AA%D8%B2%D8%A7%D9%84-%D8%A7%D9%84%D9%85%D8%B7%D8%B1%D8%A8%D8%A9-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A%D8%A9-%D8%AF%D8%A7%D9%84%D9%8A%D8%A7-%D9%85%D8%A8%D8%A7%D8%B1%D9%83/7525902
2026-08-27 | Negative Articles | Energy Live News | Saudi Arabia's renewable-energy sector faces renewed human-rights scrutiny over unresolved migrant-labour abuses | https://www.energylivenews.com/2026/08/26/saudi-arabias-renewable-sector-faces-human-rights-backlash/
2026-08-27 | Negative Articles | New York Times | Under threat, Saudi Arabia reroutes oil exports away from the Red Sea | https://www.nytimes.com/2026/08/26/business/saudi-oil-houthis-iran.html
2026-08-27 | Negative Articles | France 24 | Trump sends the US-Saudi civil-nuclear agreement to Congress for review | https://www.france24.com/en/americas/20260826-trump-saudi-civil-nuclear-agreement-congress
2026-08-27 | Global | Washington Times | Chinese artist Gao Zhen sentenced to three years over satirical Mao statues | https://www.washingtontimes.com/news/2026/aug/26/chinese-artist-gao-zhen-sentenced-3-years-prison-satirical-mao/
2026-08-27 | Global | Hyperallergic | An artist's device slows down Citi Bikes in less affordable New York neighbourhoods | https://hyperallergic.com/artists-device-slows-down-citi-bikes-in-less-affordable-neighborhoods/
2026-08-27 | Global | The Peninsula | A unique 11,000-year-old statue of a human seated on a leopard is unearthed at Karahantepe | http://thepeninsulaqatar.com/article/26/08/2026/11000-year-old-statue-of-human-riding-leopard-unearthed-in-se-t%C3%BCrkiye
2026-08-27 | Global | The Hollywood Reporter | Marina Abramovic, Lee Daniels and Nadine Labaki win Liberatum's 2026 Pioneer Awards | https://www.hollywoodreporter.com/movies/movie-news/lee-daniels-nadine-labaki-marina-abramovic-liberatum-awards-1236670800/
2026-08-27 | Global | ARTnews | Three Los Angeles museums join forces to examine architect Paul Revere Williams | https://www.artnews.com/art-news/market/lindsay-jarvis-max-werner-partnership-industry-moves-august-26-2026-1234795952/
