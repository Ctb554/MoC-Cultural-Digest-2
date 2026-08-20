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
2026-08-17 | Saudi Arabia/Regional | CP24 | Trump welcomes defence pact between Saudi Arabia, Turkiye and Pakistan | https://www.cp24.com/news/world/2026/08/16/trump-welcomes-defence-pact-between-saudi-arabia-turkiye-and-pakistan/
2026-08-17 | Saudi Arabia/Regional | Deutsche Welle | UAE, Saudi Arabia, others condemn Israel's rejection of Trump Gaza plan | https://www.dw.com/en/uae-saudi-arabia-others-condemn-israels-rejection-of-trump-gaza-plan/a-78389399
2026-08-17 | Negative Articles | Press TV | Yemen warns Saudi territory, interests will not be spared if war escalates | https://www.presstv.co.uk/Detail/2026/08/16/774481/Yemen-senior-official-warns-Saudi-Arabia-territory-interests-face-consequences-conflict-continues
2026-08-17 | Global | Arkeonews | 1,600-Year-Old Early Christian Mosaics Discovered in Croatia with a 'Great Sinners' Inscription | https://arkeonews.net/1600-year-old-early-christian-mosaics-discovered-in-croatia-with-a-great-sinners-inscription/
2026-08-17 | Global | Arkeonews | Ramesses II Lintel Discovered on Egypt's Ancient Road to Canaan May Point to Lost Mesen | https://arkeonews.net/ramesses-ii-lintel-discovered-on-egypts-ancient-road-to-canaan-may-point-to-lost-mesen/
2026-08-17 | Global | Arkeonews | 1,500-Year-Old 'Golden Shoes' Found in Elite Woman's Grave Near Ancient Caspian Trade Hub | https://arkeonews.net/1500-year-old-golden-shoes-found-in-elite-womans-grave-near-ancient-caspian-trade-hub/
2026-08-18 | Saudi Arabia/Regional | Muslim Network TV | Saudi's Riyadh expands public art across streets and transit hubs | https://www.muslimnetwork.tv/saudis-riyadh-expands-public-art-across-streets-and-transit-hubs/
2026-08-18 | Negative Articles | Middle East Eye | Houthis say they targeted Saudi military ship in Red Sea | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-they-targeted-saudi-military-ship-red-sea
2026-08-18 | Global | The Art Newspaper | Frieze Seoul to move to new venue from 2027 | https://www.theartnewspaper.com/2026/08/17/frieze-seoul-to-move-to-new-venue-from-2027
2026-08-18 | Global | The Art Newspaper | Mary Heilmann, fearless colourist and singular abstract painter, has died, aged 86 | https://www.theartnewspaper.com/2026/08/17/mary-heilmann-fearless-colourist-singular-painter-obituary
2026-08-18 | Global | The Art Newspaper | Police recover eight Matisse works stolen in Brazil heist | https://www.theartnewspaper.com/2026/08/17/stolen-matisse-works-recovered-sao-paulo-brazil-heist
2026-08-18 | Global | The Art Newspaper | Four works by Renaissance master Antonello da Messina stolen from Sicily museum | https://www.theartnewspaper.com/2026/08/17/four-works-by-sicilian-renaissance-master-stolen-from-messina-museum
2026-08-18 | Global | Arkeonews | Rare Tagar horse engravings discovered in an Early Iron Age burial mound in Khakassia | https://arkeonews.net/rare-tagar-horse-engravings-discovered-in-an-early-iron-age-burial-mound-in-khakassia/
2026-08-18 | Global | Arkeonews | Rare 4,000-year-old 'enigmatic tablet' found intact at Lucone Bronze Age village in Italy | https://arkeonews.net/rare-4000-year-old-enigmatic-tablet-found-intact-at-lucone-bronze-age-village-in-italy/
2026-08-18 | Global | Arkeonews | 1,600-year-old early Christian mosaics discovered in Croatia with a 'Great Sinners' inscription | https://arkeonews.net/1600-year-old-early-christian-mosaics-discovered-in-croatia-with-a-great-sinners-inscription/
2026-08-18 | Risks and Opportunities | gCaptain | Asian refiners ask to pick up Saudi oil outside risky Red Sea | https://gcaptain.com/asian-refiners-ask-to-pick-up-saudi-oil-outside-risky-red-sea/
2026-08-18 | Risks and Opportunities | Turkiye Today | Houthis claim strike on Saudi military vessel, 4 boats in Red Sea | https://www.turkiyetoday.com/region/houthis-claim-strike-on-saudi-military-vessel-4-boats-in-red-sea-3226269
2026-08-19 | Saudi Arabia/Regional | CairoScene | Riyadh Art Brings 75 Permanent Public Artworks Across the City | https://cairoscene.com/ArtsAndCulture/Riyadh-Art-Brings-75-Permanent-Public-Artworks-Across-the-City
2026-08-19 | Saudi Arabia/Regional | ArchDaily | From Tent to Terminal: Bedouin Craft in Contemporary Infrastructure | https://www.archdaily.com/1183404/from-tent-to-terminal-bedouin-craft-in-contemporary-infrastructure
2026-08-19 | Global | Archaeology Magazine | Mysterious Runestone Found in Floor of Faroe Islands Chapel | https://archaeology.org/news/2026/08/18/mysterious-runestone-found-embedded-in-floor-of-faroe-islands-chapel/
2026-08-19 | Global | Archaeology Magazine | Crucibles Contain Earliest Evidence of Brass Production in East Asia | https://archaeology.org/news/2026/08/18/crucibles-contain-earliest-evidence-of-brass-production-in-east-asia/
2026-08-19 | Global | Archaeology Magazine | Denisovans Were Much Taller Than Previously Thought | https://archaeology.org/news/2026/08/18/denisovans-were-much-taller-than-previously-thought/
2026-08-19 | Global | Arkeonews | Rare 4,000-Year-Old 'Enigmatic Tablet' Found Intact at Lucone Bronze Age Village in Italy | https://arkeonews.net/rare-4000-year-old-enigmatic-tablet-found-intact-at-lucone-bronze-age-village-in-italy/
2026-08-19 | Global | Arkeonews | 1,000-Year-Old Luxury Bowls in the Sudanese Desert Hide an 8-Nanometer Secret | https://arkeonews.net/1000-year-old-luxury-bowls-in-the-sudanese-desert-hide-an-8-nanometer-secret/
2026-08-19 | Global | Forbes | Venice Film Festival Lineup Comes Into Focus | https://www.forbes.com/sites/dbloom/2026/08/18/venice-film-festival-lineup-comes-into-focus/
2026-08-19 | Risks and Opportunities | New York Times | Saudi Arabia, UAE, Japan expand oil storage | https://www.nytimes.com/2026/08/18/business/saudi-uae-japan-oil-storage.html
2026-08-19 | Risks and Opportunities | The Business of Fashion | Red Sea attacks renew risks to supply chains | https://www.businessoffashion.com/articles/global-markets/worldview-red-sea-attacks-renew-risks-to-supply-chains/
2026-08-20 | Saudi Arabia/Regional | TTN Worldwide | CONTINUUM '26: Diriyah Art Futures presents cutting-edge artworks | https://www.ttnworldwide.com/ArticleTA/466718/continuum-%E2%80%9926_colon-diriyah-art-futures-presents-cutting-edge-artworks-
2026-08-20 | Saudi Arabia/Regional | The News Mill | Directors praise Salman Khan, Sanjay Dutt for Saudi film '7 Dogs' | https://thenewsmill.com/2026/08/directors-praise-salman-khan-sanjay-dutt-for-saudi-film-7-dogs/
2026-08-20 | Negative Articles | Middle East Eye | Houthis threaten wider escalation against Saudi Arabia | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-threaten-wider-escalation-against-saudi-arabia
2026-08-20 | Negative Articles | AGBI | Saudi Arabia opens new Red Sea resort despite tourism downturn | https://www.agbi.com/tourism/2026/08/saudi-arabia-opens-new-red-sea-resort-despite-tourism-downturn/
2026-08-20 | Global | The Art Newspaper | Colombia earthquake damaged 40 protected sites and dozens more cultural assets, report finds | https://www.theartnewspaper.com/2026/08/19/colombia-earthquake-ministry-culture-report-heritage-damage
2026-08-20 | Global | Arkeonews | 25 Turtle Figurines Unearthed in a Turkish Cave, Some Dating Back 16,500 Years | https://arkeonews.net/25-turtle-figurines-unearthed-in-a-turkish-cave-some-dating-back-16500-years/
2026-08-20 | Global | Archaeology Magazine | Medieval Scottish Man May Be First Confirmed Case of Death by Trebuchet | https://archaeology.org/news/2026/08/19/medieval-scottish-man-may-be-first-confirmed-case-of-death-by-trebuchet/
2026-08-20 | Global | Hyperallergic | Speed Art Museum Returns 24 Native Artifacts to Oklahoma Tribes | https://hyperallergic.com/speed-art-museum-returns-24-native-artifacts-to-oklahoma-tribes/
2026-08-20 | Global | The Art Newspaper | Donald Judd's retrofitted Artillery Sheds in Texas to undergo extensive restoration work | https://www.theartnewspaper.com/2026/08/19/donald-judd-artillery-sheds-marfa-texas-restoration-chinati-foundation
2026-08-20 | Global | ArchDaily | NCARB 2026 Report Shows a More Diverse Candidate Pool Amid Persistent Gaps in Architecture Licensure | https://www.archdaily.com/1183568/ncarb-2026-report-shows-a-more-diverse-candidate-pool-amid-persistent-gaps-in-architecture-licensure
2026-08-20 | Global | The Stage | The Stage Debut Awards 2026: Ralph Fiennes and Sadie Sink among nominees | https://www.thestage.co.uk/news/the-stage-debut-awards-2026-ralph-fiennes-and-sadie-sink-among-nominees
2026-08-20 | Global | Deadline | John Irvin Dead: 'Hamburger Hill' & 'Raw Deal' Director Was 86 | https://deadline.com/2026/08/john-irvin-dead-hamburger-hill-raw-deal-director-1237044695/
