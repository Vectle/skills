---
name: "adyen-the-provided-fingerprint-is-inva-b177d7ec42e54926"
description: "Fixes Adyen Checkout error 14_033 The provided fingerprint is invalid. Covers confirming the SDK actually returned fingerprint data, forwarding it untouched as threeds2.fingerprint in /payments/details, and setting threeDSCompInd correctly based on whether the 3DS method post arrived. Not for missing fingerprints (14_0402) or wrong-field errors (14_032)."
metadata:
  skill_id: "skl_9CnLMeIRYWZhJtNR6OvABw"
  title: "Adyen: The provided fingerprint is invalid (Checkout 14_033)"
  version: "skv_wgHm_YF55XSF7LtHk6EYcw"
  updated: "2026-10-03T04:40:07.232621+00:00"
  canonical_url: "https://vectle.com/skills/skl_9CnLMeIRYWZhJtNR6OvABw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: The provided fingerprint is invalid (Checkout 14_033)

**TL;DR:** You sent a fingerprint, but the data never actually made it into the /payments/details call intact. Usually the device fingerprint from the SDK was not forwarded, or the threeDSCompInd field was mishandled. Confirm you received the fingerprint data and pass it through untouched.

```text
14_033 - The provided fingerprint is invalid
```

## Steps

1. **Confirm the fingerprint data arrived.** Log what your SDK handed you after the IdentifyShopper step. If it is empty or you never waited for it, that is the bug.
   - *Success check:* you hold non-empty fingerprint data from the SDK callback.
2. **Forward it untouched into /payments/details.** Send it as the threeds2.fingerprint field with the paymentData from the action response. Dont re-encode, trim or rebuild it.
   - *Success check:* the details payload contains the fingerprint exactly as the SDK produced it.
3. **Set threeDSCompInd correctly.** If the 3DS method notification reached your notificationURL within 10 seconds, send Y; otherwise N. A wrong or missing value here is a known trigger.
   - *Success check:* threeDSCompInd reflects whether the method post arrived in time.
4. **Retry the details call.**
   - *Success check:* the flow advances to ChallengeShopper or a frictionless result instead of 14_033.

## When to use this

- /payments/details fails with 14_033 after IdentifyShopper.
- The fingerprint step ran but the details call still complains.

## When NOT to use this

- 14_0402 (missing 3DS2 fingerprint). That means no fingerprint was sent at all.
- 14_032 (provide fingerprint or challengeResult). That means the wrong field was sent for the step.

## Compatibility

Adyen Checkout API 3DS2 native flows, Web/iOS/Android.

## Why it happens

The fingerprint is produced asynchronously by the 3DS SDK. Code that fires /payments/details before the callback resolves, or that drops fields while mapping the SDK output to the API payload, sends a mangled or empty fingerprint.

## Edge cases

- 14_034 is the same family but names the affected field. If Adyen tells you which field, fix that one first.
- Race conditions: disable the pay button until the fingerprint callback completes.


---

Source: [Vectle](https://vectle.com/skills/skl_9CnLMeIRYWZhJtNR6OvABw). Version: `skv_wgHm_YF55XSF7LtHk6EYcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
