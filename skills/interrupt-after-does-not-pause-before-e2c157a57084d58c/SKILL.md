---
name: "interrupt-after-does-not-pause-before-e2c157a57084d58c"
description: "Explains LangGraph's interrupt_after semantics: it fires after the node AND its outgoing edges run. Use when interrupt_after seems to trigger at the wrong time or your conditional edge runs before the pause. Fixed by switching to interrupt_before on an intermediate node. Not for interrupts that never fire."
metadata:
  skill_id: "skl_FOUG6EkPDJmUNLRKEBE8Ww"
  title: "interrupt_after does not pause before the conditional edge runs"
  version: "skv_iDAEscY-ue-A5zaDrlHn5g"
  updated: "2026-10-03T04:50:10.813222+00:00"
  canonical_url: "https://vectle.com/skills/skl_FOUG6EkPDJmUNLRKEBE8Ww"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# interrupt_after does not pause before the conditional edge runs

TL;DR: `interrupt_after=["my_node"]` pauses AFTER the node and all its outgoing edges (including conditional routers) have run. If you want the pause BEFORE the router decides, that is `interrupt_during`, which does not exist. Put an empty intermediate node after your node and use `interrupt_before` on that instead.

```text
# no exception. the symptom: with interrupt_after=["agent"], your conditional
# edge function still executes before anything pauses. the interrupt lands
# one step later than you expected.
```

## When this applies

- You set `interrupt_after` and the pause happens, but too late: the router already ran.
- You wanted a human to approve the ROUTING decision, not just the node output.

## When it does not

- If no interrupt fires at all, check you passed a checkpointer and the node name is exact.
- If resume does not work, check the thread_id is stable.

## Fix it

### 1. Add an intermediate node

```python
def placeholder(state):
    return {}  # does nothing, exists so we can pause before the router

builder.add_node("placeholder", placeholder)
builder.add_edge("agent", "placeholder")
builder.add_conditional_edges("placeholder", router, {"a": "node_a", "b": "node_b"})

graph = builder.compile(
    checkpointer=saver,
    interrupt_before=["placeholder"],
)
```

Expected: the graph pauses right after `agent` finishes and BEFORE `router` runs. The human approves, then the router decides.

### 2. Resume normally

```python
config = {"configurable": {"thread_id": "t1"}}
graph.invoke(input, config)                    # pauses at placeholder
snapshot = graph.get_state(config)
print(snapshot.next)                           # ('placeholder',)
graph.invoke(Command(resume="approved"), config)  # router runs now
```

Expected: `next` shows the placeholder while paused; after resume the router executes.

### 3. Keep interrupt_after for what it is good for

`interrupt_after` is the right tool when you want to review a node's OUTPUT before anything downstream sees it, and you do not care that the router ran. Do not fight its semantics; pick the option that matches your pause point.

## Why it happens

In Pregel, a node's outgoing edges are part of that node's super-step. `interrupt_after` inserts the pause at the end of the super-step, so every edge function already ran. There is no hook between "node finished" and "edges evaluated", hence the intermediate-node pattern.

## Edge cases

- The placeholder node must return `{}` (or a valid partial state). Returning `None` errors.
- With subgraphs, `interrupt_before` on the subgraph node pauses before the whole subgraph runs. To pause INSIDE it, put the interrupt config on the subgraph's own compile.
- `interrupt_before=[START]` pauses before anything runs: useful for approving the input itself.

## Compatibility

All langgraph Python versions with `interrupt_before` / `interrupt_after` (0.1.x+). Same semantics in the JS SDK.

---

Source: [Vectle](https://vectle.com/skills/skl_FOUG6EkPDJmUNLRKEBE8Ww). Version: `skv_iDAEscY-ue-A5zaDrlHn5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
