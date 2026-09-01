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
2026-09-01 | Saudi Arabia/Regional | Egypt Telegraph | Saudi artist Alaa Al-Qahtani on merging Arabic calligraphy with carpet artistry | https://www.egypttelegraph.com/article/274855/
2026-09-01 | Saudi Arabia/Regional | Egypt Telegraph | Amr Diab to perform for fans in Saudi Arabia as part of Jeddah Season | https://www.egypttelegraph.com/article/274780/
2026-09-01 | Saudi Arabia/Regional | Gulf Times | Qatar Museums announces Fall 2026 season of expansive exhibitions | https://www.gulf-times.com/article/727719/qatar/qatar-museums-announces-fall-2026-season-of-expansive-exhibitions
2026-09-01 | Negative Articles | Middle East Eye | Saudi-backed LIV Golf preparing for bankruptcy filing | https://www.middleeasteye.net/news/saudi-backed-liv-golf-preparing-bankruptcy-filing
2026-09-01 | Negative Articles | Bloomberg | Saudis Explore About $8 Billion in Loans as War Strains Finances | https://www.bloomberg.com/news/articles/2026-08-31/saudis-explore-about-8-billion-in-loans-as-war-strains-finances
2026-09-01 | Global | PBS NewsHour | Metropolitan Museum of Art cancels planned 2027 Met Gala exhibit on fashion designer John Galliano | https://www.pbs.org/newshour/arts/metropolitan-museum-of-art-cancels-planned-2027-met-gala-exhibit-on-fashion-designer-john-galliano
2026-09-01 | Global | The Art Newspaper | London Science Museum's sponsorship deal with BP ends after almost 25 years | https://www.theartnewspaper.com/2026/08/31/london-science-museum-ends-bp-sponsorship
2026-09-01 | Global | Complex | Ib Kamara Says He's Leaving Off-White With 'Enormous Pride' | https://www.complex.com/style/a/tracewilliamcowen/ib-kamara-leaves-off-white
2026-09-01 | Global | Evening Standard | 'World class' London graffiti artist Helch dies as tributes paid from art world | https://www.aol.co.uk/articles/world-class-graffiti-artist-helch-154131000.html
2026-09-01 | Global | Archaeology Magazine | Study Tracks Diet in Polish City | https://archaeology.org/news/2026/08/31/study-tracks-diet-in-polish-city/
2026-09-01 | Global | The Canadian Press | Everything you need to know about the 2026 Venice Film Festival | https://lethbridgeherald.com/entertainment/entertainment-news/2026/08/31/everything-you-need-to-know-about-the-2026-venice-film-festival/
