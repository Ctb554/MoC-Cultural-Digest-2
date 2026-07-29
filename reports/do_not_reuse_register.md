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

<!-- CONTINUITY NOTE (2026-07-29): This register was empty at the start of this
     run, but nine prior editions (20-28 Jul 2026, incl. two MoC_Digest_YYYY-MM-DD
     variants) were found already delivered in the Dropbox "05_Claude Test" folder.
     Their article URLs were not recoverable from the delivered .docx text
     (hyperlinks are dropped on extraction), so past URLs are NOT backfilled here.
     This run reconstructed the prior headline/outlet set from those editions to
     enforce non-reuse for 29 Jul. Future runs: if this register is ever empty
     again, read the last three editions from the Dropbox folder as this run did. -->

2026-07-29 | Saudi Arabia/Regional | Associated Press | US thwarts an Iranian missile attack and launches strikes with Saudi Arabia against militias in Iraq | https://www.clickorlando.com/news/world/2026/07/28/saudi-arabia-says-it-shot-down-more-drones-as-houthis-claim-to-have-turned-back-tanker/
2026-07-29 | Saudi Arabia/Regional | The New York Times | Houthis Claim Strike on Another Saudi Oil Tanker | https://www.nytimes.com/2026/07/28/world/middleeast/houthis-strike-saudi-tanker.html
2026-07-29 | Saudi Arabia/Regional | The Guardian | US says it intercepted 'surprise' Iran missile attack on its forces in Middle East after lull in fighting | https://www.theguardian.com/world/2026/jul/29/iran-missile-attack-us-base-forces
2026-07-29 | Saudi Arabia/Regional | Deutsche Welle | Will Pakistan intervene amid Houthi attacks on Saudi ships? | https://www.dw.com/en/will-pakistan-intervene-amid-houthi-attacks-on-saudi-ships/a-78144890
2026-07-29 | Saudi Arabia/Regional | The Art Newspaper | Guggenheim Abu Dhabi announces opening date | https://www.theartnewspaper.com/2026/07/28/guggenheim-abu-dhabi-announces-opening-date
2026-07-29 | Negative Articles | Middle East Eye | Iraqi paramilitary force condemns Saudi-US attacks on headquarters | https://www.middleeasteye.net/live-blog/live-blog-update/iraqi-paramilitary-force-condemns-saudi-us-attacks-headquarters
2026-07-29 | Negative Articles | Human Rights Watch | Saudi Arabia: New Executions of Ethiopian Migrants | https://www.hrw.org/news/2026/07/28/saudi-arabia-new-executions-of-ethiopian-migrants
2026-07-29 | Global | The Art Newspaper | Culture minister Catherine Pegard reveals 'national security plan' following another major museum theft in France | https://www.theartnewspaper.com/2026/07/28/culture-minister-catherine-pegard-reveals-national-security-plan-following-another-major-museum-theft-in-france
2026-07-29 | Global | HeritageDaily | Archaeologists map buried sacred precinct of the Aztec capital - Tenochtitlan | https://www.heritagedaily.com/2026/07/archaeologists-map-buried-sacred-precinct-of-the-aztec-capital-tenochtitlan/158744
2026-07-29 | Global | ARTnews | The Philadelphia Museum of Art ran a $10m deficit this past fiscal year | https://www.artnews.com/art-news/news/phildelphia-museum-of-art-ran-a-10-m-deficit-1234793631
2026-07-29 | Global | Blooloop | Shenzhen Natural History museum opens in China | https://blooloop.com/news/shenzhen-natural-history-museum-opens
2026-07-29 | Global | The Hollywood Reporter | New Mike Leigh, Pablo Larrain Films in San Sebastian Competition | https://www.hollywoodreporter.com/movies/movie-news/marion-cotillard-mike-leigh-pablo-larrain-in-san-sebastian-1236658023
2026-07-29 | Global | The Hollywood Reporter | Penske Media Sued by Hollywood Foreign Press Over Golden Globes Buy | https://www.hollywoodreporter.com/business/business-news/penske-media-sued-hollywood-foreign-press-golden-globes-1236658413
2026-07-29 | Global | Artsy | MoMA to host chess matches in honour of Marcel Duchamp | https://www.artsy.net/article/artsy-editorial-moma-host-chess-matches-honor-marcel-duchamp
2026-07-29 | Global | Publishers Weekly | 2026 Booker Prize Longlist Announced | https://www.publishersweekly.com/pw/by-topic/industry-news/awards-and-prizes/article/100927-2026-booker-prize-longlist-announced.html
