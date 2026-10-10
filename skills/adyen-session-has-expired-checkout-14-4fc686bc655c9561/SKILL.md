---
name: "adyen-session-has-expired-checkout-14-4fc686bc655c9561"
description: "Fixes Adyen Checkout error 14_008 Session has expired. Explains the 1-hour session lifetime, how to tell a stale or reused session id is the cause, and the fix of creating a fresh session via /sessions and re-mounting the shopper on it. Not for payment-link expiry or malformed session creation requests."
metadata:
  skill_id: "skl_0ZCcyEiZR1dB0Xnn3NoNrg"
  title: "Adyen: Session has expired (Checkout 14_008)"
  version: "skv_d4LgBNoPwuVT1Q7vQ5Kidg"
  updated: "2026-10-03T04:28:51.090857+00:00"
  canonical_url: "https://vectle.com/skills/skl_0ZCcyEiZR1dB0Xnn3NoNrg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Session has expired (Checkout 14_008)

**TL;DR:** Adyen checkout sessions expire 1 hour after creation. If the shopper idles too long or your code reuses a session id, create a brand-new session and send the shopper through it. There is no way to revive an expired one.

```text
14_008 - Session has expired
```

## Steps

1. **Confirm you are reusing a session.** Check your logs for the session id: if it is older than an hour or already completed, that is the problem.
   - *Success check:* you can point at the exact stale session id your frontend is holding.
2. **Create a fresh session.** POST to /sessions again with the same amount, reference and returnUrl. Treat it as a brand-new checkout.
   - *Success check:* the response returns 200 with a new session id and sessionData.
3. **Hand the new session to the shopper.** Reload or re-mount the Drop-in/Components with the new session data. Dont try to patch the old one.
   - *Success check:* the shopper sees a working payment form and the payment completes.

## When to use this

- The checkout fails with 14_008 after the shopper left the tab open, or your retry logic replays an old session id.
- Your logs show the same session id used across multiple payment attempts.

## When NOT to use this

- The error appears immediately on a brand-new session. Then the request itself is malformed; check the session creation payload instead.
- Payment links (those have their own expiry, 14_0385).

## Compatibility

Adyen Checkout API /sessions on Web Drop-in and Components, TEST and LIVE.

## Why it happens

Sessions are short-lived by design (1 hour). Anything slower than that, a shopper who walks away, a queued retry, a cached session id, hits 14_008 on the next call.

## Edge cases

- Hosted payment links and QR codes have separate expiry errors (14_0385, 14_0389). Dont confuse them with session expiry.
- If shoppers routinely idle past an hour, refresh the session proactively before the hour mark instead of waiting for the error.


---

Source: [Vectle](https://vectle.com/skills/skl_0ZCcyEiZR1dB0Xnn3NoNrg). Version: `skv_d4LgBNoPwuVT1Q7vQ5Kidg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
