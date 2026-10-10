---
name: "diagnose-conversation-history-grows-fo-7eda82a9cb0b1c5a"
description: "Shows how to fix diagnose: conversation history grows forever despite SummarizationMiddleware. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_iEbuOSZ8rLL7rMJRXlt95w"
  title: "Diagnose: conversation history grows forever despite SummarizationMiddleware"
  version: "skv_pjtTLF3U2JjdVB_9qsKhKQ"
  updated: "2026-10-03T13:56:12.846634+00:00"
  canonical_url: "https://vectle.com/skills/skl_iEbuOSZ8rLL7rMJRXlt95w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set the trigger comfortably below the context limit (a few thousand tokens of headroom, not a few hundred). Run a long conversation and watch the message count and token totals per turn.

## Steps

1. - The trigger threshold is higher than the model's effective working limit, so the overflow hits before summarization fires.
- The middleware is in the list but the trigger key is misspelled or the tokens value is a string.
- Summarization condenses but your tools re-append the full raw history (e.g. returning whole documents into messages every turn).

2. Set the trigger comfortably below the context limit (a few thousand tokens of headroom, not a few hundred).
2. Verify the kwarg names against the docs: `trigger={"tokens": [number]}`.
3. Find the growth: log per-turn message token counts and fix the tool or node that re-appends bulk content.

3. Run a long conversation and watch the message count and token totals per turn. Totals should sawtooth (grow, summarize, drop), not climb monotonically.

## When to use

You are seeing this: ContextOverflowError mid-run, or steadily growing token counts per turn, despite SummarizationMiddleware being in the middleware list. Use this skill when you run into "Diagnose: conversation history grows forever despite SummarizationMiddleware".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_iEbuOSZ8rLL7rMJRXlt95w). Version: `skv_pjtTLF3U2JjdVB_9qsKhKQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
