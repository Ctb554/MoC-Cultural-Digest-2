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
2026-09-15 | Saudi Arabia/Regional | Arkeonews | 1,300-Year-Old Mosque with Early Islamic Inscriptions Unearthed in Saudi Arabia | https://arkeonews.net/1300-year-old-mosque-with-early-islamic-inscriptions-unearthed-in-saudi-arabia/
2026-09-15 | Negative Articles | The Guardian | Houthis seize strategic Red Sea islands as analysts warn of impending oil crunch | https://www.theguardian.com/world/2026/sep/15/houthi-rebels-seize-red-sea-hanish-islands-saudi-oil-warning
2026-09-15 | Negative Articles | The National | Oil nears $110 as Saudi pipeline shutdown deepens supply fears | https://www.thenationalnews.com/business/energy/2026/09/14/oil-nears-108-after-saudi-arabia-shuts-pipeline-amid-attacks/
2026-09-15 | Negative Articles | Foreign Policy | Houthi Strikes on Saudi Arabia Upset Planned Talks With Iran | https://foreignpolicy.com/2026/09/14/houthi-strikes-yemen-red-sea-saudi-arabia-iran-east-west-oil-pipeline/
2026-09-15 | Negative Articles | Al Jazeera | Yemen forces advance in Taiz; Houthis take key islands, attack Saudi Arabia | https://www.aljazeera.com/news/2026/9/14/yemen-govt-forces-advance-in-taiz-as-houthis-claim-attack-on-saudi-arabia
2026-09-15 | Negative Articles | Human Rights Watch | Yemen: New Attacks by Houthi Include Likely War Crimes | https://www.hrw.org/news/2026/09/15/yemen-new-attacks-by-houthi-include-likely-war-crimes
2026-09-15 | Negative Articles | Eurasia Review | How Cascading Crises Are Testing Saudi Arabia's Foundations - OpEd | https://www.eurasiareview.com/15092026-how-cascading-crises-are-testing-saudi-arabias-foundations-oped/
2026-09-15 | Global | Blooloop | teamLab reveals plans for new attraction in Tokyo's Ariake district | https://blooloop.com/news/teamlab-new-exhibition-tokyo-ariake
2026-09-15 | Global | Blooloop | Manchester Museum removes mummy from display to respect wishes of the dead | https://blooloop.com/news/manchester-museum-mummy-removed-display
2026-09-15 | Global | Archaeology Magazine | Denisovan Fossils and Possible Tools Uncovered in China | https://archaeology.org/news/2026/09/14/denisovan-fossils-and-possible-tools-uncovered-in-china/
2026-09-15 | Global | Arkeonews | Who Was the Mysterious Gallic Warrior Buried in Britain with a Unique 2,000-Year-Old Helmet | https://arkeonews.net/who-was-the-mysterious-gallic-warrior-buried-in-britain-with-a-unique-2000-year-old-helmet/
2026-09-15 | Global | Deadline | Box Office: Practical Magic 2 Opens To $46M Global Box Office | https://deadline.com/2026/09/box-office-practical-magic-2-global-1237100627/
2026-09-15 | Global | WWD | Magda Butrym Spring 2027 Ready-to-Wear | https://wwd.com/runway/spring-2027/new-york/magda-butrym/review/
2026-09-15 | Global | ArchDaily | SAGA Space Architects and 3DCP Group Complete 36-Unit 3D-Printed Student Village in Denmark | https://www.archdaily.com/1185029/saga-space-architects-and-3dcp-group-complete-36-unit-3d-printed-student-village-in-denmark
2026-09-15 | Global | The Colorado Sun | Denver restaurant snags coveted Michelin recognition | https://coloradosun.com/2026/09/14/one-michelin-star-for-colorado-restaurants/
2026-09-15 | Global | Publishers Weekly | Book Deals: Week of September 14, 2026 | https://www.publishersweekly.com/pw/by-topic/industry-news/book-deals/article/101220-book-deals-week-of-september-14-2026.html
