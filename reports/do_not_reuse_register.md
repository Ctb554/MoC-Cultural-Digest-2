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

<!-- Reconciled 2026-09-20 from delivered editions 17-19 Sep 2026 (Dropbox 05_Claude Test), the actual continuity store; repo register had been empty. -->
2026-09-17 | Saudi Arabia/Regional | CairoScene | Hafez Gallery Makes Frieze London Debut With Two-Artist Showcase | https://cairoscene.com/ArtsAndCulture/Hafez-Gallery-Makes-Frieze-London-Debut-With-Two-Artist-Showcase
2026-09-17 | Saudi Arabia/Regional | BroadcastPro ME | Film AlUla partners with Sherborne Media to boost production financing | https://www.broadcastprome.com/news/film-alula-partners-with-sherborne-media-to-boost-production-financing/
2026-09-17 | Saudi Arabia/Regional | The Washington Times | Smithsonian's National Zoo breaks ground on Arabian Leopard exhibit | https://www.washingtontimes.com/news/2026/sep/16/smithsonians-national-zoo-breaks-ground-arabian-leopard-exhibit-open/
2026-09-17 | Negative Articles | The New York Times | Global Oil Prices Could Hit Highest Levels in Months After Saudi Pipeline Attacks | https://www.nytimes.com/2026/09/16/business/saudi-pipeline-houthi-attacks.html
2026-09-17 | Risks/Opportunities | The Guardian | US officials decide against backing Saudi Arabia after meeting Houthi leaders | https://www.theguardian.com/world/2026/sep/16/us-officials-decide-against-backing-saudi-arabia-yemen-meeting-houthi-leaders
2026-09-17 | Risks/Opportunities | The Express Tribune | US urges travellers to reconsider Saudi Arabia trips over Iranian drone-missile threat | https://tribune.com.pk/story/2629641/us-urges-travellers-to-reconsider-saudi-arabia-trips-over-iranian-drone-missile-threat
2026-09-17 | Risks/Opportunities | Press TV | Yemeni Armed Forces target Aramco facilities, King Khalid Air Base | https://www.presstv.co.uk/Detail/2026/09/16/776408/Yemeni-Armed-Forces-target-Aramco-facilities,-King-Khalid-Air-Base-in-Saudi-Arabia
2026-09-17 | Global | Artnet News | Giotto and Cimabue masterpieces in Assisi get an ultra-HD digital revival | https://news.artnet.com/art-world/giotto-and-cimabue-masterpieces-in-assisi-get-a-ultra-hd-digital-revival-2811536
2026-09-17 | Global | Hyperallergic | Met Museum breaks ground on new modern and contemporary wing | https://hyperallergic.com/met-museum-breaks-ground-on-new-modern-and-contemporary-wing/
2026-09-17 | Global | ARTnews | Thyssen-Bornemisza museum to expand second location in Madrid | https://www.artnews.com/art-news/news/thyssen-bornemisza-museum-expand-second-location-madrid-1234798467/
2026-09-17 | Global | ARTnews | Chinese artist Liang Shaoji, known for silkworm works, dies | https://www.artnews.com/art-news/news/liang-shaoji-dead-chinese-artist-silkworms-1234798463/
2026-09-17 | Global | BNN Bloomberg | Director Danny Boyle defends use of AI in new film 'Ink' at TIFF screening | https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/09/16/director-danny-boyle-defends-use-of-ai-in-new-film-ink-at-tiff-screening/
2026-09-17 | Global | W Magazine | Dario Vitale named Emporio Armani creative director | https://www.wmagazine.com/fashion/dario-vitale-emporio-armani-creative-director
2026-09-17 | Global | NBC News | Trump's handpicked Kennedy Center board votes to close venue for renovations | https://www.nbcnews.com/politics/trump-administration/trumps-handpicked-kennedy-center-board-votes-close-venue-renovations-rcna597921
2026-09-18 | Saudi Arabia/Regional | ArtReview | Islamic Arts Biennale 2027 names lead curators | https://artreview.com/islamic-arts-biennale-2027-names-lead-curators/
2026-09-18 | Saudi Arabia/Regional | TIME | Dana Awartani Is on the 2026 TIME100 Art List | https://time.com/collection/time100-art/2026/dana-awartani/
2026-09-18 | Saudi Arabia/Regional | MDNtv | Saudi Film Nights Makes Historic South African Debut This October | https://mdntvlive.com/saudi-film-nights-makes-historic-south-african-debut-this-october/
2026-09-18 | Saudi Arabia/Regional | Deadline | Dubai International Film Festival To Return In December 2027, As 2026 Edition Of Saudi Arabia's Red Sea Film Festival Looks Uncertain | https://deadline.com/2026/09/dubai-film-festival-return-saudi-red-sea-film-uncertain-1237106423/
2026-09-18 | Negative Articles | Al Jazeera | Trump administration approves sale of F-35 jets to Saudi Arabia | https://www.aljazeera.com/news/2026/9/17/trump-administration-approves-sale-of-f-35-jets-to-saudi-arabia
2026-09-18 | Negative Articles | Al Jazeera | Five killed as Saudi Arabia and Yemen's Houthis trade attacks | https://www.aljazeera.com/news/2026/9/17/five-killed-as-saudi-arabia-and-yemens-houthis-trade-attacks
2026-09-18 | Negative Articles | CNBC | Oil prices fall as Saudi Arabia reportedly offers more crude via Hormuz after pipeline attack | https://www.cnbc.com/2026/09/17/oil-prices-today-wti-brent-hormuz-iran-war.html
2026-09-18 | Negative Articles | Semafor | Saudi Arabia's well-timed uranium find near Medina | https://www.semafor.com/article/09/17/2026/saudi-arabias-well-timed-uranium-find-near-medina
2026-09-18 | Global | Washingtonian | Michelin Adds 4 New Restaurants to Its DC Guide | https://washingtonian.com/2026/09/17/michelin-adds-4-new-restaurants-to-its-dc-guide/
2026-09-18 | Global | Dezeen | Ma Yansong and Daniel Libeskind join Dezeen Awards master jury | https://www.dezeen.com/2026/09/17/dezeen-awards-2026-master-jury/
2026-09-18 | Global | WhoWhatWear | Live From London Fashion Week: Everything You Need to Know About the Shows, Trends and Celebrity Moments of S/S '27 | https://www.whowhatwear.com/fashion/live/london-fashion-week-spring-summer-2027
2026-09-18 | Global | Arkeonews | New Laser Scans Reveal Six Groups of Ancient Ships on a 3,000-Year-Old Wall in Cyprus | https://arkeonews.net/new-laser-scans-reveal-six-groups-of-ancient-ships-on-a-3000-year-old-wall-in-cyprus/
2026-09-18 | Global | Arkeonews | Rare 2,000-Year-Old Celtic Silver Hoard Found Beneath a Former Sports Field | https://arkeonews.net/rare-2000-year-old-celtic-silver-hoard-found-beneath-a-former-sports-field/
2026-09-19 | Saudi Arabia/Regional | SSBCrack | Emerging Artists Showcase Innovative Works at Diriyah's 'Continuum' Exhibition | https://news.ssbcrack.com/emerging-artists-showcase-innovative-works-at-diriyahs-continuum-exhibition/
2026-09-19 | Saudi Arabia/Regional | Michelin Guide | The 2026 MICHELIN Key Hotels: A Guide to the Global Selection | https://guide.michelin.com/sa/en/article/travel/all-the-key-hotels-in-the-world-michelin-guide
2026-09-19 | Negative Articles | Gulf News | Saudi Arabia issues air raid alert in Riyadh, explosions heard | https://gulfnews.com/world/gulf/saudi/saudi-arabia-issues-air-raid-alert-in-riyadh-explosions-heard-1.500680175
2026-09-19 | Negative Articles | Al Jazeera | Pakistan pledges full committment to defence of Saudi Arabia | https://www.aljazeera.com/news/2026/9/18/pakistan-pledges-full-committment-to-defence-of-saudi-arabia
2026-09-19 | Global | The Art Newspaper | Cave markings discovered in Ireland could transform understanding of when humans first settled there | https://www.theartnewspaper.com/2026/09/18/cave-markings-discovered-in-ireland-could-transform-understanding-of-when-humans-first-settled-there
2026-09-19 | Global | Archaeology Magazine | Possible Zoroastrian Fire Altar Unearthed in Uzbekistan | https://archaeology.org/news/2026/09/18/possible-zoroastrian-fire-altar-unearthed-in-uzbekistan/
2026-09-19 | Global | HeritageDaily | Major new discoveries beneath the forest canopy near Machu Picchu | https://www.heritagedaily.com/2026/09/major-new-discoveries-beneath-the-forest-canopy-near-machu-picchu/159286
2026-09-19 | Global | The Art Newspaper | Dutch museum puts all 88 of its Van Gogh paintings on display for the first time in more than two decades | https://www.theartnewspaper.com/2026/09/18/all-the-van-goghs-opening-in-the-netherlands
2026-09-19 | Global | The Art Newspaper | ArtRio opens amid political uncertainty as Brazil's art market continues to grow | https://www.theartnewspaper.com/2026/09/18/artrio-fair-rio-de-janeiro-growing-market-presidential-election
2026-09-19 | Global | ARTnews | Art Basel Parent Group's First Half Revenue Climbed As It Opened Qatar | https://www.artnews.com/art-news/market/art-basel-parent-group-mch-first-half-2026-revenue-climbed-1234798809/
2026-09-19 | Global | The Art Newspaper | Malba picks architect for expansion that will double its exhibition space | https://www.theartnewspaper.com/2026/09/17/malba-museum-buenos-aires-frida-escobedo-architect-expansion

