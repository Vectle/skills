---
name: "adyen-14-002-paymentdata-has-not-been-1386b4f230a2e21c"
description: "Resolves Adyen checkout error 14_002 when the paymentData field is missing from a /payments/details call. Use when a redirect or 3D Secure flow returns to your server and Adyen rejects the details request. Not for the initial /payments call, which does not take paymentData."
metadata:
  skill_id: "skl_MwDXsb0-ztaMxLGsLsUOQg"
  title: "Adyen 14_002 - paymentData has not been provided in the request"
  version: "skv_r2xRKXZFfAzk7haHKfS_9g"
  updated: "2026-10-03T06:02:25.576214+00:00"
  canonical_url: "https://vectle.com/skills/skl_MwDXsb0-ztaMxLGsLsUOQg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

TL;DR: This means your /payments/details request is missing the paymentData blob from the first /payments response. Capture action.paymentData server-side when you create the payment, store it across the redirect, and send it back verbatim in /payments/details.

The exact error:

```text
14_002 - paymentData has not been provided in the request
```

## The fix

1. Capture paymentData from the /payments response: read action.paymentData on your server, not in the browser.
   Expected: Your logs show a paymentData string starting with the encrypted blob from Adyen.
2. Store it server-side keyed by your order reference (session, cache, or database) before redirecting the shopper.
   Expected: The value survives the shopper's trip to the bank and back.
3. Send it back verbatim in /payments/details alongside redirectResult or the details object.
   Expected: Adyen returns resultCode Authorised, Refused, or a further action instead of 14_002.

## When this applies

- /payments/details returns 14_002 after a redirect or 3D Secure challenge
- Your logs show the details request has no paymentData field at all
- A shopper completes their bank redirect but the payment never finalizes

## When it does NOT apply

- The initial /payments call, which creates paymentData rather than consuming it
- A 14_003 invalid paymentData error, where the value is present but corrupt (different fix)
- The /sessions + /paymentMethods flow, where the session object carries the state

## Versions

Adyen Checkout API v68 through v71. The /sessions flow uses sessionData instead of paymentData.

## Why it happens

Adyen keeps no server-side link between the redirect return and the original payment except the paymentData blob you echo back. Without it the /payments/details call is an orphan, so validation rejects it before any payment logic runs.

## Edge cases and pitfalls

- paymentData expires after about 3 hours, so a shopper who returns late will hit a different error
- Do not store paymentData in client-side local storage on a shared device; keep it server-side
- The /sessions flow uses sessionData instead; paymentData belongs to the classic /payments/details flow


---

Source: [Vectle](https://vectle.com/skills/skl_MwDXsb0-ztaMxLGsLsUOQg). Version: `skv_r2xRKXZFfAzk7haHKfS_9g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
