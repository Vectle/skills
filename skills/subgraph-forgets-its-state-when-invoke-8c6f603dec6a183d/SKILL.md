---
name: "subgraph-forgets-its-state-when-invoke-8c6f603dec6a183d"
description: "Fixes LangGraph subgraphs that lose their state when a parent graph invokes them a second time. Use when a nested subgraph remembers state on the first call but starts blank on later calls in the same parent run. Fixed by wrapping the subgraph call in a node function. Not for parent-graph state issues."
metadata:
  skill_id: "skl_BbeXoBX1PONY7on0kXlgFg"
  title: "Subgraph forgets its state when invoked a second time in the parent graph"
  version: "skv_Fb1RNXDYaGy2bzqGppWdDA"
  updated: "2026-10-03T04:40:44.997911+00:00"
  canonical_url: "https://vectle.com/skills/skl_BbeXoBX1PONY7on0kXlgFg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/3020\"]"
---

# Subgraph forgets its state when the parent graph invokes it a second time

TL;DR: do not wire a compiled subgraph directly as a node when the parent calls it repeatedly. Wrap it in a node function that invokes the subgraph, and its state persists across calls. Direct wiring can cause the subgraph to run once and then silently reuse stale or empty state.

```text
# no exception. the symptom: print() inside the subgraph node fires once,
# but the parent routes to the subgraph three times. the second and third
# visits see empty state instead of the accumulated state from run one.
```

## When this applies

- A parent graph calls the same subgraph node more than once (loop, follow-up questions, retries).
- First visit works; later visits act like a fresh subgraph.
- A debug print inside the subgraph confirms it only executed once.

## When it does not

- If the PARENT loses state between separate `invoke()` calls, that is a checkpointer/thread_id issue, not this.
- If the subgraph errors, look at the actual exception instead.

## Fix it

### 1. Wrap the subgraph in a node function

```python
# instead of: parent.add_node("agent", subgraph)
# do this:

def agent_node(state: ParentState):
    # invoke the compiled subgraph fresh each time the parent visits this node
    return subgraph.invoke({"messages": state["messages"]})

parent.add_node("agent", agent_node)
```

Expected: your debug print inside the subgraph now fires on every visit, and state accumulates across visits.

### 2. Pass state in explicitly, read it back explicitly

```python
def agent_node(state: ParentState):
    result = subgraph.invoke({
        "messages": state["messages"],
        "subgraph_state": state.get("subgraph_state"),
    })
    return {"messages": result["messages"]}
```

Expected: the parent only keeps the keys it declares; the subgraph keeps its own. Nothing leaks or gets silently dropped.

### 3. Give the subgraph its own thread namespace if it has a checkpointer

If both parent and subgraph use checkpointers, the subgraph's checkpoints live under a namespace. When invoking manually, keep the namespace stable so the subgraph resumes instead of restarting:

```python
def agent_node(state: ParentState, config):
    sub_config = {"configurable": {"thread_id": config["configurable"]["thread_id"]}}
    return subgraph.invoke({"messages": state["messages"]}, sub_config)
```

Expected: `subgraph.get_state(sub_config)` shows history across parent visits.

## Why it happens

A compiled subgraph used directly as a node is treated as a single node by the parent's Pregel loop. Its internal super-steps are managed by the parent, and on repeat visits the parent may not re-enter the subgraph's own loop the way a fresh `invoke()` would. A wrapper node function makes each visit a genuine fresh invocation with its own state lifecycle.

## Edge cases

- Streaming: with the wrapper, use `subgraph.stream()` inside the node and forward events if the parent needs them.
- Interrupts inside the subgraph still work, but the interrupt surfaces at the wrapper node. Resume with the parent's config as usual.
- Performance: each visit re-enters the subgraph from its entry point. If you need the subgraph to continue mid-loop across visits, keep its checkpointer and pass the same thread config.

## Compatibility

langgraph 0.2.x and 1.x (Python). The pattern (node function wrapping `subgraph.invoke`) works in all versions.

---

Source: [Vectle](https://vectle.com/skills/skl_BbeXoBX1PONY7on0kXlgFg). Version: `skv_Fb1RNXDYaGy2bzqGppWdDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
