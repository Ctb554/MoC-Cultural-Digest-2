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

2026-08-07 | Saudi Arabia/Regional | The Guardian | Houthi strikes kill dozens in Yemen, officials say, as Saudi Arabia warns of further attacks | https://www.theguardian.com/world/2026/aug/07/houthi-strikes-yemen-saudi-arabia-attacks-iran-war-middle-east-crisis
2026-08-07 | Saudi Arabia/Regional | Deutsche Welle | Middle East: Houthi attack wounds 11 in Saudi Arabia | https://www.dw.com/en/middle-east-houthi-attack-wounds-11-in-saudi-arabia/live-78272895
2026-08-07 | Saudi Arabia/Regional | Euronews | Saudi Arabia, Turkiye and Pakistan to sign joint defence pact amid regional escalation | https://www.euronews.com/2026/08/07/saudi-arabia-turkiye-and-pakistan-to-sign-joint-defence-pact-amid-regional-escalation
2026-08-07 | Saudi Arabia/Regional | Al Jazeera | Saudi Arabia names commander for maritime defence coalition | https://www.aljazeera.com/news/2026/8/6/saudi-arabia-names-commander-for-maritime-defence-coalition
2026-08-07 | Negative Articles | Al Jazeera | Houthi attacks on Yemeni government forces kill at least 30 | https://www.aljazeera.com/news/2026/8/6/houthis-claim-to-have-killed-45-in-attacks-on-yemeni-government-forces
2026-08-07 | Global | Arkeonews | Hidden for 1,500 Years, a Lavish Roman Imperial Complex Emerges Beneath Rome's Villa Celimontana | https://arkeonews.net/hidden-for-1500-years-a-lavish-roman-imperial-complex-emerges-beneath-romes-villa-celimontana/
2026-08-07 | Global | Archaeology Magazine | Unique Statue Found in Western Turkey | https://archaeology.org/news/2026/08/06/unique-statue-found-in-western-turkey/
2026-08-07 | Global | ARTnews | White Cube Now Represents Tesfaye Urgessa, First Artist to Represent Ethiopia at the Venice Biennale | https://www.artnews.com/art-news/market/white-cube-tesfaye-urgessa-artist-gallery-representation-1234794392/
2026-08-07 | Global | Artnet News | Late Painter Sarah Cunningham Gets First Museum Show—and Other Art World Matters | https://news.artnet.com/artnet-bulletin/sarah-cunningham-aug-6-2026-2793214
2026-08-07 | Global | Deadline | Gareth Edwards Not Returning For Next 'Jurassic World' Movie | https://deadline.com/2026/08/gareth-edwards-next-jurassic-world-movie-1237027995/
2026-08-07 | Global | Deadline | TIFF Midnight Madness Lineup Includes 'Hope' Special Screening & Replay Of Fest Acquisition Hit 'Obsession' | https://deadline.com/2026/08/tiff-midnight-madness-lineup-2026-1237027726/
