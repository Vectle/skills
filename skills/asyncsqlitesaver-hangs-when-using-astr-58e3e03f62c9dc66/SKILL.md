---
name: "asyncsqlitesaver-hangs-when-using-astr-58e3e03f62c9dc66"
description: "Fixes LangGraph's AsyncSqliteSaver hanging forever when streaming with astream_events. Use when astream_events never yields and never returns and you compiled the graph with AsyncSqliteSaver. Fixed by using the saver as an async context manager so its connection closes cleanly. Not for MemorySaver or Postgres hangs."
metadata:
  skill_id: "skl_kHDLcvxi-t0WFQj3zs7sAg"
  title: "AsyncSqliteSaver hangs when using astream_events"
  version: "skv_7EVvUnXzNjBerqebXDMgBA"
  updated: "2026-10-03T04:41:55.840186+00:00"
  canonical_url: "https://vectle.com/skills/skl_kHDLcvxi-t0WFQj3zs7sAg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/789\"]"
---

# AsyncSqliteSaver hangs when using astream_events

TL;DR: `AsyncSqliteSaver` holds its database connection open, and `astream_events` waits on it forever. Use the saver as an async context manager and the hang goes away. Nothing is wrong with your graph.

```text
# no error, no traceback. the symptom: this loop never prints anything and never exits:
async for event in graph.astream_events(10, config, version="v1"):
    print(event)
```

## When this applies

- You compiled with `checkpointer=AsyncSqliteSaver...` (not MemorySaver, not Postgres).
- `invoke()` or `stream()` works, but `astream_events()` hangs.
- Killing the process is the only way out.

## When it does not

- If `astream_events` hangs with MemorySaver, the graph itself is stuck (check for an infinite loop, or a node awaiting something that never resolves).
- If it hangs on Postgres, that is a connection-pool issue, not this.

## Fix it

### 1. Use the saver as an async context manager

```python
from langgraph.checkpoint.aiosqlite import AsyncSqliteSaver

async with AsyncSqliteSaver.from_conn_string(":memory:") as saver:
    graph = builder.compile(checkpointer=saver)
    config = {"configurable": {"thread_id": "thread-1"}}
    async for event in graph.astream_events(10, config, version="v1"):
        print(event)
# connection closes here, at the end of the block
```

Expected: events stream normally and the block exits. The context manager closes the connection, which is what the event loop was waiting on.

### 2. For a file-backed database, same pattern

```python
async with AsyncSqliteSaver.from_conn_string("checkpoints.db") as saver:
    graph = builder.compile(checkpointer=saver)
    ...
```

Expected: checkpoints persist to `checkpoints.db` and the process exits cleanly.

### 3. In a long-lived app, do not compile per request

If you need one graph for the whole app lifetime (a web server, a bot), create the saver once at startup inside a lifespan handler and close it at shutdown, instead of compiling inside each request handler.

## Why it happens

`AsyncSqliteSaver` opens a real sqlite connection in async mode. `astream_events` drives the graph through async generators, and the open connection keeps the event loop's cleanup from completing, so the stream never terminates. The sync `SqliteSaver` and the in-memory saver do not hold the loop this way, which is why only the async sqlite saver hangs.

## Edge cases

- `:memory:` databases vanish when the context manager exits. If you need persistence across restarts, use a file path.
- Mixing sync and async savers on the same file can corrupt it. Pick one.
- If you must manage the connection yourself, call the saver's close/aclose explicitly when you are done streaming. The context manager is just the tidy way.

## Compatibility

langgraph 0.0.x through 1.x (Python), `langgraph-checkpoint-sqlite` package. The `async with` pattern is the documented usage.

---

Source: [Vectle](https://vectle.com/skills/skl_kHDLcvxi-t0WFQj3zs7sAg). Version: `skv_7EVvUnXzNjBerqebXDMgBA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
