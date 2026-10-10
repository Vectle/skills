---
name: "tidb-vector-search-ann-index-not-used-fb58ef1c81445884"
description: "TiDB Vector Search: ANN index not used - EXPLAIN shows warnings. the two classic causes: ordering by the wrong distance function (the index is built on one function, for example cosine, and the query orders by L2), and using DESC order when the index only supports ascending. Use when hitting this exact issue with TiDB Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_KRvE6YJjOoAxh0Uwwzr2yg"
  title: "TiDB Vector Search: ANN index not used - EXPLAIN shows warnings"
  version: "skv_HxgN4EF6TakUHdmAGTF2gg"
  updated: "2026-10-03T04:48:54.384697+00:00"
  canonical_url: "https://vectle.com/skills/skl_KRvE6YJjOoAxh0Uwwzr2yg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The two classic causes: ordering by the wrong distance function (the index is built on one function, for example cosine, and the query orders by L2), and using DESC order when the index only supports ascending.

## The error

```text
EXPLAIN shows warnings
```

## Fix

1. The two classic causes: ordering by the wrong distance function (the index is built on one function, for example cosine, and the query orders by L2), and using DESC order when the index only supports ascending.
   Expected: you can confirm this matches your situation.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with TiDB Vector Search.
- The symptom matches: ANN index not used - EXPLAIN shows warnings.

## When NOT to use

- A different error message from TiDB Vector Search; the cause here is specific to this error.
- Unrelated TiDB Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against TiDB Vector Search (mentions 8.4.0, 8.5.0). Source: https://github.com/manasseh-zw/tidb.vector.net/blob/HEAD/docs/vector-search-index.md.

## Variant phrasings

### ANN index not used - EXPLAIN shows warnings
### EXPLAIN shows warnings

## Why it happens

A vector query runs as a full scan instead of using the vector index. EXPLAIN shows ANN index not used warnings.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/manasseh-zw/tidb.vector.net/blob/HEAD/docs/vector-search-index.md

---

Source: [Vectle](https://vectle.com/skills/skl_KRvE6YJjOoAxh0Uwwzr2yg). Version: `skv_HxgN4EF6TakUHdmAGTF2gg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
