---
name: "adyen-14-006-paymentmethod-object-has-c32ab6a1e36d0ab6"
description: "Resolves Adyen checkout error 14_006 when the /payments request has no paymentMethod object at all. Use when your request builder drops the whole block or your frontend never sends the shopper's choice. Not for a paymentMethod that is present but incomplete."
metadata:
  skill_id: "skl_8CGi_sLZhkjytIgcIxAyRQ"
  title: "Adyen 14_006 - paymentMethod object has not been provided in the request"
  version: "skv_y95SpsSlS7tAgh-7xUAk1Q"
  updated: "2026-10-03T06:08:29.219419+00:00"
  canonical_url: "https://vectle.com/skills/skl_8CGi_sLZhkjytIgcIxAyRQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Your /payments request is missing the entire paymentMethod object. Always include it with the type the shopper selected, plus the fields that type needs, and log the raw JSON to confirm it is sent.

The exact error:

```text
14_006 - paymentMethod object has not been provided in the request
```

## The fix

1. Log the full JSON body of the /payments request your server sends.
   Expected: You can see whether paymentMethod is present in the actual HTTP body.
2. Add the paymentMethod object with type set to the shopper's selected method on every code path.
   Expected: The request always carries how the shopper is paying.
3. Include the type-specific fields (encrypted card data for scheme, issuer for redirect methods) and resubmit.
   Expected: Adyen moves past validation to authorization or a further action.

## When this applies

- /payments returns 14_006
- A new checkout code path was just deployed
- The frontend posts the order but the method selection never reaches your server

## When it does NOT apply

- paymentMethod is present but missing fields (that is 14_004)
- The details inside are malformed (that is 14_005 or 14_007)
- /payments/details calls, which use a different request shape

## Versions

Adyen Checkout API v68 through v71.

## Why it happens

Adyen routes the payment based on paymentMethod.type. With the whole object missing there is nothing to route, so validation rejects the request with 14_006 before any further checks.

## Edge cases and pitfalls

- Some SDK wrappers nest the object under a different key; check the serialized JSON, not the builder code
- A redirect payment method still needs paymentMethod with type and returnUrl, not just the amount
- The /sessions flow builds paymentMethod from the shopper's selection automatically


---

Source: [Vectle](https://vectle.com/skills/skl_8CGi_sLZhkjytIgcIxAyRQ). Version: `skv_y95SpsSlS7tAgh-7xUAk1Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
