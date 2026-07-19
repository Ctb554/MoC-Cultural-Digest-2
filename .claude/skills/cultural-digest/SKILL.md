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

**ASSUMPTION FLAGGED FOR REVIEW:** two format specs exist for this digest — an
original detailed brief (2-3 paragraph Risks/Opportunities, headline bullets
first) and a later handoff note (one-paragraph Risks/Opportunities, links
embedded only in the outlet name, headline bullets after the summaries). This
playbook follows **the handoff note's formatting** throughout, since it is the
more recent and more precise spec, while keeping the original brief's
sourcing Booleans, commission classification rules, and analytical depth
guidance where the two don't conflict. If the intent was actually to keep the
original's longer Risks/Opportunities paragraphs or headline-bullets-first
ordering, that's a one-line edit to Stage 3 below, not a rebuild.

## Routine run constants

- The repository default branch (`main`) is the continuity store. Each run
  clones it fresh; everything a future run must remember has to be committed
  and pushed before the run ends.
- Coverage window: last 24 hours from run start, unless the run is invoked
  with an explicit different window.

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

**Negative/reputational coverage** — run as separate searches per theme, not
one combined query (a combined query drowns culture-adjacent reputational
stories under pure geopolitics on any heavy news day): human rights, labour/
workers, sportswashing, PIF scrutiny, Saudi-Iran/regional geopolitics, oil,
academic freedom, tourism criticism, religious tourism/Mecca commercialization,
Vision 2030 criticism, investment scrutiny, soft power criticism, general
reputation risk.

**Global culture** — run broad culture/arts/heritage/museum/film/music/theatre/
fashion/architecture/literature/culinary searches, prioritizing Tier 1 outlets:
BBC, Guardian, FT, NYT, WaPo, AP, Bloomberg, Xinhua, China Daily, CGTN, The
Hindu, Indian Express, Kathimerini, ANSA, Repubblica, Corriere, Il Sole 24 Ore,
DW, Spiegel, FAZ, Le Monde, Le Figaro, France24, AFP, Reuters, Eater, Saveur,
ArchDaily, Dezeen, Domus, Architectural Digest, Vogue Business, WWD,
FashionNetwork, FashionUnited, Billboard, ArtReview, Frieze, Art Basel,
Designboom, The Art Newspaper, Artforum.

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
  benchmarking and from credible outlets.

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

### Output structure (per the handoff note's format)

Three sections only, in this order: **Saudi Arabia/Regional**, **Negative
Articles**, **Global**. Within each, group articles under the approved
commission labels — **General, Heritage, Museums, Visual Arts, Film, Fashion,
Music, Theatre and Performing Arts, Literature Publishing and Translation,
Libraries, Culinary Arts, Architecture and Design** — using the classification
rules below. Do not invent thematic labels (no "tourism and hospitality",
"creative economy", etc.); anything not clearly fitting a commission goes
under General.

### Classification rules

- Museums: museums, museum programming, museum-led exhibitions.
- Film: cinema, production, rebates, festivals, filmmaking.
- Architecture and Design: architecture, design, urbanism, built environment.
- Fashion: designers, fashion weeks, style, luxury fashion, fashion education.
- Heritage: archaeology, UNESCO, monuments, preservation, intangible
  heritage, cultural memory.
- Culinary Arts: food, cuisine, gastronomy, chefs, culinary heritage, food
  festivals.
- Literature, Publishing, and Translation: books, authors, publishing,
  translation, manuscripts, unless library-specific.
- Libraries: libraries, archives, library policy.
- Theatre and Performing Arts: theatre, dance, opera, stage/live performance.
- Visual Arts: galleries, biennales, artists, exhibitions, art markets,
  unless museum-led.
- General: everything else, including non-culture negative/reputational
  stories that don't fit a commission.
- If a story fits multiple labels, use the most specific and strategically
  relevant one — a judgment call, not a keyword match.

### Bullet format (per the handoff note, verbatim pattern)

One bullet per article, usually two sentences:

`<Outlet name> reported that <clear factual summary>. The article is relevant as a <sector/risk/opportunity> item, <why it matters for Saudi Arabia, the Ministry of Culture, cultural positioning, reputation, investment, tourism, or global cultural trends>. (Outlet)`

(The angle brackets above mark where to substitute real text — write the
actual outlet name and summary, never literal square-bracket placeholders in
the output.)

- The link lives **only** in the outlet name at the end — never in the first
  sentence, never as a raw URL.
- Flag op-eds, Substacks, and non-English-language pickups explicitly (e.g.
  "DER SPIEGEL's official Substack", "Spanish-language coverage picked up by
  Infobae").
- Do not imply MoC involvement unless the source explicitly states it.
- Avoid inflated language ("groundbreaking", "world-leading", "landmark",
  "unprecedented", "unusually broad pickup") unless clearly and specifically
  evidenced.
- Preferred synthesis phrases: "The article is relevant as...", "The coverage
  reinforces...", "The story highlights...", "The Ministry should build on
  this coverage by...", "Messaging should foreground...".

### Headline bullets

After the full summaries (per the handoff note's ordering — not before),
produce headline bullets using the exact article headline (verify by opening
the link), in the same order as the summaries, no links, no subheadings,
only the three main sections.

### Risks and Opportunities

One numbered item each, per the handoff note:

```
Risks and Opportunities

Risks

1. [One paragraph synthesizing the key risks across today's negative and
   relevant general coverage.]

Source: Outlet, Outlet, Outlet

Consideration: [One paragraph on what the Ministry should consider in response.]

Opportunities

2. [One paragraph synthesizing the key opportunities from Saudi/regional and
   relevant global cultural coverage.]

Source: Outlet, Outlet, Outlet

Consideration: [One paragraph on how the Ministry can build on the coverage.]
```

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
- Write entirely in English — no Arabic in the output (Arabic is fine only in
  the internal Boolean search strings above, never in the produced digest).

## Stage 3.5: adversarial review (single pass)

Before building the document, one reviewer pass attacks the complete draft
from an editor's perspective, checking:

- Every hard rule above: source exclusion (no Saudi-owned outlets slipped
  through), link-in-outlet-name-only, no raw URLs, GB English, no invented
  labels, no banned inflated phrases.
- The standing preferences in `reports/editorial_learnings.md`, so edits the
  team has made before are caught pre-delivery.
- Headline-bullet accuracy against the actual linked article.
- Risks/Opportunities structure: exactly one numbered paragraph each, with
  Source and Consideration lines.

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
name, three main sections present and in order, only approved commission
labels used, no invented labels, headline bullets present after summaries and
match the article order, GB spelling scan, no banned inflated phrases,
Risks/Opportunities structure (exactly one numbered paragraph each with
Source/Consideration), no reused headlines/links against the register.
Failures are fixed and the audit re-run; a failing digest is never delivered.

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
