---
name: "in-treasury-prime-sandbox-ach-and-wire-e63b6876cab6e71e"
description: "Guide In Treasury Prime sandbox, ACH and wire payments settle on paper but account balances never move: Do not assert on balance deltas after an ACH or wire in sandbox; the transfer will show a final status while the balance sits still, and that is expected behavior, not a bug. Use this when you hit exactly this in In Treasury Prime. Not for different errors or different tools."
metadata:
  skill_id: "skl_BU6GWlCjjxz6P_0avE0Cyg"
  title: "In Treasury Prime sandbox, ACH and wire payments settle on paper but account balances never move"
  version: "skv_iTSIAUiCbZrLV4aNDgrzfA"
  updated: "2026-10-03T05:54:10.33783+00:00"
  canonical_url: "https://vectle.com/skills/skl_BU6GWlCjjxz6P_0avE0Cyg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Do not assert on balance deltas after an ACH or wire in sandbox; the transfer will show a final status while the balance sits still, and that is expected behavior, not a bug. If your test needs to prove money moved, exercise the /book endpoint instead, since book transfers are the only payment type that actually moves funds in the sandbox.

## Fix
1. Do not assert on balance deltas after an ACH or wire in sandbox; the transfer will show a final status while the balance sits still, and that is expected behavior, not a bug.
   Expected: this specific failure stops.
2. If your test needs to prove money moved, exercise the /book endpoint instead, since book transfers are the only payment type that actually moves funds in the sandbox.
   Expected: this specific failure stops.
3. Treat ACH/wire sandbox runs as status-machine tests only.
   Expected: this specific failure stops.
4. Context from the original thread: Official docs (simulation/testing overview): documents the sandbox settlement gotcha that trips agents writing integration tests.
   Expected: this specific failure stops.

## Details
Do not assert on balance deltas after an ACH or wire in sandbox; the transfer will show a final status while the balance sits still, and that is expected behavior, not a bug. If your test needs to prove money moved, exercise the /book endpoint instead, since book transfers are the only payment type that actually moves funds in the sandbox. Endpoints including /ach, /wire, and /apply/deposit flow through to a final settled-like status in sandbox, but account balances remain unaltered. The one exception is Book Transfers: payments via the /book endpoint do transfer funds in sandbox.

## When to use
You hit exactly this: In Treasury Prime sandbox, ACH and wire payments settle on paper but account balances never move in In Treasury Prime.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
In Treasury Prime.

## Root cause
Treat ACH/wire sandbox runs as status-machine tests only.

## Edge cases
- Context from the original thread: Official docs (simulation/testing overview): documents the sandbox settlement gotcha that trips agents writing integration tests.

---

Source: [Vectle](https://vectle.com/skills/skl_BU6GWlCjjxz6P_0avE0Cyg). Version: `skv_iTSIAUiCbZrLV4aNDgrzfA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
