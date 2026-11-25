---
name: "postgres-error-deadlock-detected-detai-b2e9e5c491f153f6"
description: "postgres error deadlock detected detail processes waiting for lock fails bug"
metadata:
  skill_id: "skl_miqcYQuwwgis0j02wY4zgw"
  title: "postgres error deadlock detected detail processes waiting for lock fails bug"
  version: "skv_2kjAptWi7gIJ8tzbytg1Aw"
  updated: "2026-11-25T13:52:41.656885+00:00"
  canonical_url: "https://vectle.com/skills/skl_miqcYQuwwgis0j02wY4zgw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Read the full deadlock detail in the server log.

Check what is currently blocked.

Make both code paths lock in a consistent order.

Shorten the transactions.

Add a bounded retry for the rolled back transaction.

---

Source: [Vectle](https://vectle.com/skills/skl_miqcYQuwwgis0j02wY4zgw). Version: `skv_2kjAptWi7gIJ8tzbytg1Aw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
