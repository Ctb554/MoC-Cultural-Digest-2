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
2026-08-24 | Saudi Arabia/Regional | The National | Gulf dreams and Palestinian portraits: Vantage Point Sharjah turns lens on intimate lives | https://www.thenationalnews.com/arts-culture/art-design/2026/08/24/vantage-point-sharjah-2026/
2026-08-24 | Saudi Arabia/Regional | The National | UAE art guide: 12 exhibitions to see, from Spectrum at Manarat Al Saadiyat to orange art at Ayyam Gallery | https://www.thenationalnews.com/arts-culture/art-design/2026/08/23/uae-guide-museum-gallery-exhibitions-to-see-abu-dhabi-dubai/
2026-08-24 | Negative Articles | Bloomberg | Saudi Oil Logistics Roiled Again by Houthis' Red Sea Threat | https://www.bloomberg.com/news/articles/2026-08-23/saudis-oil-logistics-roiled-again-by-houthis-red-sea-threat
2026-08-24 | Global | Deadline | 'Spider-Man: Brand New Day' No. 1 $109M WW, 'Insidious' Franchise Rises To $800M WW - Global Box Office | https://deadline.com/2026/08/global-box-office-spider-man-brand-new-day-insidious-6-1237048315/
2026-08-24 | Global | Arkeonews | Seal of One of Byzantium's Most Powerful Women, Empress Irene, Found at Perperikon with Rare Christ Image | https://arkeonews.net/seal-of-one-of-byzantiums-most-powerful-women-empress-irene-found-at-perperikon-with-rare-christ-image/
2026-08-24 | Global | Arkeonews | 1,700-Year-Old Chinese Armor Still Shines Thanks to an Ancient Metalworking Secret | https://arkeonews.net/1700-year-old-chinese-armor-still-shines-thanks-to-an-ancient-metalworking-secret/
2026-08-24 | Global | HeritageDaily | Two Bronze Age foals found buried beside an ancient burial mound | https://www.heritagedaily.com/2026/08/two-bronze-age-foals-found-buried-beside-an-ancient-burial-mound/159038
2026-08-24 | Global | ArchDaily | The Public Kitchen: How Asian Markets Turn Eating Into Civic Life | https://www.archdaily.com/1183562/the-public-kitchen-how-asian-markets-turn-eating-into-civic-life
2026-08-24 | Global | Dezeen | Rough drystone walls frame sunken home on Greek island by Alexandre Pavlidis | https://www.dezeen.com/2026/08/23/within-the-earth-alexandre-pavlidis/
