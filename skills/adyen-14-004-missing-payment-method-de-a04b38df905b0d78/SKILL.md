---
name: "adyen-14-004-missing-payment-method-de-a04b38df905b0d78"
description: "Resolves Adyen checkout error 14_004 when a /payments request is missing the card or method-specific details. Use when the paymentMethod object exists but the fields the payment type needs (like encrypted card data) are absent. Not for a missing paymentMethod object entirely (that is 14_006)."
metadata:
  skill_id: "skl_gdSGChw7v9_3Kt_u-X5QfA"
  title: "Adyen 14_004 - Missing payment method details"
  version: "skv_AY6Dy5yvR8cJQiJTCq4mUw"
  updated: "2026-10-03T06:07:38.339811+00:00"
  canonical_url: "https://vectle.com/skills/skl_gdSGChw7v9_3Kt_u-X5QfA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The paymentMethod object is missing required encrypted fields for the payment type. Use the Adyen web components to encrypt the card data and forward every encrypted field they return into the paymentMethod object unchanged.

The exact error:

```text
14_004 - Missing payment method details
```

## The fix

1. Use the Adyen web Drop-in or Card component to collect card data so the fields are encrypted client-side.
   Expected: The component state contains encrypted values for number, expiry, and CVC.
2. Map every encrypted field the component returns into the paymentMethod object without renaming or dropping any.
   Expected: No required field is null or an empty string in the outgoing request.
3. Resubmit /payments and confirm the paymentMethod block in the request matches the Adyen API reference for the type.
   Expected: Adyen accepts the request and returns a resultCode instead of 14_004.

## When this applies

- /payments returns 14_004 for a card payment
- You built a custom card form instead of using Adyen components
- The request in your logs shows a paymentMethod.type but no encrypted card fields

## When it does NOT apply

- paymentMethod itself is absent from the request (that is 14_006)
- The details are present but malformed (that is 14_005 or 14_007)
- A 3D Secure details step failing in /payments/details (that is the 14_028 family)

## Versions

Adyen Checkout API v68 through v71, Web Drop-in and Components v5 and v6.

## Why it happens

Adyen validates the paymentMethod details against the requirements of paymentMethod.type before routing. A missing encrypted field fails that validation, so the payment never reaches authorization and 14_004 is returned.

## Edge cases and pitfalls

- Encrypted card fields expire; a shopper who idles on the checkout page may submit stale blobs
- Test and live client keys are not interchangeable; encrypted details from one environment fail in the other
- Some payment methods need extra fields (issuer for iDEAL, for example) beyond the card basics


---

Source: [Vectle](https://vectle.com/skills/skl_gdSGChw7v9_3Kt_u-X5QfA). Version: `skv_AY6Dy5yvR8cJQiJTCq4mUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
