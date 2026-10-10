---
name: "send-objects-are-not-serializable-caus-987a8fd2078111f8"
description: "Fixes checkpointer failures in LangGraph map-reduce graphs where Send objects fail to serialize. Use when a graph using Send() for fan-out crashes on checkpoint writes with a serialization TypeError. Fixed in recent langgraph versions; upgrade. Not for unpicklable state values, which is a different cause."
metadata:
  skill_id: "skl_frLMZ29aZvNzf8LT3jqSvQ"
  title: "Send objects are not serializable, causing checkpointer failures"
  version: "skv_hFN7HBeJ8MQ76gst0o_wWA"
  updated: "2026-10-03T05:03:48.606339+00:00"
  canonical_url: "https://vectle.com/skills/skl_frLMZ29aZvNzf8LT3jqSvQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Send objects are not serializable, causing checkpointer failures

TL;DR: if your map-reduce graph (the one using `Send()`) crashes when writing checkpoints, upgrade langgraph. Older versions could not serialize `Send` objects into checkpoints; current versions can. Your graph code does not need to change.

```text
TypeError: ... is not serializable
# raised from the checkpointer (ormsgpack / JsonPlusSerializer path)
# when a Send object lands in pending_sends during a checkpoint write.
```

## When this applies

- You use `Send()` for map-reduce fan-out (`return [Send("worker", {...}) for ...]`).
- The graph runs fine WITHOUT a checkpointer but fails WITH one.
- The traceback points at serialization (ormsgpack, msgpack, JsonPlusSerializer) during a checkpoint write.

## When it does not

- `TypeError: cannot pickle 'X' object` about YOUR state values (an LLM client, a lock) means your state holds something unserializable. Remove it from state instead.
- If Send fails without any checkpointer, the bug is in your Send usage.

## Fix it

### 1. Upgrade langgraph

```python
# terminal
pip install -U langgraph
```

Expected: the same map-reduce graph now checkpoints cleanly. The issue reporter confirmed the failure was gone on the latest version with no code changes.

### 2. Confirm the version actually moved

```python
# terminal
pip show langgraph | grep Version
```

If you pin langgraph in a lockfile, bump the pin and redeploy. Editable installs and stale `.pyc` caches can shadow the upgrade: if the error persists after upgrading, reinstall cleanly.

### 3. Sanity-check the Send pattern itself

```python
from langgraph.types import Send

def fan_out(state):
    # Send takes a node name and the arg dict for that invocation
    return [Send("worker", {"item": item}) for item in state["items"]]
```

Expected: each Send routes one worker invocation. The serialization fix handles the rest.

## Why it happens

When a node returns `Send` objects, Pregel holds them in `pending_sends` until the target nodes run. With a checkpointer attached, that pending state gets serialized into the checkpoint. Older langgraph versions had no serializer registered for the `Send` type, so the write blew up. Newer versions serialize it like any other checkpoint payload.

## Edge cases

- The args you pass inside `Send("worker", {...})` must themselves be serializable. A dict of strings is fine; an open file handle is not.
- If you implement a CUSTOM serializer/serde, register `Send` handling there too, or writes fail the same way on your custom path.
- Deep-agent style frameworks built on langgraph hit this through the same code path; upgrading the underlying langgraph fixes them as well.

## Compatibility

langgraph Python. Broken: older 0.x/1.x versions (fixed in later releases). If you are current and still see it, check for a custom serde as above.

---

Source: [Vectle](https://vectle.com/skills/skl_frLMZ29aZvNzf8LT3jqSvQ). Version: `skv_hFN7HBeJ8MQ76gst0o_wWA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
