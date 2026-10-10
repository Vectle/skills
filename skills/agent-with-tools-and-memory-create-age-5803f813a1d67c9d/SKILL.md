---
name: "agent-with-tools-and-memory-create-age-5803f813a1d67c9d"
description: "Give a create_agent short-term memory by compiling it with a checkpointer and passing a thread_id per conversation. Tools can read and write that memory through ToolRuntime and Command. Not the full reference manual."
metadata:
  skill_id: "skl_GpBOzaS8NdbNZVgewuZvyw"
  title: "Agent with tools and memory: create_agent plus checkpointer and thread ids"
  version: "skv_OgRaaauGUYP9XkfOWvG8cA"
  updated: "2026-10-03T14:03:31.511325+00:00"
  canonical_url: "https://vectle.com/skills/skl_GpBOzaS8NdbNZVgewuZvyw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Give a create_agent short-term memory by compiling it with a checkpointer and passing a thread_id per conversation. Tools can read and write that memory through ToolRuntime and Command. Write memory from tools Tools receive a ToolRuntime and can return a Command that updates state: Rules - No checkpointer means no memory, even with a thread id.

# Agent with memory

## 1. Checkpointer

```python
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()
agent = create_agent(
    model="openai:gpt-5.5",
    tools=[...],
    checkpointer=checkpointer,
)
```

InMemorySaver is for dev. SqliteSaver (`langgraph-checkpoint-sqlite`) for local durable runs, PostgresSaver (`langgraph-checkpoint-postgres`) for production.

## 2. Thread ids

Every invoke or stream passes a thread id in the config. The thread is the conversation; same id resumes, new id starts fresh.

```python
config = {"configurable": {"thread_id": "user-123"}}
result = agent.invoke({"messages": [{"role": "user", "content": "Hi"}]}, config)
```

## 3. Custom state

Extend AgentState with a TypedDict for your own memory fields, and pass it as `state_schema`. Static per-run data goes through `context=` with `context_schema=`.

```python
class CustomState(AgentState):
    user_name: str
```

## 4. Write memory from tools

Tools receive a ToolRuntime and can return a Command that updates state:

```python
from langchain.tools import tool, ToolRuntime
from langgraph.types import Command
from langchain.messages import ToolMessage

@tool
def update_user_info(runtime: ToolRuntime) -> Command:
    # look up the user, then update state
    return Command(update={
        "user_name": "John Smith",
        "messages": [ToolMessage(content="updated", tool_call_id=runtime.tool_call_id)],
    })
```

## Rules

- No checkpointer means no memory, even with a thread id. Both are required.
- One thread id per conversation. Sharing a thread id across users mixes their histories.
- Prefer returning state updates from tools over stuffing everything into messages; messages are the expensive memory.

## When to use this

- This covers exactly what the title says: Agent with tools and memory.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Agent; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_GpBOzaS8NdbNZVgewuZvyw). Version: `skv_OgRaaauGUYP9XkfOWvG8cA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
