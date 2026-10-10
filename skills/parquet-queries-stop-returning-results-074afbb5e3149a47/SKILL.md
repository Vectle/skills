---
name: "parquet-queries-stop-returning-results-074afbb5e3149a47"
description: "Explains why Parquet-backed SQL queries in Observable Framework stop returning results after a refresh on Windows (the framework's aggressive file-attachment cache on medium+ sized files) and points to the documented cache workarounds. Use when 'No results' appears after refresh on Windows. Not for queries that never returned results, or for non-Windows platforms."
metadata:
  skill_id: "skl_Lhf5ZKMPAB0JFlAEMvaAKg"
  title: "Parquet queries stop returning results after refresh on Windows"
  version: "skv_kgP8O-XuUWFscY5vR7i7Jg"
  updated: "2026-10-03T04:43:21.557812+00:00"
  canonical_url: "https://vectle.com/skills/skl_Lhf5ZKMPAB0JFlAEMvaAKg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

If your Parquet-backed SQL queries work at first but return no results after a refresh on Windows, blame the cache, not your query. This is the framework's aggressive file-attachment cache misbehaving on medium+ sized Parquet files, a Windows-specific problem.

1. Treat 'No results' after a refresh as a cache problem first, not a query problem.
2. Apply the cache-avoidance workarounds documented in the linked discussion (observablehq/framework discussions/1691, mbostock's comment). Expected: queries return results again after refresh.

When to use: Parquet queries in Observable Framework work during development, then return nothing after a refresh, on Windows, with medium+ sized files.

When not to use: queries that never returned results (that is your SQL), or the same symptom on macOS or Linux.

Compatibility: Observable Framework, Parquet file attachments, Windows.

Variants:
- "observable framework parquet no results after refresh"
- "parquet queries stop returning results windows"
- "observable file attachment cache parquet"

Root cause: the framework's aggressive file-attachment cache goes stale on medium+ sized Parquet files on Windows.

Edge cases: small Parquet files dont seem to trigger it. If the workarounds dont help, double-check the file path and the 'sql' preamble tag before assuming a deeper bug.

---

Source: [Vectle](https://vectle.com/skills/skl_Lhf5ZKMPAB0JFlAEMvaAKg). Version: `skv_kgP8O-XuUWFscY5vR7i7Jg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
