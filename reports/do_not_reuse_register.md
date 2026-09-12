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

<!-- Backfill added 2026-09-12: the git continuity store had no prior
     digest entries, but the delivery destination held 55 prior editions.
     The article URLs from the three most recent delivered editions
     (2026-09-09/10/11) are backfilled below so their reuse is enforced by
     the rolling window. Headlines are marked backfilled where not captured. -->
2026-09-09 | prior-edition | Muslim Network TV | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.muslimnetwork.tv/saudi-experts-explore-how-geography-shaped-cultural-identity/
2026-09-09 | prior-edition | Design Middle East | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://design-middleeast.com/ithra-opens-registration-for-2026-design-challenges/
2026-09-09 | prior-edition | eHotelier | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://insights.ehotelier.com/properties/2026/09/09/red-sea-global-unveils-nammos-resort-amaala-introducing-nammos-first-resort-hotel-globally/
2026-09-09 | prior-edition | BBC | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.bbc.co.uk/news/articles/cp849n2nz01o
2026-09-09 | prior-edition | Bloomberg | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.bloomberg.com/news/articles/2026-09-08/saudi-arabia-says-several-energy-sites-halted-after-attacks
2026-09-09 | prior-edition | The Guardian | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.theguardian.com/world/2026/sep/08/rami-naimi-abducted-saudi-arabia-mira-lozi
2026-09-09 | prior-edition | Middle East Eye | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.middleeasteye.net/news/yemen-forces-push-toward-sanaa-fighting-houthis-intensifies
2026-09-09 | prior-edition | Semafor | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.semafor.com/article/09/08/2026/saudi-wealth-fund-takes-its-capital-pitch-to-wall-street
2026-09-09 | prior-edition | Al Jazeera | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.aljazeera.com/news/2026/9/8/three-paintings-worth-10m-stolen-from-renoir-museum-in-southern-france
2026-09-09 | prior-edition | ARTnews | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.artnews.com/art-news/news/jenny-holzer-and-andy-goldsworthy-win-95000-praemium-imperiale-1234797291/
2026-09-09 | prior-edition | Arkeonews | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://arkeonews.net/4400-year-old-tomb-of-an-egyptian-judge-found-at-saqqara-with-colors-still-on-the-walls/
2026-09-09 | prior-edition | Archaeology Magazine | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://archaeology.org/news/2026/09/08/lavish-roman-bath-excavated-in-eastern-serbia/
2026-09-09 | prior-edition | WWD | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://wwd.com/fashion-news/fashion-features/milan-fashion-week-september-2026-schedule-shows-presentations-1239201148/
2026-09-09 | prior-edition | ArchDaily | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.archdaily.com/1184644/ixcampus-baumschlager-eberle-architekten
2026-09-09 | prior-edition | TheWrap | (backfilled from delivered edition MoC_Digest_2026-09-09.docx) | https://www.thewrap.com/creative-content/movies/summer-box-office-2026-success-explained-spider-man-odyssey/
2026-09-10 | prior-edition | MEED | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.meed.com/why-global-capital-is-committing-to-saudi-arabias-birthplace
2026-09-10 | prior-edition | Khaleej Times | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.khaleejtimes.com/world/gulf/saudi-arabia-national-day-2026-public-holiday
2026-09-10 | prior-edition | Khaleej Times | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.khaleejtimes.com/uae/2000-year-old-sharjah-coastal-network-added-unesco-tentative-list
2026-09-10 | prior-edition | WSLS | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.wsls.com/news/world/2026/09/09/yemens-houthi-rebels-say-saudi-backed-forces-launched-airstrikes-and-other-key-mideast-news/
2026-09-10 | prior-edition | Al Jazeera | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.aljazeera.com/news/2026/9/9/pakistan-warns-mecca-defense-pact-will-activate-after-houthi-attacks
2026-09-10 | prior-edition | Semafor | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.semafor.com/article/09/09/2026/saudi-arabia-could-give-un-nuclear-watchdog-greater-inspection-powers
2026-09-10 | prior-edition | The Art Newspaper | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.theartnewspaper.com/2026/09/09/artists-jenny-holzer-and-andy-goldsworthy-among-winners-of-2026-praemium-imperiale-awards
2026-09-10 | prior-edition | ARTnews | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.artnews.com/art-news/market/leilah-babirye-joins-salon-94-industry-moves-september-9-2026-1234797601/
2026-09-10 | prior-edition | Artnet News | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://news.artnet.com/market/art-world-new-season-recalibration-2806419
2026-09-10 | prior-edition | Archaeology Magazine | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://archaeology.org/news/2026/09/09/roman-era-mosaic-floor-unearthed-in-northern-turkey/
2026-09-10 | prior-edition | Variety | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://variety.com/2026/film/festivals/beyond-fest-2026-primtetime-victorian-pscyho-1236855248/
2026-09-10 | prior-edition | Deadline | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://deadline.com/2026/09/wildwood-afi-fest-2026-opening-film-1237072469/
2026-09-10 | prior-edition | WWD | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://wwd.com/fashion-news/fashion-features/cfda-fashion-award-nominees-honorees-2026-1239203108/
2026-09-10 | prior-edition | Dezeen | (backfilled from delivered edition MoC_Daily_Cultural_Digest_10Sep26_D1.docx) | https://www.dezeen.com/2026/09/09/emea-regional-showcases-dezeen-awards/
2026-09-11 | prior-edition | CairoScene | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://cairoscene.com/News/Heritage-Commission-Documents-Over-74-000-Cultural-Assets
2026-09-11 | prior-edition | UA.NEWS | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://ua.news/en/culture/visim-filmiv-za-pidtrimki-red-sea-film-foundation-predstavliat-na-tiff-u-kanadi
2026-09-11 | prior-edition | Al Arabiya | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://english.alarabiya.net/life-style/entertainment/2026/09/10/saudi-arabia-s-music-revolution-from-underground-scene-to-global-stage
2026-09-11 | prior-edition | Al-Monitor | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.al-monitor.com/newsletter/2026-09-10/saudi-national-day-takes-shape
2026-09-11 | prior-edition | Al Jazeera | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.aljazeera.com/news/2026/9/10/fighting-escalates-in-yemen-houthi-attacks-trigger-alerts-in-saudi-arabia
2026-09-11 | prior-edition | The Guardian | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.theguardian.com/world/2026/sep/10/houthis-seize-key-port-mocha-yemen-red-sea-coast-iran-saudi-arabia-us
2026-09-11 | prior-edition | Middle East Eye | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-says-it-will-take-all-measures-deter-houthi-attacks
2026-09-11 | prior-edition | Bloomberg | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.bloomberg.com/news/articles/2026-09-10/houthi-saudi-fighting-escalates-as-rebels-push-toward-key-strait
2026-09-11 | prior-edition | Euronews | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.euronews.com/video/2026/09/10/maurizio-cattelans-night-exhibition-opens-in-berlin
2026-09-11 | prior-edition | The Art Newspaper | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.theartnewspaper.com/2026/09/10/rabkin-prizes-winners-2026
2026-09-11 | prior-edition | Artnet News | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://news.artnet.com/art-world/bayeux-tapestry-british-museum-review-2807802
2026-09-11 | prior-edition | The Hollywood Reporter | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.hollywoodreporter.com/movies/movie-news/toronto-film-festival-2026-opening-night-being-heumann-1236697379/
2026-09-11 | prior-edition | WWD | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://wwd.com/runway/spring-2027/new-york/diane-von-furstenberg/review/
2026-09-11 | prior-edition | ARTnews | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://www.artnews.com/art-news/news/princess-diana-revenge-dress-auction-sothebys-300000-1234797803/
2026-09-11 | prior-edition | Deadline | (backfilled from delivered edition MoC_Daily_Cultural_Digest_11Sep26_D1.docx) | https://deadline.com/2026/09/2026-cma-awards-nominations-list-1237073443/

