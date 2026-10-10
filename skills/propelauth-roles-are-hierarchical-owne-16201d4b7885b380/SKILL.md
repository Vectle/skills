---
name: "propelauth-roles-are-hierarchical-owne-16201d4b7885b380"
description: "Shows how to fix propelAuth roles are hierarchical, Owner beats Admin beats Member. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_B0VIxcMcFimirvqWzgPflw"
  title: "PropelAuth roles are hierarchical, Owner beats Admin beats Member"
  version: "skv_IZx8pKsK_bvE4mLZ50HUlw"
  updated: "2026-10-04T04:15:43.873918+00:00"
  canonical_url: "https://vectle.com/skills/skl_B0VIxcMcFimirvqWzgPflw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check roles with user_is_role on the org object and rely on the hierarchy: asking for Admin matches Owners too.

## Steps

1. Check roles with user_is_role on the org object and rely on the hierarchy: asking for Admin matches Owners too. If you customized the role structure, re-verify the ordering, since the hierarchy assumption only holds for the default Owner, Admin, Member chain.

## When to use

You are seeing this: If you customized the role structure, re-verify the ordering, since the hierarchy assumption only holds for the default Owner, Admin, Member chain. Use this skill when you run into "PropelAuth roles are hierarchical, Owner beats Admin beats Member".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_B0VIxcMcFimirvqWzgPflw). Version: `skv_IZx8pKsK_bvE4mLZ50HUlw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
