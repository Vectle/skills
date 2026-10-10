---
name: "sinch-number-lookup-api-402-means-acco-c0a51c374d83e2dd"
description: "Sinch Number Lookup API: 402 means account locked, not payment required. 402 means the account is locked, not that payment is required. Use when hitting this exact issue with Sinch Number Lookup API. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_0Cf5x015ZUIl8V_w0NnJpg"
  title: "Sinch Number Lookup API: 402 means account locked, not payment required"
  version: "skv_320aNeXoPcsH0ZLmdyX5GA"
  updated: "2026-10-03T14:25:05.08992+00:00"
  canonical_url: "https://vectle.com/skills/skl_0Cf5x015ZUIl8V_w0NnJpg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

402 means the account is locked, not that payment is required.

## Fix

1. 402 means the account is locked, not that payment is required.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this Sinch Number Lookup API feature.
- The symptom matches: 402 means account locked, not payment required.

## When NOT to use

- Unrelated Sinch Number Lookup API issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Sinch Number Lookup API. Source: https://github.com/sinch/skills/blob/HEAD/skills/sinch-number-lookup-api/SKILL.md.

## Variant phrasings

### 402 means account locked, not payment required

## Why it happens

Sinch's Number Lookup v2 reuses HTTP codes with Sinch-specific meanings. Reading them as generic HTTP codes misdiagnoses the problem.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/sinch/skills/blob/HEAD/skills/sinch-number-lookup-api/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_0Cf5x015ZUIl8V_w0NnJpg). Version: `skv_320aNeXoPcsH0ZLmdyX5GA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
