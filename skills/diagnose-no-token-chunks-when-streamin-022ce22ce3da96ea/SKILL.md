---
name: "diagnose-no-token-chunks-when-streamin-022ce22ce3da96ea"
description: "Shows how to fix diagnose: no token chunks when streaming a parent graph that wraps an agent. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_geyF3xC_eORHbjiEWl5Cfw"
  title: "Diagnose: no token chunks when streaming a parent graph that wraps an agent"
  version: "skv_rGXZXKTtyo13vYHtrp_omQ"
  updated: "2026-10-03T14:05:53.984712+00:00"
  canonical_url: "https://vectle.com/skills/skl_geyF3xC_eORHbjiEWl5Cfw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/streaming\"]"
---

## TL;DR

Check the structure: create\_agent returns a compiled graph, so using it as a node makes it a subgraph. Re-run and confirm token chunks now appear with subgraph namespace prefixes.

## Steps

1. Token chunks from nested graphs are suppressed unless you opt in. The parent emits its own events; the inner agent's LLM events stay inside the subgraph.

```python
for chunk in parent_graph.stream(
 {...},
 stream_mode="messages",
 subgraphs=True,
):
 ...
```

2. Re-run and confirm token chunks now appear with subgraph namespace prefixes. If you only want the inner agent's stream, consider streaming the inner agent directly instead of through the parent.

## When to use

You are seeing this: You wrapped a create\_agent result as a node in a parent StateGraph. Use this skill when you run into "Diagnose: no token chunks when streaming a parent graph that wraps an agent".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Token chunks from nested graphs are suppressed unless you opt in.


---

Source: [Vectle](https://vectle.com/skills/skl_geyF3xC_eORHbjiEWl5Cfw). Version: `skv_rGXZXKTtyo13vYHtrp_omQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
