---
name: "defining-tools-the-tool-decorator-and-112a493d4bf54947"
description: "In v1 tools are plain functions decorated with @tool from langchain.tools. A parameter annotated as ToolRuntime is injected at call time and never shown to the model. Do not name your own parameters config or runtime."
metadata:
  skill_id: "skl_hx9FX376V6bh2yBaoJqRIA"
  title: "Defining tools: the @tool decorator and the ToolRuntime injection"
  version: "skv_WUTv8rNBSHysxwH2LKBelg"
  updated: "2026-10-03T14:07:13.759627+00:00"
  canonical_url: "https://vectle.com/skills/skl_hx9FX376V6bh2yBaoJqRIA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** In v1 tools are plain functions decorated with @tool from langchain.tools. A parameter annotated as ToolRuntime is injected at call time and never shown to the model. Write it like you are explaining the tool to a smart coworker: what it does, what the arguments mean. - Tools can return state updates (a Command) to write short-term memory during execution.

## The fix

1. `runtime` is reserved for the ToolRuntime parameter. Naming your own argument `config` or `runtime` breaks the injection; use the ToolRuntime annotation instead.

2. The docstring is the tool description the model sees. Write it like you are explaining the tool to a smart coworker: what it does, what the arguments mean.

3. Tools can return state updates (a Command) to write short-term memory during execution. See the agent-with-memory workflow skill.

## When to use this

- This covers exactly what the title says: Defining tools.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Defining; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Defining behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_hx9FX376V6bh2yBaoJqRIA). Version: `skv_WUTv8rNBSHysxwH2LKBelg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
