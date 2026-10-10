---
name: "how-to-resume-a-langgraph-stream-after-935a4f3cffdd7275"
description: "Shows how to resume a LangGraph stream after a custom human_assistance tool calls interrupt(). Use when your chatbot pauses for human input mid-stream and you need the stream to continue after the human answers. Requires a checkpointer; resume with Command(resume=...) on the same thread. Not for interrupts that never pause."
metadata:
  skill_id: "skl_NKJAevs-73K2LZPrvJcZvw"
  title: "How to resume a LangGraph stream after a human_assistance tool interrupt"
  version: "skv_P_PG6e2nvH6CmDYlYFL29g"
  updated: "2026-10-03T04:52:42.872096+00:00"
  canonical_url: "https://vectle.com/skills/skl_NKJAevs-73K2LZPrvJcZvw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to resume a LangGraph stream after a human_assistance tool interrupt

TL;DR: `interrupt()` needs a checkpointer to pause at all. Stream until the `__interrupt__` event appears, collect the human's answer outside the loop, then call `graph.stream(Command(resume=answer), same_config)` to continue. Same `thread_id`, no new input.

```python
from langgraph.types import interrupt, Command
from langgraph.checkpoint.memory import MemorySaver

@tool
def human_assistance(query: str) -> str:
    """Ask the human a question."""
    human_response = interrupt({"query": query})
    return human_response["data"]
```

## When this applies

- A tool or node calls `interrupt()` to ask the human something mid-run.
- You stream with `graph.stream(...)` and the stream stops at the interrupt.
- You want to feed the answer back and keep streaming.

## When it does not

- If the stream never pauses, you are missing a checkpointer: interrupts are silently skipped without one.
- If you are not streaming, the same pattern works with `graph.invoke`.

## Fix it

### 1. Compile WITH a checkpointer

```python
graph = builder.compile(checkpointer=MemorySaver())
config = {"configurable": {"thread_id": "chat-1"}}
```

Expected: without this, `interrupt()` does nothing and the tool hangs waiting for input that never comes.

### 2. Stream until the interrupt event

```python
for event in graph.stream({"messages": [("user", user_input)]}, config):
    if "__interrupt__" in event:
        question = event["__interrupt__"][0].value["query"]
        break
    for value in event.values():
        print("Assistant:", value["messages"][-1].content)
```

Expected: the loop breaks on the interrupt event instead of hanging. The question text is in the interrupt payload.

### 3. Resume the stream with the human's answer

```python
human_answer = input(f"Assistant needs input ({question}): ")

for event in graph.stream(Command(resume={"data": human_answer}), config):
    for value in event.values():
        if "messages" in value:
            print("Assistant:", value["messages"][-1].content)
```

Expected: the tool receives the answer as the return value of `interrupt()`, the graph continues, and the stream completes. Note: NO new input dict, and the SAME config/thread_id.

## Why it happens

`interrupt()` raises a special exception that Pregel catches, persists the paused state to the checkpointer, and surfaces as an `__interrupt__` event. Resuming means re-entering the graph at the paused point with `Command(resume=...)`: the value you pass becomes the return value of the `interrupt()` call. A new input dict would start a new run instead of continuing the paused one.

## Edge cases

- The resume value shape must match what your code expects: here the tool does `human_response["data"]`, so resume with `{"data": answer}`.
- Multiple interrupts in one run surface as a list in `event["__interrupt__"]`. Resume once with a matching structure.
- In a REPL loop, keep ONE config with a stable thread_id across turns, or each turn starts a fresh thread and interrupts never connect.
- `stream()` with `stream_mode="updates"` shows node outputs; the interrupt event appears in the default `values` mode as shown.

## Compatibility

langgraph 0.2.x and 1.x (Python). The `interrupt()` / `Command(resume=...)` API is stable across both.

---

Source: [Vectle](https://vectle.com/skills/skl_NKJAevs-73K2LZPrvJcZvw). Version: `skv_P_PG6e2nvH6CmDYlYFL29g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
