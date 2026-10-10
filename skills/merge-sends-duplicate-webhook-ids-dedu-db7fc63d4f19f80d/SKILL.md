---
name: "merge-sends-duplicate-webhook-ids-dedu-db7fc63d4f19f80d"
description: "Guide Merge sends duplicate webhook IDs; dedupe on the signature header, verify on the raw body: Also verify signatures against the raw request body before any JSON parsing: if your framework auto-parses JSON (Express When you receive Merge webhooks, do not treat the hook ID as unique: the same. Use this when you hit exactly this in Merge. Not for different errors or different tools."
metadata:
  skill_id: "skl_GfjlB79ab9ELEdmbewHfHw"
  title: "Merge sends duplicate webhook IDs; dedupe on the signature header, verify on the raw body"
  version: "skv_h3wWUABcmMEwONxmKj-9cg"
  updated: "2026-10-03T04:42:25.105332+00:00"
  canonical_url: "https://vectle.com/skills/skl_GfjlB79ab9ELEdmbewHfHw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Also verify signatures against the raw request body before any JSON parsing: if your framework auto-parses JSON (Express When you receive Merge webhooks, do not treat the hook ID as unique: the same ID can fire multiple times for distinct instances of the same event (e.g. two different `candidate.created`

When you receive Merge webhooks, do not treat the hook ID as unique: the same ID can fire multiple times for distinct instances of the same event (e.g. two different `candidate.created` events). Dedupe on the `X-Merge-Webhook-Signature` header value instead, which Merge says is the unique identifier per delivery. Store seen signatures and skip repeats. Also verify signatures against the raw request body before any JSON parsing: if your framework auto-parses JSON (Express `express.json()`, Flask `request.json`), the re-serialized body will not match the HMAC. Use raw-body middleware on the webhook route (e.g. `express.raw({type: '*/*'})` or `request.get_data()` in Flask), compute HMAC-SHA256 with your webhook secret, and compare with a constant-time comparison.

## When to use
You hit exactly this: Merge sends duplicate webhook IDs; dedupe on the signature header, verify on the raw body in Merge.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Merge.

## Edge cases
- When you receive Merge webhooks, do not treat the hook ID as unique: the same ID can fire multiple times for distinct instances of the same event (e.g. two different.

---

Source: [Vectle](https://vectle.com/skills/skl_GfjlB79ab9ELEdmbewHfHw). Version: `skv_h3wWUABcmMEwONxmKj-9cg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
