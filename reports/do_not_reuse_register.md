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

<!-- 2026-08-22: entries for editions 18-21 Aug 2026 below were reconstructed
     from the delivered .docx editions in the Dropbox "05_Claude Test" folder,
     because prior automated runs delivered to Dropbox but did not commit their
     do-not-reuse entries back to this repo. Headlines are transcribed
     best-effort (truncated); dates and URLs are exact and load-bearing for
     reuse-blocking. -->

2026-08-21 | Saudi Arabia/Regional | Middle East Report | A group exhibition at Beirut's Dalloul Art Foundation, "Women at Work", sets works by lead | https://merip.org/2026/08/women-at-work-challenging-the-art-craft-divide/
2026-08-21 | Saudi Arabia/Regional | WWD | Trade title WWD reports that Saudi Arabia's beauty market is expanding rapidly, driven by | https://wwd.com/beauty-industry-news/beauty-features/saudi-arabia-beauty-market-booms-young-savvy-consumers-1239081751/
2026-08-21 | Negative Articles | Middle East Eye | The US Treasury Secretary pledged what he called the toughest sanctions yet on Iran amid a | https://www.middleeasteye.net/news/us-vows-collapse-iran-new-sanctions-energy-prices-spike
2026-08-21 | Global | ArtReview | Ten Taiwanese artists and curators, backed by Taiwan's culture ministry, have accused the | https://artreview.com/gwangju-biennale-accused-of-censoring-pavilion-title/
2026-08-21 | Global | The Art Newspaper | A new documentary, "Handmade Future", follows nine artisans across six countries — from ma | https://www.theartnewspaper.com/2026/08/20/handmade-future-documentary-craft-traditions-artisans-underpressure
2026-08-20 | Saudi Arabia/Regional | The National | A peer-reviewed study in PLOS One, led by the University of Vienna with MIT and Harvard re | https://www.thenationalnews.com/news/europe/2026/08/19/how-bronze-age-arabian-traders-invented-brand-value/
2026-08-20 | Saudi Arabia/Regional | Interior Design | The US design title Interior Design has profiled Riyadh's newly opened Black Gold Museum, | https://interiordesign.net/projects/black-gold-museum-in-riyadh/
2026-08-20 | Negative Articles | AGBI | Analysis from AGBI reports that the Kingdom's renewable-energy programme is being strained | https://www.agbi.com/analysis/renewable-energy/2026/08/saudi-renewables-push-strained-by-war-and-tighter-funding/
2026-08-20 | Negative Articles | AGBI | AGBI also reports that Red Sea Global has opened the Rosewood Amaala, its third Amaala res | https://www.agbi.com/tourism/2026/08/saudi-arabia-opens-new-red-sea-resort-despite-tourism-downturn/
2026-08-20 | Global | The Art Newspaper | The National Gallery of Art in Washington has announced around 190 acquisitions made since | https://www.theartnewspaper.com/2026/08/19/national-gallery-art-us-acquisitions-wifredo-lam-marie-bracquemond
2026-08-20 | Global | Blooloop | London's Natural History Museum will reopen a second-floor gallery in the Waterhouse build | https://blooloop.com/news/natural-history-museum-hidden-gallery
2026-08-20 | Global | Hyperallergic | The Speed Art Museum in Louisville has returned 24 cultural items — including a Cheyenne c | https://hyperallergic.com/speed-art-museum-returns-24-native-artifacts-to-oklahoma-tribes/
2026-08-20 | Global | Arkeonews | Archaeologists have reported that a pair of elaborately worked silver ornaments excavated | https://arkeonews.net/rare-silver-earrings-from-khakassia-may-preserve-an-image-of-umay-the-ancient-turkic-goddess/
2026-08-20 | Global | Archaeology Magazine | Excavations at Tell Abu Saifi in northern Sinai have uncovered a mudbrick enclosure, templ | https://archaeology.org/news/2026/08/19/new-discoveries-link-sinai-site-with-lost-egyptian-city/
2026-08-20 | Global | ArchDaily | ArchDaily has published the newly completed Bruce Springsteen Center for American Music by | https://www.archdaily.com/1183556/bruce-springsteen-center-for-american-music-cookfox
2026-08-20 | Global | The Stage | The Stage has revealed the nominees for its 2026 Debut Awards, which recognise emerging pe | https://www.thestage.co.uk/news/the-stage-debut-awards-2026-ralph-fiennes-and-sadie-sink-among-nominees
2026-08-20 | Global | Publishers Weekly | Publishers Weekly reports that Ballantine Books has acquired North American rights to "Eme | https://www.publishersweekly.com/pw/newsbrief/index.html?record=5992
2026-08-20 | Global | The Hollywood Reporter | The Hollywood Reporter reports that Martin McDonagh's "Wild Horse Nine", starring Sam Rock | https://www.hollywoodreporter.com/movies/movie-news/wild-horse-nine-sam-rockwell-mill-valley-film-festival-1236676808/
2026-08-20 | Global | Music Business Worldwide | Music Business Worldwide reports that Universal Music Group has struck an exclusive, long- | https://www.musicbusinessworldwide.com/umg-strikes-global-deal-for-the-beatles-merch-licensing-and-e-commerce/
2026-08-19 | Saudi Arabia/Regional | CairoScene | Riyadh Art, the Royal Commission for Riyadh City's public-art programme, has unveiled 75 p | https://cairoscene.com/ArtsAndCulture/Riyadh-Art-Brings-75-Permanent-Public-Artworks-Across-the-City
2026-08-19 | Saudi Arabia/Regional | ArchDaily | ArchDaily has published an essay tracing how the environmental logic of the Bedouin tent, | https://www.archdaily.com/1183404/from-tent-to-terminal-bedouin-craft-in-contemporary-infrastructure
2026-08-19 | Global | Archaeology Magazine | Archaeologists have recovered a centuries-old runestone from the floor of a medieval praye | https://archaeology.org/news/2026/08/18/mysterious-runestone-found-embedded-in-floor-of-faroe-islands-chapel/
2026-08-19 | Global | Archaeology Magazine | Chinese researchers have identified brass residue on three of around 80 crucibles from a m | https://archaeology.org/news/2026/08/18/crucibles-contain-earliest-evidence-of-brass-production-in-east-asia/
2026-08-19 | Global | Archaeology Magazine | Proteomic analysis of two leg bones dredged from the Penghu Channel off Taiwan has confirm | https://archaeology.org/news/2026/08/18/denisovans-were-much-taller-than-previously-thought/
2026-08-19 | Global | Arkeonews | The 2026 excavation at the Lucone di Polpenazze pile-dwelling settlement near Lake Garda h | https://arkeonews.net/rare-4000-year-old-enigmatic-tablet-found-intact-at-lucone-bronze-age-village-in-italy/
2026-08-19 | Global | Arkeonews | Analysis of thousand-year-old lustreware bowls excavated at Deraheib in Sudan's eastern de | https://arkeonews.net/1000-year-old-luxury-bowls-in-the-sudanese-desert-hide-an-8-nanometer-secret/
2026-08-19 | Global | Forbes | Forbes reports that the line-up for the 83rd Venice Film Festival (2 to 12 September) is t | https://www.forbes.com/sites/dbloom/2026/08/18/venice-film-festival-lineup-comes-into-focus/
2026-08-18 | Saudi Arabia/Regional | Muslim Network TV | Riyadh Art, the public-art programme run by the Royal Commission for Riyadh City, is conti | https://www.muslimnetwork.tv/saudis-riyadh-expands-public-art-across-streets-and-transit-hubs/
2026-08-18 | Negative Articles | Middle East Eye | Yemen's Houthis claimed a ballistic-missile strike on a Saudi military landing ship and fo | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-they-targeted-saudi-military-ship-red-sea
2026-08-18 | Global | The Art Newspaper | Frieze Seoul has confirmed it will move to the Zaha Hadid-designed Dongdaemun Design Plaza | https://www.theartnewspaper.com/2026/08/17/frieze-seoul-to-move-to-new-venue-from-2027
2026-08-18 | Global | The Art Newspaper | The American painter Mary Heilmann, known for bringing warmth and a relaxed sensibility to | https://www.theartnewspaper.com/2026/08/17/mary-heilmann-fearless-colourist-singular-painter-obituary
2026-08-18 | Global | The Art Newspaper | Police in Brazil have recovered eight works by Henri Matisse, from his 1947 book Jazz, tha | https://www.theartnewspaper.com/2026/08/17/stolen-matisse-works-recovered-sao-paulo-brazil-heist
2026-08-18 | Global | The Art Newspaper | Four panels by the Sicilian Renaissance master Antonello da Messina were stolen from the M | https://www.theartnewspaper.com/2026/08/17/four-works-by-sicilian-renaissance-master-stolen-from-messina-museum
2026-08-18 | Global | Arkeonews | Archaeologists in the Siberian republic of Khakassia have documented ten engraved stone sl | https://arkeonews.net/rare-tagar-horse-engravings-discovered-in-an-early-iron-age-burial-mound-in-khakassia/
2026-08-18 | Global | Arkeonews | Archaeologists in Croatia have uncovered 1,600-year-old early Christian floor mosaics carr | https://arkeonews.net/1600-year-old-early-christian-mosaics-discovered-in-croatia-with-a-great-sinners-inscription/


