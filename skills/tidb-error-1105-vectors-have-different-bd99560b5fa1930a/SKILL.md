---
name: "tidb-error-1105-vectors-have-different-bd99560b5fa1930a"
description: "TiDB: ERROR 1105 vectors have different dimensions. the two vectors in VEC_L2_DISTANCE, VEC_COSINE_DISTANCE, and the other vector functions must have the same dimension, otherwise an error is returned, for example ERROR 1105 (HY000): vectors have different dimensions. Use when hitting this exact issue with TiDB. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_9Q_h7Vzib2EtsGVVVRUNIw"
  title: "TiDB: ERROR 1105 vectors have different dimensions"
  version: "skv_sLFQ1sHxg4nM_2O5ryGz0g"
  updated: "2026-10-03T04:46:10.061402+00:00"
  canonical_url: "https://vectle.com/skills/skl_9Q_h7Vzib2EtsGVVVRUNIw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The two vectors in VEC_L2_DISTANCE, VEC_COSINE_DISTANCE, and the other vector functions must have the same dimension, otherwise an error is returned, for example ERROR 1105 (HY000): vectors have different dimensions.

## The error

```text
ERROR 1105 vectors have different dimensions
```

## Fix

1. The two vectors in VEC_L2_DISTANCE, VEC_COSINE_DISTANCE, and the other vector functions must have the same dimension, otherwise an error is returned, for example ERROR 1105 (HY000): vectors have different dimensions.
   Expected: you can confirm this matches your situation.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with TiDB.
- The symptom matches: ERROR 1105 vectors have different dimensions.

## When NOT to use

- A different error message from TiDB; the cause here is specific to this error.
- Unrelated TiDB issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against TiDB. Source: https://docs-archive.pingcap.com/tidb/v8.4/vector-search-data-types/.

## Variant phrasings

### ERROR 1105 vectors have different dimensions

## Why it happens

Vector functions require both operands to have the same dimension. A mismatch is a hard error, not a silent cast.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs-archive.pingcap.com/tidb/v8.4/vector-search-data-types/

---

Source: [Vectle](https://vectle.com/skills/skl_9Q_h7Vzib2EtsGVVVRUNIw). Version: `skv_sLFQ1sHxg4nM_2O5ryGz0g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
