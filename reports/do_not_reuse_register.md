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

<!-- 2026-08-04 continuity reconciliation: the repository continuity store had
     an empty register while 17 real editions (2026-07-20 .. 2026-08-03) had
     been delivered to the Dropbox test folder. Prior runs delivered but did
     not commit the register back to main. The entries below were reconciled
     by downloading those delivered .docx editions and extracting every
     article hyperlink (URL + outlet anchor text). Section/headline fields are
     placeholders because they were not recoverable per-link from the .docx;
     the date + URL are accurate and are what the rolling-window reuse audit
     enforces. -->
2026-07-20 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/originals/2026/07/houthis-impose-saudi-naval-blockade-opening-new-front-us-iran-war
2026-07-20 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/worlds-oldest-nearly-complete-roman-armor-may-preserve-the-fate-of-a-captured-legionary/
2026-07-20 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/1000-year-old-scandinavian-style-houses-discovered-in-polands-viking-age-wolin/
2026-07-20 | prior-edition | Business Standard | (reconciled from delivered Dropbox edition) | https://www.business-standard.com/world-news/what-wall-street-never-understood-about-gulf-investors-and-their-priorities-126072000259_1.html
2026-07-20 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/07/20/iran-houthi-yemen-saudi-arabia.html
2026-07-20 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/box-office-global-the-odyssey-1236996979/
2026-07-20 | prior-edition | Publishing Perspectives | (reconciled from delivered Dropbox edition) | https://publishingperspectives.com/2026/07/around-the-book-world-monday-july-20th-2026/
2026-07-20 | prior-edition | The Japan Times | (reconciled from delivered Dropbox edition) | https://www.japantimes.co.jp/environment/2026/07/20/climate-change/un-danger-conflict-climate-change/
2026-07-20 | prior-edition | The Korea Herald | (reconciled from delivered Dropbox edition) | https://www.koreaherald.com/article/10812733
2026-07-20 | prior-edition | Variety | (reconciled from delivered Dropbox edition) | https://variety.com/2026/music/news/future-album-billbord-chart-number-one-rolling-stones-1236816201/
2026-07-21 | prior-edition | ARTnews | (reconciled from delivered Dropbox edition) | https://www.artnews.com/art-news/news/shanghai-auction-executives-sentenced-in-major-fraud-case-1234792736/
2026-07-21 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/news/2026/7/20/yemens-houthis-declare-naval-blockade-of-saudi-arabia-what-to-know
2026-07-21 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/video/newsfeed/2026/7/20/houthis-announce-maritime-blockade-on-saudi-arabia
2026-07-21 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-20/yemen-s-houthis-vow-to-impose-maritime-blockade-on-saudi-arabia
2026-07-21 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/toronto-film-festival-2026-line-up-1236998190/
2026-07-21 | prior-edition | Egypt Independent | (reconciled from delivered Dropbox edition) | https://www.egyptindependent.com/newly-discovered-saqqara-tombs-rewrites-history-of-new-kingdom/
2026-07-21 | prior-edition | Euronews | (reconciled from delivered Dropbox edition) | https://www.euronews.com/2026/07/20/yemens-houthis-threaten-bab-el-mandeb-closure-in-embargo-on-saudi-arabia
2026-07-21 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/new-kingdom-tombs-discovered-at-saqqara-provide-new-evidence-of-connections-with-near-east/158655
2026-07-21 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-21 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/witchs-grave-excavation-sheds-new-light-on-neolithic-monument/158555
2026-07-21 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/rare-archaic-necropolis-unearthed-in-southern-italy-reveals-exceptional-ancient-treasures/158665
2026-07-21 | prior-edition | Hyperallergic | (reconciled from delivered Dropbox edition) | https://hyperallergic.com/activists-sue-to-stop-frida-kahlo-works-from-leaving-mexico/
2026-07-21 | prior-edition | Hyperallergic | (reconciled from delivered Dropbox edition) | https://hyperallergic.com/cuban-artist-luis-manuel-otero-alcantara-exiled-to-the-us/
2026-07-21 | prior-edition | Hyperallergic | (reconciled from delivered Dropbox edition) | https://hyperallergic.com/new-museums-shiny-new-building-leaks-during-flash-floods/
2026-07-21 | prior-edition | Nikkei Asia | (reconciled from delivered Dropbox edition) | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/yemen-s-houthis-declare-naval-blockade-on-saudi-arabia
2026-07-21 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/20/armory-show-unveils-230-gallery-line-up-after-moving-fair-to-late-september
2026-07-22 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/news/2026/7/21/saudi-condemns-houthi-blockade-how-will-the-rest-of-the-world-be-impacted
2026-07-22 | prior-edition | Archaeology Magazine | (reconciled from delivered Dropbox edition) | https://archaeology.org/news/2026/07/21/italy-repatriates-artifacts-to-mexico-2/
2026-07-22 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/2000-year-old-main-street-unearthed-at-aspendos-reveals-shops-sewers-and-a-monumental-gate/
2026-07-22 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/archaeologists-uncover-monumental-bronze-age-tomb-with-weapons-and-a-sacrificed-horse-in-armenia/
2026-07-22 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-21/saudi-crude-flow-from-red-sea-hit-record-before-houthi-warning
2026-07-22 | prior-edition | Hyperallergic | (reconciled from delivered Dropbox edition) | https://hyperallergic.com/the-art-institute-of-chicago-to-cut-its-entire-custodial-staff/
2026-07-22 | prior-edition | Publishers Weekly | (reconciled from delivered Dropbox edition) | https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/article/100885-may-sales-shined-aap-reports.html
2026-07-22 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/21/vanderbilt-university-california-college-arts-jensen-huang-gift
2026-07-22 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/21/when-is-appropriation-pastiche-or-copyright-infringement
2026-07-22 | prior-edition | The Boston Globe | (reconciled from delivered Dropbox edition) | https://www.bostonglobe.com/2026/07/21/nation/trump-saudi-arabia-nuclear-agreement/
2026-07-22 | prior-edition | The National | (reconciled from delivered Dropbox edition) | https://www.thenationalnews.com/news/gulf/2026/07/21/saudi-arabia-rejects-houthi-maritime-embargo-threat-and-warns-of-red-sea-escalation/
2026-07-22 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/21/world/middleeast/houthis-yemen-iran-war.html
2026-07-22 | prior-edition | WWD | (reconciled from delivered Dropbox edition) | https://wwd.com/fashion-news/fashion-features/chemena-kamali-fashion-jury-president-2026-hyeres-festival-1239077134/
2026-07-23 | prior-edition | AGBI | (reconciled from delivered Dropbox edition) | https://www.agbi.com/giga-projects/2026/07/deserted-island-what-happened-at-neom-sindalah-and-whats-next/
2026-07-23 | prior-edition | AP via PBS NewsHour | (reconciled from delivered Dropbox edition) | https://www.pbs.org/newshour/world/ap-report-trump-approves-nuclear-agreement-that-may-allow-saudi-arabia-to-enrich-uranium
2026-07-23 | prior-edition | ARTnews | (reconciled from delivered Dropbox edition) | https://www.artnews.com/art-news/news/louvre-apollo-gallery-reopens-without-crown-jewels-1234793182/
2026-07-23 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/originals/2026/07/saudi-nuclear-deal-delivers-strategic-economic-prizes-trump-boosts-gulf-allies
2026-07-23 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/bafta-ai-clause-submission-rules-2027-1237000067/
2026-07-23 | prior-edition | Designboom | (reconciled from delivered Dropbox edition) | https://www.designboom.com/architecture/sanaa-team-ecuador-national-museum-muna-competition-revised-selection-process-estudioa0-caaporarq-jeromehaferdstudio/
2026-07-23 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-23 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/news/trump-to-approve-nuclear-deal-saudi-arabia-despite-regional-proliferation-risks
2026-07-23 | prior-edition | Press TV | (reconciled from delivered Dropbox edition) | https://www.presstv.co.uk/Detail/2026/07/22/772814/Yemen-Saudi-Arabia-ships-blockade-warning
2026-07-23 | prior-edition | Publishers Weekly | (reconciled from delivered Dropbox edition) | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/100890-how-holt-finished-mahmoud-khalil-s-no-land-to-stand-on-in-just-six-months.html
2026-07-23 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/22/jessica-morgan-named-new-tate-director
2026-07-23 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/22/european-union-officially-pull-2m-venice-biennale-funding-over-russian-participation
2026-07-23 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/22/artforum-bids-farewell-to-back-cover-star-in-style
2026-07-23 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/movies/movie-news/odyssey-box-office-2026-practical-effects-1236652219/
2026-07-23 | prior-edition | The Korea Herald | (reconciled from delivered Dropbox edition) | https://www.koreaherald.com/article/10815414
2026-07-23 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/22/world/middleeast/houthis-saudi-oil-tankers-red-sea.html
2026-07-24 | prior-edition | Arab News (Pakistan) | (reconciled from delivered Dropbox edition) | https://www.arabnews.com/node/2652024/lifestyle
2026-07-24 | prior-edition | Arab News Pakistan | (reconciled from delivered Dropbox edition) | https://www.arabnews.pk/node/2652024/lifestyle
2026-07-24 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/07/23/oil-prices-today-wti-brent-trump-iran-hormuz.html
2026-07-24 | prior-edition | Condé Nast Traveller Middle East | (reconciled from delivered Dropbox edition) | https://www.cntravellerme.com/story/from-portland-to-paris-the-chefs-taking-middle-eastern-food-to-the-world
2026-07-24 | prior-edition | Foreign Policy | (reconciled from delivered Dropbox edition) | https://foreignpolicy.com/2026/07/23/trump-us-saudi-nuclear-deal-weapons-iran-israel-arms-race/
2026-07-24 | prior-edition | IndieWire | (reconciled from delivered Dropbox edition) | https://www.indiewire.com/news/festivals/venice-film-festival-reveals-2026-lineup-1235206616/
2026-07-24 | prior-edition | Pakistan Point | (reconciled from delivered Dropbox edition) | https://www.pakistanpoint.com/ar/news/saudi-arabia/story-2225211.html
2026-07-24 | prior-edition | Reporter Gourmet | (reconciled from delivered Dropbox edition) | https://reportergourmet.com/en/news/10512-michelin-guide-italy-15-new-entries-in-july-from-pascuccis-bistro-to-the-boom-in-basilicata-the-restaurants
2026-07-24 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/business/2026/jul/23/bab-al-mandab-blockade-push-oil-100-houthi-ships
2026-07-24 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/commentisfree/2026/jul/23/trump-saudi-nuclear-deal
2026-07-24 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/movies/movie-news/comic-con-2026-hall-h-preview-1236653276/
2026-07-24 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/23/world/middleeast/saudi-arabia-nuclear.html
2026-07-24 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/23/world/middleeast/trump-saudi-arabia-palestinian-state.html
2026-07-24 | prior-edition | UNESCO | (reconciled from delivered Dropbox edition) | https://www.unesco.org/en/articles/world-heritage-committee-will-examine-new-nominations-and-state-conservation-inscribed-sites
2026-07-24 | prior-edition | Variety | (reconciled from delivered Dropbox edition) | https://variety.com/2026/film/news/vijay-jana-nayagan-release-date-2-1236811540/
2026-07-25 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/byzantine-shipwreck-off-croatia-yields-record-gold-treasure-and-an-emperors-ring/
2026-07-25 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/4500-year-old-mega-dams-near-egypts-red-pyramid-may-reveal-an-ancient-engineering-breakthrough/
2026-07-25 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/two-premature-infants-possibly-twins-found-buried-in-an-abandoned-roman-latrine-at-ephesus/
2026-07-25 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/turkic-period-tomb-in-mongolia-yields-1400-year-old-peach-wood-bow-and-runic-inscribed-horse-head-fiddle/
2026-07-25 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/newsletters/2026-07-24/oil-tankers-run-the-houthi-gauntlet-to-keep-saudi-exports-flowing
2026-07-25 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-25 | prior-edition | RTÉ | (reconciled from delivered Dropbox edition) | https://www.rte.ie/news/2026/0725/1585036-houthis-strikes/
2026-07-25 | prior-edition | The A.V. Club | (reconciled from delivered Dropbox edition) | https://www.avclub.com/weird-al-yankovic-riyadh-comedy-festival
2026-07-25 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/24/unesco-adds-ancient-greek-city-tauric-chersonese-in-crimea-to-world-heritage-in-danger-list
2026-07-25 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/24/swedish-viking-centre-that-loaned-ship-for-the-odyssey-alleges-that-it-has-not-been-paid-for-damages
2026-07-25 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/24/buffalo-akg-art-museum-two-director-roles-promotions
2026-07-25 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/24/jen-catron-paul-outlaw-times-square-hot-dog-returns
2026-07-25 | prior-edition | The National | (reconciled from delivered Dropbox edition) | https://www.thenationalnews.com/news/2026/07/24/houthi-official-says-saudi-strike-targets-hodeidah-port-after-attack-on-saudi-vessel/
2026-07-26 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/roman-gold-barracks-and-surgical-tools-unearthed-at-vindonissas-first-military-camp-in-switzerland/
2026-07-26 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/5000-year-old-bronze-age-temple-with-altars-and-sacred-hearths-discovered-in-eastern-turkiye/
2026-07-26 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-25/houthi-claim-missile-strikes-on-southern-saudi-arabia
2026-07-26 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-26 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/07/25/saudi-military-strikes-iran-backed-houthi-targets-yemen.html
2026-07-26 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/ryan-gosling-ghost-rider-marvel-comic-con-1237003726/
2026-07-26 | prior-edition | Fox News | (reconciled from delivered Dropbox edition) | https://www.foxnews.com/media/weird-al-yankovic-says-he-walked-away-from-seven-figure-comedy-festival-offer-saudi-arabia
2026-07-26 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/heatwave-reveals-lost-welsh-landscapes/158718
2026-07-26 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-26 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/movies/movie-news/black-panther-3-marvel-ryan-coogler-comic-con-1236656570/
2026-07-26 | prior-edition | The Stage | (reconciled from delivered Dropbox edition) | https://www.thestage.co.uk/news/rsc-cancels-game-of-thrones-play-preview-performances
2026-07-26 | prior-edition | WWD | (reconciled from delivered Dropbox edition) | https://wwd.com/pop-culture/celebrity-news/michelle-yeoh-hunter-schafer-comic-con-outfits-1239081924/
2026-07-27 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities
2026-07-27 | prior-edition | Associated Press | (reconciled from delivered Dropbox edition) | https://apnews.com/article/unesco-mount-olympus-japan-ancient-capitals-1d3fabaa482d9384b1cb0b5c917ce5d5
2026-07-27 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-27 | prior-edition | CNN | (reconciled from delivered Dropbox edition) | https://www.cnn.com/2026/07/26/world/video/fungi-leather-farm-indonesia-transformers-hkn-spc
2026-07-27 | prior-edition | Fashionista | (reconciled from delivered Dropbox edition) | https://fashionista.com/2026/07/paris-fashion-week-september-2026-schedule
2026-07-27 | prior-edition | Newsweek | (reconciled from delivered Dropbox edition) | https://www.newsweek.com/antoni-gaudi-118-year-old-lost-nyc-skyscraper-design-interiors-unveiled-12240546
2026-07-27 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/27/peru-earthquake-damages-16th-century-church-iglesia-apostol-santiago
2026-07-27 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/commentisfree/2026/jul/26/the-guardian-view-on-a-us-saudi-nuclear-agreement-an-offer-that-further-erodes-international-safeguards
2026-07-27 | prior-edition | WWD | (reconciled from delivered Dropbox edition) | https://wwd.com/business-news/retail/saudi-arabia-fashion-food-design-selfridges-corner-shop-1239081869/
2026-07-28 | prior-edition | AGBI | (reconciled from delivered Dropbox edition) | https://www.agbi.com/analysis/oil-and-gas/2026/07/yanbu-attacks-expose-saudi-oil-export-vulnerability/
2026-07-28 | prior-edition | ARTnews | (reconciled from delivered Dropbox edition) | https://www.artnews.com/art-news/news/betye-saar-dead-1234793560/
2026-07-28 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/originals/2026/07/red-sea-shipping-slows-after-houthi-attack-saudi-arabia-data-shows
2026-07-28 | prior-edition | ArchDaily | (reconciled from delivered Dropbox edition) | https://www.archdaily.com/1040412/from-data-to-digital-twins-japans-plateau-project-offers-open-access-models-of-more-than-250-cities
2026-07-28 | prior-edition | Archaeology Magazine | (reconciled from delivered Dropbox edition) | https://archaeology.org/news/2026/07/27/funerary-complex-unearthed-in-northern-egypt/
2026-07-28 | prior-edition | Archaeology Magazine | (reconciled from delivered Dropbox edition) | https://archaeology.org/news/2026/07/27/roman-battle-camp-found-in-spain/
2026-07-28 | prior-edition | Archaeology News | (reconciled from delivered Dropbox edition) | https://archaeologymag.com/2026/07/first-roman-camp-at-vindonissa-revealed/
2026-07-28 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/unique-medieval-house-on-wheels-from-the-kimak-khaganate-unearthed-in-kazakhstan/
2026-07-28 | prior-edition | Blooloop | (reconciled from delivered Dropbox edition) | https://blooloop.com/news/franklin-institute-unveils-star-wars
2026-07-28 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/07/28/us-iran-war-trump-hormuz.html
2026-07-28 | prior-edition | Dezeen | (reconciled from delivered Dropbox edition) | https://www.dezeen.com/2026/07/27/rshps-one-shanghai-tower/
2026-07-28 | prior-edition | Foreign Policy | (reconciled from delivered Dropbox edition) | https://foreignpolicy.com/2026/07/27/trump-nuclear-saudi-arabia-deal-iran-israel/
2026-07-28 | prior-edition | Hyperallergic | (reconciled from delivered Dropbox edition) | https://hyperallergic.com/betye-saar-who-opened-portals-between-worlds-dies-at-99/
2026-07-28 | prior-edition | Press TV | (reconciled from delivered Dropbox edition) | https://www.presstv.co.uk/Detail/2026/07/27/773191/Saudi-oil-loading-volumes-fall-40--
2026-07-28 | prior-edition | Tech Times | (reconciled from delivered Dropbox edition) | https://www.techtimes.com/articles/321672/20260727/d-day-beaches-okefenokee-swamp-mount-olympus-join-unesco-world-heritage-list.htm
2026-07-28 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/27/music-fashion-film-photography-charli-xcx-image-acquired-by-londons-national-portrait-gallery
2026-07-28 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/27/biennale-sydney-curator-2028-low-kee-hong
2026-07-28 | prior-edition | The Bookseller | (reconciled from delivered Dropbox edition) | https://www.thebookseller.com/rights/atlantic-books-acquires-story-of-keir-starmers-unfulfilled-premiership
2026-07-28 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/world/2026/jul/28/asia-energy-oil-crisis-red-sea-blockade-houthis
2026-07-28 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/27/world/middleeast/houthis-saudi-arabia-iran-war.html
2026-07-28 | prior-edition | The Week | (reconciled from delivered Dropbox edition) | https://www.theweek.in/news/middle-east/2026/07/27/saudi-arabia-oil-refinery-attack-abqaiq-fire-impact.html
2026-07-28 | prior-edition | WWD | (reconciled from delivered Dropbox edition) | https://wwd.com/business-news/mergers-acquisitions/fashion-ma-deals-2026-capstone-report-1239083357/
2026-07-29 | prior-edition | ARTnews | (reconciled from delivered Dropbox edition) | https://www.artnews.com/art-news/news/phildelphia-museum-of-art-ran-a-10-m-deficit-1234793631
2026-07-29 | prior-edition | Artsy | (reconciled from delivered Dropbox edition) | https://www.artsy.net/article/artsy-editorial-moma-host-chess-matches-honor-marcel-duchamp
2026-07-29 | prior-edition | Associated Press | (reconciled from delivered Dropbox edition) | https://www.clickorlando.com/news/world/2026/07/28/saudi-arabia-says-it-shot-down-more-drones-as-houthis-claim-to-have-turned-back-tanker/
2026-07-29 | prior-edition | Blooloop | (reconciled from delivered Dropbox edition) | https://blooloop.com/news/shenzhen-natural-history-museum-opens
2026-07-29 | prior-edition | Deutsche Welle | (reconciled from delivered Dropbox edition) | https://www.dw.com/en/will-pakistan-intervene-amid-houthi-attacks-on-saudi-ships/a-78144890
2026-07-29 | prior-edition | HeritageDaily | (reconciled from delivered Dropbox edition) | https://www.heritagedaily.com/2026/07/archaeologists-map-buried-sacred-precinct-of-the-aztec-capital-tenochtitlan/158744
2026-07-29 | prior-edition | Human Rights Watch | (reconciled from delivered Dropbox edition) | https://www.hrw.org/news/2026/07/28/saudi-arabia-new-executions-of-ethiopian-migrants
2026-07-29 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/iraqi-paramilitary-force-condemns-saudi-us-attacks-headquarters
2026-07-29 | prior-edition | Publishers Weekly | (reconciled from delivered Dropbox edition) | https://www.publishersweekly.com/pw/by-topic/industry-news/awards-and-prizes/article/100927-2026-booker-prize-longlist-announced.html
2026-07-29 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/28/guggenheim-abu-dhabi-announces-opening-date
2026-07-29 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/28/culture-minister-catherine-pegard-reveals-national-security-plan-following-another-major-museum-theft-in-france
2026-07-29 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/world/2026/jul/29/iran-missile-attack-us-base-forces
2026-07-29 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/movies/movie-news/marion-cotillard-mike-leigh-pablo-larrain-in-san-sebastian-1236658023
2026-07-29 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/business/business-news/penske-media-sued-hollywood-foreign-press-golden-globes-1236658413
2026-07-29 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/28/world/middleeast/houthis-strike-saudi-tanker.html
2026-07-30 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/news/2026/7/29/iraq-calls-saudi-us-attacks-flagrant-violation-of-sovereignty
2026-07-30 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/archaeologists-unearth-two-miniature-mammoth-ivory-birds-carved-40000-years-ago/
2026-07-30 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/iberian-warrior-family-buried-2200-years-ago-with-falcatas-and-a-tanit-burner-discovered-in-alicante/
2026-07-30 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/07/29/oil-prices-today-brent-wti-iran-us-hormuz.html
2026-07-30 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-seeks-international-coalition-protect-red-sea-shipping
2026-07-30 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/29/betye-saar-obituary-legendary-los-angeles-assemblage-artist
2026-07-30 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/29/sites-in-iran-lebanon-and-palestine-among-25-new-additions-to-unescos-world-heritage-list
2026-07-30 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/29/english-heritage-debuts-daily-prize-draw-for-private-time-at-stonehenge-this-august
2026-07-30 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/29/municipal-arts-funding-covid-rebound-dataarts-southern-methodist-university-study
2026-07-30 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/world/2026/jul/29/us-saudi-strikes-in-iraq-have-pushed-the-region-into-uncharted-territory-analysts-warn
2026-07-30 | prior-edition | The Irish Times | (reconciled from delivered Dropbox edition) | https://www.irishtimes.com/culture/music/2026/07/29/glen-hansard-dies-in-dublin-motorbike-crash/
2026-07-30 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/29/world/middleeast/saudi-arabia-us-iran-war.html
2026-07-31 | prior-edition | AGBI | (reconciled from delivered Dropbox edition) | https://www.agbi.com/analysis/economy/2026/07/saudi-economy-shrinks-first-time-in-three-years-as-oil-output-drops/
2026-07-31 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/newsletter/2026-07-30/red-seas-shared-history-comes-alive-jeddah
2026-07-31 | prior-edition | Antiwar.com | (reconciled from delivered Dropbox edition) | https://news.antiwar.com/2026/07/30/al-houthi-says-there-are-indications-saudi-arabia-is-planning-major-escalation-in-yemen/
2026-07-31 | prior-edition | Archaeology Magazine | (reconciled from delivered Dropbox edition) | https://archaeology.org/news/2026/07/30/possible-marks-of-cannibalism-detected-on-adult-homo-antecessor-fossils/
2026-07-31 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/lidar-reveals-up-to-30000-earthworks-built-by-a-lost-amazonian-civilization/
2026-07-31 | prior-edition | Arkeonews | (reconciled from delivered Dropbox edition) | https://arkeonews.net/archaeologists-unearth-two-miniature-mammoth-ivory-birds-carved-40000-years-ago/
2026-07-31 | prior-edition | Artnet News | (reconciled from delivered Dropbox edition) | https://news.artnet.com/artnet-bulletin/new-tariffs-july-30-2790904
2026-07-31 | prior-edition | BBC | (reconciled from delivered Dropbox edition) | https://www.bbc.co.uk/news/articles/ckg4jxxn4ggo
2026-07-31 | prior-edition | Bloomberg | (reconciled from delivered Dropbox edition) | https://www.bloomberg.com/news/articles/2026-07-30/saudi-budget-deficit-narrows-three-quarters-on-wartime-oil-spike
2026-07-31 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/wicker-trailer-olivia-colman-alexander-skarsgard-1237013463/
2026-07-31 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/30/life-and-treasure-from-ancient-egypts-golden-city-revealed-in-san-francisco-show
2026-07-31 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/30/amazon-style-conditions-va-east-storehouse-officers-overwhelmingly-vote-to-strike-as-other-museum-workers-also-consider-industrial-action
2026-07-31 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/30/comment-obama-presidential-center-art-architecture-gothic-cathedral
2026-07-31 | prior-edition | The Guardian | (reconciled from delivered Dropbox edition) | https://www.theguardian.com/world/2026/jul/30/saudi-forces-planning-major-offensive-against-houthis-central-yemen
2026-07-31 | prior-edition | The Hollywood Reporter | (reconciled from delivered Dropbox edition) | https://www.hollywoodreporter.com/tv/tv-news/clueless-sequel-series-paramount-1236659500/
2026-07-31 | prior-edition | The New York Times | (reconciled from delivered Dropbox edition) | https://www.nytimes.com/2026/07/30/world/middleeast/saudi-arabia-red-sea-houthis.html
2026-08-01 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/originals/2026/07/oil-price-rises-after-iran-says-it-stops-ships-hormuz
2026-08-01 | prior-edition | Al-Monitor | (reconciled from delivered Dropbox edition) | https://www.al-monitor.com/originals/2026/07/italy-minister-rejects-opposition-criticism-saudi-troop-deployment
2026-08-01 | prior-edition | Artnet News | (reconciled from delivered Dropbox edition) | https://news.artnet.com/market/industry-intel-july-31-2791743
2026-08-01 | prior-edition | Billboard | (reconciled from delivered Dropbox edition) | https://www.billboard.com/pro/suno-liable-gema-german-copyright-lawsuit/
2026-08-01 | prior-edition | Billboard | (reconciled from delivered Dropbox edition) | https://www.billboard.com/pro/sonys-global-music-biz-revenue-tops-3-53-billion-2026-q2/
2026-08-01 | prior-edition | Billboard | (reconciled from delivered Dropbox edition) | https://www.billboard.com/music/pop/ariana-grande-petal-album-listen-1236306614/
2026-08-01 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/07/box-office-spider-man-brand-new-day-1237014268/
2026-08-01 | prior-edition | Deutsche Welle | (reconciled from delivered Dropbox edition) | https://www.dw.com/en/military-flare-up-between-houthis-and-saudi-arabia-challenges-relative-calm-in-yemen/a-78186262
2026-08-01 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-terms-trumps-gaza-demilitarisation-deal-historic
2026-08-01 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/yemeni-forces-say-eight-saudi-tankers-forced-reroute
2026-08-01 | prior-edition | The Art Newspaper | (reconciled from delivered Dropbox edition) | https://www.theartnewspaper.com/2026/07/31/japans-400-year-old-kumamoto-castle-damaged-by-71-magnitude-earthquake
2026-08-01 | prior-edition | WWD | (reconciled from delivered Dropbox edition) | https://wwd.com/fashion-news/fashion-scoops/costume-institute-met-next-exhibition-john-galliano-1239089295/
2026-08-02 | prior-edition | AGBI | (reconciled from delivered Dropbox edition) | https://www.agbi.com/analysis/oil-and-gas/2026/08/great-gulf-pipeline-race-which-routes-will-actually-be-built/
2026-08-02 | prior-edition | Artnet News | (reconciled from delivered Dropbox edition) | https://news.artnet.com/art-world/ai-provenance-assistant-looted-art-tool-2792609
2026-08-02 | prior-edition | Axios | (reconciled from delivered Dropbox edition) | https://www.axios.com/2026/08/01/saudi-crown-prince-trump-iran-attacks
2026-08-02 | prior-edition | Deadline | (reconciled from delivered Dropbox edition) | https://deadline.com/2026/08/vincent-pastore-dead-the-sopranos-star-big-pussy-1237015282/
2026-08-02 | prior-edition | Fortune | (reconciled from delivered Dropbox edition) | https://fortune.com/2026/08/01/trump-iran-strikes-mideast-allies-emerging-strait-of-hormuz/
2026-08-02 | prior-edition | Nikkei Asia | (reconciled from delivered Dropbox edition) | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/trump-says-mideast-allies-have-reached-outlines-of-deal-to-end-iran-war
2026-08-02 | prior-edition | Variety | (reconciled from delivered Dropbox edition) | https://variety.com/2026/film/news/box-office-spider-man-brand-new-day-opening-day-record-1236825606/
2026-08-03 | prior-edition | Al Jazeera | (reconciled from delivered Dropbox edition) | https://www.aljazeera.com/news/2026/8/2/no-breakthrough-on-strait-of-hormuz-as-trump-halts-attack-on-iran
2026-08-03 | prior-edition | CNBC | (reconciled from delivered Dropbox edition) | https://www.cnbc.com/2026/08/02/spider-man-brand-new-day-box-office-355-million-domestic-opening.html
2026-08-03 | prior-edition | Chicago Sun-Times | (reconciled from delivered Dropbox edition) | https://chicago.suntimes.com/lollapalooza/2026/08/02/review-tate-mcrae-closes-out-lollapalooza-with-surprisingly-subdued-set
2026-08-03 | prior-edition | Middle East Eye | (reconciled from delivered Dropbox edition) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-iranian-foreign-ministers-discuss-efforts-reduce-regional-tensions
2026-08-03 | prior-edition | Press TV | (reconciled from delivered Dropbox edition) | https://www.presstv.co.uk/Detail/2026/08/02/773592/Persian-Gulf-states-sovereignty-Iran-war-US-Israel-aggression-
2026-08-03 | prior-edition | The Philadelphia Inquirer | (reconciled from delivered Dropbox edition) | https://www.inquirer.com/news/nation-world/trump-iron-pause-strikes-negotiations-strait-hormuz-mohammed-bin-salman-20260802.html
2026-08-04 | Saudi Arabia/Regional | AGBI | Saudi crude moves through Red Sea despite Houthi threat | https://www.agbi.com/shipping/2026/08/houthi-threat-fails-to-deter-saudi-crude-from-red-sea-passage/
2026-08-04 | Saudi Arabia/Regional | MEED | Saudi economy swings to 4.8% contraction | https://www.meed.com/saudi-economy-swings-to-48-contraction
2026-08-04 | Saudi Arabia/Regional | Foreign Policy | A Saudi-Emirati Thaw Can Help Contain Iran | https://foreignpolicy.com/2026/08/03/saudi-arabia-emirates-iran-israel-uae-missile-defense-sanctions-hormuz/
2026-08-04 | Saudi Arabia/Regional | SANA | Syria's chargé d'affaires discusses cultural cooperation with Saudi library's CEO | https://sana.sy/en/culture-and-arts/2334040/
2026-08-04 | Global | The Art Newspaper | Unesco urged to investigate after Israeli forces trigger explosions near Lebanon's World Heritage-listed Beaufort Castle | https://www.theartnewspaper.com/2026/08/03/unesco-urged-to-investigate-after-israeli-forces-trigger-explosion-near-lebanons-world-heritage-listed-beaufort-castle
2026-08-04 | Global | Arkeonews | 2,500-Year-Old Monumental Statue of a Long-Haired Young Man Discovered Remarkably Preserved in Ancient Sardis | https://arkeonews.net/well-preserved-2-2-meter-monumental-statue-with-long-hair-emerges-after-2500-years-in-ancient-sardis/
2026-08-04 | Global | Archaeology | Funerary Complex Excavated Near Egypt's Mediterranean Coast | https://archaeology.org/news/2026/08/03/funerary-complex-excavated-near-egypts-mediterranean-coast/
2026-08-04 | Global | Arkeonews | 3,000-Year-Old Bronze Hoard Unearthed in Czech Wetland | https://arkeonews.net/3000-year-old-bronze-hoard-unearthed-in-czech-wetland/
2026-08-04 | Global | The Art Newspaper | Royal Museums Greenwich workers vote to strike over pay and working conditions | https://www.theartnewspaper.com/2026/08/03/royal-museums-greenwich-workers-vote-to-strike-over-pay-and-working-conditions
2026-08-04 | Global | ARTnews | Gagosian Gives Up London and Basel Spaces as Mega-Galleries Rethink Their Footprints | https://www.artnews.com/art-news/news/gagosian-london-basel-gallery-closures-1234794210/
2026-08-04 | Global | Deadline | Universal Becomes First Studio To Conquer $4B+ At Global B.O. YTD As 'Odyssey' Heads For $1B WW | https://deadline.com/2026/08/universal-2026-global-box-office-odyssey-billion-1237015503/
2026-08-04 | Global | WWD | WME Sells New York Fashion Week and NYFW: The Shows Trademarks and Intellectual Property to Signet Fashion | https://wwd.com/fashion-news/fashion-features/wme-sells-new-york-fashion-week-nyfw-signet-fashion-1239088648/
