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
2026-08-23 | Saudi Arabia/Regional | Travel And Tour World | France Accelerates Luxury Tourism Growth With Macron-Mohammed bin Salman Strategic Partnership | https://www.travelandtourworld.com/news/article/dllp5veduy0a/
2026-08-23 | Global | Arkeonews | 4,300-Year-Old Tomb in Inner Mongolia Reveals Earliest Known Dragon-Phoenix Pairing in Northern China | https://arkeonews.net/4300-year-old-tomb-in-inner-mongolia-reveals-earliest-known-dragon-phoenix-pairing-in-northern-china/
2026-08-23 | Global | Arkeonews | Roman Mass Grave Beneath Vienna Soccer Field Reveals Unusual Concentration of Pelvic Wounds | https://arkeonews.net/roman-mass-grave-beneath-vienna-soccer-field-reveals-unusual-concentration-of-pelvic-wounds/
2026-08-23 | Global | Arkeonews | One of Byzantium's Most Striking Images of Mary's "Last Sleep" Survives on a Mosque Wall in Istanbul | https://arkeonews.net/one-of-byzantiums-most-striking-images-of-marys-last-sleep-survives-on-a-mosque-wall-in-istanbul/
2026-08-23 | Global | Arkeonews | 1,700-Year-Old Chinese Armor Still Shines Thanks to an Ancient Metalworking Secret | https://arkeonews.net/1700-year-old-chinese-armor-still-shines-thanks-to-an-ancient-metalworking-secret/
2026-08-23 | Global | ArchDaily | Antiquity exhibition at Wawel castle / NArchitekTURA | https://www.archdaily.com/1183570/antiquity-exhibition-at-wawel-castle-narchitektura
2026-08-23 | Global | Dezeen | Estúdio Campana creates 'woven jewellery box' for Tiffany & Co in São Paulo | https://www.dezeen.com/2026/08/22/tiffany-co-pop-up-jk-iguatemi-mall-sao-paulo-estudio-campana/
2026-08-23 | Global | Dezeen | 'Light and sea breeze shape the viewing' of exhibits at open-air art gallery in Mexico | https://www.dezeen.com/2026/08/22/arte-abierto-baja-sordo-madaleno-arquitectos/
2026-08-23 | Global | Dezeen | KTGY revamps interiors of Fairmont Hotel in Chicago | https://www.dezeen.com/2026/08/23/ktgy-revamps-interiors-fairmont-hotel-chicago/
2026-08-23 | Global | ArchDaily | What is Blue Infrastructure? Rethinking Water's Role in City Design | https://www.archdaily.com/1182257/what-is-blue-infrastructure-rethinking-waters-role-in-city-design
2026-08-23 | Risks and Opportunities | The National | Saudi Crown Prince visits France to sign deals and discuss Strait of Hormuz | https://www.thenationalnews.com/news/mena/2026/08/22/saudi-crown-prince-visits-france-to-sign-deals-and-discuss-strait-of-hormuz/
