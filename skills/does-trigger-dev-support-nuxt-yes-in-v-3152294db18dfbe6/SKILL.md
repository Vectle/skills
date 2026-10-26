---
name: "does-trigger-dev-support-nuxt-yes-in-v-3152294db18dfbe6"
description: "Answers whether Trigger.dev supports Nuxt: yes, in v3, which is framework-independent. Use when setting up Trigger.dev with a Nuxt app. Not for v2, which has no Nuxt adaptor and never will."
metadata:
  skill_id: "skl_UI7S8omX_jPBYs4an5dRWw"
  title: "Does Trigger.dev support Nuxt? Yes, in v3"
  version: "skv_HY2ciCzDFoMZrouuws5egg"
  updated: "2026-10-03T04:44:55.390817+00:00"
  canonical_url: "https://vectle.com/skills/skl_UI7S8omX_jPBYs4an5dRWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/triggerdotdev/trigger.dev/issues/447\"]"
---

Yes, as of Trigger.dev v3. Maintainer matt-aitken closed the thread confirming v3 is framework-independent and works with Nuxt. Follow the standard quick-start and point your Nuxt app at it.

1. Upgrade to Trigger.dev v3. If you are on v2 and stuck, that is why there is no Nuxt adaptor: the framework-specific adaptor model was dropped in v3, so upgrading is the fix rather than waiting for a Nuxt package.
2. Follow the standard v3 quick-start against your Nuxt app. Expected: triggers fire from Nuxt.

When to use: you want Trigger.dev with Nuxt.

When not to use: Trigger.dev v2. There is no Nuxt adaptor for v2 and there wont be one; upgrade.

Compatibility: Trigger.dev v3, Nuxt. Reported in triggerdotdev/trigger.dev#447.

Variants:
- "trigger.dev nuxt support"
- "trigger dev nuxt adaptor"
- "does trigger.dev work with nuxt"

Why: v3 replaced per-framework adaptors with a framework-independent model, so Nuxt works without a dedicated package.

Edge cases: v2 users cant get Nuxt support without upgrading; no workaround in the thread.

---

Source: [Vectle](https://vectle.com/skills/skl_UI7S8omX_jPBYs4an5dRWw). Version: `skv_HY2ciCzDFoMZrouuws5egg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
