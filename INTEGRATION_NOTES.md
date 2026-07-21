# Expansion drop-in — integration notes

Two config files, both additive. Nothing here removes existing behaviour.

## 1. config/sources.yaml
Widens the GLOBAL source pool and hardens the Saudi exclusion list.

- **`global_sources`** — organised by cultural beat. `existing` = already in your
  Tier-1 `site:` filter; `added_general` and `added_trade` are new. Net additions
  vs. the current 41-outlet filter: ~70 outlets across 9 beats, with the biggest
  gains in the previously-thin beats (film trades, music trades, performing-arts
  trades, heritage/archaeology, gastronomy, publishing).
- **`excluded_saudi`** — expands the current ~13-domain block list to ~40 named
  titles/channels, grouped by owner (SRMG / MBC / Rotana / royal-family / dailies
  / digital / state broadcast). **`alarabiya.net` is in here** — it is MBC/PIF-owned
  and must NOT be treated as a permitted UAE outlet.
- **`low_trust_permitted`** — Vogue Arabia + ITP titles: allowed, but discount for
  Saudi-government stories.

### Wiring
If `audit_report.py` still uses a flat `EXCLUDED_SAUDI_DOMAINS` python list, flatten
every domain under `excluded_saudi` into it. If the RSS/site pre-filter uses an
allow-list, load `global_sources` + `permitted_regional`. Keep `sources.yaml` as the
single source of truth and generate both lists from it, so they can't drift apart.

## 2. config/saudi_search_parameters.md
Adds three new Booleans (Entities & Venues / Festivals & Seasons / Named execs) and
new supporting searches. The existing three Booleans are retained unchanged. This is
the fix for the Saudi-side coverage hole (named bodies invisible to generic phrases).

## Quarterly re-verify (ownership is dynamic)
- MBC 54% PIF stake completed 18 Sep 2025.
- SRMG Thmanyah stake move 51%→75% announced May 2026.
- Vogue Arabia moved to direct Condé Nast operation Jan 2025.
Re-check parents each quarter before trusting the exclusion list as exhaustive.

## Verify-before-hard-commit
A handful of exclusion-list domains are expected-pattern guesses, not independently
re-verified (e.g. `abouther.com`, `aljamila.com`, `ahlanwasahlan.com`, some SRMG
lifestyle domains). A wrong guess here only means one fewer domain blocked, never a
false exclusion — but spot-check before treating the list as complete.
