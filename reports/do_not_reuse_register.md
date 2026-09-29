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
2026-09-29 | Saudi Arabia/Regional | Arabisk London | Red Sea Foundation in Toronto (TIFF): 8 Films Beyond the Screen | https://www.arabisklondon.com/red-sea-foundation-in-toronto-tiff-8-films-beyond-the-screen
2026-09-29 | Saudi Arabia/Regional | Today's Traveller | Oberoi Hotels & Resorts presents a first glimpse of The Oberoi Sukoonvilas, Wadi Safar | https://www.todaystraveller.net/oberoi-hotels-the-oberoi-sukoonvilas/
2026-09-29 | Saudi Arabia/Regional | The National | Frieze Abu Dhabi unveils inaugural programme led by award-winner Dala Nasser | https://www.thenationalnews.com/arts-culture/art-design/2026/09/28/frieze-abu-dhabi-unveils-inaugural-programme-led-by-award-winner-dala-nasser/
2026-09-29 | Negative Articles | The New York Times | Over 800 Killed in Renewed Houthi-Saudi War in Yemen, W.H.O. Says | https://www.nytimes.com/2026/09/28/world/middleeast/yemen-war-800-dead.html
2026-09-29 | Negative Articles | The Nation | Houthis claim Saudi strikes on Yemen's Taiz leave dozens dead | https://www.nation.com.pk/28-Sep-2026/houthis-claim-saudi-strikes-yemen-s-taiz-leave-dozens-dead
2026-09-29 | Global | The Art Newspaper | Buyer of mysterious $9m Rembrandt painting revealed | https://www.theartnewspaper.com/2026/09/28/rembrandt-painting-buyer-revealed-leiden-collection-thomas-kaplan
2026-09-29 | Global | The Art Newspaper | Trump's Greenland threats become playable arcade game in satiric collective's latest public art intervention | https://www.theartnewspaper.com/2026/09/28/secret-handshake-trump-greenland-threats-arcade-game-washington-dc
2026-09-29 | Global | The Art Newspaper | Culture secretary confirms free admission for all at England's national museums will remain | https://www.theartnewspaper.com/2026/09/28/free-admission-nationla-museums-england-lisa-nandy-confirmed
2026-09-29 | Global | Arkeonews | Assyria's Lost Queens Were Buried With a Great Gold Treasure to Rival Tutankhamun | https://arkeonews.net/assyrias-lost-queens-were-buried-with-a-great-gold-treasure-to-rival-tutankhamun/
2026-09-29 | Global | Archaeology Magazine | Clinker Ship Found in Germany's Bay of Greifswald | https://archaeology.org/news/2026/09/28/clinker-ship-found-in-germanys-bay-of-greifswald/
2026-09-29 | Global | Archaeology Magazine | Young People Were on the Move in Bronze Age Greece | https://archaeology.org/news/2026/09/28/young-people-were-on-the-move-in-bronze-age-greece/
2026-09-29 | Global | The Stage | Rachel Zegler to return to West End with first concert residency | https://www.thestage.co.uk/news/rachel-zegler-announces-west-end-return-with-first-concert-residency
2026-09-29 | Global | Dezeen | Farshid Moussavi wins 2026 Soane Medal for architecture | https://www.dezeen.com/2026/09/28/farshid-moussavi-2026-soane-medal/
