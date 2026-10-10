---
name: "sendbird-failed-webhook-retention-is-s-8f961e96e6cd0e13"
description: "Sendbird: failed webhook retention is six months, exports are limited. The maximum data retention period for failed webhooks is six months; requesting an export older than that errors. Use when hitting this exact issue with Sendbird. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_UkbI7DDHvBrph-M65v-UMQ"
  title: "Sendbird: failed webhook retention is six months, exports are limited"
  version: "skv_70mwGHnEpbDvjdITW5EHZQ"
  updated: "2026-10-03T14:37:40.143092+00:00"
  canonical_url: "https://vectle.com/skills/skl_UkbI7DDHvBrph-M65v-UMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The maximum data retention period for failed webhooks is six months; requesting an export older than that errors.

## The error

```text
failed webhook retention is six months, exports are limited
```

## Fix

1. The maximum data retention period for failed webhooks is six months; requesting an export older than that errors.
   Expected: you can confirm this matches your situation.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Sendbird.
- The symptom matches: failed webhook retention is six months, exports are limited.

## When NOT to use

- A different error message from Sendbird; the cause here is specific to this error.
- Unrelated Sendbird issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Sendbird. Source: https://sendbird.com/docs/docsDetail?product=chat&category=platform-api&version=v3&depth1=data-export&depth2=data-export.

## Variant phrasings

### failed webhook retention is six months, exports are limited

## Why it happens

Sendbird webhook deliveries are failing but the failed-webhook data export returns nothing or an error for old ranges.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://sendbird.com/docs/docsDetail?product=chat&category=platform-api&version=v3&depth1=data-export&depth2=data-export-overview

---

Source: [Vectle](https://vectle.com/skills/skl_UkbI7DDHvBrph-M65v-UMQ). Version: `skv_70mwGHnEpbDvjdITW5EHZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
