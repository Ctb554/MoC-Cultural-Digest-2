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
2026-09-25 | Saudi Arabia/Regional | Al-Monitor | Saudi artist Abdulnasser Gharem challenges power in Berlin | https://www.al-monitor.com/newsletter/2026-09-24/saudi-artist-abdulnasser-gharem-challenges-power-berlin
2026-09-25 | Saudi Arabia/Regional | Moodie Davitt Report | PIF company Al Waha Duty Free unveils Masra brand in Cannes, 'exporting Saudi vision to global travel retail' | https://moodiedavittreport.com/al-waha-duty-free-unveils-masra-flagship-brand-as-it-seeks-to-export-saudi-vision-to-travel-retail/
2026-09-25 | Saudi Arabia/Regional | Scoop Empire | Meet Razan Al-Ajmi: Saudi's First Female Skydiver Who Just Made History Over the Red Sea | https://scoopempire.com/meet-razan-al-ajmi-saudis-first-female-skydiver-who-just-made-history-over-the-red-sea/
2026-09-25 | Negative Articles | Foreign Policy | Saudi Arabia Bribed the Wrong People | https://foreignpolicy.com/2026/09/24/iran-trump-saudi-war-mbs-bad-bet/
2026-09-25 | Negative Articles | Bloomberg | France to Send Troops, Military Aid to Protect Saudi Oil Plant After Attack | https://www.bloomberg.com/news/articles/2026-09-24/france-to-send-military-aid-troops-to-protect-saudi-oil-plant
2026-09-25 | Negative Articles | Reuters | Oil prices settle up about 3% as Houthi attack on Saudi Arabia lifts supply fears | https://finance.yahoo.com/news/oil-prices-jump-4-houthis-155757474.html
2026-09-25 | Global | The Art Newspaper | Moca Los Angeles picks longtime public media executive as next director | https://www.theartnewspaper.com/2026/09/24/moca-los-angeles-jonathan-abbott-director-chief-executive
2026-09-25 | Global | Artnet News | The 2026 Turner Prize Show Is Grim—but the Strongest in Years | https://news.artnet.com/art-world/turner-prize-exhibition-2026-review-2815574
2026-09-25 | Global | Archaeology Magazine | Is This Ancient Wall Under Central Paris From the City's Earliest Settlement? | https://archaeology.org/news/2026/09/24/is-this-ancient-wall-under-central-paris-from-the-citys-earliest-settlement/
2026-09-25 | Global | Variety | Charlie Brooker's New Netflix Series Gets Title, 'Blackmere,' as Rory Kinnear Joins Cast and First-Look Photos Revealed | https://variety.com/2026/tv/news/charlie-brooker-new-series-title-blackmere-rory-kinnear-cast-1236874481/
2026-09-25 | Global | Deadline | Paramount Eyes Elon Musk For Investment As WBD Deal Nears Finish Line – Report | https://deadline.com/2026/09/david-ellison-paramount-elon-musk-investment-warner-merger-1237111566/
2026-09-25 | Global | The Philippine Star | Michelin Guide to recognize Philippine restaurants anew this October | https://www.philstar.com/lifestyle/food-and-leisure/2026/09/24/2558639/michelin-guide-recognize-philippine-restaurants-anew-october
