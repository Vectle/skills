---
name: "langgraph-conditional-edge-to-end-does-259f6e926a4c5052"
description: "Fixes a LangGraph graph that keeps looping through a node even when the conditional edge should route to END. Use when should_continue returns \"END\" but execution continues. Usually a stray unconditional edge or a router returning \"END.\" instead of \"END\". Not for recursion-limit errors from genuine loops."
metadata:
  skill_id: "skl_XR-BgqNzEp2TvHAvs3lgYQ"
  title: "LangGraph conditional edge to END does not stop execution"
  version: "skv_2X854shFxRXjDXmXzslIiw"
  updated: "2026-10-03T04:46:30.961843+00:00"
  canonical_url: "https://vectle.com/skills/skl_XR-BgqNzEp2TvHAvs3lgYQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/78924708/langgraph-conditional-end-state-fails-to-stop-execution\"]"
---

# LangGraph conditional edge to END does not stop execution

TL;DR: if your graph keeps looping after the router says END, you almost certainly have BOTH an unconditional edge and a conditional edge leaving the same node. The unconditional edge always wins. Delete it and let the conditional edge decide. Also check you return exactly `"END"`, not `"END."`.

```text
# no exception. the symptom: should_continue returns "END" but the graph
# loops back through the generate node instead of stopping.
```

## When this applies

- A conditional edge maps some return value to `END`.
- Execution continues past it anyway, usually looping one more node.
- The router function itself returns the right value (verify with a print).

## When it does not

- `GraphRecursionError` after many loops means the router genuinely never returns END. Different problem.
- If the router raises, fix the router.

## Fix it

### 1. Remove the competing unconditional edge

```python
# wrong: this edge ALWAYS runs, so the conditional edge below never matters
graph.add_edge("eval", "generate")
graph.add_conditional_edges("eval", should_continue, {"CONTINUE": "generate", "END": END})

# right: only the conditional edge leaves "eval"
graph.add_conditional_edges("eval", should_continue, {"CONTINUE": "generate", "END": END})
```

Expected: when `should_continue` returns `"END"`, the run stops. When it returns `"CONTINUE"`, it goes to `generate`.

### 2. Return exactly "END", not "END."

```python
def should_continue(state):
    if state["done"]:
        return "END"   # not "END." -- the period makes it a different node name
    return "CONTINUE"
```

Expected: the mapping key matches and routes to END. `"END."` matches nothing and (depending on version) either errors or falls through.

### 3. Verify with a print

```python
def should_continue(state):
    decision = "END" if state["done"] else "CONTINUE"
    print("routing:", repr(decision))
    return decision
```

Expected: you see `'END'` (with quotes, no period) on the final step, and the run stops right after.

## Why it happens

Edges out of a node ALL fire unless they are conditional. An unconditional `add_edge("eval", "generate")` plus a conditional edge from `"eval"` means `generate` runs every time AND the conditional branch runs: the graph does both. Newcomers add the unconditional edge first (from a tutorial) and then add the conditional edge without removing it.

## Edge cases

- With `interrupt_before`/`interrupt_after` on the same node, the interrupt fires but the extra edge still routes afterward. Clean the edges first.
- Returning `END` (the constant) vs `"END"` (the string): both work in `add_conditional_edges` mappings, but be consistent. Mixing them across the router and the mapping is a classic miss.
- If two conditional edges leave the same node, both are evaluated. That is legal but confusing; prefer one router.

## Compatibility

All langgraph Python versions, 0.x and 1.x.

---

Source: [Vectle](https://vectle.com/skills/skl_XR-BgqNzEp2TvHAvs3lgYQ). Version: `skv_2X854shFxRXjDXmXzslIiw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
