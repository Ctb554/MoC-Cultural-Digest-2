---
name: cultural-digest
description: Generate the MoC Daily Cultural Digest as a finished branded Word document. Use when asked to run, generate, or update the Saudi Ministry of Culture daily cultural digest. Sources news live from the web for the coverage window only, maintains continuity with prior editions via a do-not-reuse register and editorial learnings, builds the .docx, and runs a programmatic audit before delivery.
---

# MoC Daily Cultural Digest: Unattended Run Playbook

This is the unattended, Claude Code cloud-routine adaptation of the MoC Daily
Cultural Digest brief, following the architecture pattern of the
`conflict-monitoring` skill this was adapted from: a scheduled, fully
autonomous cloud session that clones this repo, sources news live from the
web, writes the digest, builds the branded Word document, self-audits, and
delivers. Run every stage in order. If a hard failure occurs (no web access,
no readable priors), stop and fail loudly; never fabricate around a missing
capability.

**FORMAT CONFIRMED AGAINST REAL PRODUCTION (2026-07-19, corrected 2026-07-21):**
two written specs existed for this digest (an original detailed brief and a
later handoff note), and they disagreed with each other on several points.
Rather than choosing between them, this playbook was corrected against an
actual, currently-delivered live edition
(`MOC_Daily_Cultural_Digest_19Jul26_D1.docx`, produced by the existing manual
process this repo is meant to automate). Where the live edition settles a
disagreement between the two written specs, the live edition wins. Confirmed
findings:

- **Headline bullets come first**, before the full summaries (matches the
  original brief, not the handoff note).
- **Commission labels are plain English, colon-terminated (e.g. "Heritage:",
  "Visual Arts:"), NOT bilingual.** This was corrected 2026-07-21 against an
  earlier real edition (16 July, chronologically before the 19 July one
  above) which used no Arabic anywhere. The user confirmed directly: the
  whole document gets translated into Arabic as a separate downstream step,
  so the English edition's own labels don't need to carry Arabic at all.
  The bilingual convention this playbook used between 2026-07-20 and
  2026-07-21 is superseded — see the Classification rules section below.
- **Bullet style is free-form analytical prose ending in a plain "(Outlet)"
  citation** — not the handoff's rigid "[Outlet] reported that X. The
  article is relevant as a Y item..." template. This matches the original
  brief's looser instruction ("one concise analytical bullet explaining why
  it matters") much more closely.
- **Risks and Opportunities each contain multiple numbered items** (the
  reference edition has two of each), every item with a short bold headline,
  an analytical paragraph, then Source and Consideration lines. This matches
  neither original spec exactly and is its own confirmed pattern.
- **The Negative Articles section has no commission subheadings** — bullets
  sit directly under the section, since negative/reputational stories are
  almost never culture-commission stories anyway.
