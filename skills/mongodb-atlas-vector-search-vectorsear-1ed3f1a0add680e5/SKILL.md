---
name: "mongodb-atlas-vector-search-vectorsear-1ed3f1a0add680e5"
description: "MongoDB Atlas Vector Search: '$vectorSearch is only valid for Atlas'. the $vectorSearch aggregation stage is Atlas-only; running it against local MongoDB raises the '$vectorSearch is only valid for Atlas' error, so update the connection string to the Atlas cluster. Use when hitting this exact issue with MongoDB Atlas Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_sPMvBNBrnTr5GGKpmpBfKw"
  title: "MongoDB Atlas Vector Search: '$vectorSearch is only valid for Atlas'"
  version: "skv_hHiEbyjMKyVAXbX5xK8iKw"
  updated: "2026-10-03T05:57:02.94605+00:00"
  canonical_url: "https://vectle.com/skills/skl_sPMvBNBrnTr5GGKpmpBfKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The $vectorSearch aggregation stage is Atlas-only; running it against local MongoDB raises the '$vectorSearch is only valid for Atlas' error, so update the connection string to the Atlas cluster. Index Building Failed has three usual causes: the cluster tier must be M10 or higher for full Vector Search, the cluster version must be 6.0.11+ or 7.0.2+, and the collection needs at least one document.

## Fix

1. The $vectorSearch aggregation stage is Atlas-only; running it against local MongoDB raises the '$vectorSearch is only valid for Atlas' error, so update the connection string to the Atlas cluster.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this MongoDB Atlas Vector Search feature.
- The symptom matches: '$vectorSearch is only valid for Atlas'.

## When NOT to use

- Unrelated MongoDB Atlas Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against MongoDB Atlas Vector Search (mentions 6.0.11, 7.0.2). Source: a local/non-public address.com/luvadlamudi/tamuhack26/blob/HEAD/backend/rag/VECTOR_INDEX_SETUP.md.

## Variant phrasings

### '$vectorSearch is only valid for Atlas'

## Why it happens

Pointing a vector-search app at a local or self-hosted MongoDB fails at runtime. The stage only exists on Atlas.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

a local/non-public address.com/luvadlamudi/tamuhack26/blob/HEAD/backend/rag/VECTOR_INDEX_SETUP.md

---

Source: [Vectle](https://vectle.com/skills/skl_sPMvBNBrnTr5GGKpmpBfKw). Version: `skv_hHiEbyjMKyVAXbX5xK8iKw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
