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

2026-09-17 | Saudi Arabia/Regional | CairoScene | Hafez Gallery Makes Frieze London Debut With Two-Artist Showcase | https://cairoscene.com/ArtsAndCulture/Hafez-Gallery-Makes-Frieze-London-Debut-With-Two-Artist-Showcase
2026-09-17 | Saudi Arabia/Regional | BroadcastPro ME | Film AlUla partners with Sherborne Media to boost production financing | https://www.broadcastprome.com/news/film-alula-partners-with-sherborne-media-to-boost-production-financing/
2026-09-17 | Saudi Arabia/Regional | The Washington Times | Smithsonian's National Zoo breaks ground on Arabian leopard exhibit, to open in 2029 | https://www.washingtontimes.com/news/2026/sep/16/smithsonians-national-zoo-breaks-ground-arabian-leopard-exhibit-open/
2026-09-17 | Negative Articles | The Guardian | US opts not to back Saudi Arabia in Yemen after meeting Houthi leaders | https://www.theguardian.com/world/2026/sep/16/us-officials-decide-against-backing-saudi-arabia-yemen-meeting-houthi-leaders
2026-09-17 | Negative Articles | The New York Times | Global Oil Prices Could Hit Highest Levels in Months After Saudi Pipeline Attacks | https://www.nytimes.com/2026/09/16/business/saudi-pipeline-houthi-attacks.html
2026-09-17 | Negative Articles | The Express Tribune | US urges travellers to reconsider Saudi Arabia trips over Iranian drone, missile threat | https://tribune.com.pk/story/2629641/us-urges-travellers-to-reconsider-saudi-arabia-trips-over-iranian-drone-missile-threat
2026-09-17 | Negative Articles | Press TV | Yemeni Armed Forces target Aramco facilities, King Khalid Air Base in Saudi Arabia | https://www.presstv.co.uk/Detail/2026/09/16/776408/Yemeni-Armed-Forces-target-Aramco-facilities,-King-Khalid-Air-Base-in-Saudi-Arabia
2026-09-17 | Global | Artnet News | Giotto and Cimabue Masterpieces in Assisi Get an Ultra-HD Digital Revival | https://news.artnet.com/art-world/giotto-and-cimabue-masterpieces-in-assisi-get-a-ultra-hd-digital-revival-2811536
2026-09-17 | Global | Hyperallergic | Met Museum Breaks Ground on New Modern and Contemporary Wing | https://hyperallergic.com/met-museum-breaks-ground-on-new-modern-and-contemporary-wing/
2026-09-17 | Global | ARTnews | Thyssen-Bornemisza Museum to Expand to a Second Location in Madrid | https://www.artnews.com/art-news/news/thyssen-bornemisza-museum-expand-second-location-madrid-1234798467/
2026-09-17 | Global | ARTnews | Liang Shaoji, Chinese Artist Who Collaborated With Silkworms, Has Died at 81 | https://www.artnews.com/art-news/news/liang-shaoji-dead-chinese-artist-silkworms-1234798463/
2026-09-17 | Global | BNN Bloomberg | Danny Boyle Defends AI Use in New Film 'Ink' at TIFF Screening | https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/09/16/director-danny-boyle-defends-use-of-ai-in-new-film-ink-at-tiff-screening/
2026-09-17 | Global | W Magazine | Dario Vitale Is the New Creative Director of Emporio Armani and Giorgio Armani Accessories | https://www.wmagazine.com/fashion/dario-vitale-emporio-armani-creative-director
2026-09-17 | Global | NBC News | Trump's Handpicked Kennedy Center Board Votes to Close Venue for Renovations | https://www.nbcnews.com/politics/trump-administration/trumps-handpicked-kennedy-center-board-votes-close-venue-renovations-rcna597921
