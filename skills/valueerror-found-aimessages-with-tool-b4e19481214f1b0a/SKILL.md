---
name: "valueerror-found-aimessages-with-tool-b4e19481214f1b0a"
description: "Fixes the LangChain message-history error where an AI message contains tool calls but the matching ToolMessages are missing. Covers history trimming, filtering, and resume paths that break tool_call_id pairing."
metadata:
  skill_id: "skl_gaFrtI31LmntMU7mWWuHsA"
  title: "ValueError: Found AIMessages with tool_calls that do not have a corresponding ToolMessage"
  version: "skv_QvHtJYwDlm2-cxem1vYfoQ"
  updated: "2026-10-03T05:54:31.88115+00:00"
  canonical_url: "https://vectle.com/skills/skl_gaFrtI31LmntMU7mWWuHsA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/5277\"]"
---

## TL;DR
Somewhere your message history lost the tool results while keeping the AI message that requested them. Providers reject that shape. The fix is to never split the pair: when you trim or filter history, drop the orphaned AI message too, or rebuild the list so every tool call has its ToolMessage.

```text
ValueError: Found AIMessages with tool_calls that do not have a corresponding ToolMessage
```

## Fix it
1. Find where history gets modified: trimming, filtering, summarization, or a custom `get_session_history`. Expected: you locate the spot that drops ToolMessages.
2. Keep pairs together. When you slice history, cut at message boundaries so an `AIMessage` with `tool_calls` is never separated from its `ToolMessage` replies. Expected: re-running the same conversation no longer raises.
3. If you filter messages (for example removing old tool output to save tokens), also remove the AI message whose `tool_call_id`s you deleted. Expected: the provider sees a clean alternating history.
4. In LangGraph, let `ToolNode` append tool results instead of hand-rolling message surgery, and use the `add_messages` reducer so updates merge by id. Expected: pairing is maintained by the framework.

## When this applies
- You trim, summarize, or filter chat history and then call the model again.
- You rebuild history on resume (from a checkpointer or your own store) and some ToolMessages are missing.

## When this does NOT apply
- The error names a different missing piece (a ToolMessage without a matching AI call is the reverse problem).
- You never use tools; then the history shape issue is something else entirely.

## Compatibility
- langchain-core 0.1+, LangGraph 0.1+. Applies to any provider; OpenAI and Anthropic both validate the pairing.

## Root cause
Tool calling is a two-message contract: the AI message says "call this tool with this id" and a later ToolMessage says "here is the result for that id". Providers validate the contract server-side. Any history manipulation that deletes one side but keeps the other produces a conversation no provider will accept.

## Edge cases
- Summarization that compresses tool exchanges into prose must remove both messages, not just the tool output.
- Parallel tool calls produce several ToolMessages for one AI message; keep all of them or drop the whole group.
- Streaming chunks reassembled by hand can lose tool_call ids; prefer the framework's chunk-merging helpers.


---

Source: [Vectle](https://vectle.com/skills/skl_gaFrtI31LmntMU7mWWuHsA). Version: `skv_QvHtJYwDlm2-cxem1vYfoQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
