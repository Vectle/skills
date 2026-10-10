---
name: "asyncpostgressaver-2-0-23-fails-to-rea-da3203e499d31935"
description: "Fixes LangGraph's AsyncPostgresSaver failing to read checkpoints with a NoneType error on version 2.0.23. Use when alist/get_tuple raises about NoneType not being a mapping on langgraph-checkpoint-postgres 2.0.23. Fixed in the next release; upgrade past 2.0.23. Not for connection or table-missing errors."
metadata:
  skill_id: "skl_MtXcQrgUHKW3g1SkX_EC4A"
  title: "AsyncPostgresSaver 2.0.23 fails to read channel values: NoneType not a mapping"
  version: "skv_FSpgx7WfosBeYQagz22Qpg"
  updated: "2026-10-03T04:43:04.730408+00:00"
  canonical_url: "https://vectle.com/skills/skl_MtXcQrgUHKW3g1SkX_EC4A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AsyncPostgresSaver 2.0.23 fails to read channel values: NoneType object is not a mapping

TL;DR: version 2.0.23 of `langgraph-checkpoint-postgres` shipped a bug in checkpoint reads. Upgrade the package and the error goes away. Your data is fine; the bug is in the read path, not the stored checkpoints.

```text
TypeError: NoneType object is not a mapping
# raised when reading checkpoints, e.g. checkpointer.alist(config) or
# checkpointer.aget_tuple(config), on langgraph-checkpoint-postgres 2.0.23
```

## When this applies

- `pip show langgraph-checkpoint-postgres` says 2.0.23.
- Writes succeed but READS fail: `get_state`, `get_state_history`, `alist` raise the NoneType error.
- Sync `PostgresSaver` on the same version may work while `AsyncPostgresSaver` fails.

## When it does not

- `Undefined table 'checkpoints'` means you never ran `setup()`. Different fix.
- Connection refused / timeout means the database is unreachable. Different fix.

## Fix it

### 1. Upgrade the checkpoint package

```python
# terminal
pip install -U "langgraph-checkpoint-postgres"
```

Then confirm:

```python
# terminal
pip show langgraph-checkpoint-postgres | grep Version
# expect anything newer than 2.0.23
```

Expected: reads work again with zero code changes. The stored checkpoints were never corrupted, so history comes back.

### 2. Verify the read path

```python
config = {"configurable": {"thread_id": "thread-1"}}
state = graph.get_state(config)
print(state.values.keys())  # your channels, not an exception
```

Expected: `get_state` returns the latest checkpoint instead of raising.

### 3. If you pin versions, bump the pin

If your lockfile pins `langgraph-checkpoint-postgres==2.0.23`, update the pin and redeploy. The bug is version-specific; staying pinned keeps you broken.

## Why it happens

The 2.0.23 release changed how channel values are deserialized on the async read path and mishandled a null case, so a perfectly good checkpoint row came back as `None` where a mapping was expected. The fix release restored the correct deserialization. Writes were unaffected the whole time.

## Edge cases

- If you ALSO see the error after upgrading, clear any cached/old package: `pip install --force-reinstall "langgraph-checkpoint-postgres"`.
- The sync saver and async saver are separate code paths; a version can be broken for one and fine for the other. Always check the exact package and class you use.
- Downgrading below 2.0.23 also avoids the bug, but upgrading is better: you keep the other fixes.

## Compatibility

`langgraph-checkpoint-postgres` 2.0.23 (broken) and the release that followed (fixed). Python only.

---

Source: [Vectle](https://vectle.com/skills/skl_MtXcQrgUHKW3g1SkX_EC4A). Version: `skv_FSpgx7WfosBeYQagz22Qpg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
