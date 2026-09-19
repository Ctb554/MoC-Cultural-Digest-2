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

<!-- 2026-09-19 reconciliation: this repo's continuity store held NO prior
editions, but the delivery Dropbox folder held 63 delivered editions
(20 Jul - 18 Sep 2026). Prior automated runs delivered but never committed
register/continuity back to main. The entries below reconcile the recent
editions (13-18 Sep 2026) that fall within the realistic 24h-window
collision range for the 19 Sep edition. URLs are exact (audit enforces
URLs); headline/section fields are marked reconciled because a verified
1:1 headline-to-URL mapping was not reconstructed from the .docx. -->
2026-09-13 | archived (reconciled) | aljazeera.com | (reconciled from delivered edition) | https://www.aljazeera.com/news/2026/9/12/iraq-probes-drone-strikes-on-saudi-arabia-shuts-three-crossings-to-iran
2026-09-13 | archived (reconciled) | archaeologymag.com | (reconciled from delivered edition) | https://archaeologymag.com/2026/09/iron-age-salt-mining-complex-beneath-hallstatt/
2026-09-13 | archived (reconciled) | archaeologymag.com | (reconciled from delivered edition) | https://archaeologymag.com/2026/09/limestone-blocks-hint-at-a-etruscan-building-in-italy/
2026-09-13 | archived (reconciled) | billboard.com | (reconciled from delivered edition) | https://www.billboard.com/music/music-news/stray-kids-rock-in-rio-brazil-debut-review-recap-1236338948/
2026-09-13 | archived (reconciled) | deadline.com | (reconciled from delivered edition) | https://deadline.com/2026/09/paramount-job-losses-california-exit-antitrust-lawsuit-1237099942/
2026-09-13 | archived (reconciled) | emirates247.com | (reconciled from delivered edition) | https://www.emirates247.com/uae/35th-abu-dhabi-international-book-fair-opens-tomorrow-with-1500-events-and-exhibitors-from-95-countries/5564
2026-09-13 | archived (reconciled) | hollywoodreporter.com | (reconciled from delivered edition) | https://www.hollywoodreporter.com/movies/movie-features/your-mother-your-mother-your-mother-john-cho-interview-1236698846/
2026-09-13 | archived (reconciled) | nbcnews.com | (reconciled from delivered edition) | https://www.nbcnews.com/world/middle-east/saudi-arabia-shutdown-key-pipeline-limits-oil-flow-yemen-houthis-rcna597362
2026-09-13 | archived (reconciled) | presstv.co.uk | (reconciled from delivered edition) | https://www.presstv.co.uk/Detail/2026/09/12/776155/Iraqi-resistance-denies-involvement-attacks-Saudi-oil-infrastructure
2026-09-13 | archived (reconciled) | vanguardngr.com | (reconciled from delivered edition) | https://www.vanguardngr.com/2026/09/houthi-in-yemen-bombs-saudi-arabia/
2026-09-13 | archived (reconciled) | variety.com | (reconciled from delivered edition) | https://variety.com/2026/film/news/andrew-scott-tiff-elsinore-gay-actors-prejudice-fleabag-1236859840/
2026-09-14 | archived (reconciled) | gulfnews.com | (reconciled from delivered edition) | https://gulfnews.com/uae/abu-dhabi-international-book-fair-2026-opens-at-adnec-1.500672808
2026-09-14 | archived (reconciled) | heritagedaily.com | (reconciled from delivered edition) | https://www.heritagedaily.com/2026/09/ancient-shipwrecks-reveal-lost-history-beneath-the-red-sea
2026-09-14 | archived (reconciled) | hollywoodreporter.com | (reconciled from delivered edition) | https://www.hollywoodreporter.com/movies/movie-reviews/babies-review-anna-kendrick-seth-rogen-lauren-miller-rogen-1236699421/
2026-09-14 | archived (reconciled) | middleeasteye.net | (reconciled from delivered edition) | https://www.middleeasteye.net/live-blog/live-blog-update/houthis-say-saudi-arabia-launched-over-50-strikes-against-them-24-hours
2026-09-14 | archived (reconciled) | nytimes.com | (reconciled from delivered edition) | https://www.nytimes.com/2026/09/12/world/middleeast/yemen-iran-war-houthis.html
2026-09-14 | archived (reconciled) | thecanadianpressnews.ca | (reconciled from delivered edition) | https://www.thecanadianpressnews.ca/entertainment/seth-rogen-man-with-the-best-heart-and-worst-laugh-in-hollywood-honoured-at-tiff/article_04c192cc-3e12-556d-808b-e8d24a54e3d3.html
2026-09-14 | archived (reconciled) | theguardian.com | (reconciled from delivered edition) | https://www.theguardian.com/world/2026/sep/14/saudi-pipeline-drone-attack-houthis-global-oil-supply-prices
2026-09-14 | archived (reconciled) | ua.news | (reconciled from delivered edition) | https://ua.news/en/culture/saudivska-kinokomisiia-bere-uchast-u-tiff-u-kanadi
2026-09-14 | archived (reconciled) | variety.com | (reconciled from delivered edition) | https://variety.com/2026/film/global/tiff-2026-20-international-titles-to-track-1236860336/
2026-09-15 | archived (reconciled) | aljazeera.com | (reconciled from delivered edition) | https://www.aljazeera.com/news/2026/9/14/yemen-govt-forces-advance-in-taiz-as-houthis-claim-attack-on-saudi-arabia
2026-09-15 | archived (reconciled) | archaeology.org | (reconciled from delivered edition) | https://archaeology.org/news/2026/09/14/denisovan-fossils-and-possible-tools-uncovered-in-china/
2026-09-15 | archived (reconciled) | archdaily.com | (reconciled from delivered edition) | https://www.archdaily.com/1185029/saga-space-architects-and-3dcp-group-complete-36-unit-3d-printed-student-village-in-denmark
2026-09-15 | archived (reconciled) | arkeonews.net | (reconciled from delivered edition) | https://arkeonews.net/1300-year-old-mosque-with-early-islamic-inscriptions-unearthed-in-saudi-arabia/
2026-09-15 | archived (reconciled) | arkeonews.net | (reconciled from delivered edition) | https://arkeonews.net/who-was-the-mysterious-gallic-warrior-buried-in-britain-with-a-unique-2000-year-old-helmet/
2026-09-15 | archived (reconciled) | blooloop.com | (reconciled from delivered edition) | https://blooloop.com/news/manchester-museum-mummy-removed-display
2026-09-15 | archived (reconciled) | blooloop.com | (reconciled from delivered edition) | https://blooloop.com/news/teamlab-new-exhibition-tokyo-ariake
2026-09-15 | archived (reconciled) | coloradosun.com | (reconciled from delivered edition) | https://coloradosun.com/2026/09/14/one-michelin-star-for-colorado-restaurants/
2026-09-15 | archived (reconciled) | deadline.com | (reconciled from delivered edition) | https://deadline.com/2026/09/box-office-practical-magic-2-global-1237100627/
2026-09-15 | archived (reconciled) | eurasiareview.com | (reconciled from delivered edition) | https://www.eurasiareview.com/15092026-how-cascading-crises-are-testing-saudi-arabias-foundations-oped/
2026-09-15 | archived (reconciled) | foreignpolicy.com | (reconciled from delivered edition) | https://foreignpolicy.com/2026/09/14/houthi-strikes-yemen-red-sea-saudi-arabia-iran-east-west-oil-pipeline/
2026-09-15 | archived (reconciled) | hrw.org | (reconciled from delivered edition) | https://www.hrw.org/news/2026/09/15/yemen-new-attacks-by-houthi-include-likely-war-crimes
2026-09-15 | archived (reconciled) | publishersweekly.com | (reconciled from delivered edition) | https://www.publishersweekly.com/pw/by-topic/industry-news/book-deals/article/101220-book-deals-week-of-september-14-2026.html
2026-09-15 | archived (reconciled) | theguardian.com | (reconciled from delivered edition) | https://www.theguardian.com/world/2026/sep/15/houthi-rebels-seize-red-sea-hanish-islands-saudi-oil-warning
2026-09-15 | archived (reconciled) | thenationalnews.com | (reconciled from delivered edition) | https://www.thenationalnews.com/business/energy/2026/09/14/oil-nears-108-after-saudi-arabia-shuts-pipeline-amid-attacks/
2026-09-15 | archived (reconciled) | wwd.com | (reconciled from delivered edition) | https://wwd.com/runway/spring-2027/new-york/magda-butrym/review/
2026-09-16 | archived (reconciled) | aljazeera.com | (reconciled from delivered edition) | https://www.aljazeera.com/news/2026/9/15/houthis-report-air-strikes-in-yemen-after-saudi-arabia-vows-firm-response
2026-09-16 | archived (reconciled) | archaeology.org | (reconciled from delivered edition) | https://archaeology.org/news/2026/09/15/early-mosque-uncovered-in-saudi-arabias-al-baha-province/
2026-09-16 | archived (reconciled) | archaeology.org | (reconciled from delivered edition) | https://archaeology.org/news/2026/09/15/italian-officials-unveil-ancient-romes-largest-wall-mosaic/
2026-09-16 | archived (reconciled) | archaeology.org | (reconciled from delivered edition) | https://archaeology.org/news/2026/09/15/troys-earliest-agora-unearthed/
2026-09-16 | archived (reconciled) | archdaily.com | (reconciled from delivered edition) | https://www.archdaily.com/1185003/20-practices-expanding-architectures-agency-winners-of-the-archdaily-2026-next-practices-awards
2026-09-16 | archived (reconciled) | billboard.com | (reconciled from delivered edition) | https://www.billboard.com/music/rock/noel-gallagher-moment-oasis-knew-going-back-on-tour-new-music-1236340326/
2026-09-16 | archived (reconciled) | bloomberg.com | (reconciled from delivered edition) | https://www.bloomberg.com/news/articles/2026-09-15/mbs-and-saudi-arabia-face-crisis-with-key-oil-pipeline-shut-for-weeks
2026-09-16 | archived (reconciled) | cnbc.com | (reconciled from delivered edition) | https://www.cnbc.com/2026/09/15/oil-prices-saudi-arabia-east-west-pipeline-iran.html
2026-09-16 | archived (reconciled) | deadline.com | (reconciled from delivered edition) | https://deadline.com/2026/09/2026-emmys-analysis-widows-bay-1237103690/
2026-09-16 | archived (reconciled) | koreaherald.com | (reconciled from delivered edition) | https://www.koreaherald.com/article/10874594
2026-09-16 | archived (reconciled) | presstv.co.uk | (reconciled from delivered edition) | https://www.presstv.co.uk/Detail/2026/09/15/776310/Saudi-regime-seeks-British-strikes-on-Yemen-after-US-refusal
2026-09-16 | archived (reconciled) | publishersweekly.com | (reconciled from delivered edition) | https://www.publishersweekly.com/pw/by-topic/industry-news/publisher-news/article/101236-2026-national-book-award-longlists-announced.html
2026-09-16 | archived (reconciled) | scenenoise.com | (reconciled from delivered edition) | https://scenenoise.com/Features/SceneNoise-x-Amsterdam-Dance-Event-Present-CROSSFADE-Saudi-Arabia
2026-09-16 | archived (reconciled) | semafor.com | (reconciled from delivered edition) | https://www.semafor.com/article/09/15/2026/saudi-arabia-under-tense-military-pressure-from-iran-houthis
2026-09-16 | archived (reconciled) | smithsonianmag.com | (reconciled from delivered edition) | https://www.smithsonianmag.com/smart-news/closed-to-public-since-wwii-hidden-gallery-at-london-natural-history-museum-opens-doors-once-again-180989380/
2026-09-16 | archived (reconciled) | theartnewspaper.com | (reconciled from delivered edition) | https://www.theartnewspaper.com/2026/09/15/new-york-galleries-moving-manhattan-soho-rising-chelsea-tribeca-endure
2026-09-16 | archived (reconciled) | theguardian.com | (reconciled from delivered edition) | https://www.theguardian.com/world/2026/sep/16/saudi-arabia-houthi-drone-shot-down-mecca-iran-middle-east
2026-09-16 | archived (reconciled) | tradearabia.com | (reconciled from delivered edition) | https://tradearabia.com/News/486255/Saudi-design-leaders-emerging-talent-set-the-agenda-at-Index-expo
2026-09-16 | archived (reconciled) | wwd.com | (reconciled from delivered edition) | https://wwd.com/runway/spring-2027/new-york/thom-browne/review/
2026-09-17 | archived (reconciled) | artnews.com | (reconciled from delivered edition) | https://www.artnews.com/art-news/news/liang-shaoji-dead-chinese-artist-silkworms-1234798463/
2026-09-17 | archived (reconciled) | artnews.com | (reconciled from delivered edition) | https://www.artnews.com/art-news/news/thyssen-bornemisza-museum-expand-second-location-madrid-1234798467/
2026-09-17 | archived (reconciled) | bnnbloomberg.ca | (reconciled from delivered edition) | https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/09/16/director-danny-boyle-defends-use-of-ai-in-new-film-ink-at-tiff-screening/
2026-09-17 | archived (reconciled) | broadcastprome.com | (reconciled from delivered edition) | https://www.broadcastprome.com/news/film-alula-partners-with-sherborne-media-to-boost-production-financing/
2026-09-17 | archived (reconciled) | cairoscene.com | (reconciled from delivered edition) | https://cairoscene.com/ArtsAndCulture/Hafez-Gallery-Makes-Frieze-London-Debut-With-Two-Artist-Showcase
2026-09-17 | archived (reconciled) | hyperallergic.com | (reconciled from delivered edition) | https://hyperallergic.com/met-museum-breaks-ground-on-new-modern-and-contemporary-wing/
2026-09-17 | archived (reconciled) | nbcnews.com | (reconciled from delivered edition) | https://www.nbcnews.com/politics/trump-administration/trumps-handpicked-kennedy-center-board-votes-close-venue-renovations-rcna597921
2026-09-17 | archived (reconciled) | news.artnet.com | (reconciled from delivered edition) | https://news.artnet.com/art-world/giotto-and-cimabue-masterpieces-in-assisi-get-a-ultra-hd-digital-revival-2811536
2026-09-17 | archived (reconciled) | nytimes.com | (reconciled from delivered edition) | https://www.nytimes.com/2026/09/16/business/saudi-pipeline-houthi-attacks.html
2026-09-17 | archived (reconciled) | presstv.co.uk | (reconciled from delivered edition) | https://www.presstv.co.uk/Detail/2026/09/16/776408/Yemeni-Armed-Forces-target-Aramco-facilities,-King-Khalid-Air-Base-in-Saudi-Arabia
2026-09-17 | archived (reconciled) | theguardian.com | (reconciled from delivered edition) | https://www.theguardian.com/world/2026/sep/16/us-officials-decide-against-backing-saudi-arabia-yemen-meeting-houthi-leaders
2026-09-17 | archived (reconciled) | tribune.com.pk | (reconciled from delivered edition) | https://tribune.com.pk/story/2629641/us-urges-travellers-to-reconsider-saudi-arabia-trips-over-iranian-drone-missile-threat
2026-09-17 | archived (reconciled) | washingtontimes.com | (reconciled from delivered edition) | https://www.washingtontimes.com/news/2026/sep/16/smithsonians-national-zoo-breaks-ground-arabian-leopard-exhibit-open/
2026-09-17 | archived (reconciled) | wmagazine.com | (reconciled from delivered edition) | https://www.wmagazine.com/fashion/dario-vitale-emporio-armani-creative-director
2026-09-18 | archived (reconciled) | aljazeera.com | (reconciled from delivered edition) | https://www.aljazeera.com/news/2026/9/17/five-killed-as-saudi-arabia-and-yemens-houthis-trade-attacks
2026-09-18 | archived (reconciled) | aljazeera.com | (reconciled from delivered edition) | https://www.aljazeera.com/news/2026/9/17/trump-administration-approves-sale-of-f-35-jets-to-saudi-arabia
2026-09-18 | archived (reconciled) | arkeonews.net | (reconciled from delivered edition) | https://arkeonews.net/new-laser-scans-reveal-six-groups-of-ancient-ships-on-a-3000-year-old-wall-in-cyprus/
2026-09-18 | archived (reconciled) | arkeonews.net | (reconciled from delivered edition) | https://arkeonews.net/rare-2000-year-old-celtic-silver-hoard-found-beneath-a-former-sports-field/
2026-09-18 | archived (reconciled) | artreview.com | (reconciled from delivered edition) | https://artreview.com/islamic-arts-biennale-2027-names-lead-curators/
2026-09-18 | archived (reconciled) | cnbc.com | (reconciled from delivered edition) | https://www.cnbc.com/2026/09/17/oil-prices-today-wti-brent-hormuz-iran-war.html
2026-09-18 | archived (reconciled) | deadline.com | (reconciled from delivered edition) | https://deadline.com/2026/09/dubai-film-festival-return-saudi-red-sea-film-uncertain-1237106423/
2026-09-18 | archived (reconciled) | dezeen.com | (reconciled from delivered edition) | https://www.dezeen.com/2026/09/17/dezeen-awards-2026-master-jury/
2026-09-18 | archived (reconciled) | mdntvlive.com | (reconciled from delivered edition) | https://mdntvlive.com/saudi-film-nights-makes-historic-south-african-debut-this-october/
2026-09-18 | archived (reconciled) | semafor.com | (reconciled from delivered edition) | https://www.semafor.com/article/09/17/2026/saudi-arabias-well-timed-uranium-find-near-medina
2026-09-18 | archived (reconciled) | time.com | (reconciled from delivered edition) | https://time.com/collection/time100-art/2026/dana-awartani/
2026-09-18 | archived (reconciled) | washingtonian.com | (reconciled from delivered edition) | https://washingtonian.com/2026/09/17/michelin-adds-4-new-restaurants-to-its-dc-guide/
2026-09-18 | archived (reconciled) | whowhatwear.com | (reconciled from delivered edition) | https://www.whowhatwear.com/fashion/live/london-fashion-week-spring-summer-2027
