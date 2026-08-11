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
2026-08-11 | Saudi Arabia/Regional | Deutsche Welle | Which country is the new Mecca defense pact targeting? | https://www.dw.com/en/which-country-is-the-new-mecca-defense-pact-targeting/a-78307673
2026-08-11 | Saudi Arabia/Regional | The Diplomat | The Mecca Pact Extends Pakistan's Security Role Westward | https://thediplomat.com/2026/08/the-mecca-pact-extends-pakistans-security-role-westward/
2026-08-11 | Saudi Arabia/Regional | The Diplomat | Bangladesh Joins Saudi-led Defense Coalition as Bab el-Mandeb Risks Grow | https://thediplomat.com/2026/08/bangladesh-joins-saudi-led-defense-coalition-as-bab-el-mandeb-risks-grow/
2026-08-11 | Saudi Arabia/Regional | Middle East Eye | Iran says it is not concerned by new 'Mecca Joint Defence Agreement' | https://www.middleeasteye.net/news/iran-says-it-not-concerned-new-mecca-joint-defence-agreement
2026-08-11 | Global | Arkeonews | 2,400-Year-Old Tomb of a Possible Ancient Wrestler Discovered at Aspendos | https://arkeonews.net/2400-year-old-tomb-of-a-possible-ancient-wrestler-discovered-at-aspendos/
2026-08-11 | Global | Arkeonews | 8,500-Year-Old Shell Bead Reveals Ancient California's Hidden Trade Network | https://arkeonews.net/8500-year-old-shell-bead-reveals-ancient-californias-hidden-trade-network/
2026-08-11 | Global | The Art Newspaper | Remains of colonial hospital and church discovered in Lima's historic centre | https://www.theartnewspaper.com/2026/08/10/remains-colonial-hospital-discovered-luma
2026-08-11 | Global | Hyperallergic | Divers Stumble Upon 2,000-Year-Old Roman Shipwreck in Italy | https://hyperallergic.com/divers-stumble-upon-2-000-year-old-roman-shipwreck-in-italy/
2026-08-11 | Global | Hyperallergic | National Gallery of Art Protects Works Ahead of Trump's IndyCar Race | https://hyperallergic.com/national-gallery-of-art-protects-works-ahead-of-trumps-indycar-race/
2026-08-11 | Global | The Art Newspaper | UK Ministry of Justice spent more than £85,000 removing Banksy mural from the Royal Courts of Justice | https://www.theartnewspaper.com/2026/08/10/uk-ministry-of-justice-spent-more-than-%C2%A385000-removing-banksy-mural-from-the-royal-courts-of-justice
2026-08-11 | Global | Dezeen | Elon Musk reveals plans for world's largest building | https://www.dezeen.com/2026/08/10/terafab-elon-musk-spacex-tesla-largest-building/
2026-08-11 | Global | Dezeen | Realistic AI architectural renderings must be labelled under EU AI Act | https://www.dezeen.com/2026/08/10/ai-architectural-renderings-eu-ai-act/
