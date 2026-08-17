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
2026-08-17 | Saudi Arabia/Regional | CP24 | Trump welcomes defence pact between Saudi Arabia, Turkiye and Pakistan | https://www.cp24.com/news/world/2026/08/16/trump-welcomes-defence-pact-between-saudi-arabia-turkiye-and-pakistan/
2026-08-17 | Saudi Arabia/Regional | Deutsche Welle | UAE, Saudi Arabia, others condemn Israel's rejection of Trump Gaza plan | https://www.dw.com/en/uae-saudi-arabia-others-condemn-israels-rejection-of-trump-gaza-plan/a-78389399
2026-08-17 | Negative Articles | Press TV | Yemen warns Saudi territory, interests will not be spared if war escalates | https://www.presstv.co.uk/Detail/2026/08/16/774481/Yemen-senior-official-warns-Saudi-Arabia-territory-interests-face-consequences-conflict-continues
2026-08-17 | Global | Arkeonews | 1,600-Year-Old Early Christian Mosaics Discovered in Croatia with a 'Great Sinners' Inscription | https://arkeonews.net/1600-year-old-early-christian-mosaics-discovered-in-croatia-with-a-great-sinners-inscription/
2026-08-17 | Global | Arkeonews | Ramesses II Lintel Discovered on Egypt's Ancient Road to Canaan May Point to Lost Mesen | https://arkeonews.net/ramesses-ii-lintel-discovered-on-egypts-ancient-road-to-canaan-may-point-to-lost-mesen/
2026-08-17 | Global | Arkeonews | 1,500-Year-Old 'Golden Shoes' Found in Elite Woman's Grave Near Ancient Caspian Trade Hub | https://arkeonews.net/1500-year-old-golden-shoes-found-in-elite-womans-grave-near-ancient-caspian-trade-hub/
