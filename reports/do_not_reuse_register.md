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

<!-- Backfill added 2026-08-25: prior editions 22-24 Aug were delivered to the Dropbox test folder but never recorded here; their article links/headlines are transcribed below from the delivered .docx files for reuse-blocking continuity. Today's 25 Aug entries follow. -->
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
2026-08-23 | Saudi Arabia/Regional | Travel And Tour World | France Accelerates Luxury Tourism Growth With Macron-Mohammed bin Salman Strategic Partnership | https://www.travelandtourworld.com/news/article/dllp5veduy0a/
2026-08-23 | Global | Arkeonews | 4,300-Year-Old Tomb in Inner Mongolia Reveals Earliest Known Dragon-Phoenix Pairing in Northern China | https://arkeonews.net/4300-year-old-tomb-in-inner-mongolia-reveals-earliest-known-dragon-phoenix-pairing-in-northern-china/
2026-08-23 | Global | Arkeonews | Roman Mass Grave Beneath Vienna Soccer Field Reveals Unusual Concentration of Pelvic Wounds | https://arkeonews.net/roman-mass-grave-beneath-vienna-soccer-field-reveals-unusual-concentration-of-pelvic-wounds/
2026-08-23 | Global | Arkeonews | One of Byzantium's Most Striking Images of Mary's Last Sleep Survives on a Mosque Wall in Istanbul | https://arkeonews.net/one-of-byzantiums-most-striking-images-of-marys-last-sleep-survives-on-a-mosque-wall-in-istanbul/
2026-08-23 | Global | Arkeonews | 1,700-Year-Old Chinese Armor Still Shines Thanks to an Ancient Metalworking Secret | https://arkeonews.net/1700-year-old-chinese-armor-still-shines-thanks-to-an-ancient-metalworking-secret/
2026-08-23 | Global | ArchDaily | Antiquity exhibition at Wawel castle / NArchitekTURA | https://www.archdaily.com/1183570/antiquity-exhibition-at-wawel-castle-narchitektura
2026-08-23 | Global | Dezeen | Estudio Campana creates 'woven jewellery box' for Tiffany & Co in Sao Paulo | https://www.dezeen.com/2026/08/22/tiffany-co-pop-up-jk-iguatemi-mall-sao-paulo-estudio-campana/
2026-08-23 | Global | Dezeen | 'Light and sea breeze shape the viewing' of exhibits at open-air art gallery in Mexico | https://www.dezeen.com/2026/08/22/arte-abierto-baja-sordo-madaleno-arquitectos/
2026-08-23 | Global | Dezeen | KTGY revamps interiors of Fairmont Hotel in Chicago | https://www.dezeen.com/2026/08/23/ktgy-revamps-interiors-fairmont-hotel-chicago/
2026-08-23 | Global | ArchDaily | What is Blue Infrastructure? Rethinking Water's Role in City Design | https://www.archdaily.com/1182257/what-is-blue-infrastructure-rethinking-waters-role-in-city-design
2026-08-23 | Risks and Opportunities | The National | Saudi crown prince visits France to sign deals and discuss Strait of Hormuz | https://www.thenationalnews.com/news/mena/2026/08/22/saudi-crown-prince-visits-france-to-sign-deals-and-discuss-strait-of-hormuz/
2026-08-24 | Saudi Arabia/Regional | The National | Gulf dreams and Palestinian portraits: Vantage Point Sharjah turns lens on intimate lives | https://www.thenationalnews.com/arts-culture/art-design/2026/08/24/vantage-point-sharjah-2026/
2026-08-24 | Saudi Arabia/Regional | The National | UAE art guide: 12 exhibitions to see, from Spectrum at Manarat Al Saadiyat to orange art at Ayyam Gallery | https://www.thenationalnews.com/arts-culture/art-design/2026/08/23/uae-guide-museum-gallery-exhibitions-to-see-abu-dhabi-dubai/
2026-08-24 | Negative Articles | Bloomberg | Saudi Oil Logistics Roiled Again by Houthis' Red Sea Threat | https://www.bloomberg.com/news/articles/2026-08-23/saudis-oil-logistics-roiled-again-by-houthis-red-sea-threat
2026-08-24 | Global | Deadline | 'Spider-Man: Brand New Day' No. 1 $109M WW, 'Insidious' Franchise Rises To $800M WW - Global Box Office | https://deadline.com/2026/08/global-box-office-spider-man-brand-new-day-insidious-6-1237048315/
2026-08-24 | Global | Arkeonews | Seal of One of Byzantium's Most Powerful Women, Empress Irene, Found at Perperikon with Rare Christ Image | https://arkeonews.net/seal-of-one-of-byzantiums-most-powerful-women-empress-irene-found-at-perperikon-with-rare-christ-image/
2026-08-24 | Global | Arkeonews | 1,700-Year-Old Chinese Armor Still Shines Thanks to an Ancient Metalworking Secret | https://arkeonews.net/1700-year-old-chinese-armor-still-shines-thanks-to-an-ancient-metalworking-secret/
2026-08-24 | Global | HeritageDaily | Two Bronze Age foals found buried beside an ancient burial mound | https://www.heritagedaily.com/2026/08/two-bronze-age-foals-found-buried-beside-an-ancient-burial-mound/159038
2026-08-24 | Global | ArchDaily | The Public Kitchen: How Asian Markets Turn Eating Into Civic Life | https://www.archdaily.com/1183562/the-public-kitchen-how-asian-markets-turn-eating-into-civic-life
2026-08-24 | Global | Dezeen | Rough drystone walls frame sunken home on Greek island by Alexandre Pavlidis | https://www.dezeen.com/2026/08/23/within-the-earth-alexandre-pavlidis/
2026-08-25 | Saudi Arabia/Regional | Masrawy | Saudi actor Ibrahim Al-Hasawi to be honoured at Egypt's VS-FILM short-film festival | https://www.masrawy.com/arts/zoom/details/2026/8/24/3037831/
2026-08-25 | Negative Articles | Euronews | Houthis claim strike on Saudi tanker in latest Red Sea escalation | https://www.euronews.com/2026/08/24/houthis-claim-strike-on-saudi-tanker-in-latest-red-sea-escalation
2026-08-25 | Global | Arkeonews | 3,400-Year-Old Monumental Hittite Building at Sapinuwa Reveals Clues to Ancient Rituals | https://arkeonews.net/3400-year-old-monumental-hittite-building-at-sapinuwa-reveals-clues-to-ancient-rituals/
2026-08-25 | Global | Arkeonews | Object Mistaken for an Animal-Tooth Bead Turns Out to Be a 6,500-Year-Old Human Tooth Pendant | https://arkeonews.net/object-mistaken-for-an-animal-tooth-bead-turns-out-to-be-a-6500-year-old-human-tooth-pendant/
2026-08-25 | Global | Arkeonews | Archaeologists Unearth a Medieval Village That Was Abandoned Without Fire or Destruction | https://arkeonews.net/archaeologists-unearth-a-medieval-village-that-was-abandoned-without-fire-or-destruction/
2026-08-25 | Global | Archaeology Magazine | Neolithic Monument Unearthed in Czech Republic | https://archaeology.org/news/2026/08/24/neolithic-monument-unearthed-in-czech-republic/
2026-08-25 | Global | NL Times | Museum robberies are becoming increasingly violent, Europol warns | https://nltimes.nl/2026/08/24/museum-robberies-becoming-increasingly-violent-europol-warns
2026-08-25 | Global | Hyperallergic | Sliman Mansour, Painter of Palestinian Hope and Humanity, Dies at 79 | https://hyperallergic.com/sliman-mansour-painter-of-palestinian-hope-and-humanity-dies-at-79/
2026-08-25 | Global | ArchDaily | Oslo Architecture Triennale 2026 Announces Programme for 9th Edition Under 'What if Nature Comes First?' | https://www.archdaily.com/1183847/oslo-architecture-triennale-2026-announces-programme-for-9th-edition-under-what-if-nature-comes-first
2026-08-25 | Global | Dezeen | Shigeru Ban unveils Pasona Natureverse Retreat on Awaji Island | https://www.dezeen.com/2026/08/24/shigeru-ban-hotel-pasona-awaji-island/
