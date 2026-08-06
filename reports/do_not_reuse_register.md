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

<!-- RECONSTRUCTED 2026-08-06: The 19 editions delivered to the Dropbox
     '05_Claude Test' folder between 2026-07-20 and 2026-08-05 were never
     committed back to this repo by their runs, so this register was empty
     despite ~231 articles already having been used. The entries below were
     reconstructed by parsing the delivered .docx files' hyperlinks (Stage 0.5
     reconciliation). 'section'/'headline' fields are placeholders; the date
     and URL are authoritative and are what the rolling-window reuse check
     enforces. -->

2026-07-20 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-07-20) | https://www.al-monitor.com/originals/2026/07/houthis-impose-saudi-naval-blockade-opening-new-front-us-iran-war
2026-07-20 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-20) | https://arkeonews.net/1000-year-old-scandinavian-style-houses-discovered-in-polands-viking-age-wolin/
2026-07-20 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-20) | https://arkeonews.net/worlds-oldest-nearly-complete-roman-armor-may-preserve-the-fate-of-a-captured-legionary/
2026-07-20 | reconstructed | Business Standard | (reconstructed from delivered edition 2026-07-20) | https://www.business-standard.com/world-news/what-wall-street-never-understood-about-gulf-investors-and-their-priorities-126072000259_1.html
2026-07-20 | reconstructed | CNBC | (reconstructed from delivered edition 2026-07-20) | https://www.cnbc.com/2026/07/20/iran-houthi-yemen-saudi-arabia.html
2026-07-20 | reconstructed | Deadline | (reconstructed from delivered edition 2026-07-20) | https://deadline.com/2026/07/box-office-global-the-odyssey-1236996979/
2026-07-20 | reconstructed | Publishing Perspectives | (reconstructed from delivered edition 2026-07-20) | https://publishingperspectives.com/2026/07/around-the-book-world-monday-july-20th-2026/
2026-07-20 | reconstructed | The Japan Times | (reconstructed from delivered edition 2026-07-20) | https://www.japantimes.co.jp/environment/2026/07/20/climate-change/un-danger-conflict-climate-change/
2026-07-20 | reconstructed | The Korea Herald | (reconstructed from delivered edition 2026-07-20) | https://www.koreaherald.com/article/10812733
2026-07-20 | reconstructed | Variety | (reconstructed from delivered edition 2026-07-20) | https://variety.com/2026/music/news/future-album-billbord-chart-number-one-rolling-stones-1236816201/
2026-07-21 | reconstructed | ARTnews | (reconstructed from delivered edition 2026-07-21) | https://www.artnews.com/art-news/news/shanghai-auction-executives-sentenced-in-major-fraud-case-1234792736/
2026-07-21 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-07-21) | https://www.aljazeera.com/news/2026/7/20/yemens-houthis-declare-naval-blockade-of-saudi-arabia-what-to-know
2026-07-21 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-07-21) | https://www.aljazeera.com/video/newsfeed/2026/7/20/houthis-announce-maritime-blockade-on-saudi-arabia
2026-07-21 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-21) | https://www.bloomberg.com/news/articles/2026-07-20/yemen-s-houthis-vow-to-impose-maritime-blockade-on-saudi-arabia
2026-07-21 | reconstructed | Deadline | (reconstructed from delivered edition 2026-07-21) | https://deadline.com/2026/07/toronto-film-festival-2026-line-up-1236998190/
2026-07-21 | reconstructed | Egypt Independent | (reconstructed from delivered edition 2026-07-21) | https://www.egyptindependent.com/newly-discovered-saqqara-tombs-rewrites-history-of-new-kingdom/
2026-07-21 | reconstructed | Euronews | (reconstructed from delivered edition 2026-07-21) | https://www.euronews.com/2026/07/20/yemens-houthis-threaten-bab-el-mandeb-closure-in-embargo-on-saudi-arabia
2026-07-21 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-21) | https://www.heritagedaily.com/2026/07/new-kingdom-tombs-discovered-at-saqqara-provide-new-evidence-of-connections-with-near-east/158655
2026-07-21 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-21) | https://www.heritagedaily.com/2026/07/rare-archaic-necropolis-unearthed-in-southern-italy-reveals-exceptional-ancient-treasures/158665
2026-07-21 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-21) | https://www.heritagedaily.com/2026/07/witchs-grave-excavation-sheds-new-light-on-neolithic-monument/158555
2026-07-21 | reconstructed | Hyperallergic | (reconstructed from delivered edition 2026-07-21) | https://hyperallergic.com/activists-sue-to-stop-frida-kahlo-works-from-leaving-mexico/
2026-07-21 | reconstructed | Hyperallergic | (reconstructed from delivered edition 2026-07-21) | https://hyperallergic.com/cuban-artist-luis-manuel-otero-alcantara-exiled-to-the-us/
2026-07-21 | reconstructed | Hyperallergic | (reconstructed from delivered edition 2026-07-21) | https://hyperallergic.com/new-museums-shiny-new-building-leaks-during-flash-floods/
2026-07-21 | reconstructed | Nikkei Asia | (reconstructed from delivered edition 2026-07-21) | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/yemen-s-houthis-declare-naval-blockade-on-saudi-arabia
2026-07-21 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-21) | https://www.theartnewspaper.com/2026/07/20/armory-show-unveils-230-gallery-line-up-after-moving-fair-to-late-september
2026-07-22 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-07-22) | https://www.aljazeera.com/news/2026/7/21/saudi-condemns-houthi-blockade-how-will-the-rest-of-the-world-be-impacted
2026-07-22 | reconstructed | Archaeology Magazine | (reconstructed from delivered edition 2026-07-22) | https://archaeology.org/news/2026/07/21/italy-repatriates-artifacts-to-mexico-2/
2026-07-22 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-22) | https://arkeonews.net/2000-year-old-main-street-unearthed-at-aspendos-reveals-shops-sewers-and-a-monumental-gate/
2026-07-22 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-22) | https://arkeonews.net/archaeologists-uncover-monumental-bronze-age-tomb-with-weapons-and-a-sacrificed-horse-in-armenia/
2026-07-22 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-22) | https://www.bloomberg.com/news/articles/2026-07-21/saudi-crude-flow-from-red-sea-hit-record-before-houthi-warning
2026-07-22 | reconstructed | Hyperallergic | (reconstructed from delivered edition 2026-07-22) | https://hyperallergic.com/the-art-institute-of-chicago-to-cut-its-entire-custodial-staff/
2026-07-22 | reconstructed | Publishers Weekly | (reconstructed from delivered edition 2026-07-22) | https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/article/100885-may-sales-shined-aap-reports.html
2026-07-22 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-22) | https://www.theartnewspaper.com/2026/07/21/vanderbilt-university-california-college-arts-jensen-huang-gift
2026-07-22 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-22) | https://www.theartnewspaper.com/2026/07/21/when-is-appropriation-pastiche-or-copyright-infringement
2026-07-22 | reconstructed | The Boston Globe | (reconstructed from delivered edition 2026-07-22) | https://www.bostonglobe.com/2026/07/21/nation/trump-saudi-arabia-nuclear-agreement/
2026-07-22 | reconstructed | The National | (reconstructed from delivered edition 2026-07-22) | https://www.thenationalnews.com/news/gulf/2026/07/21/saudi-arabia-rejects-houthi-maritime-embargo-threat-and-warns-of-red-sea-escalation/
2026-07-22 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-22) | https://www.nytimes.com/2026/07/21/world/middleeast/houthis-yemen-iran-war.html
2026-07-22 | reconstructed | WWD | (reconstructed from delivered edition 2026-07-22) | https://wwd.com/fashion-news/fashion-features/chemena-kamali-fashion-jury-president-2026-hyeres-festival-1239077134/
2026-07-23 | reconstructed | AGBI | (reconstructed from delivered edition 2026-07-23) | https://www.agbi.com/giga-projects/2026/07/deserted-island-what-happened-at-neom-sindalah-and-whats-next/
2026-07-23 | reconstructed | AP via PBS NewsHour | (reconstructed from delivered edition 2026-07-23) | https://www.pbs.org/newshour/world/ap-report-trump-approves-nuclear-agreement-that-may-allow-saudi-arabia-to-enrich-uranium
2026-07-23 | reconstructed | ARTnews | (reconstructed from delivered edition 2026-07-23) | https://www.artnews.com/art-news/news/louvre-apollo-gallery-reopens-without-crown-jewels-1234793182/
2026-07-23 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-07-23) | https://www.al-monitor.com/originals/2026/07/saudi-nuclear-deal-delivers-strategic-economic-prizes-trump-boosts-gulf-allies
2026-07-23 | reconstructed | Deadline | (reconstructed from delivered edition 2026-07-23) | https://deadline.com/2026/07/bafta-ai-clause-submission-rules-2027-1237000067/
2026-07-23 | reconstructed | Designboom | (reconstructed from delivered edition 2026-07-23) | https://www.designboom.com/architecture/sanaa-team-ecuador-national-museum-muna-competition-revised-selection-process-estudioa0-caaporarq-jeromehaferdstudio/
2026-07-23 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-23) | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-23 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-07-23) | https://www.middleeasteye.net/news/trump-to-approve-nuclear-deal-saudi-arabia-despite-regional-proliferation-risks
2026-07-23 | reconstructed | Press TV | (reconstructed from delivered edition 2026-07-23) | https://www.presstv.co.uk/Detail/2026/07/22/772814/Yemen-Saudi-Arabia-ships-blockade-warning
2026-07-23 | reconstructed | Publishers Weekly | (reconstructed from delivered edition 2026-07-23) | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/100890-how-holt-finished-mahmoud-khalil-s-no-land-to-stand-on-in-just-six-months.html
2026-07-23 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-23) | https://www.theartnewspaper.com/2026/07/22/artforum-bids-farewell-to-back-cover-star-in-style
2026-07-23 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-23) | https://www.theartnewspaper.com/2026/07/22/european-union-officially-pull-2m-venice-biennale-funding-over-russian-participation
2026-07-23 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-23) | https://www.theartnewspaper.com/2026/07/22/jessica-morgan-named-new-tate-director
2026-07-23 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-23) | https://www.hollywoodreporter.com/movies/movie-news/odyssey-box-office-2026-practical-effects-1236652219/
2026-07-23 | reconstructed | The Korea Herald | (reconstructed from delivered edition 2026-07-23) | https://www.koreaherald.com/article/10815414
2026-07-23 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-23) | https://www.nytimes.com/2026/07/22/world/middleeast/houthis-saudi-oil-tankers-red-sea.html
2026-07-24 | reconstructed | Arab News (Pakistan) | (reconstructed from delivered edition 2026-07-24) | https://www.arabnews.com/node/2652024/lifestyle
2026-07-24 | reconstructed | Arab News Pakistan | (reconstructed from delivered edition 2026-07-24) | https://www.arabnews.pk/node/2652024/lifestyle
2026-07-24 | reconstructed | CNBC | (reconstructed from delivered edition 2026-07-24) | https://www.cnbc.com/2026/07/23/oil-prices-today-wti-brent-trump-iran-hormuz.html
2026-07-24 | reconstructed | Condé Nast Traveller Middle East | (reconstructed from delivered edition 2026-07-24) | https://www.cntravellerme.com/story/from-portland-to-paris-the-chefs-taking-middle-eastern-food-to-the-world
2026-07-24 | reconstructed | Foreign Policy | (reconstructed from delivered edition 2026-07-24) | https://foreignpolicy.com/2026/07/23/trump-us-saudi-nuclear-deal-weapons-iran-israel-arms-race/
2026-07-24 | reconstructed | IndieWire | (reconstructed from delivered edition 2026-07-24) | https://www.indiewire.com/news/festivals/venice-film-festival-reveals-2026-lineup-1235206616/
2026-07-24 | reconstructed | Pakistan Point | (reconstructed from delivered edition 2026-07-24) | https://www.pakistanpoint.com/ar/news/saudi-arabia/story-2225211.html
2026-07-24 | reconstructed | Reporter Gourmet | (reconstructed from delivered edition 2026-07-24) | https://reportergourmet.com/en/news/10512-michelin-guide-italy-15-new-entries-in-july-from-pascuccis-bistro-to-the-boom-in-basilicata-the-restaurants
2026-07-24 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-24) | https://www.theguardian.com/business/2026/jul/23/bab-al-mandab-blockade-push-oil-100-houthi-ships
2026-07-24 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-24) | https://www.theguardian.com/commentisfree/2026/jul/23/trump-saudi-nuclear-deal
2026-07-24 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-24) | https://www.hollywoodreporter.com/movies/movie-news/comic-con-2026-hall-h-preview-1236653276/
2026-07-24 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-24) | https://www.nytimes.com/2026/07/23/world/middleeast/saudi-arabia-nuclear.html
2026-07-24 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-24) | https://www.nytimes.com/2026/07/23/world/middleeast/trump-saudi-arabia-palestinian-state.html
2026-07-24 | reconstructed | UNESCO | (reconstructed from delivered edition 2026-07-24) | https://www.unesco.org/en/articles/world-heritage-committee-will-examine-new-nominations-and-state-conservation-inscribed-sites
2026-07-24 | reconstructed | Variety | (reconstructed from delivered edition 2026-07-24) | https://variety.com/2026/film/news/vijay-jana-nayagan-release-date-2-1236811540/
2026-07-25 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-25) | https://arkeonews.net/4500-year-old-mega-dams-near-egypts-red-pyramid-may-reveal-an-ancient-engineering-breakthrough/
2026-07-25 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-25) | https://arkeonews.net/byzantine-shipwreck-off-croatia-yields-record-gold-treasure-and-an-emperors-ring/
2026-07-25 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-25) | https://arkeonews.net/turkic-period-tomb-in-mongolia-yields-1400-year-old-peach-wood-bow-and-runic-inscribed-horse-head-fiddle/
2026-07-25 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-25) | https://arkeonews.net/two-premature-infants-possibly-twins-found-buried-in-an-abandoned-roman-latrine-at-ephesus/
2026-07-25 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-25) | https://www.bloomberg.com/news/newsletters/2026-07-24/oil-tankers-run-the-houthi-gauntlet-to-keep-saudi-exports-flowing
2026-07-25 | reconstructed | RTÉ | (reconstructed from delivered edition 2026-07-25) | https://www.rte.ie/news/2026/0725/1585036-houthis-strikes/
2026-07-25 | reconstructed | The A.V. Club | (reconstructed from delivered edition 2026-07-25) | https://www.avclub.com/weird-al-yankovic-riyadh-comedy-festival
2026-07-25 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-25) | https://www.theartnewspaper.com/2026/07/24/buffalo-akg-art-museum-two-director-roles-promotions
2026-07-25 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-25) | https://www.theartnewspaper.com/2026/07/24/jen-catron-paul-outlaw-times-square-hot-dog-returns
2026-07-25 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-25) | https://www.theartnewspaper.com/2026/07/24/swedish-viking-centre-that-loaned-ship-for-the-odyssey-alleges-that-it-has-not-been-paid-for-damages
2026-07-25 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-25) | https://www.theartnewspaper.com/2026/07/24/unesco-adds-ancient-greek-city-tauric-chersonese-in-crimea-to-world-heritage-in-danger-list
2026-07-25 | reconstructed | The National | (reconstructed from delivered edition 2026-07-25) | https://www.thenationalnews.com/news/2026/07/24/houthi-official-says-saudi-strike-targets-hodeidah-port-after-attack-on-saudi-vessel/
2026-07-26 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-26) | https://arkeonews.net/5000-year-old-bronze-age-temple-with-altars-and-sacred-hearths-discovered-in-eastern-turkiye/
2026-07-26 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-26) | https://arkeonews.net/roman-gold-barracks-and-surgical-tools-unearthed-at-vindonissas-first-military-camp-in-switzerland/
2026-07-26 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-26) | https://www.bloomberg.com/news/articles/2026-07-25/houthi-claim-missile-strikes-on-southern-saudi-arabia
2026-07-26 | reconstructed | CNBC | (reconstructed from delivered edition 2026-07-26) | https://www.cnbc.com/2026/07/25/saudi-military-strikes-iran-backed-houthi-targets-yemen.html
2026-07-26 | reconstructed | Deadline | (reconstructed from delivered edition 2026-07-26) | https://deadline.com/2026/07/ryan-gosling-ghost-rider-marvel-comic-con-1237003726/
2026-07-26 | reconstructed | Fox News | (reconstructed from delivered edition 2026-07-26) | https://www.foxnews.com/media/weird-al-yankovic-says-he-walked-away-from-seven-figure-comedy-festival-offer-saudi-arabia
2026-07-26 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-26) | https://www.heritagedaily.com/2026/07/heatwave-reveals-lost-welsh-landscapes/158718
2026-07-26 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-07-26) | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-26 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-26) | https://www.hollywoodreporter.com/movies/movie-news/black-panther-3-marvel-ryan-coogler-comic-con-1236656570/
2026-07-26 | reconstructed | The Stage | (reconstructed from delivered edition 2026-07-26) | https://www.thestage.co.uk/news/rsc-cancels-game-of-thrones-play-preview-performances
2026-07-26 | reconstructed | WWD | (reconstructed from delivered edition 2026-07-26) | https://wwd.com/pop-culture/celebrity-news/michelle-yeoh-hunter-schafer-comic-con-outfits-1239081924/
2026-07-27 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-07-27) | https://www.aljazeera.com/news/2026/7/26/new-front-in-us-iran-war-escalates-as-houthis-fire-at-saudi-oil-facilities
2026-07-27 | reconstructed | Associated Press | (reconstructed from delivered edition 2026-07-27) | https://apnews.com/article/unesco-mount-olympus-japan-ancient-capitals-1d3fabaa482d9384b1cb0b5c917ce5d5
2026-07-27 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-27) | https://www.bloomberg.com/news/articles/2026-07-25/us-pauses-nightly-strikes-on-iran-as-houthis-clash-with-saudis
2026-07-27 | reconstructed | CNN | (reconstructed from delivered edition 2026-07-27) | https://www.cnn.com/2026/07/26/world/video/fungi-leather-farm-indonesia-transformers-hkn-spc
2026-07-27 | reconstructed | Fashionista | (reconstructed from delivered edition 2026-07-27) | https://fashionista.com/2026/07/paris-fashion-week-september-2026-schedule
2026-07-27 | reconstructed | Newsweek | (reconstructed from delivered edition 2026-07-27) | https://www.newsweek.com/antoni-gaudi-118-year-old-lost-nyc-skyscraper-design-interiors-unveiled-12240546
2026-07-27 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-27) | https://www.theartnewspaper.com/2026/07/27/peru-earthquake-damages-16th-century-church-iglesia-apostol-santiago
2026-07-27 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-27) | https://www.theguardian.com/commentisfree/2026/jul/26/the-guardian-view-on-a-us-saudi-nuclear-agreement-an-offer-that-further-erodes-international-safeguards
2026-07-27 | reconstructed | WWD | (reconstructed from delivered edition 2026-07-27) | https://wwd.com/business-news/retail/saudi-arabia-fashion-food-design-selfridges-corner-shop-1239081869/
2026-07-28 | reconstructed | AGBI | (reconstructed from delivered edition 2026-07-28) | https://www.agbi.com/analysis/oil-and-gas/2026/07/yanbu-attacks-expose-saudi-oil-export-vulnerability/
2026-07-28 | reconstructed | ARTnews | (reconstructed from delivered edition 2026-07-28) | https://www.artnews.com/art-news/news/betye-saar-dead-1234793560/
2026-07-28 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-07-28) | https://www.al-monitor.com/originals/2026/07/red-sea-shipping-slows-after-houthi-attack-saudi-arabia-data-shows
2026-07-28 | reconstructed | ArchDaily | (reconstructed from delivered edition 2026-07-28) | https://www.archdaily.com/1040412/from-data-to-digital-twins-japans-plateau-project-offers-open-access-models-of-more-than-250-cities
2026-07-28 | reconstructed | Archaeology Magazine | (reconstructed from delivered edition 2026-07-28) | https://archaeology.org/news/2026/07/27/funerary-complex-unearthed-in-northern-egypt/
2026-07-28 | reconstructed | Archaeology Magazine | (reconstructed from delivered edition 2026-07-28) | https://archaeology.org/news/2026/07/27/roman-battle-camp-found-in-spain/
2026-07-28 | reconstructed | Archaeology News | (reconstructed from delivered edition 2026-07-28) | https://archaeologymag.com/2026/07/first-roman-camp-at-vindonissa-revealed/
2026-07-28 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-28) | https://arkeonews.net/unique-medieval-house-on-wheels-from-the-kimak-khaganate-unearthed-in-kazakhstan/
2026-07-28 | reconstructed | Blooloop | (reconstructed from delivered edition 2026-07-28) | https://blooloop.com/news/franklin-institute-unveils-star-wars
2026-07-28 | reconstructed | CNBC | (reconstructed from delivered edition 2026-07-28) | https://www.cnbc.com/2026/07/28/us-iran-war-trump-hormuz.html
2026-07-28 | reconstructed | Dezeen | (reconstructed from delivered edition 2026-07-28) | https://www.dezeen.com/2026/07/27/rshps-one-shanghai-tower/
2026-07-28 | reconstructed | Foreign Policy | (reconstructed from delivered edition 2026-07-28) | https://foreignpolicy.com/2026/07/27/trump-nuclear-saudi-arabia-deal-iran-israel/
2026-07-28 | reconstructed | Hyperallergic | (reconstructed from delivered edition 2026-07-28) | https://hyperallergic.com/betye-saar-who-opened-portals-between-worlds-dies-at-99/
2026-07-28 | reconstructed | Press TV | (reconstructed from delivered edition 2026-07-28) | https://www.presstv.co.uk/Detail/2026/07/27/773191/Saudi-oil-loading-volumes-fall-40--
2026-07-28 | reconstructed | Tech Times | (reconstructed from delivered edition 2026-07-28) | https://www.techtimes.com/articles/321672/20260727/d-day-beaches-okefenokee-swamp-mount-olympus-join-unesco-world-heritage-list.htm
2026-07-28 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-28) | https://www.theartnewspaper.com/2026/07/27/biennale-sydney-curator-2028-low-kee-hong
2026-07-28 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-28) | https://www.theartnewspaper.com/2026/07/27/music-fashion-film-photography-charli-xcx-image-acquired-by-londons-national-portrait-gallery
2026-07-28 | reconstructed | The Bookseller | (reconstructed from delivered edition 2026-07-28) | https://www.thebookseller.com/rights/atlantic-books-acquires-story-of-keir-starmers-unfulfilled-premiership
2026-07-28 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-28) | https://www.theguardian.com/world/2026/jul/28/asia-energy-oil-crisis-red-sea-blockade-houthis
2026-07-28 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-28) | https://www.nytimes.com/2026/07/27/world/middleeast/houthis-saudi-arabia-iran-war.html
2026-07-28 | reconstructed | The Week | (reconstructed from delivered edition 2026-07-28) | https://www.theweek.in/news/middle-east/2026/07/27/saudi-arabia-oil-refinery-attack-abqaiq-fire-impact.html
2026-07-28 | reconstructed | WWD | (reconstructed from delivered edition 2026-07-28) | https://wwd.com/business-news/mergers-acquisitions/fashion-ma-deals-2026-capstone-report-1239083357/
2026-07-29 | reconstructed | ARTnews | (reconstructed from delivered edition 2026-07-29) | https://www.artnews.com/art-news/news/phildelphia-museum-of-art-ran-a-10-m-deficit-1234793631
2026-07-29 | reconstructed | Artsy | (reconstructed from delivered edition 2026-07-29) | https://www.artsy.net/article/artsy-editorial-moma-host-chess-matches-honor-marcel-duchamp
2026-07-29 | reconstructed | Associated Press | (reconstructed from delivered edition 2026-07-29) | https://www.clickorlando.com/news/world/2026/07/28/saudi-arabia-says-it-shot-down-more-drones-as-houthis-claim-to-have-turned-back-tanker/
2026-07-29 | reconstructed | Blooloop | (reconstructed from delivered edition 2026-07-29) | https://blooloop.com/news/shenzhen-natural-history-museum-opens
2026-07-29 | reconstructed | Deutsche Welle | (reconstructed from delivered edition 2026-07-29) | https://www.dw.com/en/will-pakistan-intervene-amid-houthi-attacks-on-saudi-ships/a-78144890
2026-07-29 | reconstructed | HeritageDaily | (reconstructed from delivered edition 2026-07-29) | https://www.heritagedaily.com/2026/07/archaeologists-map-buried-sacred-precinct-of-the-aztec-capital-tenochtitlan/158744
2026-07-29 | reconstructed | Human Rights Watch | (reconstructed from delivered edition 2026-07-29) | https://www.hrw.org/news/2026/07/28/saudi-arabia-new-executions-of-ethiopian-migrants
2026-07-29 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-07-29) | https://www.middleeasteye.net/live-blog/live-blog-update/iraqi-paramilitary-force-condemns-saudi-us-attacks-headquarters
2026-07-29 | reconstructed | Publishers Weekly | (reconstructed from delivered edition 2026-07-29) | https://www.publishersweekly.com/pw/by-topic/industry-news/awards-and-prizes/article/100927-2026-booker-prize-longlist-announced.html
2026-07-29 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-29) | https://www.theartnewspaper.com/2026/07/28/culture-minister-catherine-pegard-reveals-national-security-plan-following-another-major-museum-theft-in-france
2026-07-29 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-29) | https://www.theartnewspaper.com/2026/07/28/guggenheim-abu-dhabi-announces-opening-date
2026-07-29 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-29) | https://www.theguardian.com/world/2026/jul/29/iran-missile-attack-us-base-forces
2026-07-29 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-29) | https://www.hollywoodreporter.com/business/business-news/penske-media-sued-hollywood-foreign-press-golden-globes-1236658413
2026-07-29 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-29) | https://www.hollywoodreporter.com/movies/movie-news/marion-cotillard-mike-leigh-pablo-larrain-in-san-sebastian-1236658023
2026-07-29 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-29) | https://www.nytimes.com/2026/07/28/world/middleeast/houthis-strike-saudi-tanker.html
2026-07-30 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-07-30) | https://www.aljazeera.com/news/2026/7/29/iraq-calls-saudi-us-attacks-flagrant-violation-of-sovereignty
2026-07-30 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-30) | https://arkeonews.net/iberian-warrior-family-buried-2200-years-ago-with-falcatas-and-a-tanit-burner-discovered-in-alicante/
2026-07-30 | reconstructed | CNBC | (reconstructed from delivered edition 2026-07-30) | https://www.cnbc.com/2026/07/29/oil-prices-today-brent-wti-iran-us-hormuz.html
2026-07-30 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-07-30) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-seeks-international-coalition-protect-red-sea-shipping
2026-07-30 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-30) | https://www.theartnewspaper.com/2026/07/29/betye-saar-obituary-legendary-los-angeles-assemblage-artist
2026-07-30 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-30) | https://www.theartnewspaper.com/2026/07/29/english-heritage-debuts-daily-prize-draw-for-private-time-at-stonehenge-this-august
2026-07-30 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-30) | https://www.theartnewspaper.com/2026/07/29/municipal-arts-funding-covid-rebound-dataarts-southern-methodist-university-study
2026-07-30 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-30) | https://www.theartnewspaper.com/2026/07/29/sites-in-iran-lebanon-and-palestine-among-25-new-additions-to-unescos-world-heritage-list
2026-07-30 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-30) | https://www.theguardian.com/world/2026/jul/29/us-saudi-strikes-in-iraq-have-pushed-the-region-into-uncharted-territory-analysts-warn
2026-07-30 | reconstructed | The Irish Times | (reconstructed from delivered edition 2026-07-30) | https://www.irishtimes.com/culture/music/2026/07/29/glen-hansard-dies-in-dublin-motorbike-crash/
2026-07-30 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-30) | https://www.nytimes.com/2026/07/29/world/middleeast/saudi-arabia-us-iran-war.html
2026-07-31 | reconstructed | AGBI | (reconstructed from delivered edition 2026-07-31) | https://www.agbi.com/analysis/economy/2026/07/saudi-economy-shrinks-first-time-in-three-years-as-oil-output-drops/
2026-07-31 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-07-31) | https://www.al-monitor.com/newsletter/2026-07-30/red-seas-shared-history-comes-alive-jeddah
2026-07-31 | reconstructed | Antiwar.com | (reconstructed from delivered edition 2026-07-31) | https://news.antiwar.com/2026/07/30/al-houthi-says-there-are-indications-saudi-arabia-is-planning-major-escalation-in-yemen/
2026-07-31 | reconstructed | Archaeology Magazine | (reconstructed from delivered edition 2026-07-31) | https://archaeology.org/news/2026/07/30/possible-marks-of-cannibalism-detected-on-adult-homo-antecessor-fossils/
2026-07-31 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-31) | https://arkeonews.net/archaeologists-unearth-two-miniature-mammoth-ivory-birds-carved-40000-years-ago/
2026-07-31 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-07-31) | https://arkeonews.net/lidar-reveals-up-to-30000-earthworks-built-by-a-lost-amazonian-civilization/
2026-07-31 | reconstructed | Artnet News | (reconstructed from delivered edition 2026-07-31) | https://news.artnet.com/artnet-bulletin/new-tariffs-july-30-2790904
2026-07-31 | reconstructed | BBC | (reconstructed from delivered edition 2026-07-31) | https://www.bbc.co.uk/news/articles/ckg4jxxn4ggo
2026-07-31 | reconstructed | Bloomberg | (reconstructed from delivered edition 2026-07-31) | https://www.bloomberg.com/news/articles/2026-07-30/saudi-budget-deficit-narrows-three-quarters-on-wartime-oil-spike
2026-07-31 | reconstructed | Deadline | (reconstructed from delivered edition 2026-07-31) | https://deadline.com/2026/07/wicker-trailer-olivia-colman-alexander-skarsgard-1237013463/
2026-07-31 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-31) | https://www.theartnewspaper.com/2026/07/30/amazon-style-conditions-va-east-storehouse-officers-overwhelmingly-vote-to-strike-as-other-museum-workers-also-consider-industrial-action
2026-07-31 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-31) | https://www.theartnewspaper.com/2026/07/30/comment-obama-presidential-center-art-architecture-gothic-cathedral
2026-07-31 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-07-31) | https://www.theartnewspaper.com/2026/07/30/life-and-treasure-from-ancient-egypts-golden-city-revealed-in-san-francisco-show
2026-07-31 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-07-31) | https://www.theguardian.com/world/2026/jul/30/saudi-forces-planning-major-offensive-against-houthis-central-yemen
2026-07-31 | reconstructed | The Hollywood Reporter | (reconstructed from delivered edition 2026-07-31) | https://www.hollywoodreporter.com/tv/tv-news/clueless-sequel-series-paramount-1236659500/
2026-07-31 | reconstructed | The New York Times | (reconstructed from delivered edition 2026-07-31) | https://www.nytimes.com/2026/07/30/world/middleeast/saudi-arabia-red-sea-houthis.html
2026-08-01 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-08-01) | https://www.al-monitor.com/originals/2026/07/italy-minister-rejects-opposition-criticism-saudi-troop-deployment
2026-08-01 | reconstructed | Al-Monitor | (reconstructed from delivered edition 2026-08-01) | https://www.al-monitor.com/originals/2026/07/oil-price-rises-after-iran-says-it-stops-ships-hormuz
2026-08-01 | reconstructed | Artnet News | (reconstructed from delivered edition 2026-08-01) | https://news.artnet.com/market/industry-intel-july-31-2791743
2026-08-01 | reconstructed | Billboard | (reconstructed from delivered edition 2026-08-01) | https://www.billboard.com/music/pop/ariana-grande-petal-album-listen-1236306614/
2026-08-01 | reconstructed | Billboard | (reconstructed from delivered edition 2026-08-01) | https://www.billboard.com/pro/sonys-global-music-biz-revenue-tops-3-53-billion-2026-q2/
2026-08-01 | reconstructed | Billboard | (reconstructed from delivered edition 2026-08-01) | https://www.billboard.com/pro/suno-liable-gema-german-copyright-lawsuit/
2026-08-01 | reconstructed | Deadline | (reconstructed from delivered edition 2026-08-01) | https://deadline.com/2026/07/box-office-spider-man-brand-new-day-1237014268/
2026-08-01 | reconstructed | Deutsche Welle | (reconstructed from delivered edition 2026-08-01) | https://www.dw.com/en/military-flare-up-between-houthis-and-saudi-arabia-challenges-relative-calm-in-yemen/a-78186262
2026-08-01 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-08-01) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-terms-trumps-gaza-demilitarisation-deal-historic
2026-08-01 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-08-01) | https://www.middleeasteye.net/live-blog/live-blog-update/yemeni-forces-say-eight-saudi-tankers-forced-reroute
2026-08-01 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-01) | https://www.theartnewspaper.com/2026/07/31/japans-400-year-old-kumamoto-castle-damaged-by-71-magnitude-earthquake
2026-08-01 | reconstructed | WWD | (reconstructed from delivered edition 2026-08-01) | https://wwd.com/fashion-news/fashion-scoops/costume-institute-met-next-exhibition-john-galliano-1239089295/
2026-08-02 | reconstructed | AGBI | (reconstructed from delivered edition 2026-08-02) | https://www.agbi.com/analysis/oil-and-gas/2026/08/great-gulf-pipeline-race-which-routes-will-actually-be-built/
2026-08-02 | reconstructed | Artnet News | (reconstructed from delivered edition 2026-08-02) | https://news.artnet.com/art-world/ai-provenance-assistant-looted-art-tool-2792609
2026-08-02 | reconstructed | Axios | (reconstructed from delivered edition 2026-08-02) | https://www.axios.com/2026/08/01/saudi-crown-prince-trump-iran-attacks
2026-08-02 | reconstructed | Deadline | (reconstructed from delivered edition 2026-08-02) | https://deadline.com/2026/08/vincent-pastore-dead-the-sopranos-star-big-pussy-1237015282/
2026-08-02 | reconstructed | Fortune | (reconstructed from delivered edition 2026-08-02) | https://fortune.com/2026/08/01/trump-iran-strikes-mideast-allies-emerging-strait-of-hormuz/
2026-08-02 | reconstructed | Nikkei Asia | (reconstructed from delivered edition 2026-08-02) | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/trump-says-mideast-allies-have-reached-outlines-of-deal-to-end-iran-war
2026-08-02 | reconstructed | Variety | (reconstructed from delivered edition 2026-08-02) | https://variety.com/2026/film/news/box-office-spider-man-brand-new-day-opening-day-record-1236825606/
2026-08-03 | reconstructed | Al Jazeera | (reconstructed from delivered edition 2026-08-03) | https://www.aljazeera.com/news/2026/8/2/no-breakthrough-on-strait-of-hormuz-as-trump-halts-attack-on-iran
2026-08-03 | reconstructed | CNBC | (reconstructed from delivered edition 2026-08-03) | https://www.cnbc.com/2026/08/02/spider-man-brand-new-day-box-office-355-million-domestic-opening.html
2026-08-03 | reconstructed | Chicago Sun-Times | (reconstructed from delivered edition 2026-08-03) | https://chicago.suntimes.com/lollapalooza/2026/08/02/review-tate-mcrae-closes-out-lollapalooza-with-surprisingly-subdued-set
2026-08-03 | reconstructed | Middle East Eye | (reconstructed from delivered edition 2026-08-03) | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-iranian-foreign-ministers-discuss-efforts-reduce-regional-tensions
2026-08-03 | reconstructed | Press TV | (reconstructed from delivered edition 2026-08-03) | https://www.presstv.co.uk/Detail/2026/08/02/773592/Persian-Gulf-states-sovereignty-Iran-war-US-Israel-aggression-
2026-08-03 | reconstructed | The Philadelphia Inquirer | (reconstructed from delivered edition 2026-08-03) | https://www.inquirer.com/news/nation-world/trump-iron-pause-strikes-negotiations-strait-hormuz-mohammed-bin-salman-20260802.html
2026-08-04 | reconstructed | AGBI | (reconstructed from delivered edition 2026-08-04) | https://www.agbi.com/shipping/2026/08/houthi-threat-fails-to-deter-saudi-crude-from-red-sea-passage/
2026-08-04 | reconstructed | ARTnews | (reconstructed from delivered edition 2026-08-04) | https://www.artnews.com/art-news/news/gagosian-london-basel-gallery-closures-1234794210/
2026-08-04 | reconstructed | Archaeology | (reconstructed from delivered edition 2026-08-04) | https://archaeology.org/news/2026/08/03/funerary-complex-excavated-near-egypts-mediterranean-coast/
2026-08-04 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-08-04) | https://arkeonews.net/3000-year-old-bronze-hoard-unearthed-in-czech-wetland/
2026-08-04 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-08-04) | https://arkeonews.net/well-preserved-2-2-meter-monumental-statue-with-long-hair-emerges-after-2500-years-in-ancient-sardis/
2026-08-04 | reconstructed | Deadline | (reconstructed from delivered edition 2026-08-04) | https://deadline.com/2026/08/universal-2026-global-box-office-odyssey-billion-1237015503/
2026-08-04 | reconstructed | Foreign Policy | (reconstructed from delivered edition 2026-08-04) | https://foreignpolicy.com/2026/08/03/saudi-arabia-emirates-iran-israel-uae-missile-defense-sanctions-hormuz/
2026-08-04 | reconstructed | MEED | (reconstructed from delivered edition 2026-08-04) | https://www.meed.com/saudi-economy-swings-to-48-contraction
2026-08-04 | reconstructed | SANA | (reconstructed from delivered edition 2026-08-04) | https://sana.sy/en/culture-and-arts/2334040/
2026-08-04 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-04) | https://www.theartnewspaper.com/2026/08/03/royal-museums-greenwich-workers-vote-to-strike-over-pay-and-working-conditions
2026-08-04 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-04) | https://www.theartnewspaper.com/2026/08/03/unesco-urged-to-investigate-after-israeli-forces-trigger-explosion-near-lebanons-world-heritage-listed-beaufort-castle
2026-08-04 | reconstructed | WWD | (reconstructed from delivered edition 2026-08-04) | https://wwd.com/fashion-news/fashion-features/wme-sells-new-york-fashion-week-nyfw-signet-fashion-1239088648/
2026-08-04 | reconstructed | bizpreneurme.com | (reconstructed from delivered edition 2026-08-04) | https://www.bizpreneurme.com/the-music-authority-announces-a-strategic-partnership-with-jazz-in-jeddah/
2026-08-04 | reconstructed | cnbcindonesia.com | (reconstructed from delivered edition 2026-08-04) | https://www.cnbcindonesia.com/lifestyle/20260803152213-33-756135/ahi-temukan-harta-karun-di-dekat-mekkah-diduga-milik-jamaah-haji
2026-08-04 | reconstructed | harpersbazaararabia.com | (reconstructed from delivered edition 2026-08-04) | https://www.harpersbazaararabia.com/hbanews/golden-threads-brings-traditional-saudi-dress-to-londons-va-museum
2026-08-04 | reconstructed | mirror.co.uk | (reconstructed from delivered edition 2026-08-04) | https://www.mirror.co.uk/sport/football/news/gianni-infantino-fifa-fa-embarrassment-37509485
2026-08-04 | reconstructed | nypost.com | (reconstructed from delivered edition 2026-08-04) | https://nypost.com/2026/08/03/opinion/its-time-for-the-saudis-to-put-up-or-shut-up-on-iran/
2026-08-04 | reconstructed | nypost.com | (reconstructed from delivered edition 2026-08-04) | https://nypost.com/2026/08/03/opinion/saudis-gravitate-toward-middle-east-basket-cases-when-it-should-join-us-fight-against-iran/
2026-08-04 | reconstructed | pakistanpoint.com | (reconstructed from delivered edition 2026-08-04) | https://www.pakistanpoint.com/ar/news/saudi-arabia/story-2231036.html
2026-08-04 | reconstructed | theguardian.com | (reconstructed from delivered edition 2026-08-04) | https://www.theguardian.com/travel/2026/aug/04/alice-morrison-hiking-wild-camping-highlands-scotland-affric-kintail-way
2026-08-04 | reconstructed | wwd.com | (reconstructed from delivered edition 2026-08-04) | https://wwd.com/fashion-news/fashion-scoops/london-meets-riyadh-saudi-showcase-selfridges-corner-shop-1239091075/
2026-08-05 | reconstructed | 365retail.co.uk | (reconstructed from delivered edition 2026-08-05) | https://365retail.co.uk/selfridges-hosts-25-saudi-brands-at-the-corner-shop/
2026-08-05 | reconstructed | AGBI | (reconstructed from delivered edition 2026-08-05) | https://www.agbi.com/analysis/oil-and-gas/2026/08/aramco-profits-surge-in-face-of-mounting-risks-to-exports/
2026-08-05 | reconstructed | AGBI | (reconstructed from delivered edition 2026-08-05) | https://www.agbi.com/economy/2026/08/saudi-arabia-sustains-non-oil-growth-and-kuwait-rebounds/
2026-08-05 | reconstructed | Archaeology Magazine | (reconstructed from delivered edition 2026-08-05) | https://archaeology.org/news/2026/08/04/roman-villa-featured-oldest-known-library-in-iberia/
2026-08-05 | reconstructed | Arkeonews | (reconstructed from delivered edition 2026-08-05) | https://arkeonews.net/silenced-for-6000-years-how-a-tiny-stone-seal-resurrected-irans-oldest-harp/
2026-08-05 | reconstructed | Blooloop | (reconstructed from delivered edition 2026-08-05) | https://blooloop.com/203m-donation-brown-museum/
2026-08-05 | reconstructed | Dezeen | (reconstructed from delivered edition 2026-08-05) | https://www.dezeen.com/2026/08/04/sentry-bridge-watkins-glen-gorge-snohetta-sbp/
2026-08-05 | reconstructed | Gulf Insider | (reconstructed from delivered edition 2026-08-05) | https://www.gulf-insider.com/saudi-arabia-adds-1173-archaeological-sites-to-national-register/
2026-08-05 | reconstructed | Semafor | (reconstructed from delivered edition 2026-08-05) | https://www.semafor.com/article/08/04/2026/aramco-profit-rises-33-on-higher-oil-prices
2026-08-05 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-05) | https://www.theartnewspaper.com/2026/08/04/australian-museum-repatriates-rapa-nui-remains-easter-island
2026-08-05 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-05) | https://www.theartnewspaper.com/2026/08/04/fra-angelicos-earliest-surviving-altarpiece-returns-to-fiesole-after-restoration-reveals-hidden-throne
2026-08-05 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-05) | https://www.theartnewspaper.com/2026/08/04/london-mayor-sadiq-khan-calls-for-national-museums-to-remain-free-to-enter
2026-08-05 | reconstructed | The Art Newspaper | (reconstructed from delivered edition 2026-08-05) | https://www.theartnewspaper.com/2026/08/04/reconstruction-of-legendary-sutton-hoo-ship-takes-shape
2026-08-05 | reconstructed | The Guardian | (reconstructed from delivered edition 2026-08-05) | https://www.theguardian.com/technology/2026/aug/04/x-twitter-blocks-dissident-accounts-saudi-arabia
2026-08-05 | reconstructed | Time Out | (reconstructed from delivered edition 2026-08-05) | https://www.timeout.com/singapore/news/six-new-one-michelin-star-restaurants-to-watch-the-michelin-guide-singapore-2026-080426
2026-08-05 | reconstructed | aeworld.com | (reconstructed from delivered edition 2026-08-05) | https://aeworld.com/lifestyle/saudi-arabia-reveals-its-national-day-2026-identity/
2026-08-05 | reconstructed | bbc.com | (reconstructed from delivered edition 2026-08-05) | https://www.bbc.com/news/articles/cjejyl34345o
2026-08-05 | reconstructed | freepressjournal.in | (reconstructed from delivered edition 2026-08-05) | https://www.freepressjournal.in/amp/bhopal/bhopal-brics-summit-to-discuss-digital-heritage-platform-unesco-nominations
2026-08-05 | reconstructed | theguardian.com | (reconstructed from delivered edition 2026-08-05) | https://www.theguardian.com/business/ng-interactive/2026/aug/04/revealed-major-oil-firms-make-93bn-profits-amid-war-and-climate-crisis
2026-08-05 | reconstructed | whatsonsaudiarabia.com | (reconstructed from delivered edition 2026-08-05) | https://whatsonsaudiarabia.com/2026/08/worlds-largest-date-festival-in-saudi-arabia/

