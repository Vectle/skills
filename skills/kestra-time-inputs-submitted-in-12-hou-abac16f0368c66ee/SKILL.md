---
name: "kestra-time-inputs-submitted-in-12-hou-abac16f0368c66ee"
description: "Fixes Kestra TIME inputs submitting in 12-hour format (wrong wall-clock time) and broken TIME defaults. Use this when picked times come back shifted by 12 hours or defaults show ~00:00:14. Not for other input types."
metadata:
  skill_id: "skl_5HfQ4ypORI_2jf-LKMheZg"
  title: "Kestra TIME inputs submitted in 12-hour format (wrong wall-clock time)"
  version: "skv_uBmLN-O-zWrRRrIqRD6VPg"
  updated: "2026-10-03T05:12:29.521177+00:00"
  canonical_url: "https://vectle.com/skills/skl_5HfQ4ypORI_2jf-LKMheZg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if Kestra `TIME` inputs come back shifted by 12 hours (picking 14:30:00 stores `02:30:00`) or TIME defaults show ~00:00:14, the frontend formatted TIME values with moment's `hh:mm:ss` (12-hour) instead of `HH:mm:ss` (24-hour) in `submitTask.ts` and the cURL export, and hydrated defaults without a format string (so "14:30:00" parsed as 14 seconds). Upgrade to a release containing PR #19707 (merged and backported to the v2.0.x and v1.3.x branches).

## Steps

1. Upgrade Kestra to a release with PR #19707.

2. Re-submit a TIME input.

   Expected: 24-hour values round-trip correctly. Success check: picking 14:30:00 stores 14:30:00 and defaults render properly.

## When to use this

- TIME inputs shifted by 12 hours or defaults showing ~00:00:14.

## When NOT to use this

- Other input types misbehave; those are separate.
- You are on a fixed release and still see it; report it.

## Compatibility

- Kestra releases with PR #19707 (v2.0.x and v1.3.x backports).

## Variant phrasings

- "kestra TIME input 12 hour format"
- "kestra time picker wrong time"

## Root cause

Lowercase `hh` in the moment format string means 12-hour clock; the fix switches to uppercase `HH` and parses defaults with an explicit format.

## Edge cases

- Existing wrongly-stored times are not repaired by the upgrade; re-submit them.

Source: https://vectle.com/threads/thr_zE5vXq7Cp569KH4AQ-_2vA

---

Source: [Vectle](https://vectle.com/skills/skl_5HfQ4ypORI_2jf-LKMheZg). Version: `skv_uBmLN-O-zWrRRrIqRD6VPg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
