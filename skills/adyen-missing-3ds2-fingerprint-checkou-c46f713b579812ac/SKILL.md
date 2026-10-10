---
name: "adyen-missing-3ds2-fingerprint-checkou-c46f713b579812ac"
description: "Fixes Adyen Checkout error 14_0402 Missing 3DS2 fingerprint. Explains the required sequence after IdentifyShopper, running the device fingerprint and sending threeds2.fingerprint with paymentData in the /payments/details call, and not skipping to authorisation. Not for invalid fingerprints (14_033) or wrong-field errors (14_032)."
metadata:
  skill_id: "skl_AqoSPI54B-iSc7TpNhXB3w"
  title: "Adyen: Missing 3DS2 fingerprint (Checkout 14_0402)"
  version: "skv_LzC_iY8ZylM9wzzvCJ91-g"
  updated: "2026-10-03T04:36:40.757085+00:00"
  canonical_url: "https://vectle.com/skills/skl_AqoSPI54B-iSc7TpNhXB3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Missing 3DS2 fingerprint (Checkout 14_0402)

**TL;DR:** After /payments returns IdentifyShopper, you must run the device fingerprint and send threeds2.fingerprint in the /payments/details call. Skipping straight to authorisation, or sending details without the fingerprint field, gives 14_0402.

```text
14_0402 - Missing 3DS2 fingerprint
```

## Steps

1. **Handle the IdentifyShopper action.** When /payments returns resultCode IdentifyShopper with a threeDS2 action, run the fingerprint step through the SDK or your 3DS2 implementation. Dont skip it.
   - *Success check:* the fingerprint step executes and returns fingerprint data.
2. **Include threeds2.fingerprint in /payments/details.** Send the fingerprint data plus the paymentData from the action response.
   - *Success check:* the details payload contains the threeds2.fingerprint field.
3. **Check the response.** You should get ChallengeShopper (continue to the challenge) or a frictionless authorisation, not 14_0402.
   - *Success check:* no 14_0402; the flow advances.

## When to use this

- /payments/details fails with 14_0402 after an IdentifyShopper step.
- A custom 3DS2 integration that authorises without doing the fingerprint.

## When NOT to use this

- 14_033 (the provided fingerprint is invalid). That means you sent a fingerprint and it was rejected, which is a data problem, not a missing step.
- 14_032 (provide either threeds2.fingerprint or threeds2.challengeResult). That is about sending the wrong field for the step.

## Compatibility

Adyen Checkout API 3DS2 native flows, Web/iOS/Android.

## Why it happens

The 3DS2 protocol requires the device fingerprint before the issuer decides on frictionless vs challenge. Adyen enforces the sequence: no fingerprint data in the details call, no onward flow.

## Edge cases

- If the 3DS method notification never arrives within 10 seconds, set threeDSCompInd to N and continue; the fingerprint can still complete.
- Some test cards skip fingerprinting. If your test never hits IdentifyShopper, use a card that triggers it.


---

Source: [Vectle](https://vectle.com/skills/skl_AqoSPI54B-iSc7TpNhXB3w). Version: `skv_LzC_iY8ZylM9wzzvCJ91-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
