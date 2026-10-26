---
name: "handling-toolexception-in-a-langgraph-8c0a37431c9e28d6"
description: "Shows how to handle ToolException inside a LangGraph agent so one bad tool call does not kill the run. Use when a tool raises ToolException (bad args, missing resource) and you want the model to see the error and retry. Pattern: catch it in the node and return a ToolMessage with the error. Not for validation errors at tool definition time."
metadata:
  skill_id: "skl_w6wytl-LU2AsUIS7cATtmQ"
  title: "Handling ToolException in a LangGraph agent without killing the run"
  version: "skv_0U8lQo_biUHEGmUtp5G6gA"
  updated: "2026-10-03T04:53:49.165654+00:00"
  canonical_url: "https://vectle.com/skills/skl_w6wytl-LU2AsUIS7cATtmQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/79818757/handling-langgraph-toolexceptions-in-a-repl\"]"
---

# Handling ToolException in a LangGraph agent without killing the run

TL;DR: catch `ToolException` where the tool runs and return a `ToolMessage` containing the error text, keyed to the original `tool_call_id`. The model sees the failure as a tool result and retries smarter instead of the whole run crashing.

```text
# the symptom: a tool raises, e.g.
langchain_core.tools.ToolException: Pod 'nonexistent' not found
# and the graph run dies instead of letting the model try again.
```

## When this applies

- A tool raises `ToolException` for runtime failures: bad arguments, missing resources, API errors.
- You want the agent to recover in-conversation (REPL, chatbot, multi-round flows).
- Your state requires a `ToolMessage` per tool call (the standard messages pattern).

## When it does not

- `ValidationError` at tool DEFINITION time means your args schema is wrong. Fix the schema.
- If you want the run to stop on tool errors, let the exception propagate. That is the default.

## Fix it

### 1. Catch ToolException in the tool node

```python
from langchain_core.tools import ToolException
from langchain_core.messages import ToolMessage

def tool_node(state):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        try:
            result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
            outputs.append(ToolMessage(content=str(result), tool_call_id=tool_call["id"]))
        except ToolException as e:
            outputs.append(ToolMessage(
                content=f"Tool error: {e}",
                tool_call_id=tool_call["id"],
                status="error",
            ))
    return {"messages": outputs}
```

Expected: a failing tool produces a `ToolMessage` with the error text, the graph continues, and the model reads the error on its next turn.

### 2. Or use ToolNode's built-in handling

```python
from langgraph.prebuilt import ToolNode

# handle_tool_errors=True converts ToolExceptions to ToolMessages automatically
node = ToolNode(tools, handle_tool_errors=True)
```

Expected: same result with no custom node. Check your langgraph version supports the flag.

### 3. Make the error text actionable

```python
@tool
def delete_pod(pod_name: str) -> str:
    """Delete a kubernetes pod."""
    if pod_name == "nonexistent":
        raise ToolException(f"Pod '{pod_name}' not found. Available pods: web-1, web-2.")
    return f"Pod '{pod_name}' deleted."
```

Expected: the model gets not just the failure but the fix ("Available pods: web-1, web-2"), so the retry usually succeeds.

## Why it happens

LangGraph's message state requires a `ToolMessage` for every tool call the model made. An uncaught `ToolException` breaks that contract: the AIMessage has a dangling tool call with no result, so the run cannot continue coherently. Converting the exception into a result message restores the contract and turns the failure into information the model can use.

## Edge cases

- Only catch `ToolException`, not broad `Exception`. Unexpected bugs (network down, auth expired) SHOULD crash loudly.
- `status="error"` on the ToolMessage helps downstream logging distinguish failures from successes.
- In a REPL, print the tool error to the user too: silent retries confuse humans watching the loop.
- If the model keeps retrying the same bad call, cap retries in your router (e.g. max 3 tool-error rounds, then ask the user).

## Compatibility

langgraph 0.x/1.x with langchain-core tools (Python). `ToolNode(handle_tool_errors=...)` availability varies by version; the manual pattern works everywhere.

---

Source: [Vectle](https://vectle.com/skills/skl_w6wytl-LU2AsUIS7cATtmQ). Version: `skv_0U8lQo_biUHEGmUtp5G6gA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
