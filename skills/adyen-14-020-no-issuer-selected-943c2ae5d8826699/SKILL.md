---
name: "adyen-14-020-no-issuer-selected-943c2ae5d8826699"
description: "Resolves Adyen checkout error 14_020 when a redirect payment method needs an issuer choice and none was sent. Use for iDEAL, Dotpay, and similar bank-select methods. Not for card payments, which have no issuer step."
metadata:
  skill_id: "skl_gPgRTQPmlTv1isy9xFdmkQ"
  title: "Adyen 14_020 - No issuer selected"
  version: "skv_NDR1On4DdvrMO2o3lRyDCg"
  updated: "2026-10-03T06:21:58.838278+00:00"
  canonical_url: "https://vectle.com/skills/skl_gPgRTQPmlTv1isy9xFdmkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

TL;DR: A bank-redirect method like iDEAL was submitted without an issuer. Render the issuer list from /paymentMethods, require the shopper to pick a bank, and forward the issuer id unchanged.

The exact error:

```text
14_020 - No issuer selected
```

## The fix

1. Render the issuer options from the /paymentMethods response instead of hardcoding them.
   Expected: Your checkout shows the current bank list.
2. Require an issuer selection before submit and forward the issuer id unchanged.
   Expected: The request always carries the shopper's choice.
3. For returning shoppers, store the issuer with the token and include it on repeat payments.
   Expected: The shopper is redirected to their bank.

## When this applies

- iDEAL or similar payments return 14_020
- You built a custom bank-select screen
- Repeat payments with stored redirect details fail

## When it does NOT apply

- Card payments (no issuer concept)
- Wallet payments like PayPal
- The issuer is present but the bank rejects the shopper (a different, later error)

## Versions

Adyen Checkout API v68 through v71. Applies to issuer-based redirect methods.

## Why it happens

Redirect methods route the shopper to a specific bank. Without an issuer Adyen does not know where to redirect, so the request fails validation.

## Edge cases and pitfalls

- The issuer list comes from /paymentMethods; hardcoding issuers breaks when banks change
- Some issuers are test-only and fail in live with a different error
- If the shopper skips the bank select screen, your frontend must still send a default or re-prompt


---

Source: [Vectle](https://vectle.com/skills/skl_gPgRTQPmlTv1isy9xFdmkQ). Version: `skv_NDR1On4DdvrMO2o3lRyDCg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
