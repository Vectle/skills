---
name: "pinecone-diagnosis-langchain-vector-st-7737771bcaaa49f2"
description: "Symptom: PineconeVectorStore construction succeeds but the first operation fails. LangChain never creates the index; create it first with matching dimension."
metadata:
  skill_id: "skl_o1n6T3kffu5uGgNPjLJYrw"
  title: "Pinecone diagnosis: LangChain vector store fails on a missing index"
  version: "skv_dchGsh_BT4ikJDBiXbgcEQ"
  updated: "2026-10-03T15:15:00.186912+00:00"
  canonical_url: "https://vectle.com/skills/skl_o1n6T3kffu5uGgNPjLJYrw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/integrations/langchain\"]"
---

**TL;DR:** Symptom: PineconeVectorStore construction succeeds but the first operation fails. LangChain never creates the index; create it first with matching dimension. Confirm it 1. pc.list_indexes() with the raw Pinecone client: is the name there? Check the namespace: the store may target a namespace while you verified the default.

## The fix

1. `pc.list_indexes()` with the raw Pinecone client: is the name there?

2. If present, `describe_index`: does its dimension match `len(embeddings.embed_query('test'))`?

3. Check the namespace: the store may target a namespace while you verified the default.

4. Create the index first (serverless spec, right dimension and metric), then construct the store.

5. Or point the store at the existing correct index.

6. Make index creation part of your setup script, ordered before any LangChain code runs.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: Pinecone diagnosis.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_o1n6T3kffu5uGgNPjLJYrw). Version: `skv_dchGsh_BT4ikJDBiXbgcEQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
