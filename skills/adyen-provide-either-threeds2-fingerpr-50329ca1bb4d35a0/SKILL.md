---
name: "adyen-provide-either-threeds2-fingerpr-50329ca1bb4d35a0"
description: "Fixes Adyen Checkout error 14_032 asking for either threeds2.fingerprint or threeds2.challengeResult. Covers matching the details field to the completed step (fingerprint after IdentifyShopper, challengeResult after ChallengeShopper), sending exactly one field per step, and not reusing one fixed payload shape. Not for skipped fingerprint steps or invalid fingerprint data."
metadata:
  skill_id: "skl_33VDoaRvvptMWp1QPLjaXQ"
  title: "Adyen: Provide either threeds2.fingerprint or threeds2.challengeResult (14_032)"
  version: "skv_DQPAF-a_J4gl-YM3kL7VUg"
  updated: "2026-10-03T04:37:15.42593+00:00"
  canonical_url: "https://vectle.com/skills/skl_33VDoaRvvptMWp1QPLjaXQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: Provide either threeds2.fingerprint or threeds2.challengeResult (14_032)

**TL;DR:** The /payments/details call needs the field that matches the step you just completed: threeds2.fingerprint right after IdentifyShopper, threeds2.challengeResult right after ChallengeShopper. Sending the wrong one, both, or neither gives 14_032.

```text
14_032 - Provide either threeds2.fingerprint or threeds2.challengeResult
```

## Steps

1. **Look at the last resultCode.** IdentifyShopper means the fingerprint step just ran; ChallengeShopper means the challenge just ran. That tells you which field to send.
   - *Success check:* you can name the step you are responding to.
2. **After IdentifyShopper, send threeds2.fingerprint.** Include the fingerprint data plus paymentData in /payments/details.
   - *Success check:* the details payload has threeds2.fingerprint and no challengeResult.
3. **After ChallengeShopper, send threeds2.challengeResult.** Include the challenge result plus paymentData instead.
   - *Success check:* the details payload has threeds2.challengeResult and no fingerprint.
4. **Never send both or an empty details object.** One field per step, matching the step.
   - *Success check:* /payments/details advances the flow instead of returning 14_032.

## When to use this

- /payments/details fails with 14_032 during 3DS2.
- Your details-call code uses one fixed payload shape for every step.

## When NOT to use this

- 14_0402 (missing fingerprint). That is the fingerprint step skipped entirely.
- 14_033/14_034 (fingerprint invalid). Those mean the field was present but the data was bad.

## Compatibility

Adyen Checkout API 3DS2 native flows, all channels.

## Why it happens

Each 3DS2 step produces a different artifact and Adyen expects exactly that artifact back. Generic "send the details" code that always posts the same field, or posts an empty object, fails the check.

## Edge cases

- Redirect (non-native) flows use PaRes/MD instead of these fields. Dont mix the two vocabularies.
- If the shopper abandons the challenge and you retry, you go back to a fresh fingerprint step, not a challengeResult resend.


---

Source: [Vectle](https://vectle.com/skills/skl_33VDoaRvvptMWp1QPLjaXQ). Version: `skv_DQPAF-a_J4gl-YM3kL7VUg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
