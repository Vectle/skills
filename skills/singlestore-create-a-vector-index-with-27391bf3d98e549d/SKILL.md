---
name: "singlestore-create-a-vector-index-with-27391bf3d98e549d"
description: "SingleStore: create a vector index with matching metric type and order. ADD VECTOR INDEX and INDEX_OPTIONS carrying index_type such as IVF_PQFS, metric_type such as EUCLIDEAN_DISTANCE, and nlist. Use when hitting this exact issue with SingleStore. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_6SDUH9KUg0ozQJCqEbAjHQ"
  title: "SingleStore: create a vector index with matching metric type and order"
  version: "skv_dX8ELHPzq9GSkamtrl5DtQ"
  updated: "2026-10-03T05:05:02.253614+00:00"
  canonical_url: "https://vectle.com/skills/skl_6SDUH9KUg0ozQJCqEbAjHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.singlestore.com/db/v8.9/reference/sql-reference/vector-functions/vector-indexing/\"]"
---

## TL;DR

ADD VECTOR INDEX and INDEX_OPTIONS carrying index_type such as IVF_PQFS, metric_type such as EUCLIDEAN_DISTANCE, and nlist. Create the index with ALTER TABLE ...

## Fix

1. ADD VECTOR INDEX and INDEX_OPTIONS carrying index_type such as IVF_PQFS, metric_type such as EUCLIDEAN_DISTANCE, and nlist.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this SingleStore feature.
- The symptom matches: create a vector index with matching metric type and order.

## When NOT to use

- Unrelated SingleStore issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against SingleStore. Source: https://docs.singlestore.com/db/v8.9/reference/sql-reference/vector-functions/vector-indexing/.

## Variant phrasings

### create a vector index with matching metric type and order

## Why it happens

An ANN index that does not match the query's metric and sort direction is never used. The build parameters must agree with the queries.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.singlestore.com/db/v8.9/reference/sql-reference/vector-functions/vector-indexing/

---

Source: [Vectle](https://vectle.com/skills/skl_6SDUH9KUg0ozQJCqEbAjHQ). Version: `skv_dX8ELHPzq9GSkamtrl5DtQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
