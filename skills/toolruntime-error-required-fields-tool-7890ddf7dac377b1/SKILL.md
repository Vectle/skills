---
name: "toolruntime-error-required-fields-tool-7890ddf7dac377b1"
description: "Fixes \"Required fields tool_runtime missing\" when invoking a LangGraph tool that declares a ToolRuntime parameter. Use when a tool with tool_runtime: ToolRuntime fails inside a hand-built StateGraph with ToolNode on langgraph 1.0.x. Known bug fixed in langchain 1.0.5; upgrade or switch to create_agent. Not for tools without runtime params."
metadata:
  skill_id: "skl_MoidroVw2IV5UTdKSUIreA"
  title: "ToolRuntime error: Required fields tool_runtime missing in LangGraph"
  version: "skv_LuPS_fcqyNk0O9n4n78atQ"
  updated: "2026-10-03T04:48:52.070798+00:00"
  canonical_url: "https://vectle.com/skills/skl_MoidroVw2IV5UTdKSUIreA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/79817107/toolruntime-error-required-fields-tool-runtime-missing-when-invoking-tool-in-langgraph\"]"
---

# ToolRuntime error: Required fields tool_runtime missing in LangGraph

TL;DR: on langgraph 1.0.3 / langchain 1.0.0, a tool that declares `tool_runtime: ToolRuntime` fails when run through a hand-built `ToolNode` because the runtime is never injected. Upgrade to `langchain>=1.0.5` (known bug #6318, fixed there) or switch to `create_agent()`, which injects it for you.

```text
ToolRuntime error: Required fields tool_runtime missing
```

## When this applies

- Your tool signature includes `tool_runtime: ToolRuntime` (from `langchain.tools`).
- You built the graph yourself: `StateGraph` + `ToolNode(tools)`.
- `langgraph==1.0.3`, `langchain==1.0.0` (or nearby 1.0.x).

## When it does not

- If the tool has no `ToolRuntime` param, this error cannot happen. Look at the real traceback.
- `create_agent()` users on the same versions generally do not hit this.

## Fix it

### 1. Upgrade langchain

```python
# terminal
pip install -U "langchain>=1.0.5" "langgraph>=1.0.0"
```

Expected: the same tool + ToolNode code now runs. The bug (langchain-ai/langgraph#6318) was in runtime injection, fixed in 1.0.5.

### 2. Or switch to create_agent

```python
from langchain.agents import create_agent
from langchain.tools import tool, ToolRuntime

@tool
def foo_tool(tool_runtime: ToolRuntime) -> str:
    """Explain what the tool does."""
    return f"store={tool_runtime.store}"

agent = create_agent(model, tools=[foo_tool])
```

Expected: `create_agent` wires ToolRuntime injection automatically, no manual ToolNode needed.

### 3. Or drop the runtime param if you do not need it

If you added `ToolRuntime` speculatively, remove it and read what you need from the state instead:

```python
@tool
def foo_tool(query: str) -> str:
    return search(query)
```

Expected: the tool runs anywhere, no injection required.

## Why it happens

`ToolRuntime` is a special injected parameter (like `InjectedState`): the framework is supposed to fill it in at call time with the store, stream writer, and config. In the 1.0.0-1.0.4 window, the manual `ToolNode` path skipped that injection, so the tool saw a missing required field. `create_agent` had the correct wiring all along.

## Edge cases

- After upgrading, delete stale `.pyc`/caches if the error persists: an old langchain can shadow the new one in editable installs.
- `InjectedToolCallId` and `InjectedState` had related injection gaps in the same window; upgrade fixes those too.
- If you pin versions in a lockfile, bump both `langchain` and `langgraph` together. Mixing 1.0.5 langchain with 1.0.0 langgraph reintroduces edge cases.

## Compatibility

langgraph/langchain 1.0.x (Python). Broken: langchain 1.0.0-1.0.4 with manual ToolNode. Fixed: langchain >= 1.0.5.

---

Source: [Vectle](https://vectle.com/skills/skl_MoidroVw2IV5UTdKSUIreA). Version: `skv_LuPS_fcqyNk0O9n4n78atQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
