---
name: "invalidupdateerror-invalid-update-for-9d3ade3d7d69c07a"
description: "Fixes LangGraph's \"Invalid update for channel\" error when a node writes a value the channel cannot accept. Use when the error names a custom channel (not messages) and lists the rejected values. Not for the \"must write to at least one of\" variant or reducer collisions."
metadata:
  skill_id: "skl_w35S9HLOGmSqNzcrl_UkxA"
  title: "InvalidUpdateError: Invalid update for channel 'medical' with values"
  version: "skv_zPTYKBatRJE1m6Pn5EyPww"
  updated: "2026-10-03T04:38:22.294426+00:00"
  canonical_url: "https://vectle.com/skills/skl_w35S9HLOGmSqNzcrl_UkxA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# InvalidUpdateError: Invalid update for channel 'medical' with values

TL;DR: your node returned a value for a channel, and the channel rejected it. Either the value's type does not match the channel, or two nodes wrote to the channel in the same step without a reducer. Rename or reshape the write so it matches the channel definition, or add a reducer if multiple nodes legitimately write it.

```text
langgraph.errors.InvalidUpdateError: Invalid update for channel medical with values ['...']
```

(The channel name in your error will be your own key, not `medical`. The cause and fix are the same.)

## When this applies

- The error names one of YOUR state keys and shows the rejected values.
- The node that wrote it ran fine in isolation; the failure only happens in the full graph.

## When it does not

- `At key 'x': Can receive only one value per step` means two writers, one step. Related but different fix (reducer).
- `Must write to at least one of [...]` means the node wrote to an unknown key. Different fix (channel name mismatch).

## Fix it

### 1. Check what the node actually returned

Add a print at the end of the failing node:

```python
def medical_mentor(state):
    result = {...}  # whatever you compute
    print("writing:", result)
    return {"medical": result}
```

Expected: you see the exact value LangGraph rejected. Compare it against the channel's declared type in your `TypedDict`.

### 2. Match the write to the channel type

```python
class State(TypedDict):
    medical: str          # channel expects a string

# node must return a string, not a dict:
def medical_mentor(state):
    return {"medical": "approved"}   # not {"medical": {"status": "approved"}}
```

Expected: the write matches the declared type, the channel accepts it.

### 3. If two nodes write the channel, add a reducer

```python
from typing import Annotated

def last_write(a, b):
    return b

class State(TypedDict):
    medical: Annotated[str, last_write]
```

Expected: concurrent writes merge by your rule instead of raising.

### 4. Check for a stale channel name

If you renamed a state key but a node still returns the old name, you get this error instead of the "must write to at least one of" error when the old name collides with another channel. Search every node for the old key.

## Why it happens

Channels are typed. A `LastValue` channel (the default) accepts a single value matching its type per step; a reducer channel applies your merge function. When a node returns something the channel cannot hold, or two nodes race the same channel, LangGraph raises instead of silently corrupting state. The error shows you the rejected values so you can see the mismatch.

## Edge cases

- Values that print as `[[object ...]]` usually mean you returned a non-serializable object (a class instance) where the channel expects plain data. Convert to dict/str first.
- With a checkpointer, the rejected write never persists: the checkpoint from the previous good step is still intact, so you can fix the node and re-run.
- `None` writes are rejected by most channels. Return the key with a real value or omit the key.

## Compatibility

langgraph 0.2.x and 1.x (Python).

---

Source: [Vectle](https://vectle.com/skills/skl_w35S9HLOGmSqNzcrl_UkxA). Version: `skv_zPTYKBatRJE1m6Pn5EyPww`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
