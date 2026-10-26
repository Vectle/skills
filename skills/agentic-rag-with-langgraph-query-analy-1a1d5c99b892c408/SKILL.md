---
name: "agentic-rag-with-langgraph-query-analy-1a1d5c99b892c408"
description: "For multi-hop questions, make retrieval a node in a LangGraph instead of a fixed pipeline step: analyze the query, retrieve, decide whether to retrieve again or generate. The docs' agentic RAG guide is the reference implementation. Not the full reference manual."
metadata:
  skill_id: "skl_flOeRia-iQYJstFxl6Xpwg"
  title: "Agentic RAG with LangGraph: query analysis, retrieval, and generation as nodes"
  version: "skv_U0DsrO_UP0gdssnAhgAdMw"
  updated: "2026-10-03T14:02:15.153856+00:00"
  canonical_url: "https://vectle.com/skills/skl_flOeRia-iQYJstFxl6Xpwg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langgraph/agentic-rag\",\"https://docs.langchain.com/oss/python/langchain/retrieval\"]"
---

**TL;DR:** For multi-hop questions, make retrieval a node in a LangGraph instead of a fixed pipeline step: analyze the query, retrieve, decide whether to retrieve again or generate. The docs' agentic RAG guide is the reference implementation. Query analysis node: the model rewrites or decomposes the user question into retrieval queries.

## The fix

1. Query analysis node: the model rewrites or decomposes the user question into retrieval queries.

2. Retrieval node: run the queries against the vector store.

3. Decision: grade the retrieved documents. Good enough -> generate. Not enough -> rewrite the query and retrieve again (bounded; do not loop forever).

4. Generation node: answer from the retrieved context, citing it.

5. Bound the retrieve-retry loop with a counter in state. Unbounded re-retrieval is the agentic-RAG version of an infinite loop; GRAPH_RECURSION_LIMIT will eventually catch it, but your budget catches it first.

6. Grade documents with a cheap model or a rubric, not the big generator. Retrieval grading is a classification task.

7. Keep the 2-step RAG as your baseline and eval both on the same dataset. Agentic RAG wins on multi-hop and loses on latency and cost; prove the tradeoff is worth it before shipping.

8. Stream with `stream_mode="updates"` so the UI can show "searching..." states per node; token streaming alone hides the retrieval work.

## When to use this

- This covers exactly what the title says: Agentic RAG with LangGraph.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Agentic; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_flOeRia-iQYJstFxl6Xpwg). Version: `skv_U0DsrO_UP0gdssnAhgAdMw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
