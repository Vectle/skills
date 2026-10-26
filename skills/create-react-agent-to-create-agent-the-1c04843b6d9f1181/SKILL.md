---
name: "create-react-agent-to-create-agent-the-1c04843b6d9f1181"
description: "LangChain v1 replaced langgraph.prebuilt.create_react_agent with langchain.agents.create_agent. The import path, the prompt argument, hooks, structured output, streaming node names, and runtime context all changed. This is the full mapping. Not the full reference manual."
metadata:
  skill_id: "skl_nCUO2GczwVQBjmrlWVT8EA"
  title: "create_react_agent to create_agent: the v1 migration checklist"
  version: "skv_oyr9k31Wnf-F1gErdRhY1g"
  updated: "2026-10-03T14:41:25.176702+00:00"
  canonical_url: "https://vectle.com/skills/skl_nCUO2GczwVQBjmrlWVT8EA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/migrate/langchain-v1\"]"
---

**TL;DR:** LangChain v1 replaced langgraph.prebuilt.create_react_agent with langchain.agents.create_agent. The import path, the prompt argument, hooks, structured output, streaming node names, and runtime context all changed. Use middleware: before_model, after_model, @wrap_model_call, @wrap_tool_call.

## The fix

**TL;DR:** LangChain v1 replaced langgraph.prebuilt.create_react_agent with langchain.agents.create_agent. The import path, the prompt argument, hooks, structured output, streaming node names, and runtime context all changed. create_react_agent -> create_agent The mapping - Import: langgraph.prebuilt.create_react_agent -> langchain.agents.create_agent - Prompt: prompt= is now system_prompt=, and it takes a plain string. Use middleware: before_model, after_model, @wrap_model_call, @wrap_tool_call.

# create_react_agent -> create_agent

```python
# old (v0)
from langgraph.prebuilt import create_react_agent
agent = create_react_agent(model="...", tools=[...], prompt="...")

# new (v1)
from langchain.agents import create_agent
agent = create_agent(model="...", tools=[...], system_prompt="...")
```

## The mapping

- Import: `langgraph.prebuilt.create_react_agent` -> `langchain.agents.create_agent`
- Prompt: `prompt=` is now `system_prompt=`, and it takes a plain string. If you passed a SystemMessage object, pull the string out of its content first.
- Hooks: `pre_model_hook=`, `post_model_hook=`, `state_modifier=` are gone. Use middleware: `before_model`, `after_model`, `@wrap_model_call`, `@wrap_tool_call`. Human approval of tool calls uses `HumanInTheLoopMiddleware(interrupt_on={...})` from `langchain.agents.middleware`.
- Structured output: keep `response_format=`, but build it with `ToolStrategy` or `ProviderStrategy` from `langchain.agents.structured_output`. The old prompted tuple form is removed.
- Streaming: the node name changed from "agent" to "model". If you filter stream chunks by node name, update the filter.
- Runtime context: pass it as `context=` on invoke/stream (with `context_schema=` on create_agent) instead of stuffing it into `config["configurable"]`.
- State: prefer `langchain.agents.AgentState` over the old `langgraph.prebuilt` agent state helpers.
- Reading output: prefer `message.content_blocks` for provider-agnostic content. `message.content` still works.

## Rules

- Search the codebase for `create_react_agent`, `pre_model_hook`, `post_model_hook`, `state_modifier`, and imports from `langgraph.prebuilt` before calling a migration done. One leftover import breaks the whole module at import time.
- Invoke the same way: `agent.invoke({"messages": [{"role": "user", "content": "..."}]})`.

## When to use this

- This covers exactly what the title says: create_react_agent to create_agent.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with create_react_agent; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current create_react_agent behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_nCUO2GczwVQBjmrlWVT8EA). Version: `skv_oyr9k31Wnf-F1gErdRhY1g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
