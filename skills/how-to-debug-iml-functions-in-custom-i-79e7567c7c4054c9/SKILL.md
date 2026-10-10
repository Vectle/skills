---
name: "how-to-debug-iml-functions-in-custom-i-79e7567c7c4054c9"
description: "How to debug IML functions in custom Integromat apps?. Use the debug() function inside your own IML functions instead of trying to use console.log . Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_n7vtgDoN_cKKYzCwHrVivg"
  title: "How to debug IML functions in custom Integromat apps?"
  version: "skv_M_dYOa76B9eVzJC42YvEqg"
  updated: "2026-10-04T01:35:26.132976+00:00"
  canonical_url: "https://vectle.com/skills/skl_n7vtgDoN_cKKYzCwHrVivg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use the debug() function inside your own IML functions instead of trying to use console.log . When your IML function is called from any module, the output from the debug() function will be shown in the Live Stream panel within Chrome's Integromat DevTool extension.

## Fix

1. Use the debug() function inside your own IML functions instead of trying to use console.log .
   Expected: You get the expected result; the problem is gone.

## When to use

- You are dealing with this situation.
- The symptom matches: How to debug IML functions in custom Integromat apps?.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source.

## Variant phrasings

### How to debug IML functions in custom Integromat apps?

## Why it happens

Stack Overflow question (score 1, has accepted answer): I know that it is possible to write tests for IML functions using the VS Code plugin but couldn't find anything similar to console.log . Is logging available in IML functions?

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_n7vtgDoN_cKKYzCwHrVivg). Version: `skv_M_dYOa76B9eVzJC42YvEqg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
