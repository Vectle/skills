---
name: "eppo-dart-sdk-targeting-attributes-mus-29c5d0d2901a68b6"
description: "Guide Eppo Dart SDK: targeting attributes must match the flag rules exactly: When you initialize the Dart SDK, pass categorical attributes like country and device type plus numeric attributes like age or account age, using exactly the keys and value types the flag rules use. Use this when you hit exactly this in Eppo Dart SDK. Not for different errors or different tools."
metadata:
  skill_id: "skl_vSBOKHLXmYnRe2-cfZYQpg"
  title: "Eppo Dart SDK: targeting attributes must match the flag rules exactly"
  version: "skv_3J3jWZzHwpP5aCMduNgNkA"
  updated: "2026-10-03T04:39:24.098932+00:00"
  canonical_url: "https://vectle.com/skills/skl_vSBOKHLXmYnRe2-cfZYQpg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: When you initialize the Dart SDK, pass categorical attributes like country and device type plus numeric attributes like age or account age, using exactly the keys and value types the flag rules use. keep a single source of truth for attribute names and types shared between your flag definitions and the app. Initialize once at app start, dont re-init per screen.

keep a single source of truth for attribute names and types shared between your flag definitions and the app. When you initialize the Dart SDK, pass categorical attributes like country and device type plus numeric attributes like age or account age, using exactly the keys and value types the flag rules use. Initialize once at app start, dont re-init per screen. After fetching an assignment, log it with your assignment logger so the warehouse sees what the local evaluation decided. If a targeted user keeps getting the default, compare the attribute map you sent against the rule definition character by character before suspecting the SDK.

## When to use
You hit exactly this: Eppo Dart SDK: targeting attributes must match the flag rules exactly in Eppo Dart SDK.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Eppo Dart SDK.

---

Source: [Vectle](https://vectle.com/skills/skl_vSBOKHLXmYnRe2-cfZYQpg). Version: `skv_3J3jWZzHwpP5aCMduNgNkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
