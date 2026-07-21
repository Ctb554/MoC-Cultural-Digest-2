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
2026-07-21 | Saudi Arabia/Regional | Nikkei Asia | Yemen's Houthis declare naval blockade on Saudi Arabia | https://asia.nikkei.com/spotlight/iran-tensions/iran-war/yemen-s-houthis-declare-naval-blockade-on-saudi-arabia
2026-07-21 | Saudi Arabia/Regional | Bloomberg | Saudi-Led Coalition in Yemen Vows to Protect Ships From Houthis | https://www.bloomberg.com/news/articles/2026-07-20/yemen-s-houthis-vow-to-impose-maritime-blockade-on-saudi-arabia
2026-07-21 | Saudi Arabia/Regional | Euronews | Yemen's Houthis threaten Bab el-Mandeb closure in embargo on Saudi Arabia | https://www.euronews.com/2026/07/20/yemens-houthis-threaten-bab-el-mandeb-closure-in-embargo-on-saudi-arabia
2026-07-21 | Negative Articles | Al Jazeera | Yemen's Houthis declare naval blockade of Saudi Arabia: What to know | https://www.aljazeera.com/news/2026/7/20/yemens-houthis-declare-naval-blockade-of-saudi-arabia-what-to-know
2026-07-21 | Global | HeritageDaily | New Kingdom tombs discovered at Saqqara provide new evidence of connections with Near East | https://www.heritagedaily.com/2026/07/new-kingdom-tombs-discovered-at-saqqara-provide-new-evidence-of-connections-with-near-east/158655
2026-07-21 | Global | HeritageDaily | New study reveals how Cypriot goldsmiths united four ancient cultures | https://www.heritagedaily.com/2026/07/new-study-reveals-how-cypriot-goldsmiths-united-four-ancient-cultures/158659
2026-07-21 | Global | Hyperallergic | Activists Sue to Stop Frida Kahlo Works From Leaving Mexico | https://hyperallergic.com/activists-sue-to-stop-frida-kahlo-works-from-leaving-mexico/
2026-07-21 | Global | Hyperallergic | Cuban Artist Luis Manuel Otero Alcántara Exiled to the US | https://hyperallergic.com/cuban-artist-luis-manuel-otero-alcantara-exiled-to-the-us/
2026-07-21 | Global | ARTnews | Shanghai Auction Executives Sentenced in Major Fraud Case as Industry Scrutiny Intensifies | https://www.artnews.com/art-news/news/shanghai-auction-executives-sentenced-in-major-fraud-case-1234792736/
2026-07-21 | Global | Hyperallergic | New Museum's Shiny New Building Leaks During Flash Floods | https://hyperallergic.com/new-museums-shiny-new-building-leaks-during-flash-floods/
