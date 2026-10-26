---
name: "adyen-missing-or-invalid-clientkey-ori-e510dc150deda784"
description: "Fixes Adyen Checkout error 14_0381 Missing or invalid clientKey/originKey. Covers generating the client key in the Customer Area for the matching environment, adding the exact checkout domain to allowed origins, and the mobile note that native SDKs need the key but not origin allowlisting. Not for backend API key 401s or other missing-field errors."
metadata:
  skill_id: "skl_eVAA8_SRpr8nDjMZ3-KjFQ"
  title: "Adyen: Missing or invalid clientKey/originKey (14_0381)"
  version: "skv_gB0oO9doSkWha_sctBF_fQ"
  updated: "2026-10-03T04:37:49.650287+00:00"
  canonical_url: "https://vectle.com/skills/skl_eVAA8_SRpr8nDjMZ3-KjFQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

# Adyen: Missing or invalid clientKey/originKey (14_0381)

**TL;DR:** The client key is wrong for the environment, or your checkout domain is not in the allowed origins. Generate a client key in the Customer Area for the environment you are running (TEST key on TEST), and add your exact domain to the allowed origins list.

```text
14_0381 - Missing or invalid clientKey/originKey
```

## Steps

1. **Get the right client key.** In the Customer Area, go to Developers > API credentials and copy the client key. TEST integrations need the TEST client key; LIVE needs the LIVE one. They are not interchangeable.
   - *Success check:* the key's environment matches your integration's environment.
2. **Allowlist your domain.** In the same API credential settings, add your checkout domain to allowed origins, exactly as the browser sees it (scheme + host, no path).
   - *Success check:* your domain appears verbatim in the allowed origins list.
3. **Pass it to the SDK init.** Feed the client key into your AdyenCheckout configuration on the frontend. A typo or a stale cached key fails the same way.
   - *Success check:* the initialized checkout no longer throws 14_0381.
4. **Native mobile note.** iOS/Android SDKs use the client key but not origin allowlisting. If you see this on mobile, it is the key itself, not origins.
   - *Success check:* mobile uses the plain client key for its environment.

## When to use this

- Drop-in or Components fail to initialize with 14_0381.
- It works on one domain (or your dev machine through a tunnel) but not on another.

## When NOT to use this

- API 401/403 errors. Those are about the secret API key on the backend, a different credential.
- 14_0382 (missing checkoutAttemptId). Different field, different fix.

## Compatibility

Adyen Web Drop-in and Components, iOS and Android SDKs, TEST and LIVE.

## Why it happens

The client key identifies your integration to Adyen's frontend services, and the origin check stops other sites from using your key. Wrong-env key, unlisted domain, or a key pasted with a typo all land on 14_0381.

## Edge cases

- Single-page apps that deploy preview URLs per branch need each preview domain allowlisted, or a wildcard pattern if your setup allows it.
- Rotating the API credential can invalidate the client key too. After rotation, re-copy the client key, not just the secret key.


---

Source: [Vectle](https://vectle.com/skills/skl_eVAA8_SRpr8nDjMZ3-KjFQ). Version: `skv_gB0oO9doSkWha_sctBF_fQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
