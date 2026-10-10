---
name: "flowise-flows-are-public-to-anyone-wit-4842f563d0b3096b"
description: "Shows how to fix flowise flows are public to anyone with the ID until you assign an API key. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_uvrJgAe0dRLysVR0PlT3Vw"
  title: "Flowise flows are public to anyone with the ID until you assign an API key"
  version: "skv_VeOIaoS8aQ5IcgbbTOUHFg"
  updated: "2026-10-03T14:14:40.647256+00:00"
  canonical_url: "https://vectle.com/skills/skl_uvrJgAe0dRLysVR0PlT3Vw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Every prediction call then needs the Authorization header set to Bearer plus the key. If you run multiple environments, note the APIKEY_PATH env variable controls where keys are stored, so keep keys consistent across your deployment.

## Steps

1. Decide up front whether a flow should be public: if not, assign an API key to it before sharing the chatflow ID anywhere. Every prediction call then needs the Authorization header set to Bearer plus the key. If you run multiple environments, note the APIKEY_PATH env variable controls where keys are stored, so keep keys consistent across your deployment.

## When to use

You are seeing this: Decide up front whether a flow should be public: if not, assign an API key to it before sharing the chatflow ID anywhere. Use this skill when you run into "Flowise flows are public to anyone with the ID until you assign an API key".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_uvrJgAe0dRLysVR0PlT3Vw). Version: `skv_VeOIaoS8aQ5IcgbbTOUHFg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
