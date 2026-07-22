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

2026-07-22 | Saudi Arabia/Regional | The National | Tankers carrying Saudi oil make U-turn in Red Sea after Houthi threats | https://www.thenationalnews.com/news/gulf/2026/07/21/saudi-arabia-rejects-houthi-maritime-embargo-threat-and-warns-of-red-sea-escalation/
2026-07-22 | Saudi Arabia/Regional | Bloomberg | Saudi Crude Flow From Red Sea Hit Record Before Houthi Warning | https://www.bloomberg.com/news/articles/2026-07-21/saudi-crude-flow-from-red-sea-hit-record-before-houthi-warning
2026-07-22 | Saudi Arabia/Regional | The Boston Globe | Trump approves nuclear agreement that may allow Saudi Arabia to enrich uranium, two AP sources say | https://www.bostonglobe.com/2026/07/21/nation/trump-saudi-arabia-nuclear-agreement/
2026-07-22 | Saudi Arabia/Regional | The New York Times | Houthis in Yemen Edge Closer to Entering U.S.-Iran War | https://www.nytimes.com/2026/07/21/world/middleeast/houthis-yemen-iran-war.html
2026-07-22 | Negative Articles | Al Jazeera | Saudi Arabia slams Houthi blockade: How will rest of the world be impacted? | https://www.aljazeera.com/news/2026/7/21/saudi-condemns-houthi-blockade-how-will-the-rest-of-the-world-be-impacted
2026-07-22 | Global | Arkeonews | 2,000-Year-Old Main Street Unearthed at Aspendos Reveals Shops, Sewers and a Monumental Gate | https://arkeonews.net/2000-year-old-main-street-unearthed-at-aspendos-reveals-shops-sewers-and-a-monumental-gate/
2026-07-22 | Global | Arkeonews | Archaeologists Uncover Monumental Bronze Age Tomb with Weapons and a Sacrificed Horse in Armenia | https://arkeonews.net/archaeologists-uncover-monumental-bronze-age-tomb-with-weapons-and-a-sacrificed-horse-in-armenia/
2026-07-22 | Global | Archaeology Magazine | Italy Repatriates Artifacts to Mexico | https://archaeology.org/news/2026/07/21/italy-repatriates-artifacts-to-mexico-2/
2026-07-22 | Global | Hyperallergic | The Art Institute of Chicago to Cut Its Entire Custodial Staff | https://hyperallergic.com/the-art-institute-of-chicago-to-cut-its-entire-custodial-staff/
2026-07-22 | Global | The Art Newspaper | Shuttered San Francisco arts school will become college co-named for Nvidia founder Jensen Huang | https://www.theartnewspaper.com/2026/07/21/vanderbilt-university-california-college-arts-jensen-huang-gift
2026-07-22 | Global | The Art Newspaper | Comment | How much can one artist take from another before it is copyright infringement? | https://www.theartnewspaper.com/2026/07/21/when-is-appropriation-pastiche-or-copyright-infringement
2026-07-22 | Global | ArchDaily | MVRDV Wins Competition to Design Shift Embassy in Rotterdam | https://www.archdaily.com/1181341/mvrdv-wins-competition-to-design-shift-embassy-in-rotterdam
2026-07-22 | Global | WWD | Chemena Kamali to Head 2026 Fashion Jury at Hyeres Festival | https://wwd.com/fashion-news/fashion-features/chemena-kamali-fashion-jury-president-2026-hyeres-festival-1239077134/
2026-07-22 | Global | Publishers Weekly | May Sales Shined, AAP Reports | https://www.publishersweekly.com/pw/by-topic/industry-news/financial-reporting/article/100885-may-sales-shined-aap-reports.html
