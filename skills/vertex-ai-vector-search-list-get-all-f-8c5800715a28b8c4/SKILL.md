---
name: "vertex-ai-vector-search-list-get-all-f-8c5800715a28b8c4"
description: "Vertex AI Vector Search: list()/get_all fails on non-768-dimension indexes. The proposed fix adds a configurable embedding_model_dims setting defaulting to 768. Use when hitting this exact issue with Vertex AI Vector Search. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_wCyFxHHe096qXVsqGrw4YQ"
  title: "Vertex AI Vector Search: list()/get_all fails on non-768-dimension indexes"
  version: "skv_JqgrvIa_K7pmx1IZ2toJrA"
  updated: "2026-10-03T04:45:45.8557+00:00"
  canonical_url: "https://vectle.com/skills/skl_wCyFxHHe096qXVsqGrw4YQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The proposed fix adds a configurable embedding_model_dims setting defaulting to 768. Workaround: set the query dimension to match your index's configured dimensions, or recreate the index at 768 if that fits your model. The mem0 Vertex AI Vector Search integration builds the zero query vector with a hardcoded dimension of 768 and the config has no dimension field, so any index with a different dimension (OpenAI 1536/3072) rejects the query.

## The error

```text
list()/get_all fails on non-768-dimension indexes
```

## Fix

1. The proposed fix adds a configurable embedding_model_dims setting defaulting to 768.
   Expected: You get the expected result; the problem is gone.
2. Workaround: set the query dimension to match your index's configured dimensions, or recreate the index at 768 if that fits your model.
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Vertex AI Vector Search.
- The symptom matches: list()/get_all fails on non-768-dimension indexes.

## When NOT to use

- A different error message from Vertex AI Vector Search; the cause here is specific to this error.
- Unrelated Vertex AI Vector Search issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Vertex AI Vector Search. Source: https://github.com/mem0ai/mem0/issues/6419.

## Variant phrasings

### list()/get_all fails on non-768-dimension indexes

## Why it happens

Mem0 GoogleMatchingEngine list(), get_all and delete_all fail for indexes whose embedding dimension is not 768, because the zero query vector is hardcoded to 768 dimensions.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/mem0ai/mem0/issues/6419

---

Source: [Vectle](https://vectle.com/skills/skl_wCyFxHHe096qXVsqGrw4YQ). Version: `skv_JqgrvIa_K7pmx1IZ2toJrA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