<!-- Edition 2026-08-06 -->
2026-08-06 | Saudi Arabia/Regional | The New York Times | Houthis Threaten to Expand Red Sea Attacks, and Claim Strikes on Saudi Tankers | https://www.nytimes.com/2026/08/05/world/middleeast/houthis-claim-attack-saudi-arabia-tanker.html
2026-08-06 | Saudi Arabia/Regional | Bloomberg | Trump Fuels Hopes of Hormuz Opening With Hints Deal Is Close | https://www.bloomberg.com/news/articles/2026-08-05/trump-fuels-hopes-of-hormuz-reopening-with-hints-a-deal-is-near
2026-08-06 | Saudi Arabia/Regional | Bloomberg | Saudi Arabia Can End Houthi Blockade in the Red Sea | https://www.bloomberg.com/opinion/articles/2026-08-05/saudi-arabia-can-end-houthi-blockade-in-the-red-sea
2026-08-06 | Saudi Arabia/Regional | Blooloop | Guggenheim Abu Dhabi appoints Valerie Hillings as inaugural director | https://blooloop.com/news/guggenheim-abu-dhabi-new-director
2026-08-06 | Negative Articles | Press TV | Yemen will expand attacks if Saudi-led blockade continues: Analyst | https://www.presstv.co.uk/Detail/2026/08/05/773774/Yemen-attack-Saudi-Arabia-Saudi-blockade-Red-Sea-Bab-al-Mandeb-
2026-08-06 | Global | Archaeology Magazine | Megalithic 'Giant's Tomb' Uncovered in Sardinia | https://archaeology.org/news/2026/08/05/megalithic-giants-tomb-uncovered-in-sardinia/
2026-08-06 | Global | Arkeonews | Rare Runestone Found Beneath a Medieval Chapel in the Faroe Islands | https://arkeonews.net/rare-runestone-found-beneath-a-medieval-chapel-in-the-faroe-islands/
2026-08-06 | Global | Arkeonews | Archaeologists Discover a 3,200-Year-Old Ceremonial Kitchen in Azerbaijan, Unique in the Caucasus | https://arkeonews.net/archaeologists-discover-a-3200-year-old-ceremonial-kitchen-in-azerbaijan-unique-in-the-caucasus/
2026-08-06 | Global | Arkeonews | Child Burial Discovered Beneath the Temple of Zeus in Crimea - Was It a Sacrifice? | https://arkeonews.net/child-burial-discovered-beneath-the-temple-of-zeus-in-crimea-was-it-a-sacrifice/
2026-08-06 | Global | ARTnews | Art Week NYC Names 76 Participating Galleries for Inaugural Event in November | https://www.artnews.com/art-news/news/art-week-nyc-names-2026-participating-galleries-list-1234794276/
2026-08-06 | Global | Hyperallergic | Art Orgs That Received More COVID-Era Funding Outperforming Others, Study Finds | https://hyperallergic.com/art-orgs-that-received-more-covid-era-funding-outperforming-others-study-finds/
2026-08-06 | Global | Hyperallergic | Advocates Rally to Stop Sale of Glasgow's Centre for Contemporary Arts | https://hyperallergic.com/advocates-rally-to-stop-sale-of-glasgows-centre-for-contemporary-arts/
2026-08-06 | Global | Dezeen | MAD scatters boulder-like galleries across green-roofed museum in Shenzhen | https://www.dezeen.com/2026/08/05/shenzhen-bay-culture-square-mad/
2026-08-06 | Global | The Stage | Soho Underbelly Boulevard owner submits plans for immersive space in West End | https://www.thestage.co.uk/news/soho-underbelly-boulevard-owner-submits-plans-for-immersive-space-in-west-end
