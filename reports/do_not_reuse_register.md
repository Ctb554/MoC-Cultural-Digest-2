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

2026-08-20 | Saudi Arabia/Regional | The National | How Bronze Age Arabian traders invented 'brand value' | https://www.thenationalnews.com/news/europe/2026/08/19/how-bronze-age-arabian-traders-invented-brand-value/
2026-08-20 | Saudi Arabia/Regional | Interior Design | Riyadh's Black Gold Museum Reframes Oil's Legacy | https://interiordesign.net/projects/black-gold-museum-in-riyadh/
2026-08-20 | Negative Articles | AGBI | Saudi renewables push strained by war and tighter funding | https://www.agbi.com/analysis/renewable-energy/2026/08/saudi-renewables-push-strained-by-war-and-tighter-funding/
2026-08-20 | Negative Articles | AGBI | Saudi Arabia opens new Red Sea resort despite tourism downturn | https://www.agbi.com/tourism/2026/08/saudi-arabia-opens-new-red-sea-resort-despite-tourism-downturn/
2026-08-20 | Global | The Art Newspaper | US National Gallery of Art acquires paintings, sculptures and photographs spanning five centuries | https://www.theartnewspaper.com/2026/08/19/national-gallery-art-us-acquisitions-wifredo-lam-marie-bracquemond
2026-08-20 | Global | Blooloop | Natural History Museum to reopen hidden gallery closed since the 1940s | https://blooloop.com/news/natural-history-museum-hidden-gallery
2026-08-20 | Global | Hyperallergic | Speed Art Museum Returns 24 Native Artifacts to Oklahoma Tribes | https://hyperallergic.com/speed-art-museum-returns-24-native-artifacts-to-oklahoma-tribes/
2026-08-20 | Global | Arkeonews | Rare Silver Earrings from Khakassia May Preserve an Image of Umay, the Ancient Turkic Goddess | https://arkeonews.net/rare-silver-earrings-from-khakassia-may-preserve-an-image-of-umay-the-ancient-turkic-goddess/
2026-08-20 | Global | Archaeology Magazine | New Discoveries Link Sinai Site with Lost Egyptian City | https://archaeology.org/news/2026/08/19/new-discoveries-link-sinai-site-with-lost-egyptian-city/
2026-08-20 | Global | ArchDaily | Bruce Springsteen Center for American Music / COOKFOX | https://www.archdaily.com/1183556/bruce-springsteen-center-for-american-music-cookfox
2026-08-20 | Global | The Stage | The Stage Debut Awards 2026: Ralph Fiennes and Sadie Sink among nominees | https://www.thestage.co.uk/news/the-stage-debut-awards-2026-ralph-fiennes-and-sadie-sink-among-nominees
2026-08-20 | Global | Publishers Weekly | Ballantine Lands New Novel by Nita Prose | https://www.publishersweekly.com/pw/newsbrief/index.html?record=5992
2026-08-20 | Global | The Hollywood Reporter | Wild Horse Nine: Sam Rockwell Movie to Open Mill Valley Film Festival | https://www.hollywoodreporter.com/movies/movie-news/wild-horse-nine-sam-rockwell-mill-valley-film-festival-1236676808/
2026-08-20 | Global | Music Business Worldwide | UMG strikes global deal for The Beatles' merch, licensing, and e-commerce | https://www.musicbusinessworldwide.com/umg-strikes-global-deal-for-the-beatles-merch-licensing-and-e-commerce/
2026-08-20 | Risks and Opportunities | Al Jazeera | Are Hormuz ships more willing to defy Iran or the US? What the data shows | https://www.aljazeera.com/news/2026/8/20/are-hormuz-ships-more-willing-to-defy-iran-or-the-us-what-data-shows
