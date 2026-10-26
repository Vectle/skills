---
name: "whatsapp-cloud-api-which-error-codes-a-1dd47b67d0358b7d"
description: "WhatsApp Cloud API: which error codes are retryable and which are not. Never retry: 131026 undeliverable (recipient unreachable, use another channel), 131047 re-engagement (24h customer-service window expired, must send an approved template instead), 132000/132001 template problems (fix the template, not the send). Use when hitting this exact issue with WhatsApp Cloud API. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_79yENwg9Ah-2ZYcfGKXzng"
  title: "WhatsApp Cloud API: which error codes are retryable and which are not"
  version: "skv__gBGhJnOdMio1VavFxYwqQ"
  updated: "2026-10-03T14:17:50.861783+00:00"
  canonical_url: "https://vectle.com/skills/skl_79yENwg9Ah-2ZYcfGKXzng"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/roy-wanyoike/fuatilia/blob/HEAD/src/adapters/comm-whatsapp/README.md\"]"
---

## TL;DR

Never retry: 131026 undeliverable (recipient unreachable, use another channel), 131047 re-engagement (24h customer-service window expired, must send an approved template instead), 132000/132001 template problems (fix the template, not the send). Retryable: 131048 rate limit hit and HTTP 5xx (but a 5xx may have gone through, so reconcile before re-sending).

## The error

```text
which error codes are retryable and which are not
```

## Fix

1. Never retry: 131026 undeliverable (recipient unreachable, use another channel), 131047 re-engagement (24h customer-service window expired, must send an approved template instead), 132000/132001 template problems (fix the template, not the send).
   Expected: You get the expected result; the problem is gone.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with WhatsApp Cloud API.
- The symptom matches: which error codes are retryable and which are not.

## When NOT to use

- A different error message from WhatsApp Cloud API; the cause here is specific to this error.
- Unrelated WhatsApp Cloud API issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against WhatsApp Cloud API. Source: https://github.com/roy-wanyoike/fuatilia/blob/HEAD/src/adapters/comm-whatsapp/README.md.

## Variant phrasings

### which error codes are retryable and which are not

## Why it happens

Meta's 13xxxx error codes look similar but retrying the wrong one burns quota or risks account enforcement. Each code carries its own retry rule.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/roy-wanyoike/fuatilia/blob/HEAD/src/adapters/comm-whatsapp/README.md

---

Source: [Vectle](https://vectle.com/skills/skl_79yENwg9Ah-2ZYcfGKXzng). Version: `skv__gBGhJnOdMio1VavFxYwqQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
