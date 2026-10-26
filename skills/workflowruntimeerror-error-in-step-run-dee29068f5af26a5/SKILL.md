---
name: "workflowruntimeerror-error-in-step-run-dee29068f5af26a5"
description: "Llama Index: workflowRuntimeError: Error in step 'run_agent_step': cannot access local variable 'r' where it is not associated. The verified fix is Fix: Confirmed as a real framework bug, fixed via PR and released in llama-index-core==0.12.14 - fix is pip install -U llama-index-core. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_TSxYdyKP8mCrX2ctFNrk1w"
  title: "WorkflowRuntimeError: Error in step 'run_agent_step': cannot access local variable 'r' where it is not associated"
  version: "skv_W0DlzXR_7YZv9k439co1SA"
  updated: "2026-10-03T04:44:43.935413+00:00"
  canonical_url: "https://vectle.com/skills/skl_TSxYdyKP8mCrX2ctFNrk1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/run-llama/llama_index/issues/17629\"]"
---

## TL;DR

Fix: Confirmed as a real framework bug, fixed via PR and released in llama-index-core==0.12.14 - fix is pip install -U llama-index-core. Workarounds if pinned: use FunctionAgent instead of ReAct agents, and for Anthropic set max_tokens high (their API behaves oddly when responses hit the limit).

## The error

```text
Issue run-llama/llama_index#17629 (closed, 17 comments): ### Bug Description I am trying to use a Multi-Agent workflow using AgentWorkflow, and I get this error as soon the second agent is called. I get the same error by running the code example from: https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/agent/agent_workflow_multi.ipynb `async def test(): handler = agent_workflow.run( user_msg="Write me a report on the history of the internet. Briefly describe the history of the internet, including the development of the internet, the development of the web, and the development of the internet in the 21st century." ) await handler im
```

## Fix

1. Confirmed as a real framework bug, fixed via PR and released in llama-index-core==0.12.14 - fix is pip install -U llama-index-core.
2. Workarounds if pinned: use FunctionAgent instead of ReAct agents, and for Anthropic set max_tokens high (their API behaves oddly when responses hit the limit).

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in llama_index.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in llama_index, even a similar-looking one.
- General llama_index setup or credential questions.

## Compatibility

- Llama Index (run-llama/llama_index)

## Variant phrasings

- How to fix "workflowRuntimeError: Error in step 'run_agent_step': cannot access local variable 'r' where it is not associated" in llama_index
- llama_index: workflowRuntimeError: Error in step 'run_agent_step': cannot access local variable 'r' where it is not associated
- workflowRuntimeError: problem in step 'run_agent_step': cannot access local variable 'r' where it is not associated

## Source

- https://github.com/run-llama/llama_index/issues/17629

---

Source: [Vectle](https://vectle.com/skills/skl_TSxYdyKP8mCrX2ctFNrk1w). Version: `skv_W0DlzXR_7YZv9k439co1SA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
