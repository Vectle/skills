---
name: "tidb-vector-search-error-1105-vector-h-d3b1c77c31ef76da"
description: "TiDB Vector Search: ERROR 1105 vector has N dimensions, does not fit VECTOR(M). Match the column dimension to your embedding model, or omit the dimension parameter (plain VECTOR) to store mixed dimensions, but then you cannot build a vector search index on the column since distance needs matching dimensions. Use when hitting this exact issue with TiDB Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_mE1mHEWQ3ySjgzqIHhj4Lw"
  title: "TiDB Vector Search: ERROR 1105 vector has N dimensions, does not fit VECTOR(M)"
  version: "skv_GO2v3Xv2TaW_sEfPsMUddQ"
  updated: "2026-10-03T05:00:50.906096+00:00"
  canonical_url: "https://vectle.com/skills/skl_mE1mHEWQ3ySjgzqIHhj4Lw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Match the column dimension to your embedding model, or omit the dimension parameter (plain VECTOR) to store mixed dimensions, but then you cannot build a vector search index on the column since distance needs matching dimensions. To switch models later, recreate the column with the new dimension and re-embed. The VECTOR type enforces its dimension at insert time.

## The error

```text
ERROR 1105 vector has N dimensions, does not fit VECTOR(M)
```

## Fix

1. Match the column dimension to your embedding model, or omit the dimension parameter (plain VECTOR) to store mixed dimensions, but then you cannot build a vector search index on the column since distance needs matching dimensions.
   Expected: You get the expected result; the problem is gone.
2. To switch models later, recreate the column with the new dimension and re-embed.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with TiDB Vector Search.
- The symptom matches: ERROR 1105 vector has N dimensions, does not fit VECTOR(M).

## When NOT to use

- A different error message from TiDB Vector Search; the cause here is specific to this error.
- Unrelated TiDB Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against TiDB Vector Search. Source: https://github.com/manasseh-zw/tidb.vector.net/blob/HEAD/docs/vector-search-data-types.md.

## Variant phrasings

### ERROR 1105 vector has N dimensions, does not fit VECTOR(M)

## Why it happens

Inserts fail with ERROR 1105 (HY000): vector has 2 dimensions, does not fit VECTOR(3).

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/manasseh-zw/tidb.vector.net/blob/HEAD/docs/vector-search-data-types.md

---

Source: [Vectle](https://vectle.com/skills/skl_mE1mHEWQ3ySjgzqIHhj4Lw). Version: `skv_GO2v3Xv2TaW_sEfPsMUddQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
