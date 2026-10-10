---
name: "singlestore-vector-range-search-explai-009a745ec11f8831"
description: "SingleStore vector range search: EXPLAIN proves the index is used. in the EXPLAIN output, the ColumnStoreFilter row shows INTERNAL_VECTOR_RANGE_SEARCH when the plan uses a vector index for range search. Use when hitting this exact issue with SingleStore vector range search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_hglyDQ4GLxvnlXi3x9NdgQ"
  title: "SingleStore vector range search: EXPLAIN proves the index is used"
  version: "skv_jUXFWYKI7RIS4VdVbv2_RA"
  updated: "2026-10-03T05:06:21.326106+00:00"
  canonical_url: "https://vectle.com/skills/skl_hglyDQ4GLxvnlXi3x9NdgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

In the EXPLAIN output, the ColumnStoreFilter row shows INTERNAL_VECTOR_RANGE_SEARCH when the plan uses a vector index for range search.

## The error

```text
EXPLAIN proves the index is used
```

## Fix

1. In the EXPLAIN output, the ColumnStoreFilter row shows INTERNAL_VECTOR_RANGE_SEARCH when the plan uses a vector index for range search.
   Expected: you can confirm this matches your situation.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with SingleStore vector range search.
- The symptom matches: EXPLAIN proves the index is used.

## When NOT to use

- A different error message from SingleStore vector range search; the cause here is specific to this error.
- Unrelated SingleStore vector range search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against SingleStore vector range search. Source: https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-range-search/.

## Variant phrasings

### EXPLAIN proves the index is used

## Why it happens

Vector range queries can silently fall back to full scans. The EXPLAIN plan tells you whether the index kicked in.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.singlestore.com/cloud/reference/sql-reference/vector-functions/vector-range-search/

---

Source: [Vectle](https://vectle.com/skills/skl_hglyDQ4GLxvnlXi3x9NdgQ). Version: `skv_jUXFWYKI7RIS4VdVbv2_RA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
