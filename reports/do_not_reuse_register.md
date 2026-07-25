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
2026-07-25 | Saudi Arabia/Regional | The National | Saudi strike targets Yemen's Hodeidah after attack on vessel | https://www.thenationalnews.com/news/2026/07/24/houthi-official-says-saudi-strike-targets-hodeidah-port-after-attack-on-saudi-vessel/
2026-07-25 | Saudi Arabia/Regional | Bloomberg | Oil Tankers Run the Houthi Gauntlet to Keep Saudi Exports Flowing | https://www.bloomberg.com/news/newsletters/2026-07-24/oil-tankers-run-the-houthi-gauntlet-to-keep-saudi-exports-flowing
2026-07-25 | Saudi Arabia/Regional | RTÉ | Houthi rebels claim fresh missile strikes on southern Saudi Arabia | https://www.rte.ie/news/2026/0725/1585036-houthis-strikes/
2026-07-25 | Negative Articles | The A.V. Club | "Principled Al" Yankovic turned down seven-figure offer to perform at Riyadh Comedy Festival | https://www.avclub.com/weird-al-yankovic-riyadh-comedy-festival
2026-07-25 | Negative Articles | Middle East Eye | Houthis say Saudi attack on Hodeidah will lead to 'escalation for escalation' | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-attack-hodeidah-will-lead-escalation-escalation
2026-07-25 | Global | The Art Newspaper | Unesco adds ancient Greek city Tauric Chersonese in Crimea to World Heritage in Danger list | https://www.theartnewspaper.com/2026/07/24/unesco-adds-ancient-greek-city-tauric-chersonese-in-crimea-to-world-heritage-in-danger-list
2026-07-25 | Global | Arkeonews | Byzantine Shipwreck Off Croatia Yields Record Gold Treasure and an Emperor's Ring | https://arkeonews.net/byzantine-shipwreck-off-croatia-yields-record-gold-treasure-and-an-emperors-ring/
2026-07-25 | Global | Arkeonews | 4,500-Year-Old Mega-Dams Near Egypt's Red Pyramid May Reveal an Ancient Engineering Breakthrough | https://arkeonews.net/4500-year-old-mega-dams-near-egypts-red-pyramid-may-reveal-an-ancient-engineering-breakthrough/
2026-07-25 | Global | Arkeonews | Two Premature Infants, Possibly Twins, Found Buried in an Abandoned Roman Latrine at Ephesus | https://arkeonews.net/two-premature-infants-possibly-twins-found-buried-in-an-abandoned-roman-latrine-at-ephesus/
2026-07-25 | Global | Arkeonews | Turkic-Period Tomb in Mongolia Yields 1,400-Year-Old Peach Wood Bow and Runic-Inscribed Horse-Head Fiddle | https://arkeonews.net/turkic-period-tomb-in-mongolia-yields-1400-year-old-peach-wood-bow-and-runic-inscribed-horse-head-fiddle/
2026-07-25 | Global | The Art Newspaper | Viking centre that loaned ship for 'The Odyssey' says that it has not been compensated by Universal for repairs | https://www.theartnewspaper.com/2026/07/24/swedish-viking-centre-that-loaned-ship-for-the-odyssey-alleges-that-it-has-not-been-paid-for-damages
2026-07-25 | Global | The Art Newspaper | Buffalo AKG Art Museum will split leadership duties in two and promote internally for new directors | https://www.theartnewspaper.com/2026/07/24/buffalo-akg-art-museum-two-director-roles-promotions
2026-07-25 | Global | The Art Newspaper | Artists' monumental hot dog sculpture, now with patriotic toppings, returns to Times Square | https://www.theartnewspaper.com/2026/07/24/jen-catron-paul-outlaw-times-square-hot-dog-returns
