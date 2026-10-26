---
name: "how-to-delete-a-thread-with-memorysave-47e3681e36db898d"
description: "Shows how to delete a LangGraph thread when using MemorySaver. Use when a chat session ends and you want its checkpoint history gone. There is no built-in delete; the verified workaround writes an empty checkpoint over the thread. Not for Postgres or SQLite savers, which have their own delete paths."
metadata:
  skill_id: "skl_5UoNfx2zWxNIn0bzbjvqnA"
  title: "How to delete a thread with MemorySaver in LangGraph"
  version: "skv_85hKuRyT4Ewq6Kv9lQ8fTQ"
  updated: "2026-10-03T04:47:40.238871+00:00"
  canonical_url: "https://vectle.com/skills/skl_5UoNfx2zWxNIn0bzbjvqnA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/79687931/how-to-delete-a-thread-with-memorysaver\"]"
---

# How to delete a thread with MemorySaver in LangGraph

TL;DR: there is no built-in delete. Write an empty checkpoint over the thread with `checkpointer.put(config, empty_checkpoint, {}, {})` and the thread reads back blank. Keep a reference to your checkpointer (not just the compiled graph) so you can do this.

```text
# no error. the problem: MemorySaver has no delete_thread() method,
# so finished sessions keep their checkpoint history forever.
```

## When this applies

- You use `MemorySaver` (or `InMemorySaver`) as the checkpointer.
- A session/thread ended and you want its state gone (privacy, memory, clean slate).

## When it does not

- Postgres/SQLite savers: delete the thread's rows from the checkpoints tables instead.
- If you just want a fresh conversation, start a new `thread_id`. That is simpler and always works.

## Fix it

### 1. Keep the checkpointer reference

```python
from langgraph.checkpoint.memory import MemorySaver

saver = MemorySaver()  # keep this, not just `graph`
graph = builder.compile(checkpointer=saver)
```

Expected: you can call `saver.put(...)` later. If you only kept `graph`, reach it via `graph.checkpointer` where available.

### 2. Write an empty checkpoint over the thread

```python
import uuid
from datetime import datetime, timezone

def clear_thread(checkpointer, thread_id: str):
    config = {"configurable": {"thread_id": thread_id, "checkpoint_ns": ""}}
    empty = {
        "v": 1,
        "ts": datetime.now(timezone.utc).isoformat(),
        "id": str(uuid.uuid4()),
        "channel_values": {},
        "channel_versions": {"__start__": 1},
        "versions_seen": {"__input__": {}, "__start__": {}},
        "pending_sends": [],
    }
    checkpointer.put(config, empty, {}, {})

clear_thread(saver, "session-123")
```

Expected: `graph.get_state({"configurable": {"thread_id": "session-123"}})` now returns empty values. The thread is effectively deleted.

### 3. Confirm it is gone

```python
state = graph.get_state({"configurable": {"thread_id": "session-123"}})
print(state.values)  # {} -- blank
```

Expected: empty values. History for that thread_id reads back blank from here on.

## Why it happens

`MemorySaver` is a plain in-memory dict of checkpoints with no delete API. Overwriting the thread's latest checkpoint with an empty one is the community-verified workaround: every read (`get_state`, `get_state_history`) resolves through the latest checkpoint, so a blank head means a blank thread.

## Edge cases

- Old checkpoint versions for the thread may still sit in the saver's dict until the process restarts. For true erasure (compliance), drop the whole saver or filter its storage.
- `InMemorySaver` (1.x) has the same shape; the same workaround applies.
- Subgraph namespaces: if the thread used subgraphs, clear each `checkpoint_ns` too, or stale sub-states linger.
- In production, prefer per-session processes or a real database saver with row deletes over this trick.

## Compatibility

langgraph 0.x (`MemorySaver` from `langgraph.checkpoint.memory`) and 1.x (`InMemorySaver`). Python and the equivalent JS `MemorySaver` accept the same empty-checkpoint shape.

---

Source: [Vectle](https://vectle.com/skills/skl_5UoNfx2zWxNIn0bzbjvqnA). Version: `skv_85hKuRyT4Ewq6Kv9lQ8fTQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
