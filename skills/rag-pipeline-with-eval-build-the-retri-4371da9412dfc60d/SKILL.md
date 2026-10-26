---
name: "rag-pipeline-with-eval-build-the-retri-4371da9412dfc60d"
description: "Build the RAG pipeline first (chunk, embed, retrieve, generate), then evaluate it for real: create a LangSmith dataset, run the evaluate function, and grade trajectories with the agentevals package. Ship no RAG you have not measured."
metadata:
  skill_id: "skl_5M-Nm2MpG3oJs4gsfmgWZg"
  title: "RAG pipeline with eval: build the retriever, then grade it in LangSmith"
  version: "skv_c5Q7ikz3omgUhSLJZUNrPA"
  updated: "2026-10-03T06:07:10.870206+00:00"
  canonical_url: "https://vectle.com/skills/skl_5M-Nm2MpG3oJs4gsfmgWZg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/retrieval\",\"https://docs.langchain.com/oss/python/langchain/test/evals\"]"
---

**TL;DR:** Build the RAG pipeline first (chunk, embed, retrieve, generate), then evaluate it for real: create a LangSmith dataset, run the evaluate function, and grade trajectories with the agentevals package. Ship no RAG you have not measured. Build the pipeline The docs' retrieval guide structures RAG as: build a knowledge base (chunk + embed + store), retrieve per query, generate with the retrieved context. Start with 2-step.

# RAG with eval

## 1. Build the pipeline

The docs' retrieval guide structures RAG as: build a knowledge base (chunk + embed + store), retrieve per query, generate with the retrieved context. Two architectures to choose from:

- 2-step RAG: retrieve once, then generate. Simple, predictable.
- Agentic RAG: the agent decides when and what to retrieve, possibly multiple times. Better for multi-hop questions, harder to evaluate.

Start with 2-step. Move to agentic only when single retrieval demonstrably fails.

## 2. Create a LangSmith dataset

Put your eval questions (and expected answers / reference trajectories) in a LangSmith dataset. The dataset schema is: inputs plus reference outputs.

## 3. Run evaluate

Use the `evaluate` function against the dataset. LangSmith also offers a pytest integration if you want evals in CI.

## 4. Grade with agentevals

The `agentevals` package gives you prebuilt evaluators:

- Trajectory match: deterministic comparison of the agent's tool-call trajectory against a reference.
- Trajectory LLM-as-judge (`create_trajectory_llm_as_judge`): qualitative grading of the execution path, no reference trajectory required.

## Rules

- Evaluate the retriever separately from the generator. If retrieval is bad, no generator prompt will save it; if retrieval is good and answers are bad, the problem is generation.
- Keep the eval dataset versioned and growing: every production failure becomes a new eval case.
- Re-run evals after any change to chunking, embeddings, the model, or the prompt. RAG quality is a system property, not a model property.

## When to use this

- This covers exactly what the title says: RAG pipeline with eval.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with RAG; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_5M-Nm2MpG3oJs4gsfmgWZg). Version: `skv_c5Q7ikz3omgUhSLJZUNrPA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
