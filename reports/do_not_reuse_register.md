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
2026-09-28 | Saudi Arabia/Regional | TTN Worldwide | AlUla wins gold for nature-positive tourism at 2026 ICRT Awards | https://www.ttnworldwide.com/ArticleTA/486877/alula-wins-gold-for-nature-positive-tourism-at-2026-icrt-awards
2026-09-28 | Saudi Arabia/Regional | Global Times | How Riyadh's coffee culture is creating new public sphere and redefining Saudi identity between tradition and modernity | https://www.globaltimes.cn/page/202609/1371429.shtml
2026-09-28 | Saudi Arabia/Regional | ArchDaily | Ashjar Cafe / Studio Ahmed Aldossary | https://www.archdaily.com/1185816/ashjar-cafe-studio-ahmed-aldossary
2026-09-28 | Saudi Arabia/Regional | Gulf News | Riyadh Season 2026 to begin on October 21 with 10 weeks of entertainment | https://gulfnews.com/world/gulf/saudi/riyadh-season-2026-to-begin-on-october-21-with-10-weeks-of-entertainment-1.500689955
2026-09-28 | Negative Articles | AFP via CP24 | Houthis say Saudi strikes on Yemen's Taiz leave dozens of casualties | https://www.cp24.com/news/world/2026/09/27/houthis-say-saudi-strikes-on-yemens-taiz-leave-dozens-of-casualties/
2026-09-28 | Negative Articles | Middle East Eye | Iran offers to mediate talks between Saudi Arabia and Yemen | https://www.middleeasteye.net/live-blog/live-blog-update/iran-offers-mediate-talks-between-saudi-arabia-and-yemen
2026-09-28 | Negative Articles | Al Jazeera | Yemen government forces widen attacks against Houthis: What we know | https://www.aljazeera.com/news/2026/9/27/yemen-government-forces-widen-attacks-against-houthis-what-we-know
2026-09-28 | Global | The Art Newspaper | Fourth Toronto Biennial of Art brings more than 30 artists and collectives together around the theme of rupture | https://www.theartnewspaper.com/2026/09/27/toronto-biennial-art-fourth-edition-allison-glenn-things-fall-apart-preview
2026-09-28 | Global | Arkeonews | After 26 Years, Perperikon Reveals the First Evidence of Monumental Statues | https://arkeonews.net/after-26-years-perperikon-reveals-the-first-evidence-of-monumental-statues/
2026-09-28 | Global | Arkeonews | A Burned Wall May Reveal the City Caesar Said the Gauls Set Ablaze | https://arkeonews.net/a-burned-wall-may-reveal-the-city-caesar-said-the-gauls-set-ablaze/
2026-09-28 | Global | Arkeonews | Arab Silver Coins Found Near Truso, the 'Viking Atlantis' | https://arkeonews.net/arab-silver-coins-found-near-truso-the-viking-atlantis/
2026-09-28 | Global | ArchDaily | Osmanthus Moon / HCCH Studio | https://www.archdaily.com/1035956/osmanthus-moon-hcch-studio
2026-09-28 | Global | Dezeen | Harvard University transforms waste wool into cladding for retrofits | https://www.dezeen.com/2026/09/27/waste-wool-cladding-harvard-university-oslo-architecture-triennale/
2026-09-28 | Global | WWD | Giorgio Armani Spring 2027 Ready-to-Wear Review | https://wwd.com/runway/spring-2027/milan/giorgio-armani/review/
2026-09-28 | Global | Variety | VMAs 2026 Full Winners List: Taylor Swift Takes Video of the Year, Lisa Gets Best Pop, Madonna Tops Multiple Categories and More | https://variety.com/2026/music/news/vmas-winners-list-mtv-awards-2026-show-1236876862/
