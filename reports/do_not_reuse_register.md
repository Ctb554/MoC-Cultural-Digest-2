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
2026-07-21 | Saudi Arabia/Regional | Bloomberg | Saudi-Led Coalition in Yemen Vows to Protect Ships From Houthis | https://www.bloomberg.com/news/articles/2026-07-20/yemen-s-houthis-vow-to-impose-maritime-blockade-on-saudi-arabia
2026-07-21 | Saudi Arabia/Regional | CNBC | Iran's Houthi allies declare maritime embargo against Saudi Arabia, escalating threat to oil market | https://www.cnbc.com/2026/07/20/iran-houthi-yemen-saudi-arabia.html
2026-07-21 | Negative Articles | Al Jazeera | Yemen's Houthis declare naval blockade of Saudi Arabia: What to know | https://www.aljazeera.com/news/2026/7/20/yemens-houthis-declare-naval-blockade-of-saudi-arabia-what-to-know
2026-07-21 | Negative Articles | The Spokesman-Review | Houthis announce Saudi naval blockade, threatening new front in US-Iran war | https://www.spokesman.com/stories/2026/jul/19/houthis-announce-saudi-naval-blockade-threatening-/
2026-07-21 | Global | The Art Newspaper | The Armory Show reveals 230-gallery line-up and move to late September | https://www.theartnewspaper.com/2026/07/20/armory-show-unveils-230-gallery-line-up-after-moving-fair-to-late-september
2026-07-21 | Global | Hyperallergic | Cuban Artist Luis Manuel Otero Alcántara Exiled to the US | https://hyperallergic.com/cuban-artist-luis-manuel-otero-alcantara-exiled-to-the-us/
2026-07-21 | Global | Archaeology Magazine | 2,700-Year-Old Irrigation System Studied in Armenia | https://archaeology.org/news/2026/07/20/2700-year-old-irrigation-system-studied-in-armenia/
2026-07-21 | Global | Hyperallergic | Activists Sue to Stop Frida Kahlo Works From Leaving Mexico | https://hyperallergic.com/activists-sue-to-stop-frida-kahlo-works-from-leaving-mexico/
2026-07-21 | Global | Blooloop | Kynren opens new daytime theme park, The Storied Lands | https://blooloop.com/news/kynren-storied-lands-open
2026-07-21 | Global | Hyperallergic | New Museum's Shiny New Building Leaks During Flash Floods | https://hyperallergic.com/new-museums-shiny-new-building-leaks-during-flash-floods/
2026-07-21 | Global | ArchDaily | The Architecture of the FIFA World Cup: Looking Back at 2026 and Ahead to 2030 | https://www.archdaily.com/1181248/the-architecture-of-the-fifa-world-cup-looking-back-at-2026-and-ahead-to-2030
2026-07-21 | Global | Deadline | Toronto Film Festival Unveils First 2026 Lineups | https://deadline.com/2026/07/toronto-film-festival-2026-line-up-1236998190/
2026-07-21 | Risks and Opportunities | Foreign Policy | Iran-Backed Houthis Declare Naval Blockade on Saudi Arabia | https://foreignpolicy.com/2026/07/20/houthi-blockade-saudi-iran-war-red-sea-gulf-aden-hormuz/
