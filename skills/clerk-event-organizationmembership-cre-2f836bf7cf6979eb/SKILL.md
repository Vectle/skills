---
name: "clerk-event-organizationmembership-cre-2f836bf7cf6979eb"
description: "Shows how to fix clerk event: organizationMembership.created, grant the seat from the nested payload. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_vbefljT-FhgaFkY6b13kkg"
  title: "Clerk event: organizationMembership.created, grant the seat from the nested payload"
  version: "skv_JIVV2OhpkktvZZz3OqZL_w"
  updated: "2026-10-04T05:03:09.167852+00:00"
  canonical_url: "https://vectle.com/skills/skl_vbefljT-FhgaFkY6b13kkg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Do not double-provision: the membership event is the one that grants access. - Roles are strings like org:admin. Compare against the exact role key, not a substring.

## Steps

1. Do not double-provision: the membership event is the one that grants access. - Roles are strings like org:admin.

2. Compare against the exact role key, not a substring.

## When to use

You are seeing this: Fires when a user becomes a member of an organization, by invitation acceptance, admin add, or self-join depending on your settings. Use this skill when you run into "Clerk event: organizationMembership.created, grant the seat from the nested payload".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_vbefljT-FhgaFkY6b13kkg). Version: `skv_JIVV2OhpkktvZZz3OqZL_w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
