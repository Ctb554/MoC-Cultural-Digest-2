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
2026-08-18 | Risks and Opportunities | Türkiye Today | Houthis claim strike on Saudi military vessel, 4 boats in Red Sea | https://www.turkiyetoday.com/region/houthis-claim-strike-on-saudi-military-vessel-4-boats-in-red-sea-3226269
