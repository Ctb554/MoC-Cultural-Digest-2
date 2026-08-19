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
2026-08-19 | Saudi Arabia/Regional | CairoScene | Riyadh Art Brings 75 Permanent Public Artworks Across the City | https://cairoscene.com/ArtsAndCulture/Riyadh-Art-Brings-75-Permanent-Public-Artworks-Across-the-City
2026-08-19 | Saudi Arabia/Regional | ArchDaily | From Tent to Terminal: Bedouin Craft in Contemporary Infrastructure | https://www.archdaily.com/1183404/from-tent-to-terminal-bedouin-craft-in-contemporary-infrastructure
2026-08-19 | Global | Archaeology Magazine | Mysterious Runestone Found in Floor of Faroe Islands Chapel | https://archaeology.org/news/2026/08/18/mysterious-runestone-found-embedded-in-floor-of-faroe-islands-chapel/
2026-08-19 | Global | Archaeology Magazine | Crucibles Contain Earliest Evidence of Brass Production in East Asia | https://archaeology.org/news/2026/08/18/crucibles-contain-earliest-evidence-of-brass-production-in-east-asia/
2026-08-19 | Global | Archaeology Magazine | Denisovans Were Much Taller Than Previously Thought | https://archaeology.org/news/2026/08/18/denisovans-were-much-taller-than-previously-thought/
2026-08-19 | Global | Arkeonews | Rare 4,000-Year-Old 'Enigmatic Tablet' Found Intact at Lucone Bronze Age Village in Italy | https://arkeonews.net/rare-4000-year-old-enigmatic-tablet-found-intact-at-lucone-bronze-age-village-in-italy/
2026-08-19 | Global | Arkeonews | 1,000-Year-Old Luxury Bowls in the Sudanese Desert Hide an 8-Nanometer Secret | https://arkeonews.net/1000-year-old-luxury-bowls-in-the-sudanese-desert-hide-an-8-nanometer-secret/
2026-08-19 | Global | Forbes | Venice Film Festival Lineup Comes Into Focus | https://www.forbes.com/sites/dbloom/2026/08/18/venice-film-festival-lineup-comes-into-focus/
2026-08-19 | Risks and Opportunities | New York Times | Gulf Oil Giants Push to Expand Overseas Stockpiles as Iran War Drags On | https://www.nytimes.com/2026/08/18/business/saudi-uae-japan-oil-storage.html
2026-08-19 | Risks and Opportunities | The Business of Fashion | Red Sea Attacks Renew Risks to Fashion Supply Chains | https://www.businessoffashion.com/articles/global-markets/worldview-red-sea-attacks-renew-risks-to-supply-chains/
