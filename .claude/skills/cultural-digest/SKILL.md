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

**FORMAT CONFIRMED AGAINST REAL PRODUCTION (2026-07-19):** two written specs
existed for this digest (an original detailed brief and a later handoff
note), and they disagreed with each other on several points. Rather than
choosing between them, this playbook was corrected against an actual,
currently-delivered live edition
(`MOC_Daily_Cultural_Digest_19Jul26_D1.docx`, produced by the existing manual
process this repo is meant to automate). Where the live edition settles a
disagreement between the two written specs, the live edition wins. Confirmed
findings:

- **Headline bullets come first**, before the full summaries (matches the
  original brief, not the handoff note).
- **Commission labels are bilingual**, e.g. "Heritage (التراث)", "Visual Arts
  (الفنون البصرية)" — the handoff note's "no Arabic anywhere in the output"
  rule does not match real practice and is dropped.
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
  of the digest; the bilingual `English (Arabic)` commission labels inside
  the English digest (Stage 3) are the only Arabic text this pipeline
  produces.

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
5. Note recurring Risks/Opportunities themes from the prior digest (e.g. an
   ongoing regional tension, an ongoing positive narrative arc like a
   festival season or Vision 2030 milestone) so today's synthesis reads as a
   continuation where genuinely still live, not a restart — without forcing
   continuity where the news cycle has actually moved on.

## Stage 2: source the news (live web, window-bounded)

Use WebSearch to discover, then WebFetch to verify. Run all Boolean searches
below across the last 24 hours (adjust the window only if explicitly told to).

### Credit discipline: free discovery, paid extraction only for the final report

Same split as the conflict-monitoring skill: discovery, verification, and
selection run entirely on free WebSearch/WebFetch (snippets, syndicated
copies, second-source corroboration for bot-walled premium wires). The
metered Tavily reader (or fallback connector) is spent only afterward, as one
batched basic-depth extraction of the selected articles WebFetch can't read
— typically 1-2 credits per edition. Never use Tavily search; it duplicates
free WebSearch at a cost.

### Search Booleans to run

**MoC / Minister Boolean:**
`("Saudi Arabia" OR Saudi OR "KSA") AND ("Saudi Ministry of Culture" OR "Saudi Arabia's Ministry of Culture" OR "Saudi culture ministry" OR "Saudi MoC" OR "Saudi Minister of Culture" OR "Saudi Culture Minister" OR "Prince Badr bin Abdullah bin Farhan" OR "Badr bin Farhan" OR "Vice Minister of Culture" OR "Deputy Minister of Culture" OR "Hamed Fayez")`

**Commissions Boolean:**
`("Film Commission" OR "Saudi Film Commission" OR "Fashion Commission" OR "Music Commission" OR "Heritage Commission" OR "Culinary Arts Commission" OR "Theater and Performing Arts Commission" OR "Museums Commission" OR "Architecture and Design Commission" OR "Visual Arts Commission" OR "Literature, Publishing and Translation Commission" OR "Library Commission" OR "Language Commission" OR "Saudi culture commission")`

**Saudi Culture Boolean (broad):**
`("Saudi culture" OR "Saudi cultural" OR "Saudi heritage" OR "Saudi arts" OR "Saudi artists" OR "Saudi music" OR "Saudi film" OR "Saudi cinema" OR "Saudi filmmakers" OR "Saudi fashion" OR "Saudi design" OR "Saudi literature" OR "Saudi cuisine" OR "Saudi gastronomy" OR "Saudi hospitality")`

**Named Entity Searches** — one unified category, covering outlets, people,
and places. The broad Saudi Culture Boolean above only catches stories using
generic phrasing ("Saudi fashion", "Saudi film", "Saudi heritage"). It misses
coverage that names a specific outlet, person, brand, or site directly
without ever using those generic words — e.g. Vogue covering a named Saudi
designer, or a story about new findings at Hegra that never says "heritage"
or "archaeological." These three groups exist to catch exactly that gap.
Named individuals and sites were verified via live web search as of July
2026 — **all three lists below will go stale**; re-verify periodically and
add newly prominent names/sites as they surface in real coverage rather than
treating any of this as fixed. Run each bullet below as its own separate
search, not one combined query — a combined query dilutes results the same
way the negative themes would. If a search returns nothing on a given day,
that's a normal outcome for a narrow named-entity search, not a failure; do
not pad or force a result, and every hit still passes the standard
verification gates (real, in-window, not previously used).

