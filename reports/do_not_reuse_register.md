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
