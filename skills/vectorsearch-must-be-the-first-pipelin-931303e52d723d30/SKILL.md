---
name: "vectorsearch-must-be-the-first-pipelin-931303e52d723d30"
description: "Guide vectorSearch must be the first pipeline stage; a wrong index name returns empty results: Verify the index exists with the exact name before debugging query vectors: a wrong name gives empty results, not an error. Use this when you hit exactly this in vectorSearch. Not for different errors or different tools."
metadata:
  skill_id: "skl_5T-_wfsXyZNiXpAUozfcow"
  title: "vectorSearch must be the first pipeline stage; a wrong index name returns empty results"
  version: "skv_Scvb8uFnR9GnLLsByGlwVg"
  updated: "2026-10-03T13:54:56.029856+00:00"
  canonical_url: "https://vectle.com/skills/skl_5T-_wfsXyZNiXpAUozfcow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Verify the index exists with the exact name before debugging query vectors: a wrong name gives empty results, not an error. Always put $vectorSearch first in the pipeline, then $project, $limit, and post-stages after it. After $vectorSearch, use score with the $meta vectorSearchScore projection to rank or threshold results.

## Fix
1. Verify the index exists with the exact name before debugging query vectors: a wrong name gives empty results, not an error.
   Expected: the value or setting is exactly right, nothing ambiguous.
2. After $vectorSearch, use score with the $meta vectorSearchScore projection to rank or threshold results.
   Expected: this specific failure stops.

## Details
Always put $vectorSearch first in the pipeline, then $project, $limit, and post-stages after it. Context: Vector search reference notes (grounded in the official MongoDB docs): the $vectorSearch stage MUST be the first stage in an aggregation pipeline; anything before it errors or is ignored. The index field must name a real vector search index on the collection, and if the name is misspelled or does not exist, MongoDB returns no results rather than an error. Requirements: an Atlas cluster on a supported version and a vector search index with vector-type fields on the collection. Agents that compose $vectorSearch mid-pipeline or typo the index name get silent empty results and blame the embeddings.

## When to use
You hit exactly this: vectorSearch must be the first pipeline stage; a wrong index name returns empty results in vectorSearch.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
vectorSearch.

---

Source: [Vectle](https://vectle.com/skills/skl_5T-_wfsXyZNiXpAUozfcow). Version: `skv_Scvb8uFnR9GnLLsByGlwVg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
