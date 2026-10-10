---
name: "flagsmith-local-evaluation-can-retain-3e2c578a7a1d7806"
description: "Shows how to fix flagsmith local evaluation can retain stale traits across evaluations. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_D7WMy0eFz7GWbKJ2lQwxKQ"
  title: "Flagsmith local evaluation can retain stale traits across evaluations"
  version: "skv_lBQXIDIzGnP5uzK9rbgW_Q"
  updated: "2026-10-03T14:15:22.04394+00:00"
  canonical_url: "https://vectle.com/skills/skl_D7WMy0eFz7GWbKJ2lQwxKQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Always pass the full trait set on every evaluation when using local evaluation with identity overrides; never assume omitted traits mean unset. Pin the SDK version and watch the changelog for a fix.

## Steps

1. Always pass the full trait set on every evaluation when using local evaluation with identity overrides; never assume omitted traits mean unset. If targeting behaves inconsistently across evaluations of one identity, check for trait retention before suspecting the segment rules. Pin the SDK version and watch the changelog for a fix.

## When to use

You are seeing this: If targeting behaves inconsistently across evaluations of one identity, check for trait retention before suspecting the segment rules. Use this skill when you run into "Flagsmith local evaluation can retain stale traits across evaluations".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_D7WMy0eFz7GWbKJ2lQwxKQ). Version: `skv_lBQXIDIzGnP5uzK9rbgW_Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
