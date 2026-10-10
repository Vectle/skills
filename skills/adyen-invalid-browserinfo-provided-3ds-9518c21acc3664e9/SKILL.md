---
name: "adyen-invalid-browserinfo-provided-3ds-9518c21acc3664e9"
description: "Fixes Adyen 3DS2 error 15_015 Invalid browserInfo provided. Covers sending the complete browserInfo object with all eight fields, using correct JSON types for numeric and boolean fields, valid colorDepth values, and a real acceptHeader instead of a hardcoded string. Not for native app flows or the colorDepth-specific 15_018."
metadata:
  skill_id: "skl_CeDBNqGW4aoGvUFA7zYYFQ"
  title: "Adyen: Invalid browserInfo provided (3DS2 15_015)"
  version: "skv_mQHrAosSSnpqzpw0BmBNvA"
  updated: "2026-10-03T04:34:43.00108+00:00"
  canonical_url: "https://vectle.com/skills/skl_CeDBNqGW4aoGvUFA7zYYFQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Adyen: Invalid browserInfo provided (3DS2 15_015)

**TL;DR:** Your browserInfo object is incomplete or malformed. Send every field Adyen expects: userAgent, acceptHeader, language, colorDepth, screenHeight, screenWidth, timeZoneOffset and javaEnabled, with the right types. Hand-built browserInfo missing acceptHeader or sending colorDepth as a string is the classic trigger.

```text
15_015 - Invalid browserInfo provided
```

## Steps

1. **Collect the full object.** Use the SDK's browserInfo helper if you have one; otherwise gather each field from the browser directly.
   - *Success check:* all eight fields are present: userAgent, acceptHeader, language, colorDepth, screenHeight, screenWidth, timeZoneOffset, javaEnabled.
2. **Check the types.** colorDepth, screenHeight, screenWidth and timeZoneOffset are numbers, not strings. javaEnabled is a boolean. A quoted "24" for colorDepth fails validation.
   - *Success check:* numeric fields are JSON numbers, javaEnabled is true/false unquoted.
3. **Validate colorDepth values.** Adyen only accepts 1, 4, 8, 15, 16, 24, 32 or 48. Anything else gives 15_018, a sibling of this error.
   - *Success check:* colorDepth is one of the allowed values.
4. **Use a real acceptHeader.** Dont hardcode a made-up string; read it from the actual browser request headers.
   - *Success check:* acceptHeader matches what the browser really sends.
5. **Resend /payments with the fixed object.**
   - *Success check:* the request passes validation and returns IdentifyShopper or the next action.

## When to use this

- 3DS2 /payments calls fail with 15_015.
- You build browserInfo by hand instead of using the SDK helper.

## When NOT to use this

- 15_018 colorDepth errors. Same family, but the fix is specifically the colorDepth value.
- Native app flows. Those send sdkVersion/deviceChannel instead of full browserInfo.

## Compatibility

Adyen 3DS2 browser channel, Checkout API and classic API, all browsers.

## Why it happens

Adyen forwards browserInfo to the 3DS directory server, which validates it strictly. Custom integrations usually omit a field (acceptHeader is the one everyone forgets) or send numbers as strings, and the whole object gets rejected.

## Edge cases

- Headless browsers and webviews can report screen dimensions of 0. Guard against that before sending.
- language should be a valid BCP47 tag (15_016 covers that one). "en" and "en-US" are fine; inventing your own format is not.


---

Source: [Vectle](https://vectle.com/skills/skl_CeDBNqGW4aoGvUFA7zYYFQ). Version: `skv_mQHrAosSSnpqzpw0BmBNvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
