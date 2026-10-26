---
name: "interrupt-works-the-first-time-but-doe-e2acdf8938d81583"
description: "Fixes LangGraph interrupt() silently not waiting for input on the second run. Use when the first interrupt works but the second invoke breezes past the interrupt node. Fixed in langgraph 0.2.63; older versions need the upgrade. Not for interrupts that never fire at all."
metadata:
  skill_id: "skl_VWMLrYjV6lbQTRJeIfmUgw"
  title: "interrupt() works the first time but does not wait for input on the second run"
  version: "skv_4qVxAx8PUVthXYEtM2LhjA"
  updated: "2026-10-03T04:39:34.03774+00:00"
  canonical_url: "https://vectle.com/skills/skl_VWMLrYjV6lbQTRJeIfmUgw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/3072\"]"
---

# interrupt() works the first time but does not wait for user input on the second run

TL;DR: this is a LangGraph bug fixed in 0.2.63. Upgrade with `pip install -U "langgraph>=0.2.63"` and the second interrupt pauses correctly. No code change needed. If you are already past 0.2.63 and still see it, your resume call is probably not carrying the same thread_id.

```text
# no error is raised. the symptom: the second graph.invoke() sails straight
# past interrupt() instead of pausing, so your human-in-the-loop step is skipped.
```

## When this applies

- `interrupt()` inside a node or tool pauses correctly the FIRST time.
- You resume with `Command(resume=...)`, the run finishes, and the NEXT invoke with a new input skips the interrupt entirely.
- You are on langgraph below 0.2.63.

## When it does not

- If interrupt never pauses even the first time, you are probably missing a checkpointer (interrupts need one to persist the pause).
- If resume throws, check that you pass the same `thread_id` in the config.

## Fix it

### 1. Upgrade langgraph

```python
# terminal
pip install -U "langgraph>=0.2.63"
```

Expected: the reported repro now pauses at `interrupt()` on every run, not just the first. The reporter confirmed the fix on 0.2.63 with no code changes.

### 2. Keep the thread_id stable across resume

```python
config = {"configurable": {"thread_id": "user-1"}}

# first run: pauses at interrupt()
result = graph.invoke({"messages": [...]}, config)

# resume with the SAME config
result = graph.invoke(Command(resume="approved"), config)
```

Expected: `graph.get_state(config).next` shows the interrupt node pending before resume, and empty after.

### 3. Verify the pause actually happened

```python
snapshot = graph.get_state(config)
print(snapshot.next)  # should list the node containing interrupt(), e.g. ('book_appointment',)
print(snapshot.tasks[0].interrupts)  # the Interrupt objects waiting for a resume value
```

Expected: `next` is non-empty while paused. If it is empty, the graph did not pause and your resume value will be ignored.

## Why it happens

Interrupts persist their paused state in the checkpointer keyed by thread. The pre-0.2.63 bug mishandled the checkpoint bookkeeping when a thread went through interrupt, resume, and then a second interrupt in a later run, so the second pause was never registered. The 0.2.63 release fixed the resume bookkeeping.

## Edge cases

- `interrupt()` inside a TOOL (with `InjectedToolCallId`) had the same bug; same fix.
- After upgrading, old checkpoints written by the buggy version can still misbehave. Start a fresh thread_id to confirm the fix, then migrate.
- If you pin langgraph in a lockfile, bump the pin: the fix is not in 0.2.62 or earlier.
- JS users: the equivalent fix landed in the @langchain/langgraph 0.2.x line around the same time; check your changelog.

## Compatibility

langgraph Python 0.2.63+ (fixed). Affects 0.2.x below 0.2.63. If you are on 1.x you already have the fix.

---

Source: [Vectle](https://vectle.com/skills/skl_VWMLrYjV6lbQTRJeIfmUgw). Version: `skv_4qVxAx8PUVthXYEtM2LhjA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
