---
name: "pinecone-workflow-hybrid-dense-plus-sp-ae6dd123440f2ead"
description: "Store dense and sparse vectors on each record in one index, then balance them client-side with alpha weighting. Evaluate on keyword-heavy and meaning-heavy queries separately. Not the full reference manual."
metadata:
  skill_id: "skl_uDnkHFH2ebI_KpwMX9vx0g"
  title: "Pinecone workflow: hybrid dense plus sparse search on the Vectors API"
  version: "skv_2BFZiAzb6RiKpMzjfAxGGA"
  updated: "2026-10-03T14:09:05.141848+00:00"
  canonical_url: "https://vectle.com/skills/skl_uDnkHFH2ebI_KpwMX9vx0g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/search/hybrid-search\"]"
---

**TL;DR:** Store dense and sparse vectors on each record in one index, then balance them client-side with alpha weighting. Evaluate on keyword-heavy and meaning-heavy queries separately. Create the index with metric="dotproduct". Query with both: send the dense query vector and the sparse query vector in one request.

# Hybrid search: dense plus sparse in one index

## The pattern

On the Vectors API, each record carries both a dense vector (meaning) and a sparse vector (keyword signal). One query sends both; Pinecone combines them. You set the balance client-side by scaling the query vectors before sending (alpha weighting).

## Steps

1. **Create the index** with `metric="dotproduct"`. Hybrid on the Vectors API uses dotproduct.
2. **Produce both vectors per record.** Dense from your embedding model; sparse from a sparse model (e.g. pinecone-sparse-english-v0) or BM25 weights over your text. Records without sparse values silently degrade to dense-only.
3. **Upsert both together:** each record has `values` and `sparse_values` (indices plus values).
4. **Query with both:** send the dense query vector and the sparse query vector in one request.
5. **Tune alpha.** Scale the sparse query vector relative to dense to weight keyword vs meaning. There is no universal alpha; evaluate on your queries.
6. **Evaluate properly.** Keyword-heavy queries (product codes, error strings, names) should beat dense-only; meaning-heavy queries should beat sparse-only. If hybrid loses on both, the sparse vectors are bad, not the idea.

## Traps

1. Upserting dense only and expecting hybrid: the sparse side contributes nothing and you paid the complexity for zero gain.
2. One alpha for all query types: navigational queries want keyword weight; exploratory questions want semantic weight. Consider per-query-type alpha.
3. Confusing this with filter-then-rank or RRF fusion: those are different documented patterns with different trade-offs. Pick one deliberately.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

## Edge cases

- Confusing this with filter-then-rank or RRF fusion: those are different documented patterns with different trade-offs.

---

Source: [Vectle](https://vectle.com/skills/skl_uDnkHFH2ebI_KpwMX9vx0g). Version: `skv_2BFZiAzb6RiKpMzjfAxGGA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
