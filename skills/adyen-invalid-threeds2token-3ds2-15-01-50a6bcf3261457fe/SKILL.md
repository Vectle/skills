---
name: "adyen-invalid-threeds2token-3ds2-15-01-50a6bcf3261457fe"
description: "Fixes Adyen 3DS2 error 15_014 Invalid threeDS2Token. Explains the token is single-use and bound to one transaction, the fix of never caching or replaying tokens across attempts and restarting from /payments on failure, and completing fingerprint and challenge promptly. Not for missing tokens (15_009) or the 12-hour transaction window (15_017)."
metadata:
  skill_id: "skl_ENEPwUEIApSPALxdNSfx5w"
  title: "Adyen: Invalid threeDS2Token (3DS2 15_014)"
  version: "skv_V8OYmx5E360Vj_H_nL4rRw"
  updated: "2026-10-03T04:33:20.210117+00:00"
  canonical_url: "https://vectle.com/skills/skl_ENEPwUEIApSPALxdNSfx5w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Invalid threeDS2Token (3DS2 15_014)

**TL;DR:** The threeDS2Token is single-use and bound to one transaction. If it expired, was already consumed, or came from a different payment attempt, throw it away and run /payments again to get a fresh one. Never cache or reuse tokens across attempts.

```text
15_014 - Invalid threeDS2Token
```

## Steps

1. **Stop reusing the token.** Check your code for anywhere the threeDS2Token is stored and replayed: session caches, retry queues, shared variables across attempts. Each /payments response mints a new one.
   - *Success check:* the token you send was issued by the immediately preceding /payments response for this shopper.
2. **Complete the 3DS2 steps promptly.** Fingerprint and challenge must happen against the current token. If the shopper stalls and you retry, start over from /payments.
   - *Success check:* no long gaps or retries between receiving the token and using it.
3. **On 15_014, restart the payment.** Dont try to repair the token. Make a new /payments call and continue the flow with the fresh token.
   - *Success check:* the new attempt proceeds past the step that failed.

## When to use this

- 3DS2 fingerprint or challenge calls fail with 15_014.
- Your retry logic replays a stored threeDS2Token after the shopper goes back.

## When NOT to use this

- 15_009 (threeDS2Token is required). That means you sent no token at all, not a stale one.
- 15_017 (authorisation more than 12 hours after the transaction began). That is the transaction aging out, a different clock.

## Compatibility

Adyen 3D Secure 2 native flows (Web, iOS, Android), Checkout API and classic /authorise3ds2.

## Why it happens

The token is a one-time pointer to the 3DS2 server transaction. Consuming it twice, using one minted for a different attempt, or letting it go stale while the shopper idles all produce 15_014.

## Edge cases

- Parallel /payments calls for the same shopper mint parallel tokens. Only the latest flow is valid; cancel or ignore the others.
- If your frontend and backend each hold a copy, make the backend the single source of truth for which token is current.


---

Source: [Vectle](https://vectle.com/skills/skl_ENEPwUEIApSPALxdNSfx5w). Version: `skv_V8OYmx5E360Vj_H_nL4rRw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
