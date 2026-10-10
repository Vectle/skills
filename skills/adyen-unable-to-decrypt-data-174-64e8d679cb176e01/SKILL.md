---
name: "adyen-unable-to-decrypt-data-174-64e8d679cb176e01"
description: "Fixes Adyen error 174 Unable to decrypt data. Covers matching the client-side encryption key to the right environment, sending the encrypted blob as a JSON POST, regenerating the web service user after credential rotation, and keeping the API key, encryption key and endpoint in the same environment. Not for 172 clock-skew failures."
metadata:
  skill_id: "skl_U6yHxHqdA0KipA-sCnw8wg"
  title: "Adyen: Unable to decrypt data (174)"
  version: "skv_3WaC3l3LABTFsUA-WHGgnA"
  updated: "2026-10-03T04:39:00.386624+00:00"
  canonical_url: "https://vectle.com/skills/skl_U6yHxHqdA0KipA-sCnw8wg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Unable to decrypt data (174)

**TL;DR:** The encrypted card data was made for a different environment or with the wrong key. Use the TEST encryption key on TEST endpoints and the LIVE key on LIVE, and if credentials were rotated, regenerate the web service user and re-encrypt. This is a key mismatch, not a clock problem.

```text
174 - Unable to decrypt data
```

## Steps

1. **Match the key to the environment.** The client-side encryption key (origin key) is per environment. Data encrypted with the TEST key cannot be decrypted on LIVE, and vice versa.
   - *Success check:* the key used for encryption and the endpoint belong to the same environment.
2. **Check how the data was sent.** The classic API expects the encrypted blob via HTTP POST with the right content type. A GET request, or XML/form encoding where JSON is expected, can surface as 174.
   - *Success check:* the request is a JSON POST carrying the encrypted fields.
3. **Regenerate the web service user if needed.** If keys were rotated or the credential was recreated, generate a new web service user with the relevant permissions and re-encrypt the card data with the new key.
   - *Success check:* freshly encrypted data decrypts cleanly on the first try.
4. **Confirm the API key matches the credential.** The API key in your backend must belong to the same web service user and environment as the encryption key.
   - *Success check:* all three (API key, encryption key, endpoint) are the same environment.

## When to use this

- /payments fails with 174 on encrypted card data.
- It broke right after a credential rotation or an environment switch.

## When NOT to use this

- 172 (encrypted data outside valid time period). That is clock skew, fixable with NTP.
- Plaintext card data integrations. 174 is specific to the encrypted payload.

## Compatibility

Adyen client-side encryption, Checkout API and classic /authorise, TEST and LIVE.

## Why it happens

Encryption and decryption have to agree on the key pair and the environment. TEST/LIVE mixups, rotated credentials where only one side was updated, and GET-instead-of-POST mistakes are the three usual causes.

## Edge cases

- Plugins and hosted carts sometimes cache the old public key after you rotate. Clear the plugin's key cache or re-enter the key in its settings.
- If you proxy requests, make sure the proxy is not mangling the encrypted strings (URL-encoding a base64 blob breaks it).


---

Source: [Vectle](https://vectle.com/skills/skl_U6yHxHqdA0KipA-sCnw8wg). Version: `skv_3WaC3l3LABTFsUA-WHGgnA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
