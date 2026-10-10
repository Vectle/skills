---
name: "numbers-returned-as-strings-92a803cfa363c3f3"
description: "Explains why @planetscale/database returns BIGINT and unsigned 64-bit columns as strings (deliberate, to avoid silent type changes past MAX_SAFE_INTEGER) and how to convert them with a custom cast function. Use when numeric columns come back as strings in Node. Not for other drivers, or for columns you actually want as strings."
metadata:
  skill_id: "skl_1NFUKmOV3rwbJRyVQ769mA"
  title: "Numbers returned as strings"
  version: "skv_XUm7WfrYTak5MrQWhPUGqg"
  updated: "2026-10-03T04:28:40.464492+00:00"
  canonical_url: "https://vectle.com/skills/skl_1NFUKmOV3rwbJRyVQ769mA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Thats deliberate. The driver will not guess whether a value fits in a JS number, because crossing the threshold mid-stream would silently change your types. Supply a custom cast function to convert them how you like.

1. Add a custom cast function in your connection config. See the README's custom type casting section for the hook.
2. In the cast, convert the way you like: `Number()` with a `MAX_SAFE_INTEGER` check, or `BigInt` for values that need it. Expected: the columns come back as numbers (or BigInt) instead of strings.

When to use: BIGINT or unsigned 64-bit columns arrive as strings from @planetscale/database.

When not to use: a different database driver, or columns you actually want as strings.

Compatibility: @planetscale/database (Node.js). Reported in planetscale/database-js#175.

Variants:
- "planetscale bigint string"
- "planetscale numbers returned as strings nodejs"
- "planetscale custom type casting"

Root cause: deliberate driver behavior. JS numbers lose precision past MAX_SAFE_INTEGER, so the driver hands you strings and lets you decide how to convert.

Edge cases: values above Number.MAX_SAFE_INTEGER need BigInt. Blindly calling Number() on them loses precision, which is exactly what the driver is protecting you from.

---

Source: [Vectle](https://vectle.com/skills/skl_1NFUKmOV3rwbJRyVQ769mA). Version: `skv_XUm7WfrYTak5MrQWhPUGqg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
