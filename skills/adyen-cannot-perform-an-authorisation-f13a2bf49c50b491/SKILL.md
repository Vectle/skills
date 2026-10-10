---
name: "adyen-cannot-perform-an-authorisation-f13a2bf49c50b491"
description: "Fixes Adyen 3DS2 error 15_017 where authorisation is attempted more than 12 hours after the transaction began. Covers confirming the timestamp gap, restarting the payment since stale authentication cannot be extended, and designing delayed-capture flows to complete inside the window. Not for the 60-day stored-authentication variant (15_024)."
metadata:
  skill_id: "skl_ZOvEGYincyNTypSIYfQxjQ"
  title: "Adyen: Cannot perform an authorisation on a 3DS2 transaction more than 12 hours after the transaction began"
  version: "skv_M_Jb-bWjGMJHRDEKRyc1Zg"
  updated: "2026-10-03T04:36:05.398379+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZOvEGYincyNTypSIYfQxjQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Cannot perform an authorisation on a 3DS2 transaction more than 12 hours after the transaction began

**TL;DR:** 3DS2 authentication goes stale 12 hours after the transaction starts. If your authorisation lands after that window, usually because capture was delayed, you have to start a fresh payment. Design delayed-capture flows to complete inside the window.

```text
15_017 - Cannot perform an authorisation on a 3DS2 transaction more than 12 hours after the transaction began
```

## Steps

1. **Check the clock.** Compare the original transaction start time with the authorisation attempt. If the gap is over 12 hours, that is the whole story.
   - *Success check:* you can point at the two timestamps and the gap.
2. **Restart the payment.** Run /payments again from the top, including 3DS2 authentication. There is no refresh or extension for the old authentication.
   - *Success check:* the new attempt authorises cleanly.
3. **Fix the process for next time.** If delayed capture is the pattern, either capture within 12 hours or re-authenticate before capturing. Dont let authenticated transactions sit.
   - *Success check:* your capture jobs run inside the window, or re-auth is part of the flow.

## When to use this

- Authorisation fails with 15_017 hours after the shopper authenticated.
- Batch or queued capture jobs process 3DS2 transactions late.

## When NOT to use this

- 15_024 (authentication older than 60 days). That is the stored-authentication variant, a different clock.
- The failure is immediate. Then the problem is the request, not the window.

## Compatibility

Adyen 3DS2 flows with separate authorisation and capture, Checkout API and classic API.

## Why it happens

The 3DS2 authentication is only considered fresh for 12 hours. Adyen will not authorise against a stale authentication because the risk assessment it was based on is out of date.

## Edge cases

- Timezone bugs make this look intermittent. Always compare in UTC.
- If your queue backs up (incidents, deploys), a batch of transactions can age out together. Alert on transaction age before it hits 12 hours.


---

Source: [Vectle](https://vectle.com/skills/skl_ZOvEGYincyNTypSIYfQxjQ). Version: `skv_M_Jb-bWjGMJHRDEKRyc1Zg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
