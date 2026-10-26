---
name: "mongodb-atlas-vector-search-dimension-c6850617ba0b754e"
description: "MongoDB Atlas Vector Search: dimension mismatch after switching embedding models. Vectors from different models cannot be compared in the same index: a 384-dim local model and a 1024-dim hosted model need separate Atlas vector indexes. Use when hitting this exact issue with MongoDB Atlas Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_lpC1YLDv_rqcVe0fyO5oiA"
  title: "MongoDB Atlas Vector Search: dimension mismatch after switching embedding models"
  version: "skv_m736VW8ZlcYgfwYVHtK6Sg"
  updated: "2026-10-03T05:58:55.751123+00:00"
  canonical_url: "https://vectle.com/skills/skl_lpC1YLDv_rqcVe0fyO5oiA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/neomatrix369/rag-params-finder/blob/HEAD/docs/user-guide/troubleshooting.md\"]"
---

## TL;DR

Vectors from different models cannot be compared in the same index: a 384-dim local model and a 1024-dim hosted model need separate Atlas vector indexes.

## Fix

1. Vectors from different models cannot be compared in the same index: a 384-dim local model and a 1024-dim hosted model need separate Atlas vector indexes.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this MongoDB Atlas Vector Search feature.
- The symptom matches: dimension mismatch after switching embedding models.

## When NOT to use

- Unrelated MongoDB Atlas Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against MongoDB Atlas Vector Search. Source: a local/non-public address.com/neomatrix369/rag-params-finder/blob/HEAD/docs/user-guide/troubleshooting.md.

## Variant phrasings

### dimension mismatch after switching embedding models

## Why it happens

Vector search fails with a dimension error, or results are nonsensical, after switching the embedding model.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

a local/non-public address.com/neomatrix369/rag-params-finder/blob/HEAD/docs/user-guide/troubleshooting.md

---

Source: [Vectle](https://vectle.com/skills/skl_lpC1YLDv_rqcVe0fyO5oiA). Version: `skv_m736VW8ZlcYgfwYVHtK6Sg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
