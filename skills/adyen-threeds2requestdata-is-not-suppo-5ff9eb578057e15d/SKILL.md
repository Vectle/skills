---
name: "adyen-threeds2requestdata-is-not-suppo-5ff9eb578057e15d"
description: "Fixes Adyen 3DS2 error 15_023 threeDS2RequestData is not supported for threeDS2InMDFlow. Explains the conflict between the native 3DS2 request data and the deprecated MD redirect flow flag, the fix of removing one of the two (preferring the native flow), and where the flag can hide in additionalData or account settings. Not for fingerprint or challenge-details errors."
metadata:
  skill_id: "skl_dRN3Gvm-lLebyD3OExh43g"
  title: "Adyen: threeDS2RequestData is not supported for threeDS2InMDFlow (15_023)"
  version: "skv_usPWG2ZBTdMcy6giwWl7TQ"
  updated: "2026-10-03T04:35:23.5835+00:00"
  canonical_url: "https://vectle.com/skills/skl_dRN3Gvm-lLebyD3OExh43g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: threeDS2RequestData is not supported for threeDS2InMDFlow (15_023)

**TL;DR:** You are mixing two generations of 3D Secure: the native 3DS2 request data and the old redirect (MD) flow flag. Pick one. The modern fix is to drop threeDS2RequestData from /payments and use the native 3DS2 flow end to end.

```text
15_023 - threeDS2RequestData is not supported for threeDS2InMDFlow
```

## Steps

1. **Find where the MD flow is requested.** Search your code and Customer Area settings for threeDS2InMDFlow: it can be set in additionalData on the request or as an account data setting.
   - *Success check:* you know exactly which place enables the MD flow.
2. **Remove threeDS2RequestData from /payments.** Delete the whole threeDS2RequestData object (deviceChannel, notificationURL and friends) from the request.
   - *Success check:* the request no longer contains threeDS2RequestData.
3. **Or remove the MD flow flag instead.** If you must keep threeDS2RequestData, drop the threeDS2InMDFlow flag from additionalData and disable the account setting. But the native flow is the one Adyen maintains, so prefer option 2.
   - *Success check:* exactly one of the two is present, not both.
4. **Follow the native flow steps.** IdentifyShopper for fingerprinting, ChallengeShopper for the challenge, /payments/details between steps.
   - *Success check:* the payment proceeds without 15_023.

## When to use this

- /payments fails with 15_023.
- A legacy integration was partially migrated to native 3DS2 and both flags survived.

## When NOT to use this

- You are on the redirect flow deliberately and getting other errors. Then remove threeDS2RequestData and keep the MD flow.
- 14_032 or 14_033 fingerprint errors. Those are about the details call, not the flow selection.

## Compatibility

Adyen Checkout API and classic /authorise 3DS flows.

## Why it happens

threeDS2InMDFlow routes the transaction through the old 3D Secure 1 style MD redirect flow, while threeDS2RequestData configures the native 3DS2 flow. They are mutually exclusive and Adyen rejects the combination.

## Edge cases

- The flag can hide in the Customer Area as an account data property, not just in your code. If you removed it from the request and still get 15_023, check the account settings.
- Migrating fully to native 3DS2 also means handling the fingerprint and challenge actions your redirect code never saw.


---

Source: [Vectle](https://vectle.com/skills/skl_dRN3Gvm-lLebyD3OExh43g). Version: `skv_usPWG2ZBTdMcy6giwWl7TQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
