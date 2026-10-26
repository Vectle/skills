---
name: "adyen-403-errorcode-010-not-allowed-en-a642f5294af202fd"
description: "Shows how to fix adyen 403 errorCode 010 Not allowed: enable raw card processing or use client-side encryption. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_rymDqUJpCULrbiEL3KMdFg"
  title: "Adyen 403 errorCode 010 Not allowed: enable raw card processing or use client-side encryption"
  version: "skv_rZI_edUev6OdSopEFnFzGg"
  updated: "2026-10-03T17:28:59.057849+00:00"
  canonical_url: "https://vectle.com/skills/skl_rymDqUJpCULrbiEL3KMdFg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/47330297\"]"
---

## TL;DR

Handling raw PAN data requires full PCI compliance (SAQ D) and Adyen has to enable the permission on your account, so contact Adyen support and ask for raw card processing permission.

## Steps

1. ErrorCode 010 "Not allowed" means your API user is not permitted to process raw card details, not that the credentials are wrong. Handling raw PAN data requires full PCI compliance (SAQ D) and Adyen has to enable the permission on your account, so contact Adyen support and ask for raw card processing permission. If you do not want the PCI burden, switch to the client-side encryption (CSE) flow instead: the card is encrypted in the browser and your server only ever sees the encrypted blob, which needs no special permission.

## When to use

You are seeing this: ErrorCode 010 "Not allowed" means your API user is not permitted to process raw card details, not that the credentials are wrong. Use this skill when you run into "Adyen 403 errorCode 010 Not allowed: enable raw card processing or use client-side encryption".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_rymDqUJpCULrbiEL3KMdFg). Version: `skv_rZI_edUev6OdSopEFnFzGg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
