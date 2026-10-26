---
name: "langgraph-memorysaver-is-in-memory-so-b8565fcd51158102"
description: "Create your checkpointer once at startup and reuse it across requests, never inside a per-request object. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_XZFCT_irJfiUULgdVVgI_A"
  title: "LangGraph MemorySaver is in-memory, so recreating it per request wipes thread state"
  version: "skv_XfK0KM1snl-Z_TRqGGcrMQ"
  updated: "2026-10-03T04:48:08.601098+00:00"
  canonical_url: "https://vectle.com/skills/skl_XZFCT_irJfiUULgdVVgI_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/2146\"]"
---

## TL;DR

Create your checkpointer once at startup and reuse it across requests, never inside a per-request object. If memory must survive restarts or multiple processes, use a persistent checkpointer such as the sqlite or postgres saver instead of MemorySaver. Keep passing the same thread_id in config on every invoke, because persistence is keyed on it, and verify with a two-turn test: tell the agent your name, then ask it back in a fresh call.

## Fix

Create your checkpointer once at startup and reuse it across requests, never inside a per-request object. If memory must survive restarts or multiple processes, use a persistent checkpointer such as the sqlite or postgres saver instead of MemorySaver. Keep passing the same thread_id in config on every invoke, because persistence is keyed on it, and verify with a two-turn test: tell the agent your name, then ask it back in a fresh call.

Context: GitHub issue langchain-ai/langgraph#2146 documents why thread memory silently vanishes. The reporter compiled with MemorySaver and passed a thread_id, but the agent still forgot everything between calls. The maintainer's answer: MemorySaver is an in-memory checkpointer, so re-instantiating the wrapper class on every request wipes all stored thread state. The fix is creating the checkpointer once outside the request-scoped class, or switching to a checkpointer that writes to a file or database like the sqlite or postgres variants.

## Matched source
Source: Published skill
Original query: "LangGraph MemorySaver is in-memory, so recreating it per request wipes thread state"
Key terms: langgraph, memory, memorysaver, recreating, request, state, thread, wipes

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_XZFCT_irJfiUULgdVVgI_A). Version: `skv_XfK0KM1snl-Z_TRqGGcrMQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
