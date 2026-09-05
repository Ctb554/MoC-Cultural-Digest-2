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
2026-09-05 | Saudi Arabia/Regional | Semafor | New museum reflects on Saudi's post-oil future | https://www.semafor.com/article/09/03/2026/new-museum-reflects-on-saudis-post-oil-future
2026-09-05 | Saudi Arabia/Regional | GQ Middle East | Six Arab films are screening at Venice Film Festival | https://www.gqmiddleeast.com/article/six-arab-films-are-screening-at-venice-film-festival
2026-09-05 | Negative Articles | Reuters | US approves potential sale of Joint Direct Attack Munitions-Extend Range to Saudi Arabia for $5 billion | https://www.reuters.com/world/middle-east/us-approves-potential-sale-joint-direct-attack-munitions-extend-range-saudi-2026-09-04/
2026-09-05 | Negative Articles | Business Insider Africa | Saudi Arabia, Oman and Bahrain deport over 336,000 foreign workers in 2026 amid crackdown on Ethiopians, Ugandans and Nigerians | https://africa.businessinsider.com/local/lifestyle/saudi-arabia-oman-and-bahrain-deport-over-336000-foreign-workers-in-2026-amid/4e85825
2026-09-05 | Global | The Art Newspaper | Toledo Museum of Art partners with Ethiopian Heritage Authority to find solutions for 'objects in limbo' | https://www.theartnewspaper.com/2026/09/04/toledo-museum-art-partners-ethiopian-heritage-authority-repatriation-five-artefacts
2026-09-05 | Global | Arkeonews | Assyrian capital Nimrud's 340-hectare lower town is finally coming into view after nearly 180 years | https://arkeonews.net/assyrian-capital-nimruds-340-hectare-lower-town-is-finally-coming-into-view-after-nearly-180-years
2026-09-05 | Global | CNN | 'Biggest surprise of my life': Denmark's largest Viking Age silver hoard discovered in backyard | https://www.cnn.com/2026/09/04/science/denmark-viking-silver-hoard-intl-scli
2026-09-05 | Global | Associated Press | China is boycotting a major Asian art festival over the naming of a Taiwanese exhibition | https://www.greenwichtime.com/entertainment/article/china-is-boycotting-a-major-asian-art-festival-22417416.php
2026-09-05 | Global | The Art Newspaper | 'Putin didn't win; art won': Venice Biennale president defends decision to allow Russia's participation | https://www.theartnewspaper.com/2026/09/04/venice-biennale-president-defends-decision-to-allow-russia-participation
2026-09-05 | Global | ARTnews | The Lucas Museum in Los Angeles doesn't have a narrative | https://www.artnews.com/art-news/reviews/lucas-museum-los-angeles-review-1234796964
2026-09-05 | Global | Business of Fashion | One year after founder's death, Armani faces ticking clock | https://www.businessoffashion.com/news/luxury/one-year-after-founders-death-armani-faces-ticking-clock
2026-09-05 | Global | The Stage | The Story review at the National Theatre | https://www.thestage.co.uk/reviews/the-story-review-olivier-theatre-national-theatre-london-clint-dyer-letitia-wright
2026-09-05 | Global | Variety | 'My Undesirable Friends: Part II – Exile' review | https://variety.com/2026/film/news/my-undesirable-friends-part-ii-exile-review-1236848647
2026-09-05 | Risks/Opportunities | The New York Times | Yemen's Houthis push toward Red Sea strait as ground fighting escalates | https://www.nytimes.com/2026/09/04/world/middleeast/yemen-houthis-red-sea-strait.html
