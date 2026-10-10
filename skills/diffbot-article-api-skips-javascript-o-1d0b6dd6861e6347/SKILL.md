---
name: "diffbot-article-api-skips-javascript-o-1d0b6dd6861e6347"
description: "Diffbot Article API skips JavaScript on individual calls - JS runs only in bulk and Crawlbot calls. Diffbot does execute JavaScript - it renders in a stripped-down Chrome - but there is a catch in the Article API: individual calls do NOT run JS, only bulk API and Crawlbot calls do. Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_JAAV5wMCqdiXsSWfIgGGYg"
  title: "Diffbot Article API skips JavaScript on individual calls - JS runs only in bulk and Crawlbot calls"
  version: "skv_riHrSCa4o8JzBf45EMUTgw"
  updated: "2026-10-03T20:21:53.439973+00:00"
  canonical_url: "https://vectle.com/skills/skl_JAAV5wMCqdiXsSWfIgGGYg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Diffbot does execute JavaScript - it renders in a stripped-down Chrome - but there is a catch in the Article API: individual calls do NOT run JS, only bulk API and Crawlbot calls do.

## Fix

1. Diffbot does execute JavaScript - it renders in a stripped-down Chrome - but there is a catch in the Article API: individual calls do NOT run JS, only bulk API and Crawlbot calls do.
   Expected: you can confirm this matches your situation.

## When to use

- You are dealing with this situation.
- The symptom matches: Diffbot Article API skips JavaScript on individual calls - JS runs only in bulk and Crawlbot calls.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source. Source: Stack Overflow question: https://stackoverflow.com/questions/24915127.

## Variant phrasings

### Diffbot Article API skips JavaScript on individual calls - JS runs only in bulk and Crawlbot calls

## Why it happens

Stack Overflow (Does Diffbot execute JavaScript?, answered): Yes, Diffbot renders pages in a stripped-down session-less Chrome and visually inspects the result rather than just parsing source. But the Article API does NOT execute JavaScript in individual calls - only in bulk API calls and Crawlbot calls. Single Article API calls on JS-heavy pages return what the static parse sees.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

Stack Overflow question: https://stackoverflow.com/questions/24915127

---

Source: [Vectle](https://vectle.com/skills/skl_JAAV5wMCqdiXsSWfIgGGYg). Version: `skv_riHrSCa4o8JzBf45EMUTgw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
