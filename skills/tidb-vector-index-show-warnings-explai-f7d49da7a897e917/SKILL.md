---
name: "tidb-vector-index-show-warnings-explai-f7d49da7a897e917"
description: "TiDB vector index: SHOW WARNINGS explains why the ANN index was not used. ordering by the wrong distance function gives the warning ANN index not used: not ordering by COSINE distance. Use when hitting this exact issue with TiDB vector index. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_Sr2enea0PH6th_jlHNhljg"
  title: "TiDB vector index: SHOW WARNINGS explains why the ANN index was not used"
  version: "skv__jTue3DqY_kwRUlZwnPwJA"
  updated: "2026-10-03T04:47:58.758086+00:00"
  canonical_url: "https://vectle.com/skills/skl_Sr2enea0PH6th_jlHNhljg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Ordering by the wrong distance function gives the warning ANN index not used: not ordering by COSINE distance.

## Fix

1. Ordering by the wrong distance function gives the warning ANN index not used: not ordering by COSINE distance.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this TiDB vector index feature.
- The symptom matches: SHOW WARNINGS explains why the ANN index was not used.

## When NOT to use

- Unrelated TiDB vector index issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against TiDB vector index. Source: https://docs.pingcap.com/tidb/dev/vector-search-index/.

## Variant phrasings

### SHOW WARNINGS explains why the ANN index was not used

## Why it happens

When the vector index cannot be used, TiDB emits a warning naming the cause. Check warnings right after EXPLAIN.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.pingcap.com/tidb/dev/vector-search-index/

---

Source: [Vectle](https://vectle.com/skills/skl_Sr2enea0PH6th_jlHNhljg). Version: `skv__jTue3DqY_kwRUlZwnPwJA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
