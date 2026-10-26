---
name: "migrate-a-legacy-chain-pipeline-to-a-l-0ab34113a4a8ba06"
description: "Sequential LLMChain-style pipelines become StateGraph nodes with typed state. Each chain step is a node, the state schema replaces the implicit dict passing, and conditional edges replace the branching logic people used to hide in callbacks. Not the full reference manual."
metadata:
  skill_id: "skl_qXWDAjqlyav9bgj6W3-uEQ"
  title: "Migrate a legacy chain pipeline to a LangGraph state machine"
  version: "skv_SBKwFse0OGjiPo65js_40Q"
  updated: "2026-10-03T14:00:58.778171+00:00"
  canonical_url: "https://vectle.com/skills/skl_qXWDAjqlyav9bgj6W3-uEQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langgraph/graph-api\",\"https://docs.langchain.com/oss/python/langgraph/use-graph-api\"]"
---

**TL;DR:** Sequential LLMChain-style pipelines become StateGraph nodes with typed state. Each chain step is a node, the state schema replaces the implicit dict passing, and conditional edges replace the branching logic people used to hide in callbacks.

# Chain to graph migration

## The mapping

- Each chain step -> one node function that takes state and returns a dict of state updates.
- The implicit dict passed between chains -> an explicit TypedDict state schema.
- Branching inside chain code -> conditional edges.
- `LLMChain` internals (prompt + model + parser) -> LCEL inside the node (`prompt | model | parser`), or a model call plus parsing code.

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    topic: str
    draft: str
    approved: bool

def write(state: State):
    return {"draft": model.invoke(f"Write about {state['topic']}").content}

def review(state: State):
    ...

builder = StateGraph(State)
builder.add_node("write", write)
builder.add_node("review", review)
builder.add_edge(START, "write")
builder.add_edge("write", "review")
builder.add_conditional_edges("review", lambda s: "write" if not s["approved"] else END)
graph = builder.compile(checkpointer=checkpointer)
```

## Rules

- Nodes return dicts on every path. See the InvalidUpdateError diagnostic.
- Add the checkpointer at compile time if any step needs retries, human approval, or time travel. Retrofitting persistence later means touching every invoke call site.
- Keep node functions small and single-purpose; a node that does three things is a chain hiding inside a graph.
- State keys written by parallel branches need reducers (`Annotated[list, operator.add]`). Design the schema before the edges.

## When to use this

- This covers exactly what the title says: Migrate a legacy chain pipeline to a LangGraph state machine.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Migrate; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Migrate behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_qXWDAjqlyav9bgj6W3-uEQ). Version: `skv_SBKwFse0OGjiPo65js_40Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
