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

<!-- 2026-07-28 reconciliation: prior editions (20-27 Jul 2026) were delivered
     to the Dropbox test folder but never committed back to this repo's
     continuity store (register was empty). The 23-27 Jul editions were
     downloaded and their article/source URLs transcribed below so the
     rolling 60-day reuse window enforces them. Outlet = URL domain; headlines
     were not transcribed verbatim (the mechanical reuse check keys on
     date+URL). Reconciled by the 2026-07-28 automated run. -->
2026-07-23 | reconciled-from-Dropbox | deadline.com |  | https://deadline.com/2026/07/bafta-ai-clause-submission-rules-2027-1237000067/
2026-07-23 | reconciled-from-Dropbox | agbi.com |  | https://www.agbi.com/giga-projects/2026/07/deserted-island-what-happened-at-neom-sindalah-and-whats-next/
2026-07-23 | reconciled-from-Dropbox | al-monitor.com |  | https://www.al-monitor.com/originals/2026/07/saudi-nuclear-deal-delivers-strategic-economic-prizes-trump-boosts-gulf-allies
2026-07-23 | reconciled-from-Dropbox | artnews.com |  | https://www.artnews.com/art-news/news/louvre-apollo-gallery-reopens-without-crown-jewels-1234793182/
2026-07-23 | reconciled-from-Dropbox | designboom.com |  | https://www.designboom.com/architecture/sanaa-team-ecuador-national-museum-muna-competition-revised-selection-process-estudioa0-caaporarq-jeromehaferdstudio/
2026-07-23 | reconciled-from-Dropbox | heritagedaily.com |  | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-23 | reconciled-from-Dropbox | hollywoodreporter.com |  | https://www.hollywoodreporter.com/movies/movie-news/odyssey-box-office-2026-practical-effects-1236652219/
2026-07-23 | reconciled-from-Dropbox | koreaherald.com |  | https://www.koreaherald.com/article/10815414
2026-07-23 | reconciled-from-Dropbox | middleeasteye.net |  | https://www.middleeasteye.net/news/trump-to-approve-nuclear-deal-saudi-arabia-despite-regional-proliferation-risks
2026-07-23 | reconciled-from-Dropbox | nytimes.com |  | https://www.nytimes.com/2026/07/22/world/middleeast/houthis-saudi-oil-tankers-red-sea.html
2026-07-23 | reconciled-from-Dropbox | pbs.org |  | https://www.pbs.org/newshour/world/ap-report-trump-approves-nuclear-agreement-that-may-allow-saudi-arabia-to-enrich-uranium
2026-07-23 | reconciled-from-Dropbox | presstv.co.uk |  | https://www.presstv.co.uk/Detail/2026/07/22/772814/Yemen-Saudi-Arabia-ships-blockade-warning
2026-07-23 | reconciled-from-Dropbox | publishersweekly.com |  | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/100890-how-holt-finished-mahmoud-khalil-s-no-land-to-stand-on-in-just-six-months.html
2026-07-23 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/22/artforum-bids-farewell-to-back-cover-star-in-style
2026-07-23 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/22/european-union-officially-pull-2m-venice-biennale-funding-over-russian-participation
2026-07-23 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/22/jessica-morgan-named-new-tate-director
2026-07-24 | reconciled-from-Dropbox | foreignpolicy.com |  | https://foreignpolicy.com/2026/07/23/trump-us-saudi-nuclear-deal-weapons-iran-israel-arms-race/
2026-07-24 | reconciled-from-Dropbox | reportergourmet.com |  | https://reportergourmet.com/en/news/10512-michelin-guide-italy-15-new-entries-in-july-from-pascuccis-bistro-to-the-boom-in-basilicata-the-restaurants
2026-07-24 | reconciled-from-Dropbox | variety.com |  | https://variety.com/2026/film/news/vijay-jana-nayagan-release-date-2-1236811540/
2026-07-24 | reconciled-from-Dropbox | arabnews.com |  | https://www.arabnews.com/node/2652024/lifestyle
2026-07-24 | reconciled-from-Dropbox | arabnews.pk |  | https://www.arabnews.pk/node/2652024/lifestyle
2026-07-24 | reconciled-from-Dropbox | cnbc.com |  | https://www.cnbc.com/2026/07/23/oil-prices-today-wti-brent-trump-iran-hormuz.html
2026-07-24 | reconciled-from-Dropbox | cntravellerme.com |  | https://www.cntravellerme.com/story/from-portland-to-paris-the-chefs-taking-middle-eastern-food-to-the-world
2026-07-24 | reconciled-from-Dropbox | hollywoodreporter.com |  | https://www.hollywoodreporter.com/movies/movie-news/comic-con-2026-hall-h-preview-1236653276/
2026-07-24 | reconciled-from-Dropbox | indiewire.com |  | https://www.indiewire.com/news/festivals/venice-film-festival-reveals-2026-lineup-1235206616/
2026-07-24 | reconciled-from-Dropbox | nytimes.com |  | https://www.nytimes.com/2026/07/23/world/middleeast/saudi-arabia-nuclear.html
2026-07-24 | reconciled-from-Dropbox | nytimes.com |  | https://www.nytimes.com/2026/07/23/world/middleeast/trump-saudi-arabia-palestinian-state.html
2026-07-24 | reconciled-from-Dropbox | pakistanpoint.com |  | https://www.pakistanpoint.com/ar/news/saudi-arabia/story-2225211.html
2026-07-24 | reconciled-from-Dropbox | theguardian.com |  | https://www.theguardian.com/business/2026/jul/23/bab-al-mandab-blockade-push-oil-100-houthi-ships
2026-07-24 | reconciled-from-Dropbox | theguardian.com |  | https://www.theguardian.com/commentisfree/2026/jul/23/trump-saudi-nuclear-deal
2026-07-24 | reconciled-from-Dropbox | unesco.org |  | https://www.unesco.org/en/articles/world-heritage-committee-will-examine-new-nominations-and-state-conservation-inscribed-sites
2026-07-25 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/4500-year-old-mega-dams-near-egypts-red-pyramid-may-reveal-an-ancient-engineering-breakthrough/
2026-07-25 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/byzantine-shipwreck-off-croatia-yields-record-gold-treasure-and-an-emperors-ring/
2026-07-25 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/turkic-period-tomb-in-mongolia-yields-1400-year-old-peach-wood-bow-and-runic-inscribed-horse-head-fiddle/
2026-07-25 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/two-premature-infants-possibly-twins-found-buried-in-an-abandoned-roman-latrine-at-ephesus/
2026-07-25 | reconciled-from-Dropbox | avclub.com |  | https://www.avclub.com/weird-al-yankovic-riyadh-comedy-festival
2026-07-25 | reconciled-from-Dropbox | bloomberg.com |  | https://www.bloomberg.com/news/newsletters/2026-07-24/oil-tankers-run-the-houthi-gauntlet-to-keep-saudi-exports-flowing
2026-07-25 | reconciled-from-Dropbox | middleeasteye.net |  | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-25 | reconciled-from-Dropbox | rte.ie |  | https://www.rte.ie/news/2026/0725/1585036-houthis-strikes/
2026-07-25 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/24/buffalo-akg-art-museum-two-director-roles-promotions
2026-07-25 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/24/jen-catron-paul-outlaw-times-square-hot-dog-returns
2026-07-25 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/24/swedish-viking-centre-that-loaned-ship-for-the-odyssey-alleges-that-it-has-not-been-paid-for-damages
2026-07-25 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/24/unesco-adds-ancient-greek-city-tauric-chersonese-in-crimea-to-world-heritage-in-danger-list
2026-07-25 | reconciled-from-Dropbox | thenationalnews.com |  | https://www.thenationalnews.com/news/2026/07/24/houthi-official-says-saudi-strike-targets-hodeidah-port-after-attack-on-saudi-vessel/
2026-07-26 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/5000-year-old-bronze-age-temple-with-altars-and-sacred-hearths-discovered-in-eastern-turkiye/
2026-07-26 | reconciled-from-Dropbox | arkeonews.net |  | https://arkeonews.net/roman-gold-barracks-and-surgical-tools-unearthed-at-vindonissas-first-military-camp-in-switzerland/
2026-07-26 | reconciled-from-Dropbox | deadline.com |  | https://deadline.com/2026/07/ryan-gosling-ghost-rider-marvel-comic-con-1237003726/
2026-07-26 | reconciled-from-Dropbox | wwd.com |  | https://wwd.com/pop-culture/celebrity-news/michelle-yeoh-hunter-schafer-comic-con-outfits-1239081924/
2026-07-26 | reconciled-from-Dropbox | bloomberg.com |  | https://www.bloomberg.com/news/articles/2026-07-25/houthi-claim-missile-strikes-on-southern-saudi-arabia
2026-07-26 | reconciled-from-Dropbox | bloomberg.com |  | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-26 | reconciled-from-Dropbox | cnbc.com |  | https://www.cnbc.com/2026/07/25/saudi-military-strikes-iran-backed-houthi-targets-yemen.html
2026-07-26 | reconciled-from-Dropbox | foxnews.com |  | https://www.foxnews.com/media/weird-al-yankovic-says-he-walked-away-from-seven-figure-comedy-festival-offer-saudi-arabia
2026-07-26 | reconciled-from-Dropbox | heritagedaily.com |  | https://www.heritagedaily.com/2026/07/heatwave-reveals-lost-welsh-landscapes/158718
2026-07-26 | reconciled-from-Dropbox | hollywoodreporter.com |  | https://www.hollywoodreporter.com/movies/movie-news/black-panther-3-marvel-ryan-coogler-comic-con-1236656570/
2026-07-26 | reconciled-from-Dropbox | middleeasteye.net |  | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-26 | reconciled-from-Dropbox | thestage.co.uk |  | https://www.thestage.co.uk/news/rsc-cancels-game-of-thrones-play-preview-performances
2026-07-27 | reconciled-from-Dropbox | apnews.com |  | https://apnews.com/article/unesco-mount-olympus-japan-ancient-capitals-1d3fabaa482d9384b1cb0b5c917ce5d5
2026-07-27 | reconciled-from-Dropbox | fashionista.com |  | https://fashionista.com/2026/07/paris-fashion-week-september-2026-schedule
2026-07-27 | reconciled-from-Dropbox | wwd.com |  | https://wwd.com/business-news/retail/saudi-arabia-fashion-food-design-selfridges-corner-shop-1239081869/
2026-07-27 | reconciled-from-Dropbox | aljazeera.com |  | https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities
2026-07-27 | reconciled-from-Dropbox | bloomberg.com |  | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-27 | reconciled-from-Dropbox | cnn.com |  | https://www.cnn.com/2026/07/26/world/video/fungi-leather-farm-indonesia-transformers-hkn-spc
2026-07-27 | reconciled-from-Dropbox | newsweek.com |  | https://www.newsweek.com/antoni-gaudi-118-year-old-lost-nyc-skyscraper-design-interiors-unveiled-12240546
2026-07-27 | reconciled-from-Dropbox | theartnewspaper.com |  | https://www.theartnewspaper.com/2026/07/27/peru-earthquake-damages-16th-century-church-iglesia-apostol-santiago
2026-07-27 | reconciled-from-Dropbox | theguardian.com |  | https://www.theguardian.com/commentisfree/2026/jul/26/the-guardian-view-on-a-us-saudi-nuclear-agreement-an-offer-that-further-erodes-international-safeguards