*Outlets* — pairs `"Saudi Arabia" OR Saudi` with named prestige/trade press, by sector:
- **General/Macro Press (leads the Saudi Arabia/Regional section — see Stage 3 ordering rule):** `("Saudi Arabia" OR Saudi OR KSA) AND (Bloomberg OR "Financial Times" OR Semafor OR "The Economist" OR "Wall Street Journal" OR Axios OR Politico OR Reuters OR "Associated Press" OR AFP OR "New York Times" OR "The Times" OR "Sunday Times" OR "The Telegraph" OR "Nikkei Asia" OR "Foreign Policy" OR "Foreign Affairs" OR "The Diplomat" OR AGBI OR "Arabian Business" OR "Al-Monitor" OR "Amwaj.media" OR MEED OR "Gulf News" OR "Middle East Eye" OR "Al Jazeera")`. Reuters and AP were missing from this search entirely until 2026-07-20 — they previously only appeared in the generic Global-culture outlet list, which doesn't pair them with Saudi Arabia at all. This was a real gap, not a deliberate exclusion; verified additions here (Nikkei Asia, Foreign Policy, Foreign Affairs, The Diplomat, AGBI, Arabian Business, Al-Monitor, Amwaj.media, MEED, Gulf News, The Telegraph) come from a dedicated outlet-verification research pass and are all confirmed active, credible, non-Saudi sources as of 2026. **Middle East Eye and Al Jazeera are included but flagged**: Middle East Eye's funding is opaque and widely linked to Qatar; Al Jazeera is funded by the Qatari state (Qatar Media Corporation). Neither is excluded, but their framing on politically sensitive Gulf topics should be read as reflecting Doha's interests, not treated as neutral.
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

*People* — named cultural figures, by sector:
- **Visual Arts:** `"Ahmed Mater" OR "Abdulnasser Gharem" OR "Ashraf Fayadh" OR "Manal Al Dowayan" OR "Dana Awartani" OR "Shadia Alem" OR "Sarah Abu Abdallah" OR "Sarah Mohanna Al Abdali" OR "Zahrah Al Ghamdi" OR "Safeya Binzagr"`
- **Film:** `"Haifaa Al-Mansour" OR "Haifaa Al Mansour"`
- **Fashion:** `"Waad Aloqaili" OR "Yahya Albishri" OR "Razan Alazzouni" OR "Mona Al Shebil" OR "Adnan Akbar" OR "Tima Abid" OR "Kawthar Alhoraish" OR "Eman Alajlan" OR "Khadija Al Sunaydi"`

