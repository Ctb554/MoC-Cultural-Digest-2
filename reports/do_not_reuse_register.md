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
2026-08-18 | Saudi Arabia/Regional | The New York Times | Houthis Claim Strike on Saudi Vessel as Red Sea Violence Escalates | https://www.nytimes.com/2026/08/17/world/middleeast/houthis-saudi-strike.html
2026-08-18 | Saudi Arabia/Regional | Bloomberg | Asian Refiners Ask to Pick Up Saudi Oil Outside Risky Red Sea | https://www.bloomberg.com/news/articles/2026-08-17/asian-refiners-ask-to-pick-up-saudi-oil-outside-risky-red-sea
2026-08-18 | Saudi Arabia/Regional | Bloomberg | Saudis Offer to Sell Oil Near Oman, a Possible Sign They're Sailing Dark Through Hormuz | https://www.bloomberg.com/news/articles/2026-08-17/saudis-offer-oil-from-near-oman-in-possible-sign-of-shuttling
2026-08-18 | Global | Arkeonews | Rare 4,000-Year-Old 'Enigmatic Tablet' Found Intact at Lucone Bronze Age Village in Italy | https://arkeonews.net/rare-4000-year-old-enigmatic-tablet-found-intact-at-lucone-bronze-age-village-in-italy/
2026-08-18 | Global | Archaeology Magazine | Possible Bronze Age Grave Unearthed Beneath Viking Ship Burial | https://archaeology.org/news/2026/08/17/possible-bronze-age-grave-discovered-beneath-viking-ship-burial/
2026-08-18 | Global | Arkeonews | 1,600-Year-Old Early Christian Mosaics Discovered in Croatia with a 'Great Sinners' Inscription | https://arkeonews.net/1600-year-old-early-christian-mosaics-discovered-in-croatia-with-a-great-sinners-inscription/
2026-08-18 | Global | Archaeology Magazine | Ceremonial Poles Returned to Canadian Village Site | https://archaeology.org/news/2026/08/17/ceremonial-poles-returned-to-canadian-village-site/
2026-08-18 | Global | Arkeonews | Rare Tagar Horse Engravings Discovered in an Early Iron Age Burial Mound in Khakassia | https://arkeonews.net/rare-tagar-horse-engravings-discovered-in-an-early-iron-age-burial-mound-in-khakassia/
2026-08-18 | Global | Blooloop | Breeze Creative partners with ICR Discovery Center to create immersive, hands-on experiences | https://blooloop.com/breeze-creative-icr-discovery-center/
2026-08-18 | Global | Blooloop | facts and fiction to design two pavilions for Expo 2027 Belgrade | https://blooloop.com/facts-fiction-expo-2027-belgrade/
2026-08-18 | Global | ArtAsiaPacific | Jitish Kallat commissioned for the Menil Drawing Institute's Wall Drawing Series | https://www.artasiapacific.com/news/weekly-news-roundup-august-17-2026/
