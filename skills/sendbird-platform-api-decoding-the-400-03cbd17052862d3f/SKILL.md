---
name: "sendbird-platform-api-decoding-the-400-03cbd17052862d3f"
description: "Sendbird Platform API: decoding the 400920 / 403100 / 500910 error codes. 400920 covers several distinct cases: RequestDenied (API call from an unauthorized IP), ReadOnlyMode (app is in read-only mode so only GETs work), NotAccessible (push is off in the app, invalid announcement parameter, or deleting a message that has a child message). Use when hitting this exact issue with Sendbird Platform API. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_dPN49NXkDqXDIOEQj6OMww"
  title: "Sendbird Platform API: decoding the 400920 / 403100 / 500910 error codes"
  version: "skv_-dW6Rm0sx1lxpvmSxjyBDA"
  updated: "2026-10-03T14:39:06.620244+00:00"
  canonical_url: "https://vectle.com/skills/skl_dPN49NXkDqXDIOEQj6OMww"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sendbird.com/docs/chat/platform-api/v3/error-codes\"]"
---

## TL;DR

400920 covers several distinct cases: RequestDenied (API call from an unauthorized IP), ReadOnlyMode (app is in read-only mode so only GETs work), NotAccessible (push is off in the app, invalid announcement parameter, or deleting a message that has a child message). Read the detail code, not just the HTTP status.

## The error

```text
decoding the 400920 / 403100 / 500910 error codes
```

## Fix

1. 400920 covers several distinct cases: RequestDenied (API call from an unauthorized IP), ReadOnlyMode (app is in read-only mode so only GETs work), NotAccessible (push is off in the app, invalid announcement parameter, or deleting a message that has a child message).
   Expected: You get the expected result; the problem is gone.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Sendbird Platform API.
- The symptom matches: decoding the 400920 / 403100 / 500910 error codes.

## When NOT to use

- A different error message from Sendbird Platform API; the cause here is specific to this error.
- Unrelated Sendbird Platform API issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Sendbird Platform API. Source: https://docs.sendbird.com/docs/chat/platform-api/v3/error-codes.

## Variant phrasings

### decoding the 400920 / 403100 / 500910 error codes

## Why it happens

Sendbird Platform API calls fail with numeric error codes like 400920, 403100, or 500910 instead of plain HTTP statuses.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.sendbird.com/docs/chat/platform-api/v3/error-codes

---

Source: [Vectle](https://vectle.com/skills/skl_dPN49NXkDqXDIOEQj6OMww). Version: `skv_-dW6Rm0sx1lxpvmSxjyBDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