<!-- 2026-07-28 edition (MoC_Daily_Cultural_Digest_28Jul26_D1) -->
2026-07-28 | Saudi Arabia/Regional | The Week | Why drone attack on world's largest oil processing plant in Saudi's Abqaiq poses geopolitical risk | https://www.theweek.in/news/middle-east/2026/07/27/saudi-arabia-oil-refinery-attack-abqaiq-fire-impact.html
2026-07-28 | Saudi Arabia/Regional | Al-Monitor | Red Sea shipping slows after Houthi attack on Saudi Arabia, data shows | https://www.al-monitor.com/originals/2026/07/red-sea-shipping-slows-after-houthi-attack-saudi-arabia-data-shows
2026-07-28 | Saudi Arabia/Regional | AGBI | Yanbu attacks expose Saudi oil export vulnerability | https://www.agbi.com/analysis/oil-and-gas/2026/07/yanbu-attacks-expose-saudi-oil-export-vulnerability/
2026-07-28 | Saudi Arabia/Regional | The New York Times | How the Houthis Cornered Saudi Arabia Into a New Battle | https://www.nytimes.com/2026/07/27/world/middleeast/houthis-saudi-arabia-iran-war.html
2026-07-28 | Negative Articles | Press TV | Saudi oil loading falls 40% at Red Sea port amid Yemen's reciprocal siege | https://www.presstv.co.uk/Detail/2026/07/27/773191/Saudi-oil-loading-volumes-fall-40--
2026-07-28 | Global | Arkeonews | Unique Medieval 'House on Wheels' from the Kimak Khaganate Unearthed in Kazakhstan | https://arkeonews.net/unique-medieval-house-on-wheels-from-the-kimak-khaganate-unearthed-in-kazakhstan/
2026-07-28 | Global | Archaeology Magazine | Funerary Complex Unearthed in Northern Egypt | https://archaeology.org/news/2026/07/27/funerary-complex-unearthed-in-northern-egypt/
2026-07-28 | Global | The Art Newspaper | Music, Fashion, Film—Photography? Charli xcx image acquired by London's National Portrait Gallery | https://www.theartnewspaper.com/2026/07/27/music-fashion-film-photography-charli-xcx-image-acquired-by-londons-national-portrait-gallery
2026-07-28 | Global | Blooloop | Franklin Institute Unveils Immersive 'Star Wars' Exhibition | https://blooloop.com/news/franklin-institute-unveils-star-wars
2026-07-28 | Global | Hyperallergic | Betye Saar, Who Opened Portals Between Worlds, Dies at 99 | https://hyperallergic.com/betye-saar-who-opened-portals-between-worlds-dies-at-99/
2026-07-28 | Global | The Art Newspaper | Low Kee Hong chosen to curate Biennale of Sydney's next edition | https://www.theartnewspaper.com/2026/07/27/biennale-sydney-curator-2028-low-kee-hong
2026-07-28 | Global | WWD | 75 Fashion Deals and Counting for 2026, According to Capstone Fashion Report | https://wwd.com/business-news/mergers-acquisitions/fashion-ma-deals-2026-capstone-report-1239083357/
2026-07-28 | Global | ArchDaily | From Data to Digital Twins: Japan's PLATEAU Project Offers Open-Access Models of More Than 250 Cities | https://www.archdaily.com/1040412/from-data-to-digital-twins-japans-plateau-project-offers-open-access-models-of-more-than-250-cities
2026-07-28 | Global | The Bookseller | Atlantic Books acquires story of Keir Starmer's 'unfulfilled premiership' | https://www.thebookseller.com/rights/atlantic-books-acquires-story-of-keir-starmers-unfulfilled-premiership