*Places* — named heritage and archaeological sites, verified against
UNESCO's official list (Saudi Arabia currently has 8 inscribed World
Heritage properties, most recently Al-Faw in 2024) plus other frequently-
covered named sites, including three from Saudi Arabia's tentative list
(Hejaz Railway, Farasan Islands, Rijal Almaa Heritage Village):
- **Heritage sites (one combined query — named places don't dilute each other the way broad topics do):** `(Hegra OR "Al-Hijr" OR "Madain Salih" OR "Mada'in Salih" OR Diriyah OR "At-Turaif" OR "Historic Jeddah" OR "Al-Balad" OR "Jubbah rock art" OR "Rock Art in the Hail Region" OR "Al-Ahsa Oasis" OR "Hima Cultural Area" OR "Najran rock art" OR "Al-Faw archaeological" OR AlUla OR Dadan OR "Jabal Ikmah" OR "Hejaz Railway" OR "Farasan Islands" OR "Rijal Almaa")`
  Classify hits under **Heritage** unless the story is clearly museum-led (→
  Museums) or architecture/design-led (→ Architecture and Design).

**Negative/reputational coverage** — run as separate searches per theme, not
one combined query (a combined query drowns culture-adjacent reputational
stories under pure geopolitics on any heavy news day): human rights, labour/
workers, sportswashing, PIF scrutiny, Saudi-Iran/regional geopolitics, oil,
academic freedom, tourism criticism, religious tourism/Mecca commercialization,
Vision 2030 criticism, investment scrutiny, soft power criticism, general
reputation risk.

**Watchdog/NGO monitoring (new category, added 2026-07-20)** — a dedicated
search pairing Saudi Arabia with named human-rights and press-freedom
organizations, run as its own search separate from the themes above. These
organizations regularly publish primary reports and statements on Saudi
Arabia that a generic "human rights" phrase search can miss if the
organization's own release doesn't use that exact wording:
`("Saudi Arabia" OR Saudi) AND ("Amnesty International" OR "Human Rights Watch" OR "Freedom House" OR "Reporters Without Borders" OR RSF OR "Committee to Protect Journalists" OR CPJ OR CIVICUS OR ALQST OR "Democracy for the Arab World Now" OR DAWN OR "PEN International")`.
ALQST and DAWN (Democracy for the Arab World Now, founded after Jamal
Khashoggi's killing) are Saudi-specific human-rights organizations, not
general MENA-wide ones — their statements are usually directly about Saudi
Arabia rather than requiring the "Saudi Arabia" pairing to be relevant, but
the pairing is kept for consistency and to filter out unrelated organizational
news. As with every other search in this section, a hit here still has to
pass the standard verification gates (real, in-window, not previously used,
non-Saudi-owned source reporting on it) before inclusion — an NGO's own
press release is a primary source, not automatically a "verified" media
report; prefer a credible news outlet's coverage of the NGO's findings where
one exists, and treat the raw NGO statement as a fallback for verification,
not the ideal citation for a bullet.

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

### Source eligibility (hard rule, enforced by Stage 5 audit)

- **Exclude all Saudi-based/Saudi-owned outlets** — Arab News, Asharq
  (Al-Awsat), Saudi Gazette, SPA, and any other Saudi-owned outlet, even if
  it surfaces via a broad search. When in doubt about ownership, check before
  using; if still uncertain, don't use it.
- **UAE-based credible outlets are allowed.** The National and Al Arabiya are
  explicitly allowed, along with Campaign Middle East.
- Avoid weak, hyper-local, or poor-quality outlets and raw press-release
  wires (e.g. PR Newswire, EIN Presswire) unless they're the only source for
  a genuinely significant story.
- Use the most authoritative/international source when multiple outlets
  cover the same story; do not pad with weak duplicates.
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
   articles under the approved bilingual commission labels (see table below).
   **Negative Articles has no commission subheadings** — its bullets sit
   directly under the section heading.

**Saudi Arabia/Regional ordering rule:** lead the section with up to 3-4
General items sourced from the General/Macro Press search (Bloomberg, FT,
Semafor, The Economist, WSJ, Axios, Politico) — broad, high-authority
context on Saudi Arabia, not necessarily culture-specific — before moving
into the more specific commission subsections (Heritage, Visual Arts, etc.).
This gives the section a strong opening anchor. Use up to 3-4 if that many
genuine, verified items exist; use fewer if they don't. Never pad to reach
the count — the same "don't force it" principle applies here as everywhere
else in this playbook. The headline-bullet block at the top of the document
inherits this same ordering automatically, since it must match the full
summary's article order.

Then a final **Risks and Opportunities** section (see format below).

Do not invent thematic labels (no "tourism and hospitality", "creative
economy", etc.); anything not clearly fitting a commission goes under
General.

### Classification rules and bilingual labels

Every commission label is written as `English (Arabic)` in the full-summary
section (headline bullets stay English-only, since they're just the article
headline). Labels confirmed against real production:

| English | Arabic | Classification rule |
|---|---|---|
| General | عام | Fallback for anything not fitting a specific commission; **also the home for general/macro/business/policy coverage of Saudi Arabia from elite press** (Bloomberg, FT, Semafor, The Economist, WSJ, Axios, Politico) surfaced by the General/Macro Press search above — see the Stage 3 ordering rule for how these lead the Saudi Arabia/Regional section |
| Heritage | التراث | Archaeology, UNESCO, monuments, preservation, intangible heritage, cultural memory |
| Museums | المتاحف | Museums, museum programming, museum-led exhibitions |
| Visual Arts | الفنون البصرية | Galleries, biennales, artists, exhibitions, art markets, unless museum-led |
| Film | الأفلام | Cinema, production, rebates, festivals, filmmaking |
| Fashion | الأزياء | Designers, fashion weeks, style, luxury fashion, fashion education |
| Music | الموسيقى | Music industry, artists, concerts, releases |
| Theatre and Performing Arts | المسرح والفنون الأدائية | Theatre, dance, opera, stage/live performance |
| Literature, Publishing, and Translation | الأدب والنشر والترجمة | Books, authors, publishing, translation, manuscripts, unless library-specific |
| Libraries | المكتبات | Libraries, archives, library policy |
| Culinary Arts | فنون الطهي | Food, cuisine, gastronomy, chefs, culinary heritage, food festivals |
| Architecture and Design | فنون العمارة والتصميم | Architecture, design, urbanism, built environment |

If a story fits multiple labels, use the most specific and strategically
relevant one — a judgment call, not a keyword match. If Arabic-label
convention drifts in a future reference edition, re-derive from that edition
rather than this table.

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
- Article summaries, headline bullets, and Risks/Opportunities prose are
  written in English. Arabic appears **only** inside commission subheadings
  in the `English (Arabic)` bilingual format confirmed above — never
  elsewhere in the body text.

## Stage 3.5: adversarial review (single pass)

Before building the document, one reviewer pass attacks the complete draft
from an editor's perspective, checking:

- Every hard rule above: source exclusion (no Saudi-owned outlets slipped
  through), link-in-outlet-name-only, no raw URLs, GB English, no invented
  labels, no banned inflated phrases, bilingual commission labels present and
  correctly paired.
- The standing preferences in `reports/editorial_learnings.md`, so edits the
  team has made before are caught pre-delivery.
- Headline bullets appear first (before full summaries) and match the
  full-summary article order and count.
- Negative Articles has no commission subheadings.
- Risks/Opportunities structure: at least one numbered item per subsection,
  each with a bold headline, paragraph, Source line, and Consideration line.

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

Run `scripts/audit_report.py <built-docx> --md <canonical-markdown>`. This is
an independent gate — a clean-but-wrong digest can never ship green. It
checks: no excluded-outlet source slipped through, every article has a
working direct link, no raw URLs in body text, link lives only in the outlet
name, three main sections present and in order, only approved bilingual
commission labels used (correct English/Arabic pairing), no invented labels,
Negative Articles has no commission subheadings, headline bullets present
**before** the full summaries and match the article order and count, GB
spelling scan, no banned inflated phrases, Risks/Opportunities structure (at
least one numbered item per subsection with a headline, Source, and
Consideration), no reused headlines/links against the register. Failures are
fixed and the audit re-run; a failing digest is never delivered.

## Stage 6: housekeeping and delivery

1. Append every article link and headline used today to
   `reports/do_not_reuse_register.md` (append-only, nothing ever removed).
2. Commit the `.docx` and canonical `.md` to `main`.
3. If Dropbox credentials are configured, upload via
   `scripts/dropbox_upload.py` (binary-safe; never use a connector's
   text-only `create_file` for a `.docx`, it corrupts the binary).
4. If email variables are configured, send via the optional email script.
5. End with an explicit pass/fail run log: capability check results, reader
   path used, articles sourced per section (with verification method per
   article), audit result, delivery result per channel.

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
