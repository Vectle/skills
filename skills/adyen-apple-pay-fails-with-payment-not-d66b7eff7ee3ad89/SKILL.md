---
name: "adyen-apple-pay-fails-with-payment-not-d66b7eff7ee3ad89"
description: "Shows how to fix adyen Apple Pay fails with Payment not completed inside an iframe (fixed in 6.23.0). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_e4b_-xcTaLrEc9XhBYQVIw"
  title: "Adyen Apple Pay fails with Payment not completed inside an iframe (fixed in 6.23.0)"
  version: "skv__kmpBzHFmrOvsHdFwkYJNw"
  updated: "2026-10-03T13:46:35.397692+00:00"
  canonical_url: "https://vectle.com/skills/skl_e4b_-xcTaLrEc9XhBYQVIw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_M6VRWmAc1M1rmHCmKcXTrA\",\"https://github.com/Adyen/adyen-web/issues/2351\"]"
---

## TL;DR

Upgrade @adyen/adyen-web to 6.23.0 or newer, which added support for this case (PR #3561); then configure the Apple Pay component in paymentMethodsConfiguration as described in the thread. Reporters confirmed the simpler config on 6.23.0+ resolves the immediate dismissal.

## Steps

1. Upgrade @adyen/adyen-web to 6.23.0 or newer, which added support for this case (PR #3561); then configure the Apple Pay component in paymentMethodsConfiguration as described in the thread. Reporters confirmed the simpler config on 6.23.0+ resolves the immediate dismissal. The underlying change was in how the SDK validates the Apple Pay merchant session, per PR #3561.

## When to use

You are seeing this: With the Adyen web drop-in placed on a page embedded in an iframe, the Apple Pay button showed but tapping it immediately dismissed the sheet with Payment not completed. Use this skill when you run into "Adyen Apple Pay fails with Payment not completed inside an iframe (fixed in 6.23.0)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 6.23.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_e4b_-xcTaLrEc9XhBYQVIw). Version: `skv__kmpBzHFmrOvsHdFwkYJNw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
