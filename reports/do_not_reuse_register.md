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
2026-08-05 | Saudi Arabia/Regional | Semafor | Aramco profit rises 33% on higher oil prices | https://www.semafor.com/article/08/04/2026/aramco-profit-rises-33-on-higher-oil-prices
2026-08-05 | Saudi Arabia/Regional | AGBI | Aramco profits surge in face of mounting risks to exports | https://www.agbi.com/analysis/oil-and-gas/2026/08/aramco-profits-surge-in-face-of-mounting-risks-to-exports/
2026-08-05 | Saudi Arabia/Regional | AGBI | Saudi Arabia sustains non-oil growth and Kuwait rebounds | https://www.agbi.com/economy/2026/08/saudi-arabia-sustains-non-oil-growth-and-kuwait-rebounds/
2026-08-05 | Saudi Arabia/Regional | Gulf Insider | Saudi Arabia adds 1,173 archaeological sites to National Register | https://www.gulf-insider.com/saudi-arabia-adds-1173-archaeological-sites-to-national-register/
2026-08-05 | Negative Articles | The Guardian | Elon Musk's X latest to block Saudi dissident accounts inside kingdom | https://www.theguardian.com/technology/2026/aug/04/x-twitter-blocks-dissident-accounts-saudi-arabia
2026-08-05 | Global | The Art Newspaper | The Australian Museum returns remains of Rapa Nui ancestors to Easter Island | https://www.theartnewspaper.com/2026/08/04/australian-museum-repatriates-rapa-nui-remains-easter-island
2026-08-05 | Global | The Art Newspaper | Reconstruction of legendary Sutton Hoo ship takes shape | https://www.theartnewspaper.com/2026/08/04/reconstruction-of-legendary-sutton-hoo-ship-takes-shape
2026-08-05 | Global | Arkeonews | Silenced for 6,000 Years: How a Tiny Stone Seal Resurrected Iran's Oldest Harp | https://arkeonews.net/silenced-for-6000-years-how-a-tiny-stone-seal-resurrected-irans-oldest-harp/
2026-08-05 | Global | Archaeology Magazine | Roman Villa Featured Oldest Known Library in Iberia | https://archaeology.org/news/2026/08/04/roman-villa-featured-oldest-known-library-in-iberia/
2026-08-05 | Global | The Art Newspaper | London mayor Sadiq Khan calls for city's public museums to remain free to enter | https://www.theartnewspaper.com/2026/08/04/london-mayor-sadiq-khan-calls-for-national-museums-to-remain-free-to-enter
2026-08-05 | Global | Blooloop | $203m donation to fund transformation of Brown Museum | https://blooloop.com/203m-donation-brown-museum/
2026-08-05 | Global | The Art Newspaper | Fra Angelico's earliest surviving altarpiece returns to Fiesole after restoration reveals hidden throne | https://www.theartnewspaper.com/2026/08/04/fra-angelicos-earliest-surviving-altarpiece-returns-to-fiesole-after-restoration-reveals-hidden-throne
2026-08-05 | Global | Dezeen | SBP and Snøhetta cantilever bridge across New York gorge | https://www.dezeen.com/2026/08/04/sentry-bridge-watkins-glen-gorge-snohetta-sbp/
2026-08-05 | Global | Time Out | Six new one-Michelin-star restaurants to watch: The Michelin Guide Singapore 2026 | https://www.timeout.com/singapore/news/six-new-one-michelin-star-restaurants-to-watch-the-michelin-guide-singapore-2026-080426
