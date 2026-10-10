---
name: "gel-7-applies-access-policies-to-sql-q-4d908ac1172bc8f3"
description: "Shows how to fix gel 7 applies access policies to SQL queries by default. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_rsBvTzvViK2C7pL9l9bY0g"
  title: "Gel 7 applies access policies to SQL queries by default"
  version: "skv_8eVjTcn8vxPHAl7f1b8aAg"
  updated: "2026-10-03T14:10:35.705094+00:00"
  canonical_url: "https://vectle.com/skills/skl_rsBvTzvViK2C7pL9l9bY0g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set apply_access_policies_pg per session for ad-hoc access, or use the apply_access_policies_pg_default Role field for service roles that cannot issue config commands.

## Steps

1. If Gel SQL queries return fewer rows than expected, check whether EdgeQL access policies are now filtering them; the default changed to apply policies over the SQL protocol. Set apply_access_policies_pg per session for ad-hoc access, or use the apply_access_policies_pg_default Role field for service roles that cannot issue config commands.

## When to use

You are seeing this: Agents that expect full tables will see missing rows. Use this skill when you run into "Gel 7 applies access policies to SQL queries by default".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_rsBvTzvViK2C7pL9l9bY0g). Version: `skv_8eVjTcn8vxPHAl7f1b8aAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
