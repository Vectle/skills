---
name: "invalidupdateerror-at-key-messages-can-02423c78b8494f7f"
description: "Fixes LangGraph's InvalidUpdateError when two parallel nodes write to the same state channel without a reducer. Use when you see \"At key 'messages': Can receive only one value per step\" after fanning out to parallel nodes. Not for single-node writes or checkpoint errors."
metadata:
  skill_id: "skl_FXo-Q87F9SApKl7R5LhiIg"
  title: "InvalidUpdateError: At key 'messages': Can receive only one value per step"
  version: "skv_EX2VC80o6GGETicDcVdcLw"
  updated: "2026-10-03T04:37:07.387148+00:00"
  canonical_url: "https://vectle.com/skills/skl_FXo-Q87F9SApKl7R5LhiIg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/142\"]"
---

# InvalidUpdateError: At key 'messages': Can receive only one value per step

TL;DR: two nodes in the same step both wrote to `messages` and the channel has no reducer, so LangGraph does not know how to combine them. Declare the channel with a reducer, e.g. `Annotated[list, operator.add]`, and the error goes away. If the nodes run in parallel and feed one downstream node, a reducer is required, not optional.

```text
langgraph.errors.InvalidUpdateError: At key 'messages': Can receive only one value per step.
```

## When this applies

- The error names a specific key: `'messages'`, `'plan'`, `'summary'`, whatever channel two nodes both wrote.
- You have parallel nodes (fan-out) or two edges into one node, and each node returns a dict containing the same key.

## When it does not

- `InvalidUpdateError: Must write to at least one of [...]` is the sibling error for writing to NO known channel. Different fix.
- If only one node writes the key, the bug is elsewhere: check for duplicate edges.

## Fix it

### 1. Add a reducer to the channel

```python
import operator
from typing import Annotated
from typing_extensions import TypedDict

class State(TypedDict):
    messages: Annotated[list, operator.add]  # combine writes by concatenation
```

Expected: both nodes' writes merge instead of colliding. `operator.add` appends the second node's list to the first's.

For non-list channels, write a tiny reducer that picks a winner:

```python
from typing import Any

def keep_first(a: Any, b: Any) -> Any:
    return a

class State(TypedDict):
    short_context: Annotated[Any, keep_first]
```

Expected: parallel writes resolve to the first value, no error.

### 2. Watch the argument order

In the reducer `f(x, y)`, `x` is the existing value and `y` is the new write. Reporters found that sometimes the start node's value arrives as `y` instead of `x`, so a defensive reducer looks like this:

```python
def keep_either(a: Any, b: Any) -> Any:
    return a or b
```

Expected: whichever side has a value wins, regardless of arrival order.

### 3. Or stop writing the same key from both nodes

If the two nodes are really producing different things, give them different keys and merge in the downstream node:

```python
def downstream(state: State):
    combined = state["draft_a"] + state["draft_b"]
    return {"result": combined}
```

Expected: no shared channel, no collision, no reducer needed.

## Why it happens

A LangGraph channel holds one value per step unless you tell it how to merge. When two nodes run in the same super-step and both return `{"messages": ...}`, the channel gets two values and raises instead of guessing. A reducer is the explicit merge rule. The default (no reducer) means "overwrite", which is only safe with a single writer.

## Edge cases

- `add_messages` (from `langgraph.graph`) is the standard reducer for message lists: it appends and dedupes by id.
- Dict channels need a dict-merging reducer; the default overwrite silently drops one writer's keys even when it does not error.
- This also bites subgraphs: two parallel subgraphs writing the same parent key need a reducer on the parent channel.
- Conditional edges do not cause this (only one branch runs), but parallel edges from one node to two nodes that both write back do.

## Compatibility

langgraph 0.0.x through 1.x (Python). The `Annotated[..., reducer]` syntax is stable across all of them.

---

Source: [Vectle](https://vectle.com/skills/skl_FXo-Q87F9SApKl7R5LhiIg). Version: `skv_EX2VC80o6GGETicDcVdcLw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
