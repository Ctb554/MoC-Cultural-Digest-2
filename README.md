# MoC Daily Cultural Digest

Fully autonomous production of the MoC Daily Cultural Digest: a client-facing
cultural intelligence briefing for the Saudi Ministry of Culture, generated
by [Claude Code cloud routines](https://code.claude.com/docs/en/routines)
from live web sourcing, with day-to-day continuity via a do-not-reuse
register and a learning loop that adapts to manual edits.

This repository's architecture is adapted from a sister project
(`conflict-monitoring`) built on the same pattern: the repo itself is the
system of record, sourcing and writing happen live in one reasoning session
rather than a separate fetch pipeline, and a hard programmatic audit gates
delivery.

- **Setup and operating instructions:** [SETUP.md](SETUP.md)
- **Report specification (the run playbook):** [.claude/skills/cultural-digest/SKILL.md](.claude/skills/cultural-digest/SKILL.md)
- **Report archive, registers, and learnings:** [reports/](reports/)

## What this is

Each run, a scheduled cloud session clones this repository, researches
Saudi/regional and global cultural coverage live on the web for the last 24
hours, writes the digest in the required bullet/section format, builds it
into a Word document, audits it programmatically, and delivers it. The
standard is zero fabricated content, zero broken links, and strict
adherence to the source-eligibility rules (no Saudi-owned outlets).

**The repository is the system of record.** Every edition's canonical
markdown, the do-not-reuse register, and the editorial learnings live on
`main`. Each run reads them before writing and commits its output back.

## How a run works, stage by stage

The full specification is [SKILL.md](.claude/skills/cultural-digest/SKILL.md);
this is the map.

| Stage | What happens |
|-------|--------------|
| **0. Capability check** | Verifies live web search/fetch work and priors are readable. Notes whether a Tavily reader or reader connector is available for bot-walled premium outlets, and whether delivery credentials are configured. |
| **0.5 Sync manual edits** | If a delivery destination is configured, sweeps it for manually revised drafts and learns from them before generating. |
| **1. Ingest priors** | Reads the three most recent editions, the do-not-reuse register, and the editorial learnings. |
| **2. Source the news** | Live web only, 24-hour window. Runs the MoC/Minister, Commissions, Saudi Culture, negative-theme, and Global culture Booleans from SKILL.md. Applies the source-exclusion rule (no Saudi-owned outlets; UAE outlets and Campaign ME allowed). Free WebSearch/WebFetch for discovery and verification; a metered reader (Tavily or equivalent) only for a final batched extraction of bot-walled premium wires. |
| **3. Write the content** | Three sections (Saudi Arabia/Regional, Negative Articles, Global), grouped by the approved commission labels, in the required bullet format with the link only in the outlet name, headline bullets after the summaries, and a one-paragraph-each Risks/Opportunities close. |
| **3.5 Adversarial review (single pass)** | One reviewer pass checks the draft against every hard rule and the standing preferences in editorial learnings before building the document. |
| **4. Build the Word document** | `scripts/build_docx.py` renders the canonical markdown into a `.docx`. See `templates/README.md` for swapping to a real branded template once one exists. |
| **5. Programmatic audit** | `scripts/audit_report.py` — a hard gate. Checks source exclusion, link placement, commission-label validity, banned phrases, GB spelling, no reused links, and the Risks/Opportunities structure. A failing digest is never delivered. |
| **6. Housekeeping and delivery** | Appends today's articles to the do-not-reuse register, commits to `main`, uploads via Dropbox if configured, ends with a pass/fail run log. |

## The learning loop

Same as the sister project: every user edit to a delivered digest is treated
as an editorial signal, diffed against the generated draft, classified
against a fixed taxonomy, and recorded in `reports/editorial_learnings.md`.
Patterns that repeat across editions, or that unambiguously enforce an
existing rule, get promoted to Standing preferences that every future
edition applies. No learned preference can ever relax the accuracy or
source-eligibility gates.

## Repository layout

| Path | Purpose |
|------|---------|
| `.claude/skills/cultural-digest/SKILL.md` | The run playbook: sourcing Booleans, classification rules, bullet format, Risks/Opportunities structure. Edit this on `main` to change the digest; runs pick it up next cycle. |
| `templates/` | Where a real branded MoC template will live once available; currently just guidance on pinning one. |
| `reports/*.md` | Canonical markdown of every edition; the continuity record future runs read. |
| `reports/*.docx` | The delivered Word documents. |
| `reports/do_not_reuse_register.md` | Append-only ledger of every article link/headline used. |
| `reports/editorial_learnings.md` | Standing preferences and the dated observation log. |
| `scripts/build_docx.py` | Renders canonical markdown into the `.docx`. |
| `scripts/audit_report.py` | Stage 5 hard-gate audit. |
| `scripts/dropbox_upload.py` | Optional binary docx upload via the Dropbox API. |
| `tests/` | Sample markdown fixtures (one clean, one deliberately broken) used to verify `build_docx.py` and `audit_report.py` — not real editions. |

## Things to watch for

- **Green is not success.** The run log at the end of each session is the
  real verdict: it must confirm every audit check passed.
- **Continuity lives on `main`.** Anything not merged there does not exist
  for the next run.
- **Bot walls are normal; policy blocks are not.** A uniform fetch failure
  across all domains usually means the environment's network policy isn't
  set to Full.
- **No branded template yet.** The digest currently builds from scratch,
  not from a pinned brand template — see `templates/README.md`.
- **Two format specs were reconciled into one SKILL.md**, favoring the more
  recent handoff note's structure (one-paragraph Risks/Opportunities,
  headline bullets after summaries, link-only-in-outlet-name). Flagged
  explicitly at the top of SKILL.md in case that assumption needs flipping.
