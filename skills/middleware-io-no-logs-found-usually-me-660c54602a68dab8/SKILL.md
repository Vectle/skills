---
name: "middleware-io-no-logs-found-usually-me-660c54602a68dab8"
description: "Middleware.io: no logs found usually means service.name or the clock is wrong. If event times are wrong, ensure time_unix_nano is correct and the sender's clock is synced with NTP. Use when hitting this exact issue with Middleware.io. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_jrLRHB4CDE3CT76CHOG93Q"
  title: "Middleware.io: no logs found usually means service.name or the clock is wrong"
  version: "skv_39Q1g2y3_h-GWgIXa0LsAg"
  updated: "2026-10-03T13:58:10.152569+00:00"
  canonical_url: "https://vectle.com/skills/skl_jrLRHB4CDE3CT76CHOG93Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

If event times are wrong, ensure time_unix_nano is correct and the sender's clock is synced with NTP. Avoid sending secrets in body or attributes: redact in your log pipeline. If you cannot find logs by service, include service.name consistently: attribute names are case-sensitive.

## The error

```text
no logs found usually means service.name or the clock is wrong
```

## Fix

1. If event times are wrong, ensure time_unix_nano is correct and the sender's clock is synced with NTP.
   Expected: You get the expected result; the problem is gone.
2. Avoid sending secrets in body or attributes: redact in your log pipeline.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Middleware.io.
- The symptom matches: no logs found usually means service.name or the clock is wrong.

## When NOT to use

- A different error message from Middleware.io; the cause here is specific to this error.
- Unrelated Middleware.io issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Middleware.io. Source: https://docs.middleware.io/integrations/custom-logs.

## Variant phrasings

### no logs found usually means service.name or the clock is wrong

## Why it happens

Log search misses are attribute or timestamp problems.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.middleware.io/integrations/custom-logs

---

Source: [Vectle](https://vectle.com/skills/skl_jrLRHB4CDE3CT76CHOG93Q). Version: `skv_39Q1g2y3_h-GWgIXa0LsAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
