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
2026-08-01 | Saudi Arabia/Regional | Deutsche Welle | Military flare-up between Houthis and Saudi Arabia challenges relative calm in Yemen | https://www.dw.com/en/military-flare-up-between-houthis-and-saudi-arabia-challenges-relative-calm-in-yemen/a-78186262
2026-08-01 | Saudi Arabia/Regional | Al-Monitor | Oil price rises after Iran says it stops ships in Hormuz | https://www.al-monitor.com/originals/2026/07/oil-price-rises-after-iran-says-it-stops-ships-hormuz
2026-08-01 | Saudi Arabia/Regional | Middle East Eye | Saudi Arabia calls Trump's Gaza 'demilitarisation deal' historic | https://www.middleeasteye.net/live-blog/live-blog-update/saudi-arabia-terms-trumps-gaza-demilitarisation-deal-historic
2026-08-01 | Saudi Arabia/Regional | Al-Monitor | Italy minister rejects opposition criticism of Saudi troop deployment | https://www.al-monitor.com/originals/2026/07/italy-minister-rejects-opposition-criticism-saudi-troop-deployment
2026-08-01 | Negative Articles | Middle East Eye | Yemeni forces say eight Saudi tankers forced to reroute | https://www.middleeasteye.net/live-blog/live-blog-update/yemeni-forces-say-eight-saudi-tankers-forced-reroute
2026-08-01 | Global | The Art Newspaper | Japan's 400-year-old Kumamoto Castle damaged by 7.1 magnitude earthquake | https://www.theartnewspaper.com/2026/07/31/japans-400-year-old-kumamoto-castle-damaged-by-71-magnitude-earthquake
2026-08-01 | Global | Artnet News | Art Basel could save $9m in new Miami Beach rent deal | https://news.artnet.com/market/industry-intel-july-31-2791743
2026-08-01 | Global | Deadline | Box Office: 'Spider-Man: Brand New Day' record US opening day | https://deadline.com/2026/07/box-office-spider-man-brand-new-day-1237014268/
2026-08-01 | Global | WWD | Met's Costume Institute planning John Galliano retrospective | https://wwd.com/fashion-news/fashion-scoops/costume-institute-met-next-exhibition-john-galliano-1239089295/
2026-08-01 | Global | Billboard | Suno held liable for infringing German song copyrights in Munich court ruling | https://www.billboard.com/pro/suno-liable-gema-german-copyright-lawsuit/
2026-08-01 | Global | Billboard | Sony's global music revenue tops $3.53 billion on surge in vinyl, live and merch sales | https://www.billboard.com/pro/sonys-global-music-biz-revenue-tops-3-53-billion-2026-q2/
2026-08-01 | Global | Billboard | Ariana Grande's 'Petal' album is here | https://www.billboard.com/music/pop/ariana-grande-petal-album-listen-1236306614/
