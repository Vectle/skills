---
name: "figma-webhook-passcode-lives-in-the-js-3cae9d5c06608582"
description: "Guide Figma webhook passcode lives in the JSON body, not a header: Verify it with a timing-safe compare (hmac.compare_digest) against the body value before doing anything else; checking a header will never match and leaves you open. Use this when you hit exactly this in Figma. Not for different errors or different tools."
metadata:
  skill_id: "skl__dcZoXvWDYcLFKxSNElnJQ"
  title: "Figma webhook passcode lives in the JSON body, not a header"
  version: "skv_KL9_gg_6G5YXcuS3NfO5TQ"
  updated: "2026-10-03T05:32:34.646128+00:00"
  canonical_url: "https://vectle.com/skills/skl__dcZoXvWDYcLFKxSNElnJQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Verify it with a timing-safe compare (hmac.compare_digest) against the body value before doing anything else; checking a header will never match and leaves you open. When you register a Figma webhook you get a passcode, and Figma sends that passcode back inside the JSON body of every delivery, not as an HTTP header. Failed deliveries retry 3 times at 5 minutes, 30 minutes, and 3 hours, so your handler must be idempotent.

## Fix
1. Verify it with a timing-safe compare (hmac.compare_digest) against the body value before doing anything else; checking a header will never match and leaves you open.
   Expected: the value or setting is exactly right, nothing ambiguous.

## Details
Failed deliveries retry 3 times at 5 minutes, 30 minutes, and 3 hours, so your handler must be idempotent. Limits to plan around: 20 webhooks per team, 5 per project, and 3 per file on Professional (higher tiers raise the per-file cap).

## When to use
You hit exactly this: Figma webhook passcode lives in the JSON body, not a header in Figma.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Figma.

## Edge cases
- When you register a Figma webhook you get a passcode, and Figma sends that passcode back inside the JSON body of every delivery, not as an HTTP header.
- For CI triggers prefer LIBRARY_PUBLISH or FILE_VERSION_UPDATE; FILE_UPDATE fires on every autosave and floods pipelines.

---

Source: [Vectle](https://vectle.com/skills/skl__dcZoXvWDYcLFKxSNElnJQ). Version: `skv_KL9_gg_6G5YXcuS3NfO5TQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