- **Base font is 11pt, not 12pt** (corrected 2026-07-21 against the 16 July
  edition's docDefaults) — see the formatting values in `scripts/build_docx.py`
  for the complete, current, confirmed set (colors, hyperlink color,
  paragraph spacing convention).

If practice drifts further, or a different reference edition contradicts
this one, re-derive from the most recent real delivered edition, not from
either original written spec.

## Routine run constants

- The repository default branch (`main`) is the continuity store. Each run
  clones it fresh; everything a future run must remember has to be committed
  and pushed before the run ends.
- Coverage window: last 24 hours from run start, unless the run is invoked
  with an explicit different window.
- **Delivery destination, for now, is a test folder** (`05_Claude Test`
  inside the real MoC Dropbox workstream), **not** the live production folder
  the manual process delivers into. This automation is meant to eventually
  replace that manual process, but has not been cut over yet — do not write
  to, or infer the path of, the live production delivery folder.
- **This pipeline produces the English digest only.** The real production
  workflow also produces a full Arabic translation of the entire document as
  a separate downstream step (see the live workstream's own
  `Instructions for AR Translation` material), handled outside this
  automation for now. Do not attempt to generate a full Arabic translation
  of the digest. **As of 2026-07-21, this pipeline produces NO Arabic text
  at all** — commission labels are plain English (see the Classification
  rules in Stage 3), since the confirmed downstream translation step makes
  bilingual labels in the English edition unnecessary. Arabic anywhere in
  this pipeline's output is a hard audit failure (Stage 5).

## Critical context

**Fully unattended, no interactive gates.** No stage of this playbook asks
the user to review, approve, or confirm anything mid-run. Every gate is a
self-audit the run performs itself and records in the run log. The only two
terminal states are a delivered digest and a loud, clearly explained failure.
If a decision point arises that the rules don't cover, make the call that
best serves the accuracy and source-eligibility gates, record it in the run
log, and proceed.

**Recipient.** The Saudi Ministry of Culture. Client-facing, polished,
professional, media-intelligence tone. The team reviews before circulation,
but the first pass must be near-final.

**Accuracy is non-negotiable.** Every article, headline, and summary must
come from a real, live web source found in this run, with a working link.
Nothing may be written from the model's background knowledge. If the web
cannot confirm it in this run, it does not go in the digest.

**GB English throughout**, per the handoff note.

## Stage 0: capability check (mandatory, first)

1. **Web**: run one test WebSearch (e.g. "Saudi Arabia culture news today")
   and test WebFetch against two or three results. Attribute fetch failures
   correctly: an environment policy block (`x-deny-reason: host_not_allowed`,
   or every domain failing uniformly) means the routine's network access
   isn't Full — stop and report exactly that. A site-side bot wall or
   paywall (routine for Reuters, FT, NYT, WaPo, Bloomberg, WSJ from cloud
   IPs) is normal, not a policy problem; the capability gate passes as long
   as at least one news domain fetches real content.
2. **Template**: if `templates/` contains a pinned branded template with a
   recorded SHA-256 (see `templates/README.md`), verify the hash matches
   before building. Until a real branded MoC template is supplied, the
   digest builds as a clean, professionally formatted document from scratch
   via `scripts/build_docx.py` — no template gate applies yet.
3. **Priors**: confirm `reports/` contains at least one prior digest and
   `reports/do_not_reuse_register.md`.
4. **Reader path** (sourcing, non-fatal): check whether `TAVILY_API_KEY` is
   set (primary path for bot-walled premium wires) or a reader MCP connector
   is available (fallback: any tool whose name contains `extract`, `scrape`,
   `reader`, or `read_url`). Note which is available in the run log;
   generation proceeds either way, with reduced body-text depth on premium
   wires if neither is present.
5. **Delivery credentials** (non-fatal): check for Dropbox upload
   credentials (`DROPBOX_APP_KEY`, `DROPBOX_APP_SECRET`,
   `DROPBOX_REFRESH_TOKEN`) and/or email variables (see SETUP.md). Note
   their state; the repo commit is the delivery floor regardless.

## Stage 0.5: sync manual revisions

If a Dropbox connector or destination is configured, sweep it for manually
revised drafts (higher `_D<n>` than recorded) or `_FINAL` versions of recent
digests, following the same pattern as the conflict-monitoring skill this was
adapted from: archive, transcribe verbatim, reconcile the do-not-reuse
register, and run the learning procedure (Stage 3.5 preferences) on each
before generating, so this run already writes to the corrected standard.
Skip silently if no delivery destination is configured yet.

## Stage 1: ingest priors

1. Read the three most recent prior digests in `reports/` in full (the
   `_FINAL` version if one exists for an edition, otherwise the highest
   `_D<n>` draft).
2. Read `reports/do_not_reuse_register.md` in full — every article link and
   headline used in recent editions.
3. Read `reports/editorial_learnings.md` and apply its **Standing
   preferences** while writing. Treat **Observations** as context.
4. Build the do-not-reuse lists across the priors and the register combined:
   article URLs (and near-duplicates) and headlines already used.
5. **Cross-edition consistency check (strengthened 2026-07-20).** Note
   recurring Risks/Opportunities themes from the prior digests (e.g. an
   ongoing regional tension, an ongoing positive narrative arc like a
   festival season or Vision 2030 milestone) so today's synthesis reads as a
   continuation where genuinely still live, not a restart — without forcing
   continuity where the news cycle has actually moved on. **This is not
   just about tone continuity — it is a hard check against direct
   contradiction.** Before finalizing today's Risks/Opportunities, compare
   each item against what the prior editions said about the same or a
   closely related ongoing situation (an active conflict, a recurring
   reputational theme, an ongoing infrastructure or policy story). If
   today's Consideration would recommend something that contradicts a
   prior edition's Consideration on the same live situation — e.g.
   yesterday said "keep the cultural story deliberately separate from this
   narrative" and today would say "lean into direct engagement with it" —
   do not write the contradiction silently. Either the situation has
   genuinely changed enough to justify a different recommendation, in which
   case say so explicitly ("unlike yesterday's assessment, X has now
   changed because Y"), or the framing should stay consistent with the
   prior edition rather than drift for no stated reason.

## Stage 2: source the news (live web, window-bounded)

Use WebSearch to discover, then WebFetch to verify. Run all Boolean searches
below across the last 24 hours (adjust the window only if explicitly told to).

### Credit discipline: free discovery, paid extraction only for the final report

Same split as the conflict-monitoring skill: discovery, verification, and
selection run entirely on free WebSearch/WebFetch (snippets, syndicated
copies, second-source corroboration for bot-walled premium wires). The
metered Tavily reader is spent only afterward, on the selected articles
WebFetch can't read.

**Verified 2026-07-20 via a dedicated 9-article diagnostic (3 each from
Bloomberg, Reuters, FT) — use these findings, not assumptions, when deciding
how to spend Tavily credits:**

- **Use `extract_depth: advanced`, not `basic`.** At `basic` depth, Tavily
  only succeeded on 2 of 9 test articles — essentially luck. At `advanced`
  depth, it succeeded on all 6 Bloomberg and Reuters articles. `basic` was
  the original spec's assumption for cost reasons; the diagnostic showed
  that assumption throws away roughly two-thirds of Tavily's real value.
  Accept the higher per-call cost of `advanced` — it's the difference
  between "barely helps" and "genuinely unlocks two major wire services."
- **Bloomberg and Reuters: Tavily at `advanced` depth works well.** Both
  went from completely unreachable (Bloomberg hard-403s on WebFetch;
  Reuters can't even be attempted — see below) to fully readable, correct
  title, real byline, substantive content.
- **FT: currently a dead end regardless of method.** 0 of 3 test articles
  succeeded at any depth. Some calls returned HTTP 200 but the actual
  content was a paywall interstitial ("Subscribe to read") or bare page
  navigation chrome with zero substantive text — verified by checking
  actual content (byline presence, on-topic mention count, title match),
  not just Tavily's own success/failure flag, which can be misleading on
  its own. **Do not keep retrying FT expecting a different result** — treat
  it as unreachable for now. A larger future sample could revisit this, but
  three clean failures is enough to stop treating FT as "should eventually
  work."
- **Reuters and FT can't even be discovered via plain WebSearch** — this is
  a separate, more structural problem than the extraction/paywall issue
  above. WebSearch itself returns a categorical "not accessible" error for
  both domains, meaning the normal "free WebSearch discovers, Tavily only
  extracts" split doesn't work for these two outlets specifically — there's
  nothing for WebFetch/Tavily to extract if WebSearch can never surface a
  URL in the first place. **Workaround: when a Reuters or FT lead needs
  discovering specifically** (e.g., the General/Macro Press search is
  clearly missing coverage from one of these two), use Tavily's own search
  function to find the URL, then its extraction to read it — both steps
  spend credits, which is a real cost increase versus the original
  free-discovery assumption. Don't do this routinely for every search; only
  when there's a specific, otherwise-unfindable lead worth spending the
  extra credit on.
- **Credit usage will be higher than originally planned** as a direct
  result of the two points above (`advanced` depth costing more per call,
  and Reuters/FT sometimes needing search credits too, not just
  extraction). Monitor actual monthly usage against the 1,000 free-tier
  credits over the first few weeks rather than assuming the original
  "1-2 credits per edition" estimate still holds.

### RSS pre-filter (Saudi Arabia/Regional only, added 2026-07-20)

Before running the search Booleans below, run
`scripts/rss_saudi_filter.py --hours 24 --output /tmp/rss_candidates.json`.
This is a supplement to the WebSearch-based sweep, not a replacement for
it — it exists because WebSearch depends on a search engine having already
indexed an outlet's latest article, which can lag by hours; an outlet's own
RSS feed updates the instant it publishes. The script pulls ~20 outlets'
own feeds directly (BBC, Guardian, NYT, DW, Middle East Eye,
The Diplomat, Foreign Policy, HeritageDaily, Arkeonews, The Art Newspaper,
Dezeen, ArchDaily, Variety, The Hollywood Reporter, Deadline, WWD, Billboard,
Publishers Weekly, Eater — see the script's `OUTLET_FEEDS` dict for the
current list), filters to items mentioning "Saudi" or "KSA" as a whole word
within the last 24 hours, and writes candidates to a JSON file.

**Every candidate from this script is unverified and must still pass every
normal Stage 2 verification gate** (real, in-window confirmed via WebFetch,
non-Saudi-owned, not previously used) before it can be written into the
digest — this script finds candidates, it does not decide what's true.
Treat its output the same way as any other search result: a starting point
to verify, not a finished fact.

**Feed URL reliability caveat, important for the first several real runs:**
this script was built in a sandboxed environment without general internet
access, so its feed URLs could not be live-tested against the real outlets
before being added here — they're either independently verified or are
long-standing, well-documented feed patterns for these outlets, but some
may have changed or 404 in practice. **The first few real runs should treat
this as a live test**: check which feeds actually resolved (the script logs
failures to stderr) versus which came back empty or errored, and report
this in the run log. An outlet whose feed consistently fails should either
have its URL corrected or be removed from `OUTLET_FEEDS` and left to the
existing WebSearch-based sweep instead — a feed failure here is not fatal,
since every outlet remains covered by the normal outlet sweep regardless.

Outlets known to have **no reliable public RSS feed** (Bloomberg, Reuters,
FT, WSJ, Semafor, Axios, Politico, Al-Monitor, AGBI, Amwaj.media, MEED,
Gulf News, Arabian Business, The National, Nikkei Asia, Al Jazeera, and most
smaller sector trade press) are deliberately not in this script — they rely
entirely on the existing WebSearch-based outlet sweep below, same as before
this addition. **Al Jazeera was removed from this script's outlet list on
2026-07-20** after real operational evidence surfaced from a separate,
already-running RSS project: its feed had gone stale (stopped returning
fresh items) around 2026-06-17. Bloomberg, Reuters, AP, Politico, Gulf News,
MEED, and The National being confirmed stale in that same project's history
corroborates their exclusion here rather than contradicting it — this
script's own "should be correct" confidence is always subordinate to real
operational evidence like this when the two conflict.

### Search Booleans to run

**These three Booleans were made bilingual on 2026-07-21**, after a real
Arabic-language article (`hiamag.com`, a Gulf lifestyle/culture site) was
surfaced by a backup monitoring tool (Talkwalker) that this pipeline's
English-only searches had no way to find. This exposed a structural blind
spot: a large amount of genuine Gulf culture coverage happens in Arabic, and
every search in this playbook was English-only until this fix. The Arabic
terms below are provided directly from a tested, working configuration, not
newly guessed. **Note: these Arabic search terms are internal search inputs,
not output** — they don't conflict with the "no Arabic anywhere in the
digest" rule elsewhere in this playbook, which applies to the delivered
document, not to how the routine searches for content.

**MoC / Minister Boolean:**
`("Saudi Arabia" OR Saudi OR "KSA" OR "السعودية" OR "المملكة العربية السعودية") AND ("Saudi Ministry of Culture" OR "Saudi Arabia's Ministry of Culture" OR "Saudi culture ministry" OR "Saudi MoC" OR "Saudi MOC" OR "وزارة الثقافة" OR "وزارة الثقافة السعودية" OR "Saudi Minister of Culture" OR "Saudi Culture Minister" OR "Saudi Arabia's Culture Minister" OR "Minister of Culture Prince Badr" OR "Saudi Culture Minister Prince Badr" OR "Prince Badr bin Abdullah bin Farhan" OR "Prince Badr bin Abdullah bin Farhan Al Saud" OR "Badr bin Abdullah bin Farhan" OR "Badr bin Abdullah bin Farhan Al Saud" OR "Badr bin Farhan" OR "Prince Badr bin Farhan" OR "الأمير بدر بن عبد الله بن فرحان" OR "بدر بن عبد الله بن فرحان آل سعود" OR "Vice Minister of Culture" OR "Deputy Minister of Culture" OR "Saudi Vice Minister of Culture" OR "وزير الثقافة" OR "معالي وزير الثقافة" OR "نائب وزير الثقافة" OR "معالي نائب وزير الثقافة" OR "Vice Minister of Culture Hamed Fayez")`

**Commissions Boolean:**
`("Film Commission" OR "Saudi Film Commission" OR "Fashion Commission" OR "Saudi Fashion Commission" OR "Music Commission" OR "Saudi Music Commission" OR "Heritage Commission" OR "Saudi Heritage Commission" OR "Culinary Arts Commission" OR "Theater and Performing Arts Commission" OR "Museums Commission" OR "Museum Commission" OR "Architecture and Design Commission" OR "Visual Arts Commission" OR "Literature, Publishing and Translation Commission" OR "Library Commission" OR "Language Commission" OR "Saudi culture commission" OR "Saudi cultural commission" OR "هيئة الأفلام" OR "هيئة الأزياء" OR "هيئة الموسيقى" OR "هيئة التراث" OR "هيئة فنون الطهي" OR "هيئة المسرح والفنون الأدائية" OR "هيئة المتاحف" OR "هيئة العمارة والتصميم" OR "هيئة الفنون البصرية" OR "هيئة الأدب والنشر والترجمة" OR "هيئة المكتبات" OR "هيئة اللغة")`

**Saudi Culture Boolean (broad):**
`("Saudi culture" OR "Saudi cultural" OR "Saudi heritage" OR "Saudi traditions" OR "Saudi traditional" OR "Saudi arts" OR "Saudi art" OR "Saudi artists" OR "Saudi music" OR "Saudi musicians" OR "Saudi film" OR "Saudi cinema" OR "Saudi filmmakers" OR "Saudi fashion" OR "Saudi design" OR "Saudi literature" OR "Saudi cuisine" OR "Saudi food" OR "Saudi dishes" OR "Saudi gastronomy" OR "Saudi coffee" OR "Saudi hospitality" OR "الثقافة السعودية" OR "التراث السعودي" OR "الفنون السعودية" OR "الموسيقى السعودية" OR "السينما السعودية" OR "الموضة السعودية" OR "المطبخ السعودي" OR "القهوة السعودية" OR "الضيافة السعودية")`

**Named Entity Searches** — one unified category, covering outlets, people,
and places. The broad Saudi Culture Boolean above only catches stories using
generic phrasing ("Saudi fashion", "Saudi film", "Saudi heritage"). It misses
coverage that names a specific outlet, person, brand, or site directly
without ever using those generic words — e.g. Vogue covering a named Saudi
designer, or a story about new findings at Hegra that never says "heritage"
or "archaeological." These three groups exist to catch exactly that gap.

**LAST VERIFIED: 2026-07-20.** Named individuals and sites were verified via
live web search as of this date — **all three lists below will go stale**;
re-verify periodically and add newly prominent names/sites as they surface
in real coverage rather than treating any of this as fixed. Update this date
every time the People/Places lists (not just the Outlets Booleans, which
carry their own dated notes above) are re-verified. **Every run must check
this date against today and flag it in the run log/status
(`stale_named_entity_lists` in `reports/last_run_status.json` — see Stage 6)
if it is more than 180 days old** — a stale flag doesn't block the run, but
it's a signal the People/Places lists need a re-verification pass before
they're trusted much further. Run each bullet below as its own separate
search, not one combined query — a combined query dilutes results the same
way the negative themes would. If a search returns nothing on a given day,
that's a normal outcome for a narrow named-entity search, not a failure; do
not pad or force a result, and every hit still passes the standard
verification gates (real, in-window, not previously used).

*Outlets* — pairs `"Saudi Arabia" OR Saudi` with named prestige/trade press, by sector:
- **General/Macro Press (leads the Saudi Arabia/Regional section — see Stage 3 ordering rule; targets and outlet list both expanded 2026-07-20).** Rewritten to fix the same dilution problem the Global section had before its direct outlet sweep: previously this was one combined query across ~25 outlets at once (`("Saudi Arabia" OR Saudi OR KSA) AND (Bloomberg OR "Financial Times" OR ...)`), which underperforms for exactly the same reason a single "Direct outlet sweep" call for Global would have — one giant OR-query buries individual outlets' results rather than actually checking each one. **Go through the outlets below one at a time, in order, each its own search pairing that single outlet's name with "Saudi Arabia" — not one combined query.** Work through the entire list every run; don't stop early once the target below is hit, since a later outlet in the list might still turn up something better than an earlier one. Record which outlets yielded nothing, same as the Global sweep:
  Bloomberg, Financial Times, Semafor, The Economist, Wall Street Journal,
  Axios, Politico, Reuters, Associated Press, AFP, New York Times, The Times,
  Sunday Times, The Telegraph, BBC, Guardian, Washington Post, CNBC, Deutsche
  Welle, Le Monde, Le Figaro, Der Spiegel, Nikkei Asia, Foreign Policy,
  Foreign Affairs, The Diplomat, AGBI, Arabian Business, Al-Monitor,
  Amwaj.media, MEED, Gulf News, Middle East Eye, Al Jazeera.
  **Target: 3-4 verified, in-window geopolitical/general-news items about
  Saudi Arabia to lead the Saudi Arabia/Regional section**, per the Stage 3
  ordering rule below — this is the concrete number the ordering rule's "up
  to 3-4" cap was always meant to describe, made explicit and tied directly
  to working through the outlet list above, not left as a vague ceiling.
  Same discipline as everywhere else in this playbook: hit the target with
  real, verified items or fall genuinely short — never pad with a weak or
  marginal story to reach 3-4.
  BBC, Guardian, Washington Post, CNBC, DW, Le Monde, Le Figaro, and Der
  Spiegel were missing from this Saudi-paired list entirely until this
  revision — they previously only existed in the generic Global-culture
  outlet list (which doesn't pair them with Saudi Arabia at all), the exact
  same gap Reuters and AP had before the 2026-07-20 fix earlier that day.
  Verified additions here (Nikkei Asia, Foreign Policy, Foreign Affairs, The
  Diplomat, AGBI, Arabian Business, Al-Monitor, Amwaj.media, MEED, Gulf News,
  The Telegraph) come from a dedicated outlet-verification research pass and
  are all confirmed active, credible, non-Saudi sources as of 2026. **Middle
  East Eye and Al Jazeera are included but flagged**: Middle East Eye's
  funding is opaque and widely linked to Qatar; Al Jazeera is funded by the
  Qatari state (Qatar Media Corporation). Neither is excluded, but their
  framing on politically sensitive Gulf topics should be read as reflecting
  Doha's interests, not treated as neutral.
- **Fashion:** `("Saudi Arabia" OR Saudi) AND (Vogue OR "Vogue Arabia" OR WWD OR "Harper's Bazaar Arabia" OR Elle OR GQ OR "Business of Fashion" OR Hypebeast OR "The Fashion Law")`
- **Film:** `("Saudi Arabia" OR Saudi) AND (Variety OR "Hollywood Reporter" OR "Screen Daily" OR Deadline OR IndieWire OR "Sight and Sound" OR "Little White Lies" OR "MUBI Notebook")`
- **Architecture and Design:** `("Saudi Arabia" OR Saudi) AND ("Architectural Digest" OR Dezeen OR ArchDaily OR "Wallpaper*" OR Designboom OR "The Architectural Review" OR Metropolis OR "The Architect's Newspaper")`
- **Music:** `("Saudi Arabia" OR Saudi) AND (Billboard OR "Rolling Stone" OR Pitchfork OR NME OR "Resident Advisor" OR "DJ Mag")`
- **Visual Arts and Heritage:** `("Saudi Arabia" OR Saudi) AND (Artforum OR ArtNews OR "The Art Newspaper" OR Hyperallergic OR Frieze OR Ocula OR Colossal OR "Artnet News" OR "ArtReview" OR Apollo)`
- **Archaeology and Heritage News:** `("Saudi Arabia" OR Saudi) AND (HeritageDaily OR Arkeonews OR "Archaeology Magazine" OR "Live Science" OR "Current Archaeology" OR "Popular Archaeology" OR "Ancient Origins")`. New category added 2026-07-20 — the Places search below only catches stories naming a specific site; this catches heritage/archaeology news outlets covering Saudi Arabia's archaeology sector generally, even when no specific named site is mentioned.
- **Culinary Arts:** `("Saudi Arabia" OR Saudi) AND (Eater OR "Bon Appétit" OR "Food and Wine" OR Michelin OR "Michelin Guide" OR "Fine Dining Lovers" OR "World's 50 Best")`
- **Literature, Publishing, and Translation:** `("Saudi Arabia" OR Saudi) AND ("Publishers Weekly" OR "The Bookseller" OR "London Review of Books" OR "LRB")`
- **Museums:** `("Saudi Arabia" OR Saudi) AND ("Museums Journal" OR "Apollo Magazine" OR Blooloop OR "MuseumNext" OR "Museum-iD")`
- **Theatre and Performing Arts:** `("Saudi Arabia" OR Saudi) AND ("The Stage" OR Playbill OR "American Theatre")`. New category added 2026-07-20 — this commission previously had no dedicated named-outlet search at all, only the generic Commissions Boolean.
- **Travel/lifestyle (heritage and tourism crossover):** `("Saudi Arabia" OR Saudi) AND ("Condé Nast Traveler" OR "Travel and Leisure" OR AFAR OR "Travel and Tour World" OR "Hotelier Middle East" OR "Outlook Traveller")`

**Named Festivals, Venues & Programs (added 2026-07-21, from a 6-month
coverage-frequency review of international media Feb-Jul 2026).** The broad
Saudi Culture Boolean and the Commissions Boolean above miss most of the
specific recurring cultural programs driving actual coverage volume, because
articles about them rarely use generic phrasing like "Saudi culture" — a
piece on Wadi AlFann or Riyadh Fashion Week is Saudi-culture coverage but
won't be caught by either existing Boolean. Run as one combined query (named
programs don't dilute each other the way broad topics do, same reasoning as
the Heritage sites query above):
`("Diriyah Contemporary Art Biennale" OR "Diriyah Biennale" OR "Islamic Arts Biennale" OR "Desert X AlUla" OR "Wadi AlFann" OR "Wadi Al-Fann" OR "AlUla Arts Festival" OR "Winter at Tantora" OR "Riyadh Fashion Week" OR "Saudi 100 Brands" OR "Tuwaiq Sculpture" OR "Riyadh Art" OR "Noor Riyadh" OR "Zarqa Al Yamama" OR "Royal Diriyah Opera House" OR "Saudi Founding Day" OR "Year of Handicrafts" OR "Riyadh University of Arts" OR "Royal Institute of Traditional Arts")`
Classify hits by their actual subject matter using the standard commission
rules (a Diriyah Biennale story → Visual Arts; Riyadh Fashion Week → Fashion;
Zarqa Al Yamama/Royal Diriyah Opera House → Theatre and Performing Arts;
Riyadh University of Arts/Royal Institute of Traditional Arts → General
unless the story is sector-specific). **Coverage-frequency finding this list
is based on:** over the six months reviewed, the Diriyah Contemporary Art
Biennale (3rd edition, JAX District, Jan-May 2026), the Venice Biennale Saudi
Pavilion, and the AlUla cluster (Desert X AlUla, Wadi AlFann's permanent
land-art commissions, AlUla Arts Festival) generated near-continuous
international coverage; Riyadh Fashion Week/Saudi 100 Brands, Tuwaiq
Sculpture, and the Saudi Cultural Years program (Calligraphy → Coffee →
Poetry → Camel → Handicrafts → the current "Year of AI") generated strong
recurring seasonal coverage. Re-verify this list periodically the same way as
the People/Places lists below — festival names and editions change year to
year.

*People* — named cultural figures, by sector:
- **Visual Arts:** `"Ahmed Mater" OR "Abdulnasser Gharem" OR "Ashraf Fayadh" OR "Manal Al Dowayan" OR "Dana Awartani" OR "Shadia Alem" OR "Sarah Abu Abdallah" OR "Sarah Mohanna Al Abdali" OR "Zahrah Al Ghamdi" OR "Safeya Binzagr"`
- **Film:** `"Haifaa Al-Mansour" OR "Haifaa Al Mansour"`
- **Fashion:** `"Waad Aloqaili" OR "Yahya Albishri" OR "Razan Alazzouni" OR "Mona Al Shebil" OR "Adnan Akbar" OR "Tima Abid" OR "Kawthar Alhoraish" OR "Eman Alajlan" OR "Khadija Al Sunaydi"`
- **Commission Leadership (added 2026-07-21, partially verified only — see caveat below):** `"Dina Amin" OR "Sultan Al-Bazie" OR "Hamed Fayez"`. These three are independently confirmed as of 2026-07-21: Dina Amin (Visual Arts Commission CEO since 2020, confirmed still serving via a July 2025 interview), Sultan Al-Bazie (Theatre and Performing Arts Commission CEO, confirmed via the commission's own official site), Hamed Fayez (Vice Minister, already covered above). **The other 8 commissions' CEOs are NOT yet in this list** — research hit a genuine conflict (the Film Commission shows as led by "Abdullah Al-Eyaf" on one source and "Abdullah Alqahtani" on another, not resolved here) and found no confirmed-current name at all for Heritage, Museums, Culinary Arts, Architecture and Design, Literature/Publishing/Translation, Libraries, or Fashion Commission. The Music Commission's only found name (Paul Pacifico) is from a 2022 appointment announcement and needs re-verification, not just re-use, since executive tenures in this space can be short. **Do not add a name to this Boolean without independently verifying it's current** — an unverified or stale name in a government digest's own search list is worse than not having it. Complete this list via a dedicated research pass, or ideally by pulling the confirmed-current roster directly from the Ministry's own site or a trusted internal source, rather than incremental web searches.
- **Fashion Commission (added 2026-07-21):** `"Burak Cakmak"`. Confirmed as Fashion Commission CEO via a direct WWD interview (Oct 2025) discussing Riyadh Fashion Week's growth; this fills the Fashion Commission gap the entry above flags as missing.
- **Non-commission cultural bodies (added 2026-07-21, from the 6-month coverage-frequency review — not commission CEOs, but named figures generating regular international coverage of Saudi cultural programs):** `"Aya Al-Bakree" OR "Suzan Alyahya" OR "Antonia Carver"`. Aya Al-Bakree is CEO of the Diriyah Biennale Foundation (organiser of both the Diriyah Contemporary Art Biennale and the Islamic Arts Biennale) — confirmed via SCMP coverage of the 2026 Diriyah Biennale. Suzan Alyahya is CEO of the Royal Institute of Traditional Arts (Wrth), a Quality of Life Program initiative under the Ministry — confirmed via the institute's own site. Antonia Carver directs Art Jameel (Hayy Jameel, Jeddah) and curated the Saudi Pavilion at the 2026 Venice Biennale — she is not a Saudi government employee, but her name recurs across Saudi Pavilion and Art Jameel coverage often without the words "Saudi culture" appearing. **None of these three should be read as MoC staff or as implying Ministry ownership of their institutions** — the Diriyah Biennale Foundation and Wrth are PIF/Quality-of-Life-Program bodies, and Art Jameel is an independent philanthropic foundation; attribute accurately per the do-not-overclaim rule elsewhere in this playbook.

*Places* — named heritage and archaeological sites, verified against
UNESCO's official list (Saudi Arabia currently has 8 inscribed World
Heritage properties, most recently Al-Faw in 2024) plus other frequently-
covered named sites, including three from Saudi Arabia's tentative list
(Hejaz Railway, Farasan Islands, Rijal Almaa Heritage Village):
- **Heritage sites (one combined query — named places don't dilute each other the way broad topics do):** `(Hegra OR "Al-Hijr" OR "Madain Salih" OR "Mada'in Salih" OR Diriyah OR "At-Turaif" OR "Historic Jeddah" OR "Al-Balad" OR "Jubbah rock art" OR "Rock Art in the Hail Region" OR "Al-Ahsa Oasis" OR "Hima Cultural Area" OR "Najran rock art" OR "Al-Faw archaeological" OR AlUla OR Dadan OR "Jabal Ikmah" OR "Hejaz Railway" OR "Farasan Islands" OR "Rijal Almaa")`
  Classify hits under **Heritage** unless the story is clearly museum-led (→
  Museums) or architecture/design-led (→ Architecture and Design).
- **Named Museums (added 2026-07-21, one combined query):** `("Black Gold Museum" OR "JAX District" OR SAMOCA OR "Saudi Arabia Museum of Contemporary Art" OR Ithra OR "King Abdulaziz Center for World Culture" OR "National Museum of Saudi Arabia" OR "Al Masmak" OR "Masmak Palace" OR "Masmak Fort")`.
  Verified 2026-07-21: Black Gold Museum (KAPSARC, Riyadh — oil/energy
  told through contemporary art, Zaha Hadid-designed building); JAX District
  / SAMOCA (Diriyah — Saudi Arabia's first dedicated contemporary art
  museum); Ithra / King Abdulaziz Center for World Culture (Dhahran — Saudi
  Aramco-built cultural centre with museum, library, cinema, theatre);
  National Museum of Saudi Arabia (Riyadh, part of the King Abdulaziz
  Historical Center); Al Masmak Palace Museum (Riyadh, the 1865 fort central
  to the Kingdom's founding narrative). Classify hits under **Museums**
  unless clearly heritage-preservation-led (→ Heritage) or architecture/
  design-led (→ Architecture and Design). This list is a starting point, not
  exhaustive — Saudi Arabia has more named museums beyond these five (e.g.
  Royal Art Complex, Digital Art Museum, Borderless Jeddah, the Prince
  Mohammad bin Salman International Center for Arabic Calligraphy) that
  weren't independently verified in this pass; add them once confirmed
  rather than assuming they're still open/correctly named.

**Negative/reputational coverage** — run as separate searches per theme, not
one combined query (a combined query drowns culture-adjacent reputational
stories under pure geopolitics on any heavy news day): human rights, labour/
workers, sportswashing, PIF scrutiny, Saudi-Iran/regional geopolitics, oil,
academic freedom, tourism criticism, religious tourism/Mecca commercialization,
Vision 2030 criticism, investment scrutiny, soft power criticism, general
reputation risk.

**Adversarial-framing check on the day's own top Regional story (added
2026-07-21, closes a real regression).** The themed searches above will
usually miss this case: a comparison against a real prior edition (21 July
2026) showed that when the General/Macro Press sweep's lead story concerns
Saudi Arabia directly (e.g. a regional-security or geopolitical event), one
edition correctly pulled a Negative Articles item from it while a later
automated run did not, leaving Negative Articles empty on a day where a real
negative item existed. The cause: none of the themed searches above are
built to catch "the same story, framed adversarially by a different outlet"
— they are categorical (human rights, labour, PIF, etc.), not comparative.
**Required step:** whenever the General/Macro Press sweep surfaces a lead
story that names Saudi Arabia in a geopolitical/security/conflict context,
check 2-3 additional outlets' coverage of that *same* underlying event
specifically for framing that casts Saudi Arabia as aggressor, oppressor, or
otherwise adversarially (watch in particular for outlets with a documented
state-alignment or adversarial-source caveat elsewhere in this playbook,
e.g. Al Jazeera, Middle East Eye, Iranian state media) — this is a distinct
check from corroborating facts, and from the themed searches above. If such
framing exists, it goes in its own Negative Articles item citing the
framing outlet, even though the underlying event is the same one already
covered in Saudi Arabia/Regional/General. Do not treat "we already covered
this story in General" as a reason to skip this check or as grounds to
leave Negative Articles empty — same-event coverage in two sections, each
capturing a different angle (factual event vs. adversarial framing), is the
correct pattern, not a duplicate to avoid. Record in `search_log.json`
whether this check was run and what it found, using the same
`negative_hits_found_in_window` field — a hit found this way counts toward
that total exactly like a themed-search hit.

**Watchdog/NGO monitoring — made mechanical 2026-07-20, same fix as the
other two outlet lists above.** This was previously one combined query
across all named organizations at once — the identical dilution problem
General/Macro Press and the Global outlet list both had before their fixes
earlier the same day. **Go through the organizations below one at a time,
each its own search pairing that single organization's name with "Saudi
Arabia," not one combined query.** Work through the entire list every run.
These organizations regularly publish primary reports and statements on
Saudi Arabia that a generic "human rights" phrase search can miss if the
organization's own release doesn't use that exact wording:
Amnesty International, Human Rights Watch, Freedom House, Reporters Without
Borders (RSF), Committee to Protect Journalists (CPJ), CIVICUS, ALQST,
Democracy for the Arab World Now (DAWN), PEN International.
ALQST and DAWN (founded after Jamal Khashoggi's killing) are Saudi-specific
human-rights organizations, not general MENA-wide ones — their statements
are usually directly about Saudi Arabia rather than requiring the "Saudi
Arabia" pairing to be relevant, but the pairing is kept for consistency and
to filter out unrelated organizational news. As with every other search in
this section, a hit here still has to pass the standard verification gates
(real, in-window, not previously used, non-Saudi-owned source reporting on
it) before inclusion — an NGO's own press release is a primary source, not
automatically a "verified" media report; prefer a credible news outlet's
coverage of the NGO's findings where one exists, and treat the raw NGO
statement as a fallback for verification, not the ideal citation for a
bullet.

**Record the negative/watchdog search results in `reports/search_log.json`**
before moving to Stage 3, regardless of what they turned up. This is the
evidence Stage 5's minimum-coverage ladder (see Stage 5 below) requires to
allow a legitimately empty Negative Articles section — its absence is a hard
audit failure, not a free pass. Minimum schema:

```json
{
  "negative_searches_run": true,
  "negative_themes_searched": ["human rights", "labour/workers", "...", "watchdog/NGO monitoring"],
  "adversarial_framing_check_run": true,
  "adversarial_framing_check_applicable": true,
  "negative_hits_found_in_window": 0
}
```

`adversarial_framing_check_applicable` is `true` only when the General/Macro
Press sweep's lead story names Saudi Arabia in a geopolitical/security/
conflict context (see the Adversarial-framing check above); `false` on a day
with no such lead story, in which case `adversarial_framing_check_run` may
also be `false` without penalty. When applicable is `true`, `run` must also
be `true` or the empty-Negative-Articles justification does not hold —
same fail-closed principle as `negative_searches_run` below.

Set `negative_searches_run: true` only once every theme in this section
(including the watchdog/NGO search) was actually run this cycle — not
planned, not "mostly." If any theme was skipped for any reason, this must
say `false` (or the file must not claim `true`), and the run must then
either go back and run the missing searches or accept the resulting hard
audit failure honestly rather than fabricate the log.

**Global culture** — run broad culture/arts/heritage/museum/film/music/theatre/
fashion/architecture/literature/culinary searches, prioritizing Tier 1 outlets:
BBC, Guardian, FT, NYT, WaPo, AP, Bloomberg, Reuters, AFP, CNBC, Forbes,
Fortune, The Atlantic, The New Yorker, "The Telegraph", "Al Jazeera",
"Middle East Eye", MEED, "Gulf News", Xinhua, China Daily, CGTN, Global
Times, The Hindu, Indian Express, Nikkei Asia, "Foreign Policy", "Foreign
Affairs", "The Diplomat", Kathimerini, ANSA, Repubblica, Corriere, Il Sole 24
Ore, DW, Spiegel, FAZ, Le Monde, Le Figaro, France24, Eater, Saveur,
ArchDaily, Dezeen, Domus, "The Architectural Review", Metropolis,
"The Architect's Newspaper", Architectural Digest, Vogue Business, WWD,
FashionNetwork, FashionUnited, "The Fashion Law", Billboard, NME,
"Resident Advisor", "DJ Mag", ArtReview, Frieze, Art Basel, Designboom,
"The Art Newspaper", Artforum, Ocula, Colossal, "Artnet News", HeritageDaily,
Arkeonews, "Archaeology Magazine", Blooloop, "MuseumNext", "Museum-iD",
"Sight and Sound", "Little White Lies", "MUBI Notebook", "The Stage",
Playbill, "American Theatre", "London Review of Books", Michelin,
"Fine Dining Lovers", "World's 50 Best", AGBI, "Arabian Business",
"Al-Monitor", "Amwaj.media", "Korea Herald", "South China Morning Post",
"The Jakarta Post", "Bangkok Post", Daily Times (Pakistan), Antara News
(Indonesia), Taipei Times, The Standard (Hong Kong), Korea Times, Korea
Economic Daily. This list was expanded 2026-07-20 twice in one day: first
after a real-edition comparison showed the earlier Western-leaning list
missing legitimate Asia-Pacific and South Asia cultural-diplomacy coverage
(a Naadam Festival story, a Pakistani cultural festival in Australia,
Indonesia's creative-economy push, a Taiwan culture-budget story, and a Hong
Kong Book Fair piece all ran that day in outlets not on the prior list), then
again after a dedicated outlet-verification research pass covering general/
macro press, every sector-specific trade press vertical, and non-Western
culture outlets. **Ownership/state-alignment notes carried over from that
research**, since these affect how coverage should be read even though the
outlets remain includable: The National (UAE) is state-owned via
International Media Investments and has documented self-censorship; Middle
East Eye's funding is opaque and widely linked to Qatar; Xinhua, China Daily,
CGTN, and Global Times are Chinese state media; Antara is Indonesian
state-owned; The Standard (Hong Kong) and South China Morning Post lean
pro-Beijing. None of this excludes them, but framing from these outlets on
politically sensitive topics should be treated as reflecting their backers'
interests, not as neutral reporting. Al Jazeera (Qatari state-funded) and
Middle East Eye (opaque, widely linked to Qatar) carry the same caveat here
as in the General/Macro Press note above. Treat this whole list as inherently
incomplete — broaden it further whenever a comparison against a real edition
surfaces another credible outlet this pipeline missed.

**Direct outlet sweep — a required step, separate from the topic searches
above (added 2026-07-20).** A run on 2026-07-20 treated the outlet list
above only as a loose "prefer these if they turn up" signal attached to
generic topic searches (e.g. "heritage news," "museum exhibition"), and
never directly checked what these specialist outlets had actually published
that day. That's not what was intended and undersells exactly the trade
press this list was built for.

**Process (made explicit and mechanical 2026-07-20 — this is not optional
and not a loose suggestion):** Go through the outlet list below one at a
time, in order. For each outlet, run one search checking specifically what
that outlet published in the last 24 hours (e.g. "Ocula latest articles" or
an outlet-restricted search), not a generic topic search that might
happen to surface it. Record, for every single outlet, whether it yielded
an in-window, verified candidate or nothing — do not skip an outlet because
earlier ones already produced enough, and do not stop partway through the
list once a target is hit. Work through the entire list every run:

The Art Newspaper, Ocula, Artnet News, ARTnews, Hyperallergic, HeritageDaily,
Arkeonews, Archaeology Magazine, Blooloop, Variety, The Hollywood Reporter,
Deadline, Screen Daily, Dezeen, ArchDaily, Business of Fashion, WWD,
Billboard, Publishers Weekly, The Bookseller, The Stage, Michelin, Eater.

**Target: compile 8-10 verified, in-window, non-duplicate articles for the
Global section from working through this full list**, supplemented by the
broad topic search above only if the sweep alone doesn't reach that range.
This is the same distinction as the Named Entity Searches for Saudi Arabia/
Regional (Stage 2 above) — those pair the outlet with "Saudi Arabia"; this
is the same outlets, unpaired, checked for their own latest global output.

**This target does not override the verification gates or the "never
pad" principle stated throughout this playbook.** Every one of the 8-10
must still be real, in-window, non-duplicate, and from a non-excluded
outlet — reaching the number with a weak or marginal story is worse than
falling short of it honestly. A zero result from any single outlet in the
sweep is a normal, legitimate outcome for that outlet on a quiet day; the
target is about total volume across the full list, not forcing a hit on
every individual outlet. `scripts/audit_report.py` warns (does not hard-
fail) if the section ends up below 8 — see the minimum-coverage ladder
below for why this stays a warning rather than a block.

### Source eligibility (hard rule, enforced by Stage 5 audit)

- **Exclude all Saudi-based/Saudi-owned outlets** — Arab News, Asharq
  (Al-Awsat), Saudi Gazette, SPA, and any other Saudi-owned outlet, even if
  it surfaces via a broad search. When in doubt about ownership, check before
  using; if still uncertain, don't use it.
- **Exclude all Israeli outlets, always, as a hard rule** — jpost.com,
  Times of Israel, Haaretz, Ynet, i24NEWS, TheMarker, and any other
  Israeli-owned outlet, even if it surfaces via a broad search and even for
  an otherwise neutral or factually solid citation. **This is a deliberate
  reputational-caution decision for a Saudi government deliverable, not a
  claim about these outlets' factual reliability** — the reputational risk
  of citing Israeli media exists for this client regardless of how credible
  or neutral the specific article is. This closes a prior inconsistency
  where jpost.com alone was excluded while Times of Israel/Haaretz/Ynet/i24/
  TheMarker were only flagged as a warning; all are now hard exclusions,
  enforced identically to Saudi-owned outlets in Stage 5's audit. This rule
  is overridable **only by a human editing the digest directly** (e.g. the
  team deciding a specific citation is warranted for a specific edition) —
  no stage of this playbook should ever treat one of these outlets as usable
  on its own initiative.
- **UAE-based credible outlets are allowed.** The National and Al Arabiya are
  explicitly allowed, along with Campaign Middle East.
- Avoid weak, hyper-local, or poor-quality outlets and raw press-release
  wires (e.g. PR Newswire, EIN Presswire) unless they're the only source for
  a genuinely significant story.
- **Use the most authoritative/international source when multiple outlets
  cover the same story; do not pad with weak duplicates.** This rule has one
  genuine ambiguity, exposed by comparing two real 21 July 2026 editions of
  the same underlying event (a Houthi naval blockade on Saudi Arabia): one
  edition wrote three bullets (Nikkei on the oil-export exposure, Bloomberg
  on the coalition's protective response, Euronews on the Bab el-Mandeb
  chokepoint's tourism/heritage exposure); the other wrote one bullet
  (Nikkei only), explicitly reasoning "use the single most authoritative
  source, don't pad duplicates." Both readings are defensible under the rule
  as it was written before this clarification — **this is the resolution:**
  "duplicate coverage" means multiple outlets reporting the *same fact* with
  no material difference in angle (e.g. three wire services all reporting
  "X happened" with the same details) — collapse these to one bullet citing
  the most authoritative source. It does NOT mean multiple outlets covering
  the same underlying event from **materially different, individually
  newsworthy angles** (e.g. one outlet on the market/economic exposure,
  another on the security/diplomatic response, another on the
  tourism/reputational exposure) — these are distinct analytical angles on
  one event and each earns its own bullet, citing its own source, the same
  way the "Adversarial-framing check" above treats a differently-framed
  angle on the same event as its own Negative Articles item rather than a
  duplicate to fold away. The test: would removing this bullet lose an
  analytical point the digest doesn't make anywhere else? If yes, it is not
  a duplicate. If the bullet would say nothing beyond what another bullet on
  the same event already says, it is a duplicate — collapse it.
- Do not pad with weak stories if Saudi/MoC coverage is genuinely limited on
  a given day — a short Saudi/Regional section is more honest than a padded
  one, per the original brief's explicit instruction on this point.
- Wider GCC/regional culture stories are includable only when useful for
  benchmarking and from credible outlets. **Placement: these go under Saudi
  Arabia/Regional, not Global** — confirmed against a real edition
  (2026-07-20) that placed a UAE exhibitions roundup under Saudi Arabia/
  Regional as GCC-benchmarking context, not under Global. This repo's own
  routine had previously placed an equivalent UAE story under Global, which
  was an inconsistency; Saudi Arabia/Regional is the correct section for
  any non-Saudi GCC story used for regional benchmarking.

### Verification gates (every article passes all)

- **Real source.** Appears in actual WebSearch results this run. WebFetch to
  confirm headline and date. If fetch is blocked (bot wall/paywall, routine
  for premium wires), the article may be used only if the URL, exact
  headline, and date come verbatim from search results and a second source
  corroborates the substance. A working link is mandatory regardless — no
  article without a resolvable, direct link to the piece (not a homepage).
- **In-window.** Publication time falls inside the 24-hour coverage window.
- **Not previously used.** Cross-check against the do-not-reuse register and
  the last three editions; do not reuse a headline or link already used
  recently.

## Stage 3: write the content

### Output structure (confirmed against real production)

Two blocks, in this order:

1. **Headline bullets first** — three sections (Saudi Arabia/Regional,
   Negative Articles, Global), each just a plain list of exact article
   headlines, no links, no subheadings.
2. **Full summaries** — the same three sections again, this time with the
   analytical bullets. Within Saudi Arabia/Regional and Global, group
   articles under the approved commission labels (see table below).
   **Negative Articles has no commission subheadings** — its bullets sit
   directly under the section heading.

**Saudi Arabia/Regional ordering rule:** lead the section with a **target of
3-4** General items sourced from the General/Macro Press search (the full
outlet list above — Bloomberg, FT, BBC, Reuters, AP, Guardian, and the rest,
each checked individually, not a combined query) — broad, high-authority
geopolitical and general-news context on Saudi Arabia, not necessarily
culture-specific — before moving into the more specific commission
subsections (Heritage, Visual Arts, etc.). This gives the section a strong
opening anchor. Hit the target with real, verified items; use fewer only if
that many genuinely don't exist after working through the entire outlet
list. Never pad to reach the count — the same "don't force it" principle
applies here as everywhere else in this playbook. The headline-bullet block
at the top of the document inherits this same ordering automatically, since
it must match the full summary's article order.

Then a final **Risks and Opportunities** section (see format below).

Do not invent thematic labels (no "tourism and hospitality", "creative
economy", etc.); anything not clearly fitting a commission goes under
General.

### Classification rules and commission labels

**Changed 2026-07-21: labels are plain English, colon-terminated (e.g.
"Heritage:"), NOT bilingual.** A bilingual `English (Arabic)` convention was
used between 2026-07-20 and 2026-07-21, reverse-engineered from the 19 July
real edition — but a separately-reviewed, chronologically earlier real
edition (16 July) used no Arabic anywhere, and the user confirmed directly
that this is correct: the whole document gets translated into Arabic as a
separate downstream step, so the English edition's own labels don't need to
carry Arabic at all. Every commission label below is written as `Label:` in
the full-summary section (headline bullets stay label-free, since they're
just the article headline). Labels confirmed against real production:

| Label | Classification rule |
|---|---|
| General: | Fallback for anything not fitting a specific commission; **also the home for general/macro/business/policy coverage of Saudi Arabia from elite press** (Bloomberg, FT, Semafor, The Economist, WSJ, Axios, Politico, and the rest of the General/Macro Press list) surfaced by the General/Macro Press search above — see the Stage 3 ordering rule for how these lead the Saudi Arabia/Regional section |
| Heritage: | Archaeology, UNESCO, monuments, preservation, intangible heritage, cultural memory |
| Museums: | Museums, museum programming, museum-led exhibitions |
| Visual Arts: | Galleries, biennales, artists, exhibitions, art markets, unless museum-led |
| Film: | Cinema, production, rebates, festivals, filmmaking |
| Fashion: | Designers, fashion weeks, style, luxury fashion, fashion education |
| Music: | Music industry, artists, concerts, releases |
| Theatre and Performing Arts: | Theatre, dance, opera, stage/live performance |
| Literature, Publishing, and Translation: | Books, authors, publishing, translation, manuscripts, unless library-specific |
| Libraries: | Libraries, archives, library policy |
| Culinary Arts: | Food, cuisine, gastronomy, chefs, culinary heritage, food festivals |
| Architecture and Design: | Architecture, design, urbanism, built environment |

If a story fits multiple labels, use the most specific and strategically
relevant one — a judgment call, not a keyword match. If the label convention
drifts in a future reference edition, re-derive from that edition rather
than this table.

### Bullet format (confirmed against real production)

One bullet per article, free-form analytical prose — not a rigid template.
Two to three sentences: what happened (with attribution and concrete
facts), then the analytical read — why it matters for Saudi Arabia, the
Ministry of Culture, cultural positioning, reputation, investment, tourism,
or global cultural trends. Close with a plain `(Outlet)` citation, the link
attached to the outlet name only.

Example (paraphrased from the reference edition, not to be reused verbatim):
"W Hotels has opened its first Saudi property in Riyadh, with interiors
drawing directly on Saudi cultural heritage — Najdi textiles, Al Sadu
weaving patterns, and a lobby tapestry by a Saudi artist. The design signals
how heritage-rooted storytelling is becoming part of the Kingdom's luxury
hospitality identity. (BW Hotelier)"

- The link lives **only** in the outlet name at the end — never in the first
  sentence, never as a raw URL.
- Flag op-eds, Substacks, and non-English-language pickups explicitly (e.g.
  "DER SPIEGEL's official Substack", "Spanish-language coverage picked up by
  Infobae").
- Do not imply MoC involvement unless the source explicitly states it.
- Avoid inflated language ("groundbreaking", "world-leading", "landmark",
  "unprecedented", "unusually broad pickup") unless clearly and specifically
  evidenced.
- Write in analytical, editorial prose — not the mechanical "[Outlet]
  reported that... The article is relevant as a... item" template; vary
  sentence structure the way a human analyst would.

### Headline bullets

Written **first**, before the full summaries. Exact article headline (verify
by opening the link), in the same order the full summary will later use, no
links, no subheadings, only the three main sections, English only.

### Risks and Opportunities (confirmed against real production)

**Multiple numbered items per subsection** (two is typical, not a fixed
count) — not a single paragraph each. Every item has a short bold headline
naming the specific risk or opportunity, then an analytical paragraph, then
Source and Consideration lines:

```
Risks and Opportunities

Risks

1. [Short bold headline naming the specific risk]
[Analytical paragraph synthesizing the risk from today's coverage.]
Source: Outlet, Outlet
Consideration: [What the Ministry should consider in response.]

2. [Short bold headline naming a second risk, if the day's coverage supports it]
[Paragraph.]
Source: Outlet
Consideration: [Response.]

Opportunities

1. [Short bold headline naming the specific opportunity]
[Analytical paragraph synthesizing the opportunity from today's coverage.]
Source: Outlet, Outlet, Outlet, Outlet
Consideration: [How the Ministry can build on this coverage.]

2. [Short bold headline naming a second opportunity, if supported]
[Paragraph.]
Source: Outlet
Consideration: [Response.]
```

Each subsection (Risks, Opportunities) restarts its own numbering at 1. Item
count should reflect what the day's coverage actually supports — don't force
a second item if only one genuine risk or opportunity exists, and don't
inflate beyond what's honestly supported by sourced material.

Risk angles to draw from: regional conflict/security instability, geopolitical
spillover, human rights scrutiny, labour rights, sportswashing, PIF-linked
scrutiny, censorship/speech/AI bias concerns, mega-project funding/delivery
questions, visitor confidence/tourism risk. Considerations should generally
recommend separating the Ministry's cultural story from broader risk
narratives by foregrounding credible delivery, public access, Saudi talent,
skills/education, institutional professionalism, heritage stewardship, safe
international participation, and genuine cultural exchange.

Opportunity angles: visitor economy, cultural tourism, heritage discoveries,
culinary identity, visual arts and creative districts, fashion education and
talent pathways, film funding and festivals, AI-enabled cultural programming,
architecture and design, international cultural partnerships, skills
development, non-oil growth, Vision 2030 delivery. Considerations should
explain how the Ministry can connect individual stories into a broader
national narrative, not treat them as isolated announcements. Do not overclaim
MoC ownership of stories where the Ministry isn't stated as involved.

### Tone discipline

- Professional, concise, media-intelligence-focused, client-facing.
- GB English throughout.
- No raw URLs anywhere in the body text.
- No casual phrasing, no unsupported claims, no overly long dense paragraphs.
- **The entire document is written in English — no Arabic anywhere**
  (changed 2026-07-21; a prior bilingual-labels convention is superseded,
  see the "FORMAT CONFIRMED AGAINST REAL PRODUCTION" note above). The
  Ministry's own downstream process produces a full Arabic translation
  separately; this pipeline's output should never contain Arabic text.

## Stage 3.5: adversarial review (single pass)

Before building the document, one reviewer pass attacks the complete draft
from an editor's perspective, checking:

- Every hard rule above: source exclusion (no Saudi-owned outlets, and no
  Israeli outlets of any kind, slipped through), link-in-outlet-name-only,
  no raw URLs, GB English, no invented labels, no banned inflated phrases,
  approved commission labels used correctly, no Arabic anywhere in the
  document.
- The standing preferences in `reports/editorial_learnings.md`, so edits the
  team has made before are caught pre-delivery.
- Headline bullets appear first (before full summaries) and match the
  full-summary article order and count.
- Negative Articles has no commission subheadings.
- Risks/Opportunities structure: at least one numbered item per subsection,
  each with a bold headline, paragraph, Source line, and Consideration line.
- The minimum-coverage ladder (Stage 5): Saudi Arabia/Regional and Global
  are not empty; if Negative Articles is empty, `reports/search_log.json`
  has already been written confirming the negative/watchdog searches ran.
- **Cross-edition consistency** (Stage 1, item 5): does any Consideration
  in today's Risks/Opportunities contradict what a prior edition said about
  the same ongoing situation, without explicitly stating that the situation
  changed? If so, fix before delivery — either add the explicit change note
  or bring the framing back in line with the prior edition.
- Every link genuinely resolves — this pass can't run the live Stage 5 URL
  check itself, but it should sanity-check that no link looks fabricated or
  copy-pasted from a different article before Stage 5 catches it mechanically.

Findings are applied unless they'd require fabrication or out-of-window
sourcing; every disposition is logged. Exactly one pass — the reviewer never
re-reviews its own corrections.

## Stage 4: build the Word document

Run `scripts/build_docx.py <canonical-markdown>` to build the branded digest.
Until a real branded MoC template with a pinned SHA-256 is supplied (see
`templates/README.md`), this builds a clean, professionally formatted
document from scratch — headings, bullets, section structure — matching the
reference digests' visual style. The matching canonical markdown is written
alongside the `.docx`; the markdown is the continuity record for future runs.

## Stage 5: programmatic audit (hard gate)

Run `scripts/audit_report.py <canonical-markdown> --docx <built-docx> --register reports/do_not_reuse_register.md --search-log reports/search_log.json --reader-used <tavily|connector|none> --delivery-result <result-once-known>`.
This is an independent gate — a clean-but-wrong digest can never ship green.
It checks: no excluded-outlet source slipped through (Saudi-owned outlets,
**and, separately, all Israeli outlets — see the Source Eligibility rule in
Stage 2, enforced identically as a hard fail**), every article link
**actually resolves live** (not just correct formatting — see below), no raw
URLs in body text, link lives only in the outlet name, three main sections
present and in order, only approved commission labels used, no Arabic
anywhere in the document (hard fail — see Tone discipline above), no
invented labels, Negative Articles has no commission subheadings, headline
bullets present **before** the full summaries and match the article order
and count, GB spelling scan, no banned inflated phrases, Risks/Opportunities
structure (at least one
numbered item per subsection with a headline, Source, and Consideration),
no reused headlines/links against the register (rolling 60-day window — see
Stage 6), the minimum-coverage ladder below, and the fixture-safety guard
below. Failures are fixed and the audit re-run; a failing digest is never
delivered.

### URL resolution (hard gate)

Correct markdown formatting is not enough — a fabricated or dead link with
perfect formatting used to sail through. Every article/source URL now gets
a real HEAD request (GET fallback for servers that reject HEAD). A live
2xx/3xx passes. A bot-wall or rate-limit response (401/403/429) also
passes — that still proves the URL exists, the same "bot wall is normal"
principle Stage 0 already applies to WebFetch. A 404, other 4xx/5xx, DNS/
connection failure, or timeout hard-fails. Checks run with a short delay
between requests for polite rate-limiting. `--skip-url-check` disables this
for offline testing only — **never pass it on a real run**; it is not a
substitute for verifying links actually resolve.

Known limitation, not a bug: a domain that bot-walls with a blanket 401/403
for *any* path, including a nonexistent one, will pass even if the specific
article path is fabricated, because 401/403 is deliberately treated as
"exists" per the rule above. This is an accepted trade-off, not something to
work around by treating 401/403 as a failure (that would make every
legitimately bot-walled premium-wire citation fail).

### Fixture safety (hard gate)

`tests/*.md` fixtures live inside the cloned repo and are deliberately
well-formed, so a confused run that built a digest from (or copied) fixture
content would otherwise pass every other check. The audit hard-fails if the
digest: contains any URL with `/example` in it (the fixtures' placeholder
pattern); contains a known fixture headline verbatim; is identical to a
known fixture file; or contains the `DO-NOT-SHIP: FIXTURE CONTENT` marker
that both `tests/sample_test_digest.md` and `tests/sample_broken_digest.md`
carry. None of this should ever trigger on a real, live-sourced edition —
if it does, stop and treat it as a serious process failure, not a false
positive to suppress.

### Minimum-coverage ladder

| Section | Minimum | Empty allowed? |
|---|---|---|
| Saudi Arabia/Regional | ≥1 article | **No.** Hard-fails if empty, no exception. A short section (per the "don't pad" rule elsewhere in this playbook) is fine; an empty one is not. |
| Global | ≥1 article | **No.** Same as above. |
| Negative Articles | 0 allowed | **Yes, but only with evidence.** Empty is legitimate — a culture digest must never manufacture criticism of the client to fill a quota — but ONLY if `reports/search_log.json` confirms `negative_searches_run: true` (see Stage 2's watchdog/NGO paragraph for the schema). Missing or absent evidence is a hard failure, not a free pass: fail-closed, not fail-open. |

This ladder replaces the earlier undocumented assumption (never actually
implemented) that every section hard-fails on empty; that would have forced
Negative Articles to be padded with weak or manufactured criticism on a
genuinely quiet news day, which is worse than an honest empty section.

## Stage 6: housekeeping and delivery

1. Append every article link and headline used today to
   `reports/do_not_reuse_register.md` (append-only, nothing ever removed),
   one line per entry: `<YYYY-MM-DD> | <section> | <outlet> | <headline> | <url>`
   using today's date. `scripts/audit_report.py` enforces a rolling 60-day
   reuse window against this file (`--register-window-days`, default 60):
   entries within the window hard-block reuse, older entries stay on file
   for the permanent record but no longer block a future edition from
   citing that outlet again.
2. Commit the `.docx` and canonical `.md` to `main`.
3. If Dropbox credentials are configured, upload via
   `scripts/dropbox_upload.py` (binary-safe; never use a connector's
   text-only `create_file` for a `.docx`, it corrupts the binary).
4. If email variables are configured, send via the optional email script.
5. End with an explicit pass/fail run log: capability check results, reader
   path used, articles sourced per section (with verification method per
   article), audit result, delivery result per channel.
6. `scripts/audit_report.py` writes `reports/last_run_status.json` itself as
   part of running Stage 5 (pass `--reader-used` and `--delivery-result`
   once those are known, so they're captured in the same file rather than
   requiring a second pass) — this is the machine-readable counterpart to
   the run log in step 5, the foundation for any future external alerting,
   and it is written reliably even if the audit call itself crashes (see
   Stage 5). It captures: timestamp, per-section item counts, the full
   minimum-coverage ladder result, audit pass/fail with the complete list of
   hard failures and warnings, whether the URL-resolution check ran or was
   skipped, the register rolling-window size, reader used, delivery result,
   and named-entity-list staleness. Commit this file alongside the `.docx`
   and `.md` in step 2 so it's part of the same continuity record. **This
   step does not itself send an alert anywhere** — only emitting the status
   file reliably is in scope for now; do not build email/Slack notification
   on top of it without being asked.

   A hard failure at an earlier stage (Stage 0's capability check, Stage 1's
   unreadable priors) is the one class of failure `scripts/audit_report.py`
   cannot wrap, since it never gets invoked. In that case, write a minimal
   `reports/last_run_status.json` by hand before stopping —
   `{"timestamp": "...", "audit": {"result": "error"}, "run_error": "<what
   failed and why>"}` at minimum — so the run never simply vanishes without
   a trace.

## Learning from manual edits

Same procedure as the conflict-monitoring skill this was adapted from: when
someone revises a delivered digest, diff it against the generated draft,
classify each change against a fixed taxonomy (sourcing quality, Saudi/MoC
relevance, accuracy, tone/register, structure, classification/labeling), log
it in `reports/editorial_learnings.md` as a dated Observation with an
inferred rationale (never stated as fact), and promote a pattern to a
Standing preference once it recurs across two or more editions or
unambiguously enforces an existing rule. No learned preference can ever
relax the accuracy or source-eligibility gates. When a promoted preference is
mechanically checkable, add the matching check to `scripts/audit_report.py`
in the same change.
