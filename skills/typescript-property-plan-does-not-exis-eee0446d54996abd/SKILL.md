---
name: "typescript-property-plan-does-not-exis-eee0446d54996abd"
description: "Shows how to fix typeScript - Property 'plan' does not exist on type 'Subscription'. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_BlqgOaEtqmBOuv0FArx96A"
  title: "TypeScript - Property 'plan' does not exist on type 'Subscription'"
  version: "skv_806GnclrfkPztkdWZtHNNA"
  updated: "2026-10-03T23:10:25.770651+00:00"
  canonical_url: "https://vectle.com/skills/skl_BlqgOaEtqmBOuv0FArx96A"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/stripe/stripe-node/issues/1794\"]"
---

## TL;DR

Use items.data[xxx].price instead. [remi-stripe (maintainer)]: The plan property on Subscription was deprecated years ago, so it is intentionally absent from the TypeScript types and the docs.

## Steps

1. [remi-stripe (maintainer)]: The `plan` property on Subscription was deprecated years ago, so it is intentionally absent from the TypeScript types and the docs. Use `items.data[xxx].price` instead. The property still comes back in API responses for older API versions (any removal would be gated behind a new API version), but do not build new integrations on it.

## When to use

You are seeing this: Issue stripe/stripe-node#1794 (closed, 14 comments): ### Describe the bug The property plan is not accessible on Subscription objects when used in TypeScript. Use this skill when you run into "TypeScript - Property 'plan' does not exist on type 'Subscription'".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_BlqgOaEtqmBOuv0FArx96A). Version: `skv_806GnclrfkPztkdWZtHNNA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
