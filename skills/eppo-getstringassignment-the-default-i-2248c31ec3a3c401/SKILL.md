---
name: "eppo-getstringassignment-the-default-i-2248c31ec3a3c401"
description: "Guide Eppo getStringAssignment: the default is a real fallback, and subject keys must be stable: call it with intent. Use a stable subject key like your user ID, never a session ID or a random value, and pass subjectAttributes that match your flag targeting rules, things like country or plan. Use this when you hit exactly this in Eppo getStringAssignment. Not for different errors or different tools."
metadata:
  skill_id: "skl_wBb8uG73bM8OD8W773lH1g"
  title: "Eppo getStringAssignment: the default is a real fallback, and subject keys must be stable"
  version: "skv_o_m1ihOPPinkej4iGNnpDA"
  updated: "2026-10-03T05:33:20.489592+00:00"
  canonical_url: "https://vectle.com/skills/skl_wBb8uG73bM8OD8W773lH1g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: call it with intent. Use a stable subject key like your user ID, never a session ID or a random value, and pass subjectAttributes that match your flag targeting rules, things like country or plan tier. Set the default assignment to the control variant explicitly, so a flag that fails to evaluate behaves exactly like the control group instead of producing mystery data.

## Fix
1. call it with intent.
   Expected: this specific failure stops.
2. Use a stable subject key like your user ID, never a session ID or a random value, and pass subjectAttributes that match your flag targeting rules, things like country or plan tier.
   Expected: this specific failure stops.
3. Set the default assignment to the control variant explicitly, so a flag that fails to evaluate behaves exactly like the control group instead of producing mystery data.
   Expected: this specific failure stops.
4. And log the assignment with your assignment logger at the same call site, so evaluation and logging cant drift apart.
   Expected: this specific failure stops.

## Details
Keep boolean, numeric, and JSON variants in their typed getters rather than parsing strings yourself.

## When to use
You hit exactly this: Eppo getStringAssignment: the default is a real fallback, and subject keys must be stable in Eppo getStringAssignment.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Eppo getStringAssignment.

---

Source: [Vectle](https://vectle.com/skills/skl_wBb8uG73bM8OD8W773lH1g). Version: `skv_o_m1ihOPPinkej4iGNnpDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
