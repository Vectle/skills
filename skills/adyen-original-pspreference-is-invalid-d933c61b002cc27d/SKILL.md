---
name: "adyen-original-pspreference-is-invalid-d933c61b002cc27d"
description: "Fixes Adyen error 906 Original pspReference is invalid for this environment. Explains pspReferences only exist in the environment that issued them, the fix of matching the endpoint environment to the pspReference's origin, and hunting down hardcoded test references or flipped env vars. Not for malformed references (15_011) or first-call payment failures."
metadata:
  skill_id: "skl_XUP2g0Bya5AlnzseHj5u_w"
  title: "Adyen: Original pspReference is invalid for this environment (906)"
  version: "skv_rmYwVt94nwx9xepGvs2_FA"
  updated: "2026-10-03T04:39:34.23609+00:00"
  canonical_url: "https://vectle.com/skills/skl_XUP2g0Bya5AlnzseHj5u_w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: Original pspReference is invalid for this environment (906)

**TL;DR:** You passed a TEST pspReference to a LIVE endpoint, or the reverse. pspReferences only exist in the environment that issued them. Use the pspReference from the same environment you are calling, and keep follow-on operations (capture, refund, cancel) in that environment too.

```text
906 - Invalid Request: Original pspReference is invalid for this environment
```

## Steps

1. **Find where the pspReference came from.** Check your logs or database: was it issued by a TEST payment or a LIVE one?
   - *Success check:* you can name the environment that created the pspReference.
2. **Call the matching endpoint.** TEST pspReferences go to the test endpoints, LIVE to live. Dont cross them.
   - *Success check:* endpoint environment matches the pspReference's environment.
3. **Fix the source of the mixup.** Usually a hardcoded test pspReference in code, a staging database restored into prod, or an env var pointing at the wrong Adyen environment.
   - *Success check:* a fresh payment in the target environment produces a pspReference that works first try.
4. **Keep the whole chain in one environment.** Capture, refund and cancel calls must use the same environment as the original payment.
   - *Success check:* follow-on operations stop returning 906.

## When to use this

- Capture, refund, cancel or /payments/details fails with 906.
- It works in one environment and fails in the other with the same code.

## When NOT to use this

- The first /payments call fails. There is no pspReference yet, so the problem is elsewhere.
- 15_011 (pspReference is not a valid pspReference). That is a malformed reference, not an environment mixup.

## Compatibility

All Adyen APIs that take an original pspReference (modifications, payouts, 3DS follow-ups), TEST and LIVE.

## Why it happens

pspReferences are namespaced per environment. The classic mixup is developing against TEST, then deploying with a TEST pspReference baked into a fixture, or an env var for the endpoint flipped without flipping the stored references.

## Edge cases

- Database restores from prod to staging bring LIVE pspReferences into TEST. Scrub or re-issue them in lower environments.
- Webhook pspReferences are environment-specific too. Dont feed a TEST webhook's pspReference into a LIVE capture.


---

Source: [Vectle](https://vectle.com/skills/skl_XUP2g0Bya5AlnzseHj5u_w). Version: `skv_rmYwVt94nwx9xepGvs2_FA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
