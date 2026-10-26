---
name: "crash-with-many-objects-with-geocoordi-c6e3bac9e89c5ddf"
description: "Fixes Weaviate crashing with 'panic: runtime error: makeslice: len out of range' while importing objects with geoCoordinates props by upgrading to v1.17.2 or later. Use when the crash hits mid-import on geo data. Not for crashes without geoCoordinates."
metadata:
  skill_id: "skl_Lk8OuR4_HRemovQFAwEMHQ"
  title: "Crash with many objects with geoCoordinates props: \"panic: runtime error: makeslice: len out of range\""
  version: "skv_s_Ud0gpJx05F0zaLsSYRmA"
  updated: "2026-10-03T04:49:31.983824+00:00"
  canonical_url: "https://vectle.com/skills/skl_Lk8OuR4_HRemovQFAwEMHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/weaviate/weaviate/issues/2539\"]"
---

Fix first: upgrade to Weaviate v1.17.2 or later. As a stopgap, slowing the import loop (a short sleep every few thousand records) helped.

```text
panic: runtime error: makeslice: len out of range
```

1. Upgrade Weaviate to v1.17.2 or later.
2. Re-run the import. Expected: it completes instead of crashing the server.
3. If you cant upgrade yet: add a short sleep every few thousand records in your import loop. Expected: the crash stops (stopgap, not a fix).

When to use: Weaviate crashes and cant recover while importing objects with geoCoordinates props.

When not to use: crashes with no geoCoordinates involved (different bug).

Compatibility: Weaviate v1.17.2+. Reported in weaviate/weaviate#2539.

Variants:
- "weaviate panic makeslice len out of range"
- "weaviate crash geoCoordinates import"
- "weaviate import crash 88000 records"

Root cause: the HNSW index struggled with duplicate geo coordinates, which made a race condition much more likely.

Edge cases: the crash point varies (around 88,000 records in the report). The sleep stopgap only reduces the odds; the upgrade is the fix.

---

Source: [Vectle](https://vectle.com/skills/skl_Lk8OuR4_HRemovQFAwEMHQ). Version: `skv_s_Ud0gpJx05F0zaLsSYRmA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
