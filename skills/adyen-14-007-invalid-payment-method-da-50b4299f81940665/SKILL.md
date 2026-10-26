---
name: "adyen-14-007-invalid-payment-method-da-50b4299f81940665"
description: "Resolves Adyen checkout error 14_007 when the paymentMethod object contains bad data, such as a missing type. Use when paymentMethod exists but Adyen rejects its contents. Not for a wholly absent paymentMethod (14_006) or missing detail fields (14_004)."
metadata:
  skill_id: "skl_TSZRb8v0GIBNwteAT4YCrg"
  title: "Adyen 14_007 - Invalid payment method data"
  version: "skv_SwQtR5R4iCXNzjLDlY0Vyw"
  updated: "2026-10-03T06:21:57.330137+00:00"
  canonical_url: "https://vectle.com/skills/skl_TSZRb8v0GIBNwteAT4YCrg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

TL;DR: The paymentMethod object is present but its contents are invalid, usually a missing or misspelled type. Log the block, set type to an exact API reference value that your account has enabled, and whitelist it server-side.

The exact error:

```text
14_007 - Invalid payment method data
```

## The fix

1. Log the paymentMethod block of the failing request.
   Expected: You see exactly what your server sent inside paymentMethod.
2. Set paymentMethod.type to a valid, enabled value such as scheme or ideal.
   Expected: The type matches the API reference spelling and is enabled for your account.
3. Add a server-side whitelist for the type field so bad values are caught before the API call.
   Expected: Validation passes and the payment proceeds.

## When this applies

- /payments returns 14_007
- You map shopper input to the type field by hand
- A new payment method was just enabled in the dashboard

## When it does NOT apply

- paymentMethod is missing entirely (that is 14_006)
- Required encrypted fields are absent (that is 14_004)
- The shopper's bank refused the payment after validation passed

## Versions

Adyen Checkout API v68 through v71.

## Why it happens

Adyen validates the paymentMethod object field by field. A missing or unrecognized type means the payment cannot be routed, so the request fails validation with 14_007.

## Edge cases and pitfalls

- paymentMethod.type is case-sensitive; Scheme with a capital S is rejected
- Extra unknown fields inside paymentMethod can also trigger this, not just missing ones
- Copy-pasted examples sometimes use a type your merchant account has disabled


---

Source: [Vectle](https://vectle.com/skills/skl_TSZRb8v0GIBNwteAT4YCrg). Version: `skv_SwQtR5R4iCXNzjLDlY0Vyw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
