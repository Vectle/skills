---
name: "running-langgraph-dev-inside-a-uv-mana-9b5a946f02c7ef88"
description: "Shows how to fix running langgraph dev inside a uv-managed project. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_fwH53iv6lihUx-tvNq93Lw"
  title: "Running langgraph dev inside a uv-managed project"
  version: "skv_IojLlMZux3V8ZhFco4R_-g"
  updated: "2026-10-03T05:10:49.504084+00:00"
  canonical_url: "https://vectle.com/skills/skl_fwH53iv6lihUx-tvNq93Lw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langgraph/issues/5463\"]"
---

## TL;DR

If langgraph dev misbehaves inside a uv-managed project, sync the project first (uv sync), then invoke the CLI through uv's Python instead of the bare langgraph dev shim: uv run python -m langgraph_cli dev.

## Steps

1. If langgraph dev misbehaves inside a uv-managed project, sync the project first (uv sync), then invoke the CLI through uv's Python instead of the bare langgraph dev shim: uv run python -m langgraph_cli dev. That boots the same dev server (API, Studio UI, docs) with your locked dependencies. If you see a stale langgraph-api version warning, bump it in your project deps and re-sync; the reporter went from 0.4.28 to 0.5.x this way.

2. _Source: https://github.com/langchain-ai/langgraph/issues/5463 (LangGraph)_

## When to use

You are seeing this: That boots the same dev server (API, Studio UI, docs) with your locked dependencies. Use this skill when you run into "Running langgraph dev inside a uv-managed project".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 0.4.28. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/langchain-ai/langgraph/issues/5463


---

Source: [Vectle](https://vectle.com/skills/skl_fwH53iv6lihUx-tvNq93Lw). Version: `skv_IojLlMZux3V8ZhFco4R_-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
