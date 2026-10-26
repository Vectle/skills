---
name: "sinch-sms-api-403-blocked-account-ille-467666ea85086567"
description: "Sinch SMS API: 403 blocked_account, illegal_number_type, missing_callback_url. blocked_account means the account is blocked, contact the account manager. illegal_number_type means the number type is not legal for the chosen region, send to a different MSISDN. missing_callback_url means a callback was requested with no URL provided, add it via the dashboard or the request body. unknown_group means the referenced group ID is invalid or deleted. Use when hitting this exact issue with Sinch SMS API."
metadata:
  skill_id: "skl_1xBeGPwv2MamHmuHw4pDyg"
  title: "Sinch SMS API: 403 blocked_account, illegal_number_type, missing_callback_url"
  version: "skv_VExYVH6mlZywGhIxXYkBoQ"
  updated: "2026-10-03T14:32:02.503593+00:00"
  canonical_url: "https://vectle.com/skills/skl_1xBeGPwv2MamHmuHw4pDyg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developers.sinch.com/docs/sms/api-reference/status-codes\"]"
---

## TL;DR

Blocked_account means the account is blocked, contact the account manager. illegal_number_type means the number type is not legal for the chosen region, send to a different MSISDN. missing_callback_url means a callback was requested with no URL provided, add it via the dashboard or the request body. unknown_group means the referenced group ID is invalid or deleted. Also check the token matches the service plan ID in the call, since a plan/credential mismatch is a common 403-adjacent auth failure.

## Fix

1. Blocked_account means the account is blocked, contact the account manager. illegal_number_type means the number type is not legal for the chosen region, send to a different MSISDN. missing_callback_url means a callback was requested with no URL provided, add it via the dashboard or the request body. unknown_group means the referenced group ID is invalid or deleted.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Sinch SMS API feature.
- The symptom matches: 403 blocked_account, illegal_number_type, missing_callback_url.

## When NOT to use

- Unrelated Sinch SMS API issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Sinch SMS API. Source: https://developers.sinch.com/docs/sms/api-reference/status-codes.

## Variant phrasings

### 403 blocked_account, illegal_number_type, missing_callback_url

## Why it happens

Sinch SMS API calls fail with 403 Forbidden and a code like blocked_account, illegal_number_type, missing_callback_url, or unknown_group.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://developers.sinch.com/docs/sms/api-reference/status-codes

---

Source: [Vectle](https://vectle.com/skills/skl_1xBeGPwv2MamHmuHw4pDyg). Version: `skv_VExYVH6mlZywGhIxXYkBoQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
