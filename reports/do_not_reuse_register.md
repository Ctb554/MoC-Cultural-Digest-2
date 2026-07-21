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
2026-07-21 | Saudi Arabia/Regional | Nikkei Asia | Yemen's Houthis declare naval blockade on Saudi Arabia | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/yemen-s-houthis-declare-naval-blockade-on-saudi-arabia
2026-07-21 | Saudi Arabia/Regional | Al Jazeera | Houthis announce maritime blockade on Saudi Arabia | https://www.aljazeera.com/video/newsfeed/2026/7/20/houthis-announce-maritime-blockade-on-saudi-arabia
2026-07-21 | Global | The Art Newspaper | The Armory Show reveals 230-gallery line-up and move to late September | https://www.theartnewspaper.com/2026/07/20/armory-show-unveils-230-gallery-line-up-after-moving-fair-to-late-september
2026-07-21 | Global | Egypt Independent | Newly discovered Saqqara tombs rewrites history of New Kingdom | https://www.egyptindependent.com/newly-discovered-saqqara-tombs-rewrites-history-of-new-kingdom/
2026-07-21 | Global | HeritageDaily | "Witch's Grave" excavation sheds new light on neolithic monument | https://www.heritagedaily.com/2026/07/witchs-grave-excavation-sheds-new-light-on-neolithic-monument/158555
2026-07-21 | Global | HeritageDaily | Rare archaic necropolis unearthed in southern Italy reveals exceptional ancient treasures | https://www.heritagedaily.com/2026/07/rare-archaic-necropolis-unearthed-in-southern-italy-reveals-exceptional-ancient-treasures/158665
2026-07-21 | Global | Deadline | Toronto Film Festival Unveils First 2026 Lineups | https://deadline.com/2026/07/toronto-film-festival-2026-line-up-1236998190/
