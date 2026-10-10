---
name: "google-pay-multiparty-confirmorder-fai-9a43760fcdd80755"
description: "Shows how to fix google Pay Multiparty: confirmOrder() fails with INVALID_GOOGLE_PAY_TOKEN. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_c4PciDGDxMX9a3zFeOOLzg"
  title: "Google Pay Multiparty: confirmOrder() fails with INVALID_GOOGLE_PAY_TOKEN"
  version: "skv_wnmbTH7yVwoUkytUc_Iczw"
  updated: "2026-10-04T15:48:07.812617+00:00"
  canonical_url: "https://vectle.com/skills/skl_c4PciDGDxMX9a3zFeOOLzg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

The platform team deployed a fix, and the reporter verified Sandbox works correctly after it.

## Steps

1. [EvanReinstein (contributor)]: INVALID_GOOGLE_PAY_TOKEN on every confirmOrder in Sandbox was a known issue in the Sandbox Google Pay token-decryption service, not your integration. The platform team deployed a fix, and the reporter verified Sandbox works correctly after it.

## When to use

You are seeing this: Issue paypal/paypal-js#1012 (closed, 6 comments): ### Library used Direct PayPal JavaScript SDK integration (Google Pay component) ### 🐞 Describe the Bug We are integrating Google Pay with PayPal in a Multiparty (Marketplace/PPCP) integration. Use this skill when you run into "Google Pay Multiparty: confirmOrder() fails with INVALID_GOOGLE_PAY_TOKEN".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_c4PciDGDxMX9a3zFeOOLzg). Version: `skv_wnmbTH7yVwoUkytUc_Iczw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
