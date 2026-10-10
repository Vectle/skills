---
name: "apideck-webhooks-can-be-created-disabl-a78fae470ee2974f"
description: "Fix for Apideck webhooks can be created disabled: check status after subscribing: Each delivery also has a hard 60-second timeout; slow endpoints get logged as failed (status_code 0) and retried. ## What to do When an Apideck webhook silently never fires, don't debug your handler Use this when you hit exactly this in Apideck webhooks can be created disabled. Not for different errors or different tools."
metadata:
  skill_id: "skl_WLsMtkLffoW_DOKVAc7ZQQ"
  title: "Apideck webhooks can be created disabled: check status after subscribing"
  version: "skv_K7clSk2f2QpZt1jTuItYcw"
  updated: "2026-10-03T04:38:49.250073+00:00"
  canonical_url: "https://vectle.com/skills/skl_WLsMtkLffoW_DOKVAc7ZQQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Each delivery also has a hard 60-second timeout; slow endpoints get logged as failed (status_code 0) and retried. ## What to do When an Apideck webhook silently never fires, don't debug your handler first: GET /webhook/webhooks and check the subscription's status. Web (Apideck official OpenAPI spec, webhook.yml): documents that creating a webhook subscription triggers synchronous delivery_url validation: Apideck POSTs an HMAC-signed request to your URL at creation time.

Web (Apideck official OpenAPI spec, webhook.yml): documents that creating a webhook subscription triggers synchronous delivery_url validation: Apideck POSTs an HMAC-signed request to your URL at creation time. If validation fails (network error, timeout, non-2xx response), the webhook is STILL created but with status disabled and disabled_reason delivery_url_validation_failed. Each delivery also has a hard 60-second timeout; slow endpoints get logged as failed (status_code 0) and retried.

## What to do
When an Apideck webhook silently never fires, don't debug your handler first: GET /webhook/webhooks and check the subscription's status. If it says disabled with disabled_reason delivery_url_validation_failed, your endpoint failed the synchronous validation POST at creation time (timeout, non-2xx, network error). Fix the endpoint and re-enable the webhook. Separately, keep your handler fast: Apideck gives each delivery 60 seconds, then marks it failed and retries. Acknowledge with HTTP 2xx immediately and do the real work asynchronously, or you'll get duplicate deliveries from the retry policy.

## When to use
You hit exactly this: Apideck webhooks can be created disabled: check status after subscribing in Apideck webhooks can be created disabled.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Apideck webhooks can be created disabled.

---

Source: [Vectle](https://vectle.com/skills/skl_WLsMtkLffoW_DOKVAc7ZQQ). Version: `skv_K7clSk2f2QpZt1jTuItYcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
