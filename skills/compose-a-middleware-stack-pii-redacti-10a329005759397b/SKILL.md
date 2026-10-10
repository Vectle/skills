---
name: "compose-a-middleware-stack-pii-redacti-10a329005759397b"
description: "The three prebuilt middlewares that cover most production agents: PIIMiddleware to keep sensitive data from the model, SummarizationMiddleware to bound history, HumanInTheLoopMiddleware to gate risky tool calls. Compose them in one list. Not the full reference manual."
metadata:
  skill_id: "skl_Q8HSqCaNgGbV73vO1MQ-sg"
  title: "Compose a middleware stack: PII redaction, summarization, human approval"
  version: "skv_vh_0sBMH1IhQ9ZOOWiYGlQ"
  updated: "2026-10-03T13:51:00.776056+00:00"
  canonical_url: "https://vectle.com/skills/skl_Q8HSqCaNgGbV73vO1MQ-sg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The three prebuilt middlewares that cover most production agents: PIIMiddleware to keep sensitive data from the model, SummarizationMiddleware to bound history, HumanInTheLoopMiddleware to gate risky tool calls. Compose them in one list. Middleware stack Rules - Order matters: PII redaction belongs early so sensitive data never reaches the model or the trace. Set the token trigger with headroom below the context limit. - HumanInTheLoopMiddleware pauses execution with an interrupt; resuming needs a checkpointer and the approve/edit/reject decision.

## The fix

**TL;DR:** The three prebuilt middlewares that cover most production agents: PIIMiddleware to keep sensitive data from the model, SummarizationMiddleware to bound history, HumanInTheLoopMiddleware to gate risky tool calls. Compose them in one list. Middleware stack Rules - Order matters: PII redaction belongs early so sensitive data never reaches the model or the trace. Set the token trigger with headroom below the context limit. - HumanInTheLoopMiddleware pauses execution with an interrupt; resuming needs a checkpointer and the approve/edit/reject decision.

## The fix

1. Order matters: PII redaction belongs early so sensitive data never reaches the model or the trace. Summarization sits in the middle. Approval gates wrap the tools they guard.

2. SummarizationMiddleware needs its own model for the summary calls; it does not have to be the agent's main model. Set the token trigger with headroom below the context limit.

3. HumanInTheLoopMiddleware pauses execution with an interrupt; resuming needs a checkpointer and the approve/edit/reject decision. Test the full interrupt-resume path, not just the happy path.

4. Custom behavior goes in an AgentMiddleware subclass with hooks: before_agent, before_model, wrap_model_call, wrap_tool_call, after_model, after_agent.

## When to use this

- This covers exactly what the title says: Compose a middleware stack.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Compose; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Compose behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_Q8HSqCaNgGbV73vO1MQ-sg). Version: `skv_vh_0sBMH1IhQ9ZOOWiYGlQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
