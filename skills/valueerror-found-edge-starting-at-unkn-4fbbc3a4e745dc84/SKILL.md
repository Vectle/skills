---
name: "valueerror-found-edge-starting-at-unkn-4fbbc3a4e745dc84"
description: "Explains LangGraph's \"Found edge starting at unknown node\" validation error. Use when graph.compile() or validate() raises it. It means an edge references a node name that was never added, usually a typo. Fix the name; every edge source must be a known node or START. Not for runtime routing errors."
metadata:
  skill_id: "skl_ACcaDWN3FVOJANdlwCOvWg"
  title: "ValueError: Found edge starting at unknown node"
  version: "skv_KU0OWMgkh_GSBsok5vMHgg"
  updated: "2026-10-03T04:44:15.614483+00:00"
  canonical_url: "https://vectle.com/skills/skl_ACcaDWN3FVOJANdlwCOvWg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/429\"]"
---

# ValueError: Found edge starting at unknown node

TL;DR: one of your edges names a node that does not exist, usually a typo. Compare every `add_edge` / `add_conditional_edges` source name against your `add_node` names character by character. The error fires at build/validate time, before anything runs.

```text
ValueError: Found edge starting at unknown node 'my_nod'
```

## When this applies

- Raised by `graph.compile()` or `builder.validate()`, not during a run.
- The quoted name is close to, but not exactly, one of your node names.

## When it does not

- Errors DURING a run about unknown nodes come from a router returning a bad name. Different fix.
- `InvalidUpdateError` is about state writes, not edges.

## Fix it

### 1. Diff the names

```python
builder.add_node("my_node", my_node_fn)
builder.add_edge("my_nod", "other_node")  # typo: 'my_nod' was never added
```

Fix the typo:

```python
builder.add_edge("my_node", "other_node")
```

Expected: `compile()` succeeds.

### 2. Check conditional edges too

```python
builder.add_conditional_edges(
    "router",
    lambda state: "summarize" if state["done"] else "research",
    {"summarize": "summarize", "research": "reserach"},  # typo in the mapping
)
```

Both the source (`"router"`) and every destination in the mapping must be added nodes (or `END`).

### 3. Remember the special names

`START` is valid as an edge source without being added. `END` is valid as a destination. Everything else must come from `add_node`.

```python
from langgraph.graph import START, END

builder.add_edge(START, "first")   # fine
builder.add_edge("last", END)      # fine
```

Expected: no validation error for the special nodes.

## Why it happens

LangGraph validates the whole edge list before compiling. Every edge source must resolve to a known node so the Pregel engine can schedule it. An unknown source means a node that could never be scheduled, so it fails fast with this error instead of hanging at runtime.

## Edge cases

- Renaming a node? Search for every string reference to the old name. Edges are plain strings, so no IDE refactor catches them.
- Node names are case-sensitive: `"Agent"` and `"agent"` are different nodes.
- In older langgraph versions the validation message itself had a bug (it printed the wrong variable); if the quoted name looks unrelated, upgrade and re-read the message.

## Compatibility

All langgraph Python versions. The validation exists in every 0.x and 1.x release.

---

Source: [Vectle](https://vectle.com/skills/skl_ACcaDWN3FVOJANdlwCOvWg). Version: `skv_KU0OWMgkh_GSBsok5vMHgg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
