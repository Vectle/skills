---
name: "adyen-invalid-hmac-signature-on-webhoo-c7f8dec754d80048"
description: "Fixes Adyen webhook handlers that reject notifications with Invalid HMAC signature. Covers using the HMAC key from the correct webhook configuration, verifying the signature over the raw request bytes instead of re-serialized JSON, the 10-minute propagation window after key rotation, and the different header-based signing used by non-standard webhooks. Not for notifications that arrive with no signature at all."
metadata:
  skill_id: "skl_b8-o-Vb6YyVd_aLQtR8vSg"
  title: "Adyen: Invalid HMAC signature on webhooks"
  version: "skv_Saed-wdT6UgukHTWQ__KRQ"
  updated: "2026-10-03T04:27:46.499479+00:00"
  canonical_url: "https://vectle.com/skills/skl_b8-o-Vb6YyVd_aLQtR8vSg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Invalid HMAC signature on webhooks

**TL;DR:** Your webhook handler is probably using the wrong HMAC key, or verifying the signature over re-serialized JSON instead of the raw request bytes. Use the HMAC key from *that specific* webhook's settings in the Customer Area, compute the signature over the untouched raw body, and if you just rotated the key, keep the old one around for about 10 minutes because Adyen signs with both during propagation.

```text
Invalid HMAC signature
```

## Steps

1. **Grab the right key.** In the Customer Area go to Developers > Webhooks, open the exact webhook configuration that sent the event, and copy its HMAC key. Each webhook has its own key, and mixing up TEST/LIVE or dev/prod configs is the most common cause.
   - *Success check:* the key you pasted matches the one shown for that webhook config, same environment.
2. **Verify over the raw bytes.** Read the request body as raw bytes and never JSON-parse-then-stringify it first. Re-serialization changes whitespace and key order, which breaks the signature.
   - *Success check:* your handler uses the raw body (e.g. the raw buffer in Express, the raw string in your framework) for the HMAC input.
3. **Compare against the right field.** For standard webhooks, compare your computed signature with `hmacSignature` inside `additionalData`. For non-standard webhooks (e.g. recurring token lifecycle events), Adyen puts the signature in the `hmacsignature` request header instead, computed over the raw payload bytes, then base64-encoded.
   - *Success check:* signature comparison is constant-time and matches on a known-good test notification.
4. **Handle key rotation.** If you regenerated the HMAC key, Adyen can take up to 10 minutes to propagate it everywhere. During that window both the old and new keys are valid, so accept either.
   - *Success check:* validation stops failing within 10 minutes without another code change.
5. **Prefer the official SDK validator.** Adyen's server-side libraries ship an HMAC validator helper (e.g. HMACValidator in the Java library). Use it instead of hand-rolled crypto.
   - *Success check:* the SDK validator returns true on the same payload your code rejected.

## When to use this

- Your Adyen webhook endpoint logs "Invalid HMAC signature" or returns 401 on notifications.
- Validation broke right after you regenerated the HMAC key.
- Validation works for one webhook config but not another.

## When NOT to use this

- The notification arrives with no signature at all. Thats a webhook configuration problem, not a validation bug. Check the webhook is set to sign notifications.
- You get duplicate events. Duplicates share the same eventCode + pspReference; deduplicate on that pair instead of re-validating.

## Compatibility

Adyen webhooks (standard and non-standard/header-signed), all server-side languages. Respond 202 with an empty body (or legacy 200 with `[accepted]`) after consuming the event.

## Why it happens

HMAC validation is brittle by design: one wrong byte anywhere in the key, the payload, or the comparison input and it fails. The usual culprits are a key copied from the wrong webhook config or environment, the framework parsing the JSON body before the signature check (which mutates it), or a key rotation whose propagation delay was not accounted for.

## Edge cases

- Non-standard webhooks sign differently: header-based `hmacsignature` over raw bytes, SHA256, base64. Dont reuse the `additionalData` logic for those.
- Webhook events can arrive more than once. Always ack quickly and dedupe on eventCode + pspReference.
- Never put the HMAC key in the webhook URL or query string.


---

Source: [Vectle](https://vectle.com/skills/skl_b8-o-Vb6YyVd_aLQtR8vSg). Version: `skv_Saed-wdT6UgukHTWQ__KRQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
