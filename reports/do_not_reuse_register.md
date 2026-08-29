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
2026-08-29 | Saudi Arabia/Regional | Middle East Online | Riyadh Introduces Venice to Contemporary Saudi Art at the 2026 Biennale | https://middle-east-online.com/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6-%D8%AA%D9%8F%D8%B9%D8%B1%D9%91%D9%81-%D8%A7%D9%84%D8%A8%D9%86%D8%AF%D9%82%D9%8A%D8%A9-%D8%B9%D9%84%D9%89-%D8%A7%D9%84%D9%81%D9%86-%D8%A7%D9%84%D8%B3%D8%B9%D9%88%D8%AF%D9%8A-%D8%A7%D9%84%D9%85%D8%B9%D8%A7%D8%B5%D8%B1
2026-08-29 | Negative Articles | AGBI | New Murabba Replaces Chief Executive as Saudi Reassesses Giga-Project Spending | https://www.agbi.com/construction/2026/08/saudi-giga-project-new-murabba-replaces-chief-executive/
2026-08-29 | Global | The Art Newspaper | Art-o-rama Fair's Winning Formula: Low Fees, Young Blood, Bold Ideas | https://www.theartnewspaper.com/2026/08/28/art-fair-art-o-ramas-winning-formula-low-fees-young-blood-bold-ideas
2026-08-29 | Global | ARTnews | UK Places Temporary Export Bar on £71.7m Rembrandt Portrait | https://www.artnews.com/art-news/news/uk-government-temporary-export-ban-rembrandt-painting-1234796213/
2026-08-29 | Global | ARTnews | Sydney's Powerhouse Parramatta CEO Steps Aside Weeks Before Opening | https://www.artnews.com/art-news/news/morning-links-august-28-2026-1234796193/
2026-08-29 | Global | Bloomberg | Diamond Necklace Once Worn by Egypt's Queen Nazli Stolen From Vienna Museum | https://www.bloomberg.com/news/articles/2026-08-28/thieves-snatch-4-million-diamond-necklace-from-vienna-museum
2026-08-29 | Global | Dezeen | Helsinki Design Week Opens With 250 Events Under 'The Oncoming Other' | https://www.dezeen.com/eventsguide/2026/08/helsinki-design-week-2026/
2026-08-29 | Global | Billboard | Olivia Rodrigo Releases 'Serena Joy' Ahead of All-Women Benefit Festival | https://www.billboard.com/music/music-news/olivia-rodrigo-alex-warren-jennie-new-music-friday-guide-1236327055/
