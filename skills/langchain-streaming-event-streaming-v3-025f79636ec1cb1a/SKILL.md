---
name: "langchain-streaming-event-streaming-v3-025f79636ec1cb1a"
description: "For new apps the docs recommend event streaming via stream_events with version v3, which returns typed projections you consume independently. The older stream_mode chunks still work for graphs: updates for step events, messages for tokens, and you can combine them. Not the full reference manual."
metadata:
  skill_id: "skl_tIq_R2IsaiB4MZqsGzeVqA"
  title: "LangChain streaming: event streaming v3, stream modes, and thread ids"
  version: "skv_gIcjUDUVs-yPxb1Lcd2J5g"
  updated: "2026-10-03T14:08:25.441198+00:00"
  canonical_url: "https://vectle.com/skills/skl_tIq_R2IsaiB4MZqsGzeVqA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/streaming\",\"https://docs.langchain.com/oss/python/langchain/event-streaming\"]"
---

**TL;DR:** For new apps the docs recommend event streaming via stream_events with version v3, which returns typed projections you consume independently. The older stream_mode chunks still work for graphs: updates for step events, messages for tokens, and you can combine them. Note OpenAI needs an explicit opt-in for usage metadata in streaming chunks.

## The fix

1. `stream_mode="updates"` emits an event after every agent step; `stream_mode="messages"` streams LLM token chunks; pass a list to get both.

2. Always pass a `thread_id` via config when streaming a conversation. It is independent of stream mode and it is what makes follow-up turns resume the same history.

3. Wrapping a create_agent as a node in a parent StateGraph? The parent's `stream_mode="messages"` will not emit the inner agent's token chunks unless you pass `subgraphs=True`.

4. `stream_mode="custom"` is for your own `writer()` events inside nodes.

5. For token accounting while streaming, use UsageMetadataCallbackHandler or get_usage_metadata_callback. Note OpenAI needs an explicit opt-in for usage metadata in streaming chunks.

## When to use this

- This covers exactly what the title says: LangChain streaming.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LangChain; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_tIq_R2IsaiB4MZqsGzeVqA). Version: `skv_gIcjUDUVs-yPxb1Lcd2J5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
