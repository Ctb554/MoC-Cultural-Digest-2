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

<!-- Backfill reconciliation 2026-08-13: the repo's reports/ history and this
     register were empty on clone, but the Dropbox delivery folder held ~24
     prior delivered editions (20 Jul - 12 Aug 2026). The three most recent
     (10, 11, 12 Aug) were downloaded and reconciled below so this edition's
     reuse gate and continuity are protected. Older delivered editions were
     not backfilled (out of a 24h coverage window's realistic reuse range);
     flagged in the run log for a possible future full backfill. -->
2026-08-12 | Saudi Arabia/Regional | Nikkei Asia | Turkey-Pakistan-Saudi pact a 'Muslim NATO'?: 5 things to know | https://asia.nikkei.com/politics/defense/turkey-pakistan-saudi-pact-a-muslim-nato-5-things-to-know
2026-08-12 | Saudi Arabia/Regional | The New York Times | Four Killed in Houthi Strike on Red Sea Ship, Yemeni Government Says | https://www.nytimes.com/2026/08/11/world/middleeast/deadly-houthi-strike-red-sea.html
2026-08-12 | Saudi Arabia/Regional | Semafor | Saudi data center capacity projected to boom, but financing a challenge | https://www.semafor.com/article/08/11/2026/saudi-data-center-capacity-projected-to-boom-but-financing-a-challenge
2026-08-12 | Saudi Arabia/Regional | AGBI | Ades confirms all offshore rigs in Saudi Arabia are operational | https://www.agbi.com/oil-and-gas/2026/08/ades-confirms-all-offshore-rigs-in-saudi-arabia-are-operational/
2026-08-12 | Negative Articles | Al Jazeera | Six killed in Houthi attack on Bab al-Mandeb ship, Yemen's government says | https://www.aljazeera.com/news/2026/8/12/six-killed-in-houthi-attack-on-bab-al-mandeb-ship-yemens-government-says
2026-08-12 | Negative Articles | Middle East Eye | Saudi defence pact with Turkey and Pakistan sparks UAE backlash | https://www.middleeasteye.net/trending/saudi-arabia-defence-pact-turkey-pakistan-sparks-uae-backlash
2026-08-12 | Global | The Art Newspaper | Bottoms up: vast Roman shipwreck filled with ancient wine amphoras discovered near Sicily | https://www.theartnewspaper.com/2026/08/11/bottoms-up-vast-roman-shipwreck-filled-with-ancient-wine-amphoras-discovered-near-sicily
2026-08-12 | Global | The Art Newspaper | Earthquake damages Colombia's tallest church | https://www.theartnewspaper.com/2026/08/11/colombia-earthquake-damages-manizales-cathedral
2026-08-12 | Global | Hyperallergic | Russia Has Damaged or Destroyed Over 4,500 Cultural Sites in Ukraine | https://hyperallergic.com/russia-has-damaged-or-destroyed-over-4-500-cultural-sites-in-ukraine/
2026-08-12 | Global | Hyperallergic | San Diego Museum of Art Lays Off 11 Workers | https://hyperallergic.com/san-diego-museum-of-art-lays-off-11-workers/
2026-08-12 | Global | The Art Newspaper | 'Stopping while we're ahead': London gallery Sid Motion to shut after a decade | https://www.theartnewspaper.com/2026/08/11/stopping-while-were-ahead-london-gallery-sid-motion-to-shut-after-a-decade
2026-08-12 | Global | Hyperallergic | Maori Karmael Holmes Looks Back on 15 Years of BlackStar | https://hyperallergic.com/maori-karmael-holmes-looks-back-on-15-years-of-blackstar/
2026-08-12 | Global | ArchDaily | Peter Zumthor's Architecture Takes Center Stage in Wim Wenders' New Film "From Inside Out" | https://www.archdaily.com/1183086/peter-zumthors-architecture-takes-center-stage-in-wim-wenders-new-film-from-inside-out
2026-08-12 | Global | The Stage | ATG Entertainment agrees sale to global events firm Mari | https://www.thestage.co.uk/news/atg-entertainment-sold-to-global-events-firm-mari
2026-08-11 | Saudi Arabia/Regional | Deutsche Welle | Which country is the new Mecca defense pact targeting? | https://www.dw.com/en/which-country-is-the-new-mecca-defense-pact-targeting/a-78307673
2026-08-11 | Saudi Arabia/Regional | The Diplomat | The Mecca Pact Extends Pakistan's Security Role Westward | https://thediplomat.com/2026/08/the-mecca-pact-extends-pakistans-security-role-westward/
2026-08-11 | Saudi Arabia/Regional | The Diplomat | Bangladesh Joins Saudi-led Defense Coalition as Bab el-Mandeb Risks Grow | https://thediplomat.com/2026/08/bangladesh-joins-saudi-led-defense-coalition-as-bab-el-mandeb-risks-grow/
2026-08-11 | Saudi Arabia/Regional | Middle East Eye | Iran says it is not concerned by new 'Mecca Joint Defence Agreement' | https://www.middleeasteye.net/news/iran-says-it-not-concerned-new-mecca-joint-defence-agreement
2026-08-11 | Global | Arkeonews | 2,400-Year-Old Tomb of a Possible Ancient Wrestler Discovered at Aspendos | https://arkeonews.net/2400-year-old-tomb-of-a-possible-ancient-wrestler-discovered-at-aspendos/
2026-08-11 | Global | Arkeonews | 8,500-Year-Old Shell Bead Reveals Ancient California's Hidden Trade Network | https://arkeonews.net/8500-year-old-shell-bead-reveals-ancient-californias-hidden-trade-network/
2026-08-11 | Global | The Art Newspaper | Remains of colonial hospital and church discovered in Lima's historic centre | https://www.theartnewspaper.com/2026/08/10/remains-colonial-hospital-discovered-luma
2026-08-11 | Global | Hyperallergic | Divers Stumble Upon 2,000-Year-Old Roman Shipwreck in Italy | https://hyperallergic.com/divers-stumble-upon-2-000-year-old-roman-shipwreck-in-italy/
2026-08-11 | Global | Hyperallergic | National Gallery of Art Protects Works Ahead of Trump's IndyCar Race | https://hyperallergic.com/national-gallery-of-art-protects-works-ahead-of-trumps-indycar-race/
2026-08-11 | Global | The Art Newspaper | UK Ministry of Justice spent more than £85,000 removing Banksy mural from the Royal Courts of Justice | https://www.theartnewspaper.com/2026/08/10/uk-ministry-of-justice-spent-more-than-%C2%A385000-removing-banksy-mural-from-the-royal-courts-of-justice
2026-08-11 | Global | Dezeen | Elon Musk reveals plans for world's largest building | https://www.dezeen.com/2026/08/10/terafab-elon-musk-spacex-tesla-largest-building/
2026-08-11 | Global | Dezeen | Realistic AI architectural renderings must be labelled under EU AI Act | https://www.dezeen.com/2026/08/10/ai-architectural-renderings-eu-ai-act/
2026-08-10 | Saudi Arabia/Regional | NBC News | Yemen's Houthis attack Saudi Aramco Jazan refinery | https://www.nbcnews.com/world/middle-east/yemens-houthis-attack-saudi-aramco-jazan-refinery-rcna591561
2026-08-10 | Saudi Arabia/Regional | Al-Monitor | Yemen's Houthis attack Saudi refinery after kingdom signs defence pact | https://www.al-monitor.com/originals/2026/08/yemens-houthis-attack-saudi-refinery-after-kingdom-signs-defence-pact
2026-08-10 | Saudi Arabia/Regional | CNBC | Iran denies any direct talks with U.S. on opening Strait of Hormuz as Houthis claim attack on Saudi refinery | https://www.cnbc.com/2026/08/09/saudi-aramco-extinguishes-refinery-fire-houthis-claim-attack.html
2026-08-10 | Negative Articles | Al Jazeera | Houthi attacks kill seven in Yemen, refinery targeted in Saudi Arabia | https://www.aljazeera.com/news/2026/8/9/saudi-arabia-says-fire-extinguished-at-aramco-facility-in-jizan
2026-08-10 | Global | Arkeonews | 450 Mice Found in a 2,700-Year-Old Sanctuary in Crete Point to an Unknown Cult | https://arkeonews.net/450-mice-found-in-a-2700-year-old-sanctuary-in-crete-point-to-an-unknown-cult/
2026-08-10 | Global | Arkeonews | Şanlıurfa Castle Excavations Uncover a Martyr's Church in Ancient Edessa | https://arkeonews.net/sanliurfa-castle-excavations-uncover-a-martyrs-church-in-ancient-edessa/
2026-08-10 | Global | Variety | Florian Hoffmann's U.N. Compound Drama 'Yazz' Takes Main Alliance 4 Development Prizes at Locarno Pro Awards | https://variety.com/2026/film/global/florian-hoffmann-yazz-alliance-4-development-prizes-locarno-1236830871/
2026-08-10 | Global | Dezeen | Design profession receives own classification in upcoming Australian census | https://www.dezeen.com/2026/08/10/design-profession-category-australia-census/
2026-08-10 | Global | Dezeen | Crystal-shaped sauna rises from former industrial site in Sweden | https://www.dezeen.com/2026/08/09/lithium-crystal-sauna-bigert-bergstrom/
2026-08-10 | Global | Dezeen | I IN clads Human Made store in handcrafted Korean celadon tiles with "powerful presence" | https://www.dezeen.com/2026/08/09/i-in-human-made-store-korean-celadon-tiles/
2026-08-13 | Saudi Arabia/Regional | Deutsche Welle | Gulf states scramble for Strait of Hormuz alternative | https://www.dw.com/en/gulf-states-scramble-for-strait-of-hormuz-alternative/a-78336679
2026-08-13 | Saudi Arabia/Regional | Bloomberg | Saudi Arabia Sees First Supertanker at Persian Gulf Export Terminal in Weeks | https://www.bloomberg.com/news/articles/2026-08-12/oil-tanker-seen-loading-at-key-saudi-hub-for-first-time-in-weeks
2026-08-13 | Saudi Arabia/Regional | Semafor | Israeli textbook watchdog commends Saudi education reforms | https://www.semafor.com/article/08/12/2026/saudi-education-reforms-commended-by-israeli-textbook-watchdog
2026-08-13 | Negative Articles | Middle East Eye | Saudi Arabia opposed Egypt's inclusion in Mecca agreement, sources say | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-opposed-egypts-inclusion-mecca-agreement-sources-say
2026-08-13 | Global | Archaeology Magazine | Nile Delta Necropolis Used for Thousands of Years | https://archaeology.org/news/2026/08/12/nile-delta-necropolis-used-for-thousands-of-years/
2026-08-13 | Global | ARTnews | Zeitz MOCAA Names Elvira Dyangani Ose as Next Artistic Director | https://www.artnews.com/art-news/news/zeitz-mocaa-elvira-dyangani-ose-artistic-director-1234794757/
2026-08-13 | Global | ARTnews | SF Camerawork To Close After Five Decades, Citing 'Changing Philanthropic Landscape' | https://www.artnews.com/art-news/news/sf-camerawork-close-rising-costs-dwindling-public-funding-1234794668/
2026-08-13 | Global | ARTnews | Sotheby's Lands Another Blockbuster Collection as Blaquier Family Parts With $450 M. of Impressionist Treasures | https://www.artnews.com/art-news/news/sothebys-blaquier-450-million-art-collection-1234794798/
