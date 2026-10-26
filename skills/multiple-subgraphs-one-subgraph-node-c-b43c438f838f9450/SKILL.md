---
name: "multiple-subgraphs-one-subgraph-node-c-b43c438f838f9450"
description: "A subgraph compiled with checkpointer=True (continuations mode) cannot be called multiple times inside one node. Pick the checkpointer mode that matches what you actually need. Not the full reference manual."
metadata:
  skill_id: "skl_6rAjT5zl2pCF492YbD0VyQ"
  title: "MULTIPLE_SUBGRAPHS: one subgraph node called repeatedly with checkpointer=True"
  version: "skv_e2YUk00QH9i8XkDXyT29mQ"
  updated: "2026-10-03T15:20:05.507826+00:00"
  canonical_url: "https://vectle.com/skills/skl_6rAjT5zl2pCF492YbD0VyQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langgraph/errors/MULTIPLE_SUBGRAPHS\"]"
---

**TL;DR:** A subgraph compiled with checkpointer=True (continuations mode) cannot be called multiple times inside one node. Pick the checkpointer mode that matches what you actually need. Read the subgraph persistence docs before choosing mode 3.

## The fix

1. No interrupts needed: opt out entirely.

2. Interrupts yes, cross-invocation persistence no: omit the checkpointer (inherited mode). Each invocation gets a unique namespace, parallel execution works, the subgraph starts fresh each time but `interrupt()` still works.

3. Cross-invocation persistence needed: keep `checkpointer=True`. LangGraph assigns position-based namespace suffixes (`calling_node`, `calling_node|1`, ...). For stable names, wrap each subgraph call in a uniquely named node.

## When to use this

- This covers exactly what the title says: MULTIPLE_SUBGRAPHS.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with MULTIPLE_SUBGRAPHS; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current MULTIPLE_SUBGRAPHS behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_6rAjT5zl2pCF492YbD0VyQ). Version: `skv_e2YUk00QH9i8XkDXyT29mQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
