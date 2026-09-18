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

2026-09-18 | Saudi Arabia/Regional | ArtReview | Islamic Arts Biennale 2027 names lead curators | https://artreview.com/islamic-arts-biennale-2027-names-lead-curators/
2026-09-18 | Saudi Arabia/Regional | TIME | Dana Awartani Is on the 2026 TIME100 Art List | https://time.com/collection/time100-art/2026/dana-awartani/
2026-09-18 | Saudi Arabia/Regional | MDNtv | Saudi Film Nights Makes Historic South African Debut This October | https://mdntvlive.com/saudi-film-nights-makes-historic-south-african-debut-this-october/
2026-09-18 | Saudi Arabia/Regional | Deadline | Dubai International Film Festival To Return In December 2027 As 2026 Edition Of Saudi Arabia's Red Sea Film Festival Looks Uncertain | https://deadline.com/2026/09/dubai-film-festival-return-saudi-red-sea-film-uncertain-1237106423/
2026-09-18 | Negative Articles | Al Jazeera | Trump administration approves sale of F-35 jets to Saudi Arabia | https://www.aljazeera.com/news/2026/9/17/trump-administration-approves-sale-of-f-35-jets-to-saudi-arabia
2026-09-18 | Negative Articles | Al Jazeera | Five killed as Saudi Arabia and Yemen's Houthis trade attacks | https://www.aljazeera.com/news/2026/9/17/five-killed-as-saudi-arabia-and-yemens-houthis-trade-attacks
2026-09-18 | Negative Articles | CNBC | Oil prices fall as Saudi Arabia reportedly offers more crude via Hormuz after pipeline attack | https://www.cnbc.com/2026/09/17/oil-prices-today-wti-brent-hormuz-iran-war.html
2026-09-18 | Negative Articles | Semafor | Saudi Arabia's well-timed uranium find near Medina | https://www.semafor.com/article/09/17/2026/saudi-arabias-well-timed-uranium-find-near-medina
2026-09-18 | Global | Washingtonian | Michelin Adds 4 New Restaurants to Its DC Guide | https://washingtonian.com/2026/09/17/michelin-adds-4-new-restaurants-to-its-dc-guide/
2026-09-18 | Global | Dezeen | Ma Yansong and Daniel Libeskind join Dezeen Awards master jury | https://www.dezeen.com/2026/09/17/dezeen-awards-2026-master-jury/
2026-09-18 | Global | WhoWhatWear | Live From London Fashion Week SS27 | https://www.whowhatwear.com/fashion/live/london-fashion-week-spring-summer-2027
2026-09-18 | Global | Arkeonews | New Laser Scans Reveal Six Groups of Ancient Ships on a 3000-Year-Old Wall in Cyprus | https://arkeonews.net/new-laser-scans-reveal-six-groups-of-ancient-ships-on-a-3000-year-old-wall-in-cyprus/
2026-09-18 | Global | Arkeonews | Rare 2000-Year-Old Celtic Silver Hoard Found Beneath a Former Sports Field | https://arkeonews.net/rare-2000-year-old-celtic-silver-hoard-found-beneath-a-former-sports-field/
