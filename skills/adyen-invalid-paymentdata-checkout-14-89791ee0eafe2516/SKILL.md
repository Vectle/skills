---
name: "adyen-invalid-paymentdata-checkout-14-89791ee0eafe2516"
description: "Fixes Adyen Checkout error 14_003 Invalid paymentData on /payments/details calls. Explains that paymentData is single-use and rotated every step, the fix of always forwarding the paymentData from the latest action response, and keeping paymentData and MD paired from the same attempt. Not for missing paymentData (14_002) or first-call /payments failures."
metadata:
  skill_id: "skl_G7GBIaFGotGUIimJVwkwyw"
  title: "Adyen: Invalid paymentData (Checkout 14_003)"
  version: "skv_5JzMAkMjv30HZNJif1rO9w"
  updated: "2026-10-03T04:29:28.565496+00:00"
  canonical_url: "https://vectle.com/skills/skl_G7GBIaFGotGUIimJVwkwyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Invalid paymentData (Checkout 14_003)

**TL;DR:** paymentData is single-use and tied to one specific payment attempt. Always forward the exact paymentData from the *latest* action response, and never mix it with an MD value from a different attempt. If you lost track of which is newest, restart the payment.

```text
14_003 - Invalid paymentData
```

## Steps

1. **Use the newest paymentData you have.** Every /payments and /payments/details response can return a fresh paymentData. Always take it from the latest response in this attempt.
   - *Success check:* the paymentData you send matches the one from the most recent API response for this shopper.
2. **Keep paymentData and MD as a pair.** If the flow also involves an MD value, both must come from the same attempt. Mixing paymentData from attempt 1 with MD from attempt 2 gives 14_0448 (paymentData and MD dont belong to the same payment) or 14_003.
   - *Success check:* both values were issued together in one response.
3. **Send /payments/details once per step.** Dont replay an old details call after the shopper retries; each step consumes its paymentData.
   - *Success check:* /payments/details returns the next action or a resultCode instead of 14_003.
4. **When in doubt, restart.** If your server lost track of which paymentData is current, create a new payment rather than guessing.
   - *Success check:* the new attempt flows without 14_003.

## When to use this

- /payments/details fails with 14_003 during 3D Secure or redirect flows.
- The shopper retried or went back, and your backend replayed a stored paymentData.

## When NOT to use this

- The first /payments call fails. paymentData only exists after an action response, so the problem is elsewhere.
- You get 14_002 (paymentData missing entirely). That is a missing-field problem, not a stale-value one.

## Compatibility

Adyen Checkout API /payments/details, all channels (Web, iOS, Android), TEST and LIVE.

## Why it happens

paymentData is a server-side pointer to the in-flight payment state. It is rotated on every step and invalidated when the shopper starts over. Storing one copy and replaying it across retries, or pairing values from two different attempts, is what triggers 14_003.

## Edge cases

- 3DS2 flows rotate paymentData at fingerprint and challenge steps. Update your stored copy on every response.
- Redirect flows: the MD in the return URL belongs to the same attempt as the paymentData. Dont cache either across attempts.


---

Source: [Vectle](https://vectle.com/skills/skl_G7GBIaFGotGUIimJVwkwyw). Version: `skv_5JzMAkMjv30HZNJif1rO9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
