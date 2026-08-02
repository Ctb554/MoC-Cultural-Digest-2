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

2026-08-02 | Saudi Arabia/Regional | Nikkei Asia | Trump says Mideast allies have reached outlines of deal to end Iran war | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/trump-says-mideast-allies-have-reached-outlines-of-deal-to-end-iran-war
2026-08-02 | Saudi Arabia/Regional | Axios | Scoop: Saudi crown prince raises concerns over Trump's plans for massive Iran strikes | https://www.axios.com/2026/08/01/saudi-crown-prince-trump-iran-attacks
2026-08-02 | Saudi Arabia/Regional | AGBI | Great Gulf pipeline race: which routes will actually be built? | https://www.agbi.com/analysis/oil-and-gas/2026/08/great-gulf-pipeline-race-which-routes-will-actually-be-built/
2026-08-02 | Global | Variety | Box Office: 'Spider-Man: Brand New Day' Breaks Opening Day Record With $168 Million | https://variety.com/2026/film/news/box-office-spider-man-brand-new-day-opening-day-record-1236825606/
2026-08-02 | Global | Deadline | Vincent Pastore Dies: 'The Sopranos' Star Was 80 | https://deadline.com/2026/08/vincent-pastore-dead-the-sopranos-star-big-pussy-1237015282/
2026-08-02 | Global | Artnet News | This New A.I. Chatbot Hunts Nazi-Looted Art | https://news.artnet.com/art-world/ai-provenance-assistant-looted-art-tool-2792609
2026-08-02 | Risks and Opportunities | Fortune | Trump backs off from new strikes on Iran, claiming Mideast allies have outlines of an emerging deal to reopen the Strait of Hormuz | https://fortune.com/2026/08/01/trump-iran-strikes-mideast-allies-emerging-strait-of-hormuz/
