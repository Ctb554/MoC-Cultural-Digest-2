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

2026-09-03 | Saudi Arabia/Regional | Masrawy | Turki Al Sheikh offers a SAR 1 million prize for the one-millionth ticket to the Saudi film 7 Dogs | https://www.masrawy.com/arts/cinema/details/2026/9/2/3042342/
2026-09-03 | Saudi Arabia/Regional | Harper's Bazaar Arabia | HH Princess Deena Aljuhani Abdulaziz is the Harper's Bazaar Arabia September 2026 cover star | https://www.harpersbazaararabia.com/hbanews/princess-deena-aljuhani-abdulaziz-harpers-bazaar-arabia-september-2026-issue-cover-star
2026-09-03 | Saudi Arabia/Regional | Blooloop | Abu Dhabi's new Harry Potter land to offer Hogwarts Castle, Diagon Alley and Forbidden Forest | https://blooloop.com/news/harry-potter-abu-dhabi-lands
2026-09-03 | Global | The Art Newspaper | Four artists explore AI's effect on culture as part of Serpentine's new art and technology fellowship | https://www.theartnewspaper.com/2026/09/02/four-artists-explore-ais-effect-on-culture-as-part-of-serpentines-new-art-and-technology-award
2026-09-03 | Global | Hyperallergic | Critics Slam 'Petty' Removal of Joel Shapiro Sculpture From Kennedy Center | https://hyperallergic.com/critics-slam-petty-removal-of-joel-shapiro-sculpture-from-kennedy-center/
2026-09-03 | Global | The Art Newspaper | A Churchill painting that mysteriously fell into the hands of a Nazi collaborator is on show in London | https://www.theartnewspaper.com/2026/09/02/a-churchill-painting-that-mysteriously-fell-into-the-hands-of-a-nazi-collaborator-is-on-show-in-london
2026-09-03 | Global | Arkeonews | A New Type of 4,600-Year-Old Board Game Discovered at Iran's Burnt City | https://arkeonews.net/a-new-type-of-4600-year-old-board-game-discovered-at-irans-burnt-city/
2026-09-03 | Global | Archaeology Magazine | Vessel Tied to Eastern Cult Identified at Villa in Roman Spain | https://archaeology.org/news/2026/09/02/vessel-tied-to-eastern-cult-identified-at-villa-in-roman-spain/
2026-09-03 | Global | The Hollywood Reporter | Danny Boyle's Rupert Murdoch Drama 'Ink' Gives Venice a Rollicking Start on Opening Night | https://www.hollywoodreporter.com/movies/movie-news/danny-boyles-rupert-murdoch-drama-ink-venice-ovation-1236688040/
2026-09-03 | Global | Dezeen | Studios turning to AI floor plan generator to speed up design process | https://www.dezeen.com/2026/09/03/laiout-ai-floor-plan-generator-jll-design/
2026-09-03 | Global | Publishers Weekly | U.K.'s SPCK Group Acquires Eerdmans | https://www.publishersweekly.com/pw/by-topic/industry-news/religion/article/101172-u-k-s-spck-group-acquires-eerdmans.html
2026-09-03 | Risks | Philstar | Two Filipino seafarers killed as Saudi tanker attacked in Hormuz | https://www.philstar.com/headlines/2026/09/03/2553745/two-filipino-seafarers-killed-saudi-tanker-attacked-hormuz
2026-09-03 | Risks | The Manila Times | Two Pinoy sailors killed in attack on oil tanker | https://www.manilatimes.net/2026/09/03/news/national/two-pinoy-sailors-killed-in-attack-on-oil-tanker/2417294
