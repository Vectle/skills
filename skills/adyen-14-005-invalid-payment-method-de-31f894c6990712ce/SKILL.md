---
name: "adyen-14-005-invalid-payment-method-de-31f894c6990712ce"
description: "Resolves Adyen checkout error 14_005 when payment method details fail validation, most often a recurring contract mismatch. Use when a stored card or token payment is rejected and the docs point at the recurring contract. Not for malformed card data on a first payment."
metadata:
  skill_id: "skl_IeiGF-6tKV7AqCMEZR6uXA"
  title: "Adyen 14_005 - Invalid payment method details"
  version: "skv_C79PVb-xUcBhBGVC4yBxWg"
  updated: "2026-10-03T06:07:51.672805+00:00"
  canonical_url: "https://vectle.com/skills/skl_IeiGF-6tKV7AqCMEZR6uXA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

TL;DR: The recurring contract on the stored token does not match the contract in your request. Check the token's contract in the Customer Area, request the matching contract, or re-tokenize the card with the contract you need.

The exact error:

```text
14_005 - Invalid payment method details
```

## The fix

1. Look up the stored payment method in the Adyen Customer Area and note its recurring contract.
   Expected: You see whether the token is RECURRING, ONECLICK, or both.
2. Set recurringProcessingModel and shopperInteraction in /payments to match the token's contract.
   Expected: The requested contract matches what the token supports.
3. If the contracts cannot be reconciled, re-tokenize the card with the contract you need and retry.
   Expected: The payment proceeds past validation to authorization.

## When this applies

- /payments with a stored card returns 14_005
- You recently changed between one-click and subscription flows
- Tokens came from a migration and now fail validation

## When it does NOT apply

- A first-time card payment with fresh details (look at 14_004 or 14_007 instead)
- The token itself is missing or expired
- A 3D Secure failure after the payment was accepted for processing

## Versions

Adyen Checkout API v68 through v71. Applies to stored payment methods and tokens.

## Why it happens

The stored payment method carries a fixed recurring contract. Adyen compares the contract in your request against the token's contract during validation, and a mismatch is rejected as invalid payment method details.

## Edge cases and pitfalls

- A token created with a RECURRING contract cannot be used for a ONECLICK payment and vice versa
- Migrated tokens from another processor may carry a contract type your Adyen config does not allow
- The shopperReference must match the one the token was stored under


---

Source: [Vectle](https://vectle.com/skills/skl_IeiGF-6tKV7AqCMEZR6uXA). Version: `skv_C79PVb-xUcBhBGVC4yBxWg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