<!-- Edition 2026-09-20 (this run) -->
2026-09-20 | Saudi Arabia/Regional | The National | Guggenheim Abu Dhabi tickets go on sale ahead of grand opening | https://www.thenationalnews.com/arts-culture/art-design/2026/09/18/guggenheim-abu-dhabi-tickets-go-on-sale-with-prices-revealed
2026-09-20 | Negative Articles | The Wall Street Journal | Air Attack Sets Fuel Depot Ablaze at Airport in Saudi Capital | https://www.wsj.com/world/middle-east/air-attack-sets-fuel-depot-ablaze-at-airport-in-saudi-capital-8bcc439c
2026-09-20 | Negative Articles | The Guardian | Pact with Saudi Arabia threatens to draw Pakistan into Middle East conflict | https://www.theguardian.com/world/2026/sep/19/pakistan-saudi-arabia-mecca-pact-joint-defence-agreement-houthis-yemen-conflict
2026-09-20 | Negative Articles | Yahoo Sports | 'You always have a choice': Tessel Middag speaks out against Saudi Arabia's influence on football | https://sports.yahoo.com/articles/always-choice-tessel-middag-speaks-220500370.html
2026-09-20 | Global | Deadline | Lucas Museum Of Narrative Art Opening: Oprah Winfrey, Laura Dern, Mark Hamill & More | https://deadline.com/gallery/lucas-museum-of-narrative-art-opening-oprah-winfrey-laura-dern-mark-hamill-more
2026-09-20 | Global | The Montrealer | Upcoming highlights at the Montreal Museum of Fine Arts | https://themontrealeronline.com/2026/09/upcoming-highlights-at-the-montreal-museum-of-fine-arts
2026-09-20 | Global | Baltic Review | Warsaw opens Tilda Swinton exhibition focused on artistic collaboration | https://baltic-review.com/warsaw-tilda-swinton-ongoing-exhibition
2026-09-20 | Global | Dezeen | This week we reported on London Design Festival | https://www.dezeen.com/2026/09/19/london-design-festival-this-week
2026-09-20 | Risks/Opportunities | CNN | Frustration grows as Houthis widen Middle East conflict with US unwilling to intervene | https://www.cnn.com/2026/09/19/politics/frustration-houthis-saudi-arabia-iran
