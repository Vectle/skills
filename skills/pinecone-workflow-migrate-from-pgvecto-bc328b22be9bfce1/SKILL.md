---
name: "pinecone-workflow-migrate-from-pgvecto-bc328b22be9bfce1"
description: "Export vectors and metadata from Postgres, create the Pinecone index with matching dimension and metric, bulk load, then dual-run queries to validate parity before cutover. Not the full reference manual."
metadata:
  skill_id: "skl_GH1XJwtvpPOq_OxwovVINg"
  title: "Pinecone workflow: migrate from pgvector to Pinecone"
  version: "skv_xbamjeIampGanFqiyag5vA"
  updated: "2026-10-03T14:05:06.252413+00:00"
  canonical_url: "https://vectle.com/skills/skl_GH1XJwtvpPOq_OxwovVINg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Export vectors and metadata from Postgres, create the Pinecone index with matching dimension and metric, bulk load, then dual-run queries to validate parity before cutover. The Pinecone metric must match the pgvector operator semantics: cosine distance maps to cosine, L2 to euclidean, inner product to dotproduct. Create the Pinecone index with the source dimension and mapped metric.

# pgvector to Pinecone migration

## Steps

1. **Inventory the source.** Dimension, distance operator (`[-]` cosine, `[=]` etc.), row count, metadata columns and types. The Pinecone metric must match the pgvector operator semantics: cosine distance maps to `cosine`, L2 to `euclidean`, inner product to `dotproduct`.
2. **Create the Pinecone index** with the source dimension and mapped metric. Serverless unless you have measured sustained throughput that justifies pods.
3. **Export in chunks.** `COPY` vectors and metadata to Parquet or CSV in id-ordered chunks. Validate one chunk fully (dimensions, null handling, id uniqueness) before exporting terabytes.
4. **Bulk load.** Object-storage import for large data, batched upserts for smaller. Map Postgres ids to Pinecone ids (512-char cap); map columns to flat typed metadata.
5. **Dual-run.** Send production queries to both pgvector and Pinecone; compare top-k overlap. Investigate systematic divergences (usually metric mapping or normalization differences).
6. **Cut over.** Flip reads to Pinecone, keep pgvector as rollback for a window, then decommission.

## Traps

1. Metric mismatch: pgvector `[-]` with unnormalized vectors vs Pinecone `cosine` on normalized ones. Normalize consistently on both sides or the rankings diverge.
2. Null and type handling: Postgres nulls become absent metadata fields, which never match `$eq`. Decide the mapping explicitly.
3. Id collisions: Pinecone ids are strings; integer pkeys need a stable string mapping, ideally namespaced by table.

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

- Serverless unless you have measured sustained throughput that justifies pods.

---

Source: [Vectle](https://vectle.com/skills/skl_GH1XJwtvpPOq_OxwovVINg). Version: `skv_xbamjeIampGanFqiyag5vA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
