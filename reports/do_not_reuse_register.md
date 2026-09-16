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
2026-09-16 | Saudi Arabia/Regional | Archaeology Magazine | Early Mosque Uncovered in Saudi Arabia's Al-Baha Province | https://archaeology.org/news/2026/09/15/early-mosque-uncovered-in-saudi-arabias-al-baha-province/
2026-09-16 | Saudi Arabia/Regional | TradeArabia | Saudi design leaders, emerging talent set the agenda at Index expo | https://tradearabia.com/News/486255/Saudi-design-leaders-emerging-talent-set-the-agenda-at-Index-expo
2026-09-16 | Saudi Arabia/Regional | SceneNoise | SceneNoise x Amsterdam Dance Event Present CROSSFADE: Saudi Arabia | https://scenenoise.com/Features/SceneNoise-x-Amsterdam-Dance-Event-Present-CROSSFADE-Saudi-Arabia
2026-09-16 | Negative Articles | Bloomberg | MBS and Saudi Arabia Face Crisis With Key Oil Pipeline Shut for Weeks | https://www.bloomberg.com/news/articles/2026-09-15/mbs-and-saudi-arabia-face-crisis-with-key-oil-pipeline-shut-for-weeks
2026-09-16 | Negative Articles | Semafor | Saudi Arabia under military pressure from Iran, Houthis | https://www.semafor.com/article/09/15/2026/saudi-arabia-under-tense-military-pressure-from-iran-houthis
2026-09-16 | Negative Articles | CNBC | Oil's safety net is fraying as Saudi Arabia races to restart a key pipeline | https://www.cnbc.com/2026/09/15/oil-prices-saudi-arabia-east-west-pipeline-iran.html
2026-09-16 | Negative Articles | Al Jazeera | Saudi Arabia promises to respond to Houthi attacks 'firmly' | https://www.aljazeera.com/news/2026/9/15/houthis-report-air-strikes-in-yemen-after-saudi-arabia-vows-firm-response
2026-09-16 | Negative Articles | Press TV | Saudi Arabia seeks British strikes on Yemen after US refusal, Burnham undecided | https://www.presstv.co.uk/Detail/2026/09/15/776310/Saudi-regime-seeks-British-strikes-on-Yemen-after-US-refusal
2026-09-16 | Global | Archaeology Magazine | Troy's Earliest Agora Unearthed | https://archaeology.org/news/2026/09/15/troys-earliest-agora-unearthed/
2026-09-16 | Global | Archaeology Magazine | Italian Officials Unveil Ancient Rome's Largest Wall Mosaic | https://archaeology.org/news/2026/09/15/italian-officials-unveil-ancient-romes-largest-wall-mosaic/
2026-09-16 | Global | Smithsonian Magazine | Closed to public since WWII, hidden gallery at London Natural History Museum opens doors once again | https://www.smithsonianmag.com/smart-news/closed-to-public-since-wwii-hidden-gallery-at-london-natural-history-museum-opens-doors-once-again-180989380/
2026-09-16 | Global | The Art Newspaper | Dealers make moves around Manhattan | https://www.theartnewspaper.com/2026/09/15/new-york-galleries-moving-manhattan-soho-rising-chelsea-tribeca-endure
2026-09-16 | Global | Deadline | Emmys 2026 Analysis: The TV Academy Shakes Things Up | https://deadline.com/2026/09/2026-emmys-analysis-widows-bay-1237103690/
2026-09-16 | Global | WWD | Thom Browne Spring 2027 Ready-to-Wear | https://wwd.com/runway/spring-2027/new-york/thom-browne/review/
2026-09-16 | Global | Billboard | Noel Gallagher Reveals the Exact Moment Oasis Knew They Were Going to Tour Again in 2027 | https://www.billboard.com/music/rock/noel-gallagher-moment-oasis-knew-going-back-on-tour-new-music-1236340326/
2026-09-16 | Global | The Korea Herald | SPAF brings global and experimental works to Seoul this fall | https://www.koreaherald.com/article/10874594
2026-09-16 | Global | ArchDaily | 20 Practices Expanding Architecture's Agency: Winners of the ArchDaily 2026 Next Practices Awards | https://www.archdaily.com/1185003/20-practices-expanding-architectures-agency-winners-of-the-archdaily-2026-next-practices-awards
2026-09-16 | Global | Publishers Weekly | 2026 NBA Longlists for Translated, Young People's Literature Announced | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/101236-2026-national-book-award-longlists-announced.html
2026-09-16 | Risks and Opportunities | The Guardian | Saudi Arabia warns of 'red line' after Houthi drone intercepted close to holy city of Mecca | https://www.theguardian.com/world/2026/sep/16/saudi-arabia-houthi-drone-shot-down-mecca-iran-middle-east
