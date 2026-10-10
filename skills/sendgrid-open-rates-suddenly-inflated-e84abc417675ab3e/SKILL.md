---
name: "sendgrid-open-rates-suddenly-inflated-e84abc417675ab3e"
description: "Shows how to fix sendGrid open rates suddenly inflated: Apple Mail Privacy Protection. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_XObcVUoV1ZrChtc_fTvcMQ"
  title: "SendGrid open rates suddenly inflated: Apple Mail Privacy Protection"
  version: "skv_pPRmAHO5dvIxiRDknRWX8Q"
  updated: "2026-10-03T14:10:30.010818+00:00"
  canonical_url: "https://vectle.com/skills/skl_XObcVUoV1ZrChtc_fTvcMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Stop making send decisions on raw open rate alone: sunset rules, A/B winners, and engagement scoring should weight clicks and replies, not prefetchable opens. Do not 'fix' it by disabling open tracking; you lose the signal instead of cleaning it.

## Steps

1. Symptom: open rates spike across campaigns while clicks stay flat.

2. Cause: privacy-prefetching clients open (or pre-load) mail on the recipient's behalf. These are machine opens, not human attention.

3. Confirmation: check the sg_machine_open property on Opened events. A surge of machine opens matching the open-rate spike confirms it.

4. Fix:
1. Segment reporting: track human opens (machine open false) separately from total opens.
2. Stop making send decisions on raw open rate alone: sunset rules, A/B winners, and engagement scoring should weight clicks and replies, not prefetchable opens.
3. Do not 'fix' it by disabling open tracking; you lose the signal instead of cleaning it.

5. Verification: human-open trend stays continuous across the spike while total opens show the step change. Decisions made on the cleaned metric stop flip-flopping.

## When to use

You are seeing this: Symptom: open rates spike across campaigns while clicks stay flat. Use this skill when you run into "SendGrid open rates suddenly inflated: Apple Mail Privacy Protection".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_XObcVUoV1ZrChtc_fTvcMQ). Version: `skv_pPRmAHO5dvIxiRDknRWX8Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
