---
name: "mongodb-query-doing-collscan-instead-o-9fa8f7e57a5b8a0b"
description: "mongodb query doing COLLSCAN instead of IXSCAN is slow and times out"
metadata:
  skill_id: "skl_33Y08Lx1yvhXM8G3CDHpqA"
  title: "mongodb query doing COLLSCAN instead of IXSCAN is slow and times out"
  version: "skv_GXGnuQUKKwgixnWGU0F4Tw"
  updated: "2026-11-07T01:53:42.66996+00:00"
  canonical_url: "https://vectle.com/skills/skl_33Y08Lx1yvhXM8G3CDHpqA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

**Capture the exact query shape.** Copy the filter, sort and projection from the slow log or app code for one timing out call. Expected: you know the fields, operators and sort order, not just the collection name.

**Confirm the scan with explain.** Run explain with executionStats for that query in the mongo shell. Success check: the winning plan stage is COLLSCAN and totalDocsExamined is close to the collection size.

**Design the index in ESR order.** Put equality fields first, then the sort field, then range fields, using the actual query shape. Expected: the index definition mirrors the query instead of being one single field guess.

**Create the index safely.** Create the index in the background / online manner your MongoDB version uses by default, during a lower traffic window for very large collections. Success check: the build completes and appears in the index list for the collection.

**Re-run explain and the real query.** Run the same explain again. Expected: winning plan is IXSCAN, docs examined drops close to documents returned, and the query finishes well under the timeout.

**Check for a competing plan cache issue.** If explain still picks COLLSCAN, clear the plan cache for that collection once or restart the app after the index is ready, then recheck. Success check: new executions use the new index.

---

Source: [Vectle](https://vectle.com/skills/skl_33Y08Lx1yvhXM8G3CDHpqA). Version: `skv_GXGnuQUKKwgixnWGU0F4Tw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
