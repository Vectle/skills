---
name: "pinecone-workflow-full-text-bm25-index-69f50055f9d098eb"
description: "Newer Pinecone indexes can declare a document schema with full-text string fields for BM25 ranking alongside dense vector fields. Declare ranking fields up front; metadata stays schemaless. Not the full reference manual."
metadata:
  skill_id: "skl_WpoheyQN38l7HgAAUOiUTA"
  title: "Pinecone workflow: full-text BM25 index with a document schema"
  version: "skv_J-rNxqx7YKfpCSMTUsYLTA"
  updated: "2026-10-03T14:10:24.958541+00:00"
  canonical_url: "https://vectle.com/skills/skl_WpoheyQN38l7HgAAUOiUTA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Newer Pinecone indexes can declare a document schema with full-text string fields for BM25 ranking alongside dense vector fields. Declare ranking fields up front; metadata stays schemaless. Build the schema declaring which string fields get BM25. Create the index with the schema (API version 2026-07; REST or Python SDK).

## The fix

**TL;DR:** Newer Pinecone indexes can declare a document schema with full-text string fields for BM25 ranking alongside dense vector fields. Declare ranking fields up front; metadata stays schemaless. Build the schema declaring which string fields get BM25. Create the index with the schema (API version 2026-07; REST or Python SDK).

# Full-text search with a document schema

## What it is

An index with a document schema stores typed JSON documents. You declare ranking fields: `string` fields with full-text search enabled (BM25 ranking), `dense_vector` fields (ANN similarity), and `sparse_vector` fields. Non-ranking fields ride along as metadata, auto-indexed for filtering at upsert time. One index can mix all three ranking types; each query picks its scoring signal.

## Steps

1. **Build the schema** declaring which string fields get BM25. Only declared fields are full-text indexed; undeclared text is metadata, not searchable by BM25.
2. **Create the index** with the schema (API version 2026-07; REST or Python SDK).
3. **Upsert documents** as JSON records matching the schema. Ranking fields must be present and correctly typed.
4. **Query with the right clause:** BM25 text clauses on the full-text fields, dense queries on the vector fields, or combine a text-match filter with a dense rank in one request.
5. **Remember what BM25 is not.** A full-text field does not call an embedding model. It is Lucene-style keyword ranking. For semantic matching you need the dense field too.

## Traps

1. Expecting semantic matches from a BM25-only index: synonyms and paraphrases will not match. That is working as designed.
2. Declaring every string field as full-text: index what you search, not everything. Unneeded full-text fields cost index size and write speed.
3. Mixing APIs: document-schema indexes use the newer API version; older SDK versions do not know the schema calls. Keep the SDK current.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_WpoheyQN38l7HgAAUOiUTA). Version: `skv_J-rNxqx7YKfpCSMTUsYLTA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
