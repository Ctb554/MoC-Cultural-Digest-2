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

2026-09-11 | Saudi Arabia/Regional | CairoScene | Heritage Commission Documents Over 74,000 Cultural Assets | https://cairoscene.com/News/Heritage-Commission-Documents-Over-74-000-Cultural-Assets
2026-09-11 | Saudi Arabia/Regional | UA.NEWS | Eight films supported by Red Sea Film Foundation to be presented at TIFF in Canada | https://ua.news/en/culture/visim-filmiv-za-pidtrimki-red-sea-film-foundation-predstavliat-na-tiff-u-kanadi
2026-09-11 | Saudi Arabia/Regional | Al Arabiya | Saudi Arabia's music revolution: From underground scene to global stage | https://english.alarabiya.net/life-style/entertainment/2026/09/10/saudi-arabia-s-music-revolution-from-underground-scene-to-global-stage
2026-09-11 | Saudi Arabia/Regional | Al-Monitor | Saudi National Day takes shape | https://www.al-monitor.com/newsletter/2026-09-10/saudi-national-day-takes-shape
2026-09-11 | Negative Articles | Al Jazeera | Fighting escalates in Yemen; Houthi attacks trigger alerts in Saudi Arabia | https://www.aljazeera.com/news/2026/9/10/fighting-escalates-in-yemen-houthi-attacks-trigger-alerts-in-saudi-arabia
2026-09-11 | Negative Articles | The Guardian | Houthis seize key Yemeni port of Mocha in drive to take control of Red Sea coast | https://www.theguardian.com/world/2026/sep/10/houthis-seize-key-port-mocha-yemen-red-sea-coast-iran-saudi-arabia-us
2026-09-11 | Negative Articles | Middle East Eye | Saudi Arabia says it will take 'all measures to deter Houthi attacks' | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-says-it-will-take-all-measures-deter-houthi-attacks
2026-09-11 | Negative Articles | Bloomberg | Houthi-Saudi Fighting Escalates as Rebels Push Toward Key Strait | https://www.bloomberg.com/news/articles/2026-09-10/houthi-saudi-fighting-escalates-as-rebels-push-toward-key-strait
2026-09-11 | Global | Euronews | Maurizio Cattelan's 'Night' exhibition opens in Berlin | https://www.euronews.com/video/2026/09/10/maurizio-cattelans-night-exhibition-opens-in-berlin
2026-09-11 | Global | The Art Newspaper | Writers for Artforum, The New York Times and others win $50,000 Rabkin Prizes | https://www.theartnewspaper.com/2026/09/10/rabkin-prizes-winners-2026
2026-09-11 | Global | artnet News | Worth the Wait! The Bayeux Tapestry's British Museum Debut Is a Hard-Won Triumph | https://news.artnet.com/art-world/bayeux-tapestry-british-museum-review-2807802
2026-09-11 | Global | The Hollywood Reporter | Sian Heder Says 'Collective Action Matters' as 'Being Heumann' Opens Toronto Film Festival | https://www.hollywoodreporter.com/movies/movie-news/toronto-film-festival-2026-opening-night-being-heumann-1236697379/
2026-09-11 | Global | WWD | Diane von Furstenberg Spring 2027: A Modern Rebellious Spirit | https://wwd.com/runway/spring-2027/new-york/diane-von-furstenberg/review/
2026-09-11 | Global | ARTnews | Princess Diana's Revenge Dress Returns to Sotheby's With $300,000 Price Tag | https://www.artnews.com/art-news/news/princess-diana-revenge-dress-auction-sothebys-300000-1234797803/
2026-09-11 | Global | Deadline | Ella Langley Leads CMA Awards Nominations; Taylor Swift Back In Mix With 'Toy Story' Song | https://deadline.com/2026/09/2026-cma-awards-nominations-list-1237073443/