<!-- 2026-08-22 edition (this run) -->
2026-08-22 | Saudi Arabia/Regional | The Art Newspaper | Riyadh's JAX cultural district expands with Lift gallery arrival | https://www.theartnewspaper.com/2026/08/21/riyadhs-jax-cultural-district-expands-with-lift-gallery-arrival
2026-08-22 | Negative Articles | Middle East Eye | Tanker traffic at Saudi Arabia's Yanbu port falls by a third, report says | https://www.middleeasteye.net/live-blog/live-blog-update/tanker-traffic-saudi-arabias-yanbu-port-falls-third-report-says
2026-08-22 | Negative Articles | Semafor | Saudi Arabia renews diplomatic efforts with Iraq | https://www.semafor.com/article/08/21/2026/saudi-arabia-renews-diplomatic-efforts-with-iraq
2026-08-22 | Global | The Art Newspaper | More than 100 works from Canada's federal collection of Indigenous art are 'unaccounted for' | https://www.theartnewspaper.com/2026/08/21/canada-federal-indigenous-art-collection-111-works-unaccounted-for
2026-08-22 | Global | Blooloop | Powerhouse Parramatta in Sydney sets opening date | https://blooloop.com/news/powerhouse-parramatta-november-opening-date
2026-08-22 | Global | The Art Newspaper | Smithsonian races to finalise site for national Latino museum | https://www.theartnewspaper.com/2026/08/21/smithsonian-institution-latino-museum-arts-industries-building-washington
2026-08-22 | Global | Hyperallergic | Maya Lin to Build Otherworldly 'Floating Landscape' at UT Austin | https://hyperallergic.com/maya-lin-to-build-otherworldly-floating-landscape-at-ut-austin/
2026-08-22 | Global | The Art Newspaper | Young adults with experience of having parents in prison to curate exhibition at London's Southbank Centre | https://www.theartnewspaper.com/2026/08/21/young-adults-with-experience-of-having-parents-in-prison-to-curate-southbank-centre-exhibition
2026-08-22 | Global | Deadline | 'Spider-Man' Fourth Box Office Weekend Arrives; 'Insidious 6' Opens | https://deadline.com/2026/08/spider-man-insidious-out-of-the-further-global-box-office-1237046811/
2026-08-22 | Global | WWD | Dior PR Executive Mathilde Favier Dies at 57 | https://wwd.com/fashion-news/designer-luxury/mathilde-favier-dies-dior-pr-1239127748/
2026-08-22 | Global | Dezeen | ZHA designs forest neighbourhoods for Baku Expo City masterplan | https://www.dezeen.com/2026/08/21/zha-baku-expo-city-masterplan/
