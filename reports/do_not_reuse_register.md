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
2026-09-14 | Saudi Arabia/Regional | UA.NEWS | Saudi Film Commission to participate in TIFF in Canada | https://ua.news/en/culture/saudivska-kinokomisiia-bere-uchast-u-tiff-u-kanadi
2026-09-14 | Saudi Arabia/Regional | Gulf News | Abu Dhabi International Book Fair 2026 opens at ADNEC | https://gulfnews.com/uae/abu-dhabi-international-book-fair-2026-opens-at-adnec-1.500672808
2026-09-14 | Negative Articles | The Guardian | Satellite images show extent of damage to major Saudi pipeline, amid global oil supply fears | https://www.theguardian.com/world/2026/sep/14/saudi-pipeline-drone-attack-houthis-global-oil-supply-prices
2026-09-14 | Negative Articles | The New York Times | 'We Left in the Clothes We Were Wearing': Yemenis Flee New Fighting | https://www.nytimes.com/2026/09/12/world/middleeast/yemen-iran-war-houthis.html
2026-09-14 | Negative Articles | Middle East Eye | Houthis say Saudi Arabia launched over 50 strikes against them in 24 hours | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-arabia-launched-over-50-strikes-against-them-24-hours
2026-09-14 | Global | Variety | TIFF 2026: 20 International Titles to Track, From Feng-I Fiona Roan's Shuhua Starrer to a Taxidermy Musical and a John Madden Parkinson's Rom-Com | https://variety.com/2026/film/global/tiff-2026-20-international-titles-to-track-1236860336/
2026-09-14 | Global | The Hollywood Reporter | 'Babies' Review: Anna Kendrick and Seth Rogen in Sparkling Comedy | https://www.hollywoodreporter.com/movies/movie-reviews/babies-review-anna-kendrick-seth-rogen-lauren-miller-rogen-1236699421/
2026-09-14 | Global | The Canadian Press | Seth Rogen, man with the 'best heart and worst laugh' in Hollywood, honoured at TIFF | https://www.thecanadianpressnews.ca/entertainment/seth-rogen-man-with-the-best-heart-and-worst-laugh-in-hollywood-honoured-at-tiff/article_04c192cc-3e12-556d-808b-e8d24a54e3d3.html
2026-09-14 | Global | HeritageDaily | Ancient shipwrecks reveal lost history beneath the Red Sea | https://www.heritagedaily.com/2026/09/ancient-shipwrecks-reveal-lost-history-beneath-the-red-sea
