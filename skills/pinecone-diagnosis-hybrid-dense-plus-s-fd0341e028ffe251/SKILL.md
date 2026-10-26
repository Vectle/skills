---
name: "pinecone-diagnosis-hybrid-dense-plus-s-fd0341e028ffe251"
description: "Symptom: hybrid queries return worse results than dense-only. Check that sparse values are present on records, the alpha balance is sane, and you picked the right combination pattern. Not the full reference manual."
metadata:
  skill_id: "skl_TRvcvXZ31jvt5BovekmWyw"
  title: "Pinecone diagnosis: hybrid dense plus sparse search underperforms"
  version: "skv_s5PDOEhvCGeg0VGXMZv-GQ"
  updated: "2026-10-03T15:19:19.456097+00:00"
  canonical_url: "https://vectle.com/skills/skl_TRvcvXZ31jvt5BovekmWyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/guides/search/hybrid-search\"]"
---

**TL;DR:** Symptom: hybrid queries return worse results than dense-only. Check that sparse values are present on records, the alpha balance is sane, and you picked the right combination pattern. Confirm it 1. Fetch a few records and confirm sparse_values are present and nonzero.

## The fix

1. Fetch a few records and confirm `sparse_values` are present and nonzero.

2. Run dense-only and sparse-only queries separately; if sparse-only returns junk, the sparse vectors (or the sparse index config) are the problem.

3. Check how you combine: server-side combination needs both vectors on each record in one index; client-side fusion needs two queries plus RRF.

4. Missing sparse values: re-ingest with sparse vectors (e.g. from a sparse embedding model like pinecone-sparse-english-v0 or BM25 weights).

5. Balance: scale query vectors to adjust the dense/sparse weight (alpha) and evaluate; do not leave it at a default nobody chose.

6. Wrong pattern: pick one documented pattern (filter-then-rank, client-side RRF fusion, or server-side combination) and implement exactly that.

## When to use this

- This covers exactly what the title says: Pinecone diagnosis.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_TRvcvXZ31jvt5BovekmWyw). Version: `skv_s5PDOEhvCGeg0VGXMZv-GQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
