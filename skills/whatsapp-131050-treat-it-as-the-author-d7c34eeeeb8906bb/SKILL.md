---
name: "whatsapp-131050-treat-it-as-the-author-d7c34eeeeb8906bb"
description: "WhatsApp 131050: treat it as the authoritative marketing opt-out and never retry. wire 131050 to a dedicated opt-out handler that records the user in an OptInRegistry and blocks future marketing sends. Use when hitting this exact issue with WhatsApp 131050. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_NlM92YGnFvXSXMU8LpKWHA"
  title: "WhatsApp 131050: treat it as the authoritative marketing opt-out and never retry"
  version: "skv_0W99JPSa--wHWsdTiJIr8g"
  updated: "2026-10-03T14:15:01.853461+00:00"
  canonical_url: "https://vectle.com/skills/skl_NlM92YGnFvXSXMU8LpKWHA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/dojocodinglabs/whatsapp-adapter/blob/HEAD/docs/compliance.md\"]"
---

## TL;DR

Wire 131050 to a dedicated opt-out handler that records the user in an OptInRegistry and blocks future marketing sends.

## Fix

1. Wire 131050 to a dedicated opt-out handler that records the user in an OptInRegistry and blocks future marketing sends.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this WhatsApp 131050 feature.
- The symptom matches: treat it as the authoritative marketing opt-out and never retry.

## When NOT to use

- Unrelated WhatsApp 131050 issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against WhatsApp 131050. Source: https://github.com/dojocodinglabs/whatsapp-adapter/blob/HEAD/docs/compliance.md.

## Variant phrasings

### treat it as the authoritative marketing opt-out and never retry

## Why it happens

Meta sends 131050 when a user opts out of marketing messages. Retrying is worse than useless: it feeds spam-rate enforcement.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/dojocodinglabs/whatsapp-adapter/blob/HEAD/docs/compliance.md

---

Source: [Vectle](https://vectle.com/skills/skl_NlM92YGnFvXSXMU8LpKWHA). Version: `skv_0W99JPSa--wHWsdTiJIr8g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
