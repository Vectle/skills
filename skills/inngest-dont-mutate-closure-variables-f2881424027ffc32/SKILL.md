---
name: "inngest-dont-mutate-closure-variables-f2881424027ffc32"
description: "When you aggregate results across Inngest steps, return values from step.run() and combine them in the outer scope instead of mutating closure variables inside callbacks. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_d1K43pclgFV_Npn59lHXYQ"
  title: "Inngest: dont mutate closure variables inside step.run()"
  version: "skv_F7vUOkVOrcFPxv9U8VFXIw"
  updated: "2026-10-03T05:10:05.837727+00:00"
  canonical_url: "https://vectle.com/skills/skl_d1K43pclgFV_Npn59lHXYQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

When you aggregate results across Inngest steps, return values from step.run() and combine them in the outer scope instead of mutating closure variables inside callbacks. Memoized steps skip their callback bodies on replay, so any counter incremented there misses on resume. Inngest replays the function body but memoizes completed steps, so increments inside already-completed callbacks dont re-run on replay.

## Fix

When you aggregate results across Inngest steps, return values from step.run() and combine them in the outer scope instead of mutating closure variables inside callbacks. Memoized steps skip their callback bodies on replay, so any counter incremented there misses on resume.

Context: Inngest audit notes (smj1860/fieldstay): counters declared in the outer function scope and mutated inside step.run() callbacks are fragile. Inngest replays the function body but memoizes completed steps, so increments inside already-completed callbacks dont re-run on replay. Counts can silently undercount after partial failures or refactors.

## Matched source
Source: Published skill
Original query: "Inngest: dont mutate closure variables inside step.run()"
Key terms: closure, dont, inngest, inside, mutate, step, variables

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_d1K43pclgFV_Npn59lHXYQ). Version: `skv_F7vUOkVOrcFPxv9U8VFXIw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
