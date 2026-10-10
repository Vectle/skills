---
name: "github-actions-log-lines-for-active-st-aca8f2a727fa1eb2"
description: "Notes the GitHub Actions UI fix for active-step log lines being inaccessible while the step runs. Use this when completed steps show full logs but the active step only streams new lines. Not for runner-side log collection failures."
metadata:
  skill_id: "skl_8cs9bqho7bS_c5FADbDOLw"
  title: "GitHub Actions: log lines for active step were inaccessible (fixed in UI)"
  version: "skv_Q4mMnDAJ15eDheVwJwQZ7A"
  updated: "2026-10-03T04:44:06.599553+00:00"
  canonical_url: "https://vectle.com/skills/skl_8cs9bqho7bS_c5FADbDOLw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if the GitHub Actions run page hides log lines for the currently active step (completed steps show everything, but the active step only shows lines emitted after the page loaded), that was a product limitation in the web UI, and GitHub shipped the fix in the April 2024 changelog. Refresh; if it persists on the current UI, check for an ongoing incident.

## Steps

1. Refresh the run page on the current GitHub UI.

   Expected: active-step log lines are visible, including lines emitted before the page loaded. Success check: scrolling the active step shows its full history.

2. If it still happens, check GitHub's status for an ongoing incident.

## When to use this

- Active step shows only newly streaming lines; lines from before page load are missing until the step finishes.
- Completed steps display fine.

## When NOT to use this

- No logs at all, even for completed steps; that points at the runner, not the UI.
- Self-hosted UI mirrors; this was github.com web UI.

## Compatibility

- GitHub Actions web UI, fixed April 2024. Older runner versions are unaffected either way since this was a web UI change.

## Variant phrasings

- "github actions active step logs missing"
- "github actions cannot see running step logs"

## Root cause

The log viewer simply did not backfill lines for in-progress steps; it only attached to the live stream.

## Edge cases

- None; this was purely a UI limitation with a shipped fix.

Source: https://github.com/actions/runner/issues/886

---

Source: [Vectle](https://vectle.com/skills/skl_8cs9bqho7bS_c5FADbDOLw). Version: `skv_Q4mMnDAJ15eDheVwJwQZ7A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
