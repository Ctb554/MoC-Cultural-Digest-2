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
2026-08-09 | Saudi Arabia/Regional | Al Jazeera | UAE says Iran targeted ADNOC tanker in Strait of Hormuz, no casualties | https://www.aljazeera.com/news/2026/8/8/uae-says-iran-targeted-adnoc-tanker-in-hormuz-no-casualties-2
2026-08-09 | Saudi Arabia/Regional | Middle East Eye | Turkey says Saudi-Pakistan defence pact mirrors NATO's Article 5, Egypt could also join | https://www.middleeasteye.net/live-blog/live-blog-update/turkey-says-saudi-pakistan-defence-pact-mirrors-natos-article-5-egypt
2026-08-09 | Saudi Arabia/Regional | Al Jazeera | Iran deliberates Hormuz arrangement amid uncertain prospects with US | https://www.aljazeera.com/news/2026/8/8/iran-deliberates-hormuz-arrangement-amid-uncertain-prospects-with-us
2026-08-09 | Saudi Arabia/Regional | Middle East Eye | Fire doused at Saudi Aramco facility in Jizan, Saudi ministry says | https://www.middleeasteye.net/live-blog/live-blog-update/fire-doused-saudi-aramco-facility-jizan-saudi-ministry-says
2026-08-09 | Negative Articles | Al Jazeera | Saudi-Pakistan-Turkiye pact: a new shield or strategic signal? | https://www.aljazeera.com/news/2026/8/8/saudi-pakistan-turkiye-pact-a-new-shield-or-strategic-signal
2026-08-09 | Global | Arkeonews | 2,100-year-old Roman shipwreck loaded with hundreds of amphorae found off Sicily | https://arkeonews.net/2100-year-old-roman-shipwreck-loaded-with-hundreds-of-amphorae-found-off-sicily/
2026-08-09 | Global | Arkeonews | Danube drought uncovers Roman altar and inscribed tablets | https://arkeonews.net/danube-drought-uncovers-roman-altar-and-inscribed-tablets-along-with-a-wartime-bomb-scare/
2026-08-09 | Global | Arkeonews | Shackled men in ancient Athens mass grave were locals, not invaders, study confirms | https://arkeonews.net/shackled-men-in-ancient-athens-mass-grave-were-locals-not-invaders-study-confirms/
2026-08-09 | Global | Arkeonews | Bronze Age Greek rulers wore 'space bling' | https://arkeonews.net/bronze-age-greek-rulers-wore-space-bling/
2026-08-09 | Global | Dezeen | AOR Architects draws on harbour warehouses for Talas community centre in Helsinki | https://www.dezeen.com/2026/08/08/aor-architects-talas-community-centre-helsinki/
