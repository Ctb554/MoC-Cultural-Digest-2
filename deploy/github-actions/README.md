# GitHub Actions deployment (not built)

The sister project this repo was adapted from keeps a parked GitHub Actions
cron deployment here as an alternative to Claude Code cloud routines. That
alternative hasn't been built for this project yet — routines are the
primary (and only) deployment path right now.

If a self-hosted cron fallback is ever wanted (e.g. to avoid depending on
routines being in research preview, or to run outside a claude.ai account),
build it here following the same shape: a workflow that checks out this
repo, runs the sourcing/writing/build/audit steps via the Anthropic API
directly, and pushes the result back to `main`. Requires a Console API key
as a repo secret, which the routines path does not need.
