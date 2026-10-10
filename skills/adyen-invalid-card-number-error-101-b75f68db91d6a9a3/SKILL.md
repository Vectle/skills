---
name: "adyen-invalid-card-number-error-101-b75f68db91d6a9a3"
description: "Fixes Adyen error 101 Invalid card number on /payments calls. Covers sanitizing the input, checking digit length against the card brand, running a Luhn check before sending, and switching to Adyen's secured card component with client-side encryption instead of custom card forms. Not for error 102 (unknown BIN) or genuine issuer declines."
metadata:
  skill_id: "skl_o26vVfWulfRvoDggpHHeVQ"
  title: "Adyen: Invalid card number (error 101)"
  version: "skv_kCvadcnHmEAQe1j8A2Bv8Q"
  updated: "2026-10-03T04:30:15.221026+00:00"
  canonical_url: "https://vectle.com/skills/skl_o26vVfWulfRvoDggpHHeVQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Invalid card number (error 101)

**TL;DR:** The card number failed basic validation: wrong length, non-numeric characters, or a failed Luhn check. Strip spaces, confirm it is all digits, and re-collect it through Adyen's secured card component instead of hand-rolled inputs.

```text
101 - Invalid card number
```

## Steps

1. **Sanitize the input.** Remove spaces and dashes, then confirm the result is digits only. A single stray character is enough to trigger 101.
   - *Success check:* the cleaned value matches the digits the shopper typed.
2. **Check the length against the brand.** Most brands are 16 digits, Amex is 15. Anything outside the brand's valid lengths fails.
   - *Success check:* digit count matches the detected brand.
3. **Run a Luhn check client-side.** It catches typos before the number ever reaches Adyen.
   - *Success check:* the number passes Luhn before you call /payments.
4. **Use the secured card component.** Adyen's Card component and client-side encryption handle formatting, brand detection and encryption for you. Raw card numbers posted by custom forms are the main source of 101s.
   - *Success check:* the payment request carries encrypted card data and 101 stops appearing.

## When to use this

- /payments returns 101 on card payments.
- Shoppers report "card declined" but your logs show 101, which is a validation failure, not a decline.

## When NOT to use this

- Error 102 (unable to determine variant). That means the BIN is unknown, not that the number is malformed.
- A real decline (resultCode Refused). That is the issuer saying no, not a formatting problem.

## Compatibility

Adyen Checkout API card payments, Web Drop-in/Components and API-only integrations.

## Why it happens

101 is Adyen telling you the number itself is malformed: typo, pasted with spaces, truncated by a maxlength on your input, or a test card number used in the wrong environment. It can also surface from 3DS flows when PaRes comes back with wrong capitalization.

## Edge cases

- Test card numbers only work in TEST. Using one against LIVE gives confusing failures.
- If your own input masks the number (maxlength 16), Amex cards (15 digits) still work but 19-digit cards get truncated. Prefer the Adyen component.


---

Source: [Vectle](https://vectle.com/skills/skl_o26vVfWulfRvoDggpHHeVQ). Version: `skv_kCvadcnHmEAQe1j8A2Bv8Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
