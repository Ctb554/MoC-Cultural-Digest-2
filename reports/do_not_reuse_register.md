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

2026-08-26 | Saudi Arabia/Regional | WWD | London Meets Riyadh at Saudi Design Show in Selfridges' Corner Shop | https://wwd.com/fashion-news/fashion-scoops/london-meets-riyadh-saudi-showcase-selfridges-corner-shop-1239091075/
2026-08-26 | Negative Articles | France 24 | Trump sends Saudi civil nuclear agreement to Congress for review | https://www.france24.com/en/americas/20260826-trump-saudi-civil-nuclear-agreement-congress
2026-08-26 | Negative Articles | Middle East Eye | Houthi leader underlines support for Palestinians, slams Saudi 'tyranny' | https://www.middleeasteye.net/live-blog/live-blog-update/houthi-leader-underlines-support-palestinians-slams-saudi-tyranny
2026-08-26 | Global | Arkeonews | A Unique 11,000-Year-Old Statue of a Human Sitting on a Leopard Unearthed at Karahantepe | https://arkeonews.net/a-unique-11000-year-old-statue-of-a-human-sitting-on-a-leopard-unearthed-at-karahantepe/
2026-08-26 | Global | Archaeology Magazine | U.S. Returns Artifacts to Egypt | https://archaeology.org/news/2026/08/25/u-s-returns-artifacts-to-egypt/
2026-08-26 | Global | The Art Newspaper | Somebody to Love at the V&A as Freddie Mercury's costumes to go on view | https://www.theartnewspaper.com/2026/08/25/somebody-to-love-at-the-va-as-freddie-mercurys-costumes-to-go-on-view
2026-08-26 | Global | Hyperallergic | Famed 'Portrait of Omai' Will Go on View at LA's Getty Museum | https://hyperallergic.com/famed-portrait-of-omai-will-go-on-view-at-las-getty-museum/
2026-08-26 | Global | Billboard | Billboard Affirms Commitment to Transparency Around AI-Generated Music | https://www.billboard.com/music/music-news/ai-generated-music-billboard-transparency-1236323619/
2026-08-26 | Global | The Stage | Rose Playhouse site opens doors to public for first time in six years | https://www.thestage.co.uk/news/rose-playhouse-site-opens-doors-to-public-for-first-time-in-six-years
2026-08-26 | Global | ArchDaily | Donald Judd's Artillery Sheds in Texas to Undergo Major Restoration | https://www.archdaily.com/1183915/donald-judds-artillery-sheds-in-texas-to-undergo-major-restoration
2026-08-26 | Global | ArchDaily | OMA/AMO and OPEN Architecture Design Opening Exhibitions for Powerhouse Parramatta in Sydney, Australia | https://www.archdaily.com/1183902/oma-amo-and-open-architecture-design-opening-exhibitions-for-powerhouse-parramatta-in-sydney-australia
