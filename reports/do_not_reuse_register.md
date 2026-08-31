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
2026-08-31 | Saudi Arabia/Regional | The National | Sultan bin Fahad explores historical links between jazz and Islam in solo exhibition | https://www.thenationalnews.com/arts-culture/art-design/2026/08/31/saudi-artist-sultan-bin-fahad-links-jazz-islam-blue-note-exhibition/
2026-08-31 | Negative Articles | Middle East Eye | Mecca pact's first trilateral meeting to be held in Istanbul on Monday | https://www.middleeasteye.net/live-blog/live-blog-update/mecca-pacts-first-trilateral-meeting-be-held-istanbul-monday
2026-08-31 | Global | The Art Newspaper | Egyptian queen's 673-diamond necklace stolen from Vienna museum in brazen daytime heist | https://www.theartnewspaper.com/2026/08/30/queen-egypt-diamond-platinum-necklace-stolen-vienna-museum-applied-arts-robbery
2026-08-31 | Global | Deadline | Venice Film Festival Changes Course To Reinstate Jury Press Conference: How It Went Down | https://deadline.com/2026/08/venice-film-festival-uturn-reinstates-jury-press-conference-1237062875/
2026-08-31 | Global | Variety | Box Office: 'The Dog Stars' Bombs With $8 Million; 'Spider-Man' Continues Reign in Fifth Weekend | https://variety.com/2026/film/news/box-office-the-dog-stars-bombs-spider-man-brand-new-day-1236846879/
