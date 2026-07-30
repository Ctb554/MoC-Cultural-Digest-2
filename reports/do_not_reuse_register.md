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

2026-07-30 | Saudi Arabia/Regional | The New York Times | Saudi Arabia's Strikes in Iraq Mark Entry Into U.S.-Iran War | https://www.nytimes.com/2026/07/29/world/middleeast/saudi-arabia-us-iran-war.html
2026-07-30 | Saudi Arabia/Regional | The Guardian | US-Saudi strikes in Iraq push region into 'uncharted territory', analysts warn | https://www.theguardian.com/world/2026/jul/29/us-saudi-strikes-in-iraq-have-pushed-the-region-into-uncharted-territory-analysts-warn
2026-07-30 | Saudi Arabia/Regional | CNBC | Oil jumps as U.S.-Iran resume strikes after a brief pause | https://www.cnbc.com/2026/07/29/oil-prices-today-brent-wti-iran-us-hormuz.html
2026-07-30 | Saudi Arabia/Regional | Middle East Eye | Saudi Arabia seeks international coalition to protect Red Sea shipping from Houthis, two sources say | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-seeks-international-coalition-protect-red-sea-shipping
2026-07-30 | Negative Articles | Al Jazeera | Iraq calls Saudi-US attacks a 'flagrant violation of sovereignty' | https://www.aljazeera.com/news/2026/7/29/iraq-calls-saudi-us-attacks-flagrant-violation-of-sovereignty
2026-07-30 | Global | The Art Newspaper | Betye Saar, assemblage artist who reframed racist and sexist imagery, has died, aged 99 | https://www.theartnewspaper.com/2026/07/29/betye-saar-obituary-legendary-los-angeles-assemblage-artist
2026-07-30 | Global | The Art Newspaper | Sites in Iran, Lebanon and Palestine among 25 new additions to Unesco's World Heritage List | https://www.theartnewspaper.com/2026/07/29/sites-in-iran-lebanon-and-palestine-among-25-new-additions-to-unescos-world-heritage-list
2026-07-30 | Global | The Art Newspaper | English Heritage debuts daily prize draw for 'private time' at Stonehenge this August | https://www.theartnewspaper.com/2026/07/29/english-heritage-debuts-daily-prize-draw-for-private-time-at-stonehenge-this-august
2026-07-30 | Global | Arkeonews | Archaeologists Unearth Two Miniature Mammoth Ivory Birds Carved 40,000 Years Ago | https://arkeonews.net/archaeologists-unearth-two-miniature-mammoth-ivory-birds-carved-40000-years-ago/
2026-07-30 | Global | Arkeonews | Iberian Warrior Family Buried 2,200 Years Ago with Falcatas and a Tanit Burner Discovered in Alicante | https://arkeonews.net/iberian-warrior-family-buried-2200-years-ago-with-falcatas-and-a-tanit-burner-discovered-in-alicante/
2026-07-30 | Global | The Art Newspaper | Arts groups in US cities that increased culture funding during Covid have rebounded more quickly: report | https://www.theartnewspaper.com/2026/07/29/municipal-arts-funding-covid-rebound-dataarts-southern-methodist-university-study
2026-07-30 | Global | The Irish Times | Glen Hansard died in single-vehicle crash in Dublin shortly before 4.30am | https://www.irishtimes.com/culture/music/2026/07/29/glen-hansard-dies-in-dublin-motorbike-crash/