<!-- 2026-09-12 edition (MoC_Daily_Cultural_Digest_12Sep26_D1) -->
2026-09-12 | Saudi Arabia/Regional | Lovin Riyadh | The First-Ever Lovin Riyadh Awards: Meet The Pillar Of Culture Nominees | https://lovin.co/riyadh/en/best-of/the-first-ever-lovin-riyadh-awards-meet-the-pillar-of-culture-nominees
2026-09-12 | Saudi Arabia/Regional | Travel and Tour World | WTM Spotlight Riyadh Highlights New Strategies to Develop Saudi Outbound Demand | https://www.travelandtourworld.com/news/article/y9e1cvjn4ati/
2026-09-12 | Negative Articles | CNBC | Saudi Arabia shut down East-West crude oil pipeline after multiple attacks by drones from Iraq | https://www.cnbc.com/2026/09/11/saudi-arabia-shut-down-east-west-crude-oil-pipeline.html
2026-09-12 | Negative Articles | Bloomberg | Houthi Gains Leave MBS With Few Good Options in Yemen | https://www.bloomberg.com/news/articles/2026-09-11/houthi-gains-leave-mbs-with-few-good-options-in-yemen
2026-09-12 | Negative Articles | Nikkei Asia | Houthis advance along Yemeni coast, threaten Saudi Red Sea oil exports | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/houthis-advance-along-yemeni-coast-threaten-saudi-red-sea-oil-exports
2026-09-12 | Negative Articles | Showbiz411 | 9-11 Activist Terry Strada Speaks Out Against Saudi Arabia: Will Hollywood Remember in December and Skip Red Sea Festival? | https://www.showbiz411.com/2026/09/11/9-11-activist-terry-strada-speaks-out-against-saudi-arabia-will-hollywood-remember-in-december-and-skip-red-sea-festival
2026-09-12 | Negative Articles | Axios | 9/11 widow blasts Saudi Arabia during annual ceremony | https://www.axios.com/2026/09/11/911-widow-saudi-arabia-trump
2026-09-12 | Global | The Art Newspaper | UK governments proposed tourist tax should be ring-fenced for the arts, cultural leaders say | https://www.theartnewspaper.com/2026/09/11/uk-governments-proposed-tourist-tax-should-be-ring-fenced-for-the-arts-cultural-leaders-say
2026-09-12 | Global | Arkeonews | Vast 300-Meter Iron Age Mining Complex Discovered Beneath Hallstatt | https://arkeonews.net/vast-300-meter-iron-age-mining-complex-discovered-beneath-hallstatt
2026-09-12 | Global | Archaeology Magazine | Indonesian Hunter-Gatherers May Have Treated Toothaches with Betel Nuts | https://archaeology.org/news/2026/09/11/indonesian-hunter-gatherers-may-have-treated-toothaches-with-betel-nuts
2026-09-12 | Global | Artnet News | U.K. Pushes to Standardize Auction Data and More Industry Intel | https://news.artnet.com/market/industry-intel-sept-11-2809958
2026-09-12 | Global | Variety | Thailand Bets on Film Tourism to Turn Movie Locations Into Travel Destinations | https://variety.com/2026/film/markets-festivals/thailand-film-tourism-locations-travel-destinations-1236855735
2026-09-12 | Global | Business of Fashion | How a UK Hairstylist Brought Black Hair Into the Global Spotlight | https://www.businessoffashion.com/articles/beauty/charlotte-mensah-london-exhibition
2026-09-12 | Global | Billboard | Sienna Spiro's 'Great Expectation' Becomes Her First U.K. No. 1 Single | https://www.billboard.com/music/chart-beat/sienna-spiro-great-expectation-uk-number-1-single-1236338204
2026-09-12 | Global | Publishers Weekly | Publishing's AI Reckoning | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/101215-publishing-s-ai-reckoning.html
