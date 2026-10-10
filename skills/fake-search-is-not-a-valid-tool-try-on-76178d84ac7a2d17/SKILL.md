---
name: "fake-search-is-not-a-valid-tool-try-on-76178d84ac7a2d17"
description: "Fixes \"[name] is not a valid tool, try one of [tool]\" when a custom LangGraph tool is rejected at runtime. Use when built-in tools work but your custom function gets this error. Cause: tools registered in only one of the two places. Fix: pass the tool to BOTH bind_tools on the LLM and the ToolNode constructor. Not for tool-definition validation errors."
metadata:
  skill_id: "skl_ipRigiN2fNx3V22ePpZejg"
  title: "\"fake_search is not a valid tool, try one of [tool]\" in LangGraph"
  version: "skv_Ob8J3bes8FiEUlmDRN82zQ"
  updated: "2026-10-03T04:54:54.847873+00:00"
  canonical_url: "https://vectle.com/skills/skl_ipRigiN2fNx3V22ePpZejg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# "Error: my_tool is not a valid tool, try one of [tool]" in LangGraph

TL;DR: your tools are registered in exactly one of the two places they need to be. Pass the tool list to BOTH `llm.bind_tools(tools)` AND `ToolNode(tools)`. The model can only call tools it knows about, and the ToolNode can only execute tools it was given. Miss either one and you get this error.

```text
Assistant: Error: fake_search is not a valid tool, try one of [tool]
```

## When this applies

- Built-in tools (Tavily, DuckDuckGo) work, but YOUR custom function gets rejected.
- The error names your function and lists the tools that ARE valid.
- You followed a tutorial and swapped in your own tool.

## When it does not

- If NO tools work, check your imports and that the tools list is not empty.
- `ValidationError` when DEFINING the tool means the function signature is bad. Different fix.

## Fix it

### 1. Register the tool in both places

```python
from langgraph.prebuilt import ToolNode

tools = [tavily_tool, duckduckgo_tool, fake_search]  # your custom tool included

# place 1: the model must know the tool exists
llm_with_tools = llm.bind_tools(tools)

# place 2: the ToolNode must be able to execute it
tool_node = ToolNode(tools)
```

Expected: the model emits a `fake_search` tool call, and the ToolNode executes it instead of erroring.

### 2. Check the name matches exactly

```python
from langchain_core.tools import tool

@tool
def fake_search(query: str) -> str:
    """Search a fake index."""
    return "result"

print(fake_search.name)  # 'fake_search' -- this is the name the model must emit
```

Expected: the name the model calls matches `tool.name`. A mismatch (e.g. the model says `fakeSearch`) means the bind_tools schema did not reach the model.

### 3. If you defined the tool in another file, verify the import

```python
# the classic tutorial-swap bug: you imported the tutorial's tools list
# instead of your own
from my_tools import fake_search   # make sure THIS is what lands in `tools`
```

Expected: `tools` actually contains your function, not just the tutorial's examples.

## Why it happens

LangGraph splits tool use in two: `bind_tools` teaches the MODEL the tool schemas (so it emits the right tool calls), and `ToolNode(tools)` gives the EXECUTOR the implementations. Tutorials often define `tools = [tavily]` once and pass it to both; when you add your custom function you update one call site and forget the other. The model then either never calls your tool (bind_tools missed) or calls it and the executor rejects it (ToolNode missed), which is this error.

## Edge cases

- `create_react_agent(model, tools=[...])` does both registrations for you. If you keep hitting this with a manual graph, consider switching.
- Tool names must be valid identifiers for most models: no spaces, no special characters.
- After changing the tools list, restart the notebook kernel. Stale `bind_tools` closures are a real gotcha.

## Compatibility

All langgraph versions with `ToolNode` and `bind_tools` (0.x and 1.x, Python).

---

Source: [Vectle](https://vectle.com/skills/skl_ipRigiN2fNx3V22ePpZejg). Version: `skv_Ob8J3bes8FiEUlmDRN82zQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
