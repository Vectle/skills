---
name: "singlestore-vector-query-not-using-the-d45b27c9e2837e39"
description: "SingleStore Vector: query not using the ANN index - EXPLAIN check. To force a specific index, specify USE INDEX with the key name; if the index is missing the query errors instead of silently scanning. Use when hitting this exact issue with SingleStore Vector. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_waeQ7pes0sYDKTR6a9Hwzw"
  title: "SingleStore Vector: query not using the ANN index - EXPLAIN check"
  version: "skv_sDq9Lz3d1nk7tm-2G763Nw"
  updated: "2026-10-03T05:09:12.798112+00:00"
  canonical_url: "https://vectle.com/skills/skl_waeQ7pes0sYDKTR6a9Hwzw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.singlestore.com/db/v8.7/reference/sql-reference/vector-functions/vector-indexing/\"]"
---

## TL;DR

To force a specific index, specify USE INDEX with the key name; if the index is missing the query errors instead of silently scanning. If INTERNAL_VECTOR_SEARCH is not in the ColumnStoreFilter line of EXPLAIN, the vector index is not being used.

## The error

```text
EXPLAIN check
```

## Fix

1. To force a specific index, specify USE INDEX with the key name; if the index is missing the query errors instead of silently scanning.
   Expected: You get the expected result; the problem is gone.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with SingleStore Vector.
- The symptom matches: query not using the ANN index - EXPLAIN check.

## When NOT to use

- A different error message from SingleStore Vector; the cause here is specific to this error.
- Unrelated SingleStore Vector issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against SingleStore Vector. Source: https://docs.singlestore.com/db/v8.7/reference/sql-reference/vector-functions/vector-indexing/.

## Variant phrasings

### query not using the ANN index - EXPLAIN check
### EXPLAIN check

## Why it happens

A vector query runs slowly as if the vector index does not exist. Check EXPLAIN to see whether the index is used at all.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.singlestore.com/db/v8.7/reference/sql-reference/vector-functions/vector-indexing/

---

Source: [Vectle](https://vectle.com/skills/skl_waeQ7pes0sYDKTR6a9Hwzw). Version: `skv_sDq9Lz3d1nk7tm-2G763Nw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
