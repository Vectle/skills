---
name: "adyen-14-016-invalid-sdkversion-provid-47d6c05f099f17fb"
description: "Resolves Adyen checkout error 14_016 when the sdkVersion you sent is not recognized. Use when a web integration passes a version string Adyen does not know, often after a bad upgrade. Not for a missing sdkVersion (14_019)."
metadata:
  skill_id: "skl_ppUL9p1B8oB8GTjuOvqGJA"
  title: "Adyen 14_016 - Invalid sdkVersion provided"
  version: "skv_qxR9yDDHqfKWtbBaIsk_JQ"
  updated: "2026-10-03T06:22:01.53927+00:00"
  canonical_url: "https://vectle.com/skills/skl_ppUL9p1B8oB8GTjuOvqGJA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.adyen.com/development-resources/error-codes/\"]"
---

TL;DR: The sdkVersion string does not match a known Adyen release. Use the exact version of the script you load, ideally read from the SDK object at runtime, and update every place the old string was hardcoded.

The exact error:

```text
14_016 - Invalid sdkVersion provided
```

## The fix

1. Find the exact version in your script URL or package lock and use that string.
   Expected: The version string matches a real Adyen release.
2. Read the version from the loaded Adyen object at runtime instead of hardcoding it.
   Expected: The client and the request agree on the version.
3. Redeploy and confirm the failing requests now carry a valid version.
   Expected: Adyen accepts the sdkVersion and processes the payment.

## When this applies

- /payments returns 14_016
- You just upgraded the Adyen web SDK
- The version string is built by hand somewhere in your code

## When it does NOT apply

- sdkVersion is missing entirely (that is 14_019)
- A native iOS or Android integration (those use the SDK token)
- The version is valid but the channel is wrong (that is 14_011)

## Versions

Adyen Checkout API v68 through v71, Web Components v5 and v6.

## Why it happens

Adyen checks sdkVersion against its release list as a sanity check on the integration. An unknown string suggests a broken or tampered client, so the request is rejected.

## Edge cases and pitfalls

- Pin the version string to the SDK file you actually load; mismatched pairs fail
- Beta or canary builds report version strings Adyen may not accept
- Server-side SDK version and client components version are different fields


---

Source: [Vectle](https://vectle.com/skills/skl_ppUL9p1B8oB8GTjuOvqGJA). Version: `skv_qxR9yDDHqfKWtbBaIsk_JQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
