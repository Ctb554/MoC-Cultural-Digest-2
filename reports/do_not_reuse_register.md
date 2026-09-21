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

2026-09-21 | Saudi Arabia/Regional | ArtDependence | Islamic Arts Biennale Announces Curators for 2027 | https://www.artdependence.com/articles/islamic-arts-biennale-announces-curators-for-2027/
2026-09-21 | Saudi Arabia/Regional | Mid-East.info | Celebrate Saudi National Day in AlUla through cultural heritage activations and luxury hospitality | https://mid-east.info/celebrate-saudi-national-day-in-alula-through-cultural-heritage-activations-and-luxury-hospitality/
2026-09-21 | Negative Articles | Associated Press | Iran-backed Houthi rebels warn against joining Saudi Arabia in Yemen's growing civil war | https://www.clickorlando.com/news/world/2026/09/20/iran-backed-houthi-rebels-warn-against-joining-saudi-arabia-in-yemens-growing-civil-war/
2026-09-21 | Negative Articles | Press TV | Yemen warns Saudi escalation will draw stronger response | https://www.presstv.co.uk/Detail/2026/09/20/776657/sanaa-warns-saudi-arabia-of-response-
2026-09-21 | Negative Articles | The New York Times | Trump Gets Caught in a Dilemma Over a Saudi Plea for Military Help | https://www.nytimes.com/2026/09/20/us/politics/trump-yemen-houthis-red-sea-iran.html
2026-09-21 | Negative Articles | The Guardian | How Saudi oil scientists ended up working on the world's most important climate reports | https://www.theguardian.com/environment/2026/sep/21/saudi-arabia-aramco-oil-scientists-ipcc-climate-reports
2026-09-21 | Global | The Art Newspaper | Hundreds gather at Kennedy Center to protest Trump's attacks | https://www.theartnewspaper.com/2026/09/21/trump-kennedy-center-protest-hands-off-the-arts
2026-09-21 | Global | Ocula | New Lawsuit Reopens Decades-Long Legal Battle Over Nazi-Looted Painting | https://ocula.com/magazine/art-news/nazi-looted-lawsuit-norton-simon-museum-cranach/
2026-09-21 | Global | Arkeonews | 8,000-Year-Old 'Guardians of Grain' Discovered in a Neolithic House | https://arkeonews.net/8000-year-old-guardians-of-grain-discovered-in-a-neolithic-house/
2026-09-21 | Global | Arkeonews | A Legendary Chinese Empress May Lie in a Royal Tomb Surrounded by 45 Mysterious Graves | https://arkeonews.net/a-legendary-chinese-empress-may-lie-in-a-royal-tomb-surrounded-by-45-mysterious-graves/
2026-09-21 | Global | Variety | 'Resident Evil' Box Office: Zach Cregger Reboot Surpasses Expectations | https://variety.com/2026/film/box-office/resident-evil-box-office-zach-cregger-reboot-opening-weekend-record-breaking-1236867659/
2026-09-21 | Global | Dezeen | Bugatti unveils Miami skyscraper as first US branded residence | https://www.dezeen.com/2026/09/20/bugatti-skyscraper-miami-brandon-haw-yabu-pushelberg/
2026-09-21 | Global | ArchDaily | The Sacred Ordinary: Studio Ghibli and the Ritual of Coming Home | https://www.archdaily.com/1185096/the-sacred-ordinary-studio-ghibli-and-the-ritual-of-coming-home
