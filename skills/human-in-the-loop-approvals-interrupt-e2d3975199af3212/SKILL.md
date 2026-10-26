---
name: "human-in-the-loop-approvals-interrupt-e2d3975199af3212"
description: "Gate sensitive tool calls with HumanInTheLoopMiddleware, persist with a checkpointer, and handle the approve/edit/reject decision on resume. The interrupt is the feature; the resume path is the part people forget to build. Not the full reference manual."
metadata:
  skill_id: "skl_BTCff_kKSU9xDSRXLWIPtw"
  title: "Human-in-the-loop approvals: interrupt_on and the resume path"
  version: "skv_PNUVwXWGw42eRgcH6v4g9Q"
  updated: "2026-10-03T13:55:16.323731+00:00"
  canonical_url: "https://vectle.com/skills/skl_BTCff_kKSU9xDSRXLWIPtw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/middleware/built-in\",\"https://docs.langchain.com/oss/python/langgraph/persistence\"]"
---

**TL;DR:** Gate sensitive tool calls with HumanInTheLoopMiddleware, persist with a checkpointer, and handle the approve/edit/reject decision on resume. The interrupt is the feature; the resume path is the part people forget to build. Edit is the one that breaks: the edited arguments must still validate against the tool schema. Test all three decisions.

## The fix

**TL;DR:** Gate sensitive tool calls with HumanInTheLoopMiddleware, persist with a checkpointer, and handle the approve/edit/reject decision on resume. The interrupt is the feature; the resume path is the part people forget to build. Edit is the one that breaks: the edited arguments must still validate against the tool schema.

## The fix

1. The agent calls a gated tool. Execution pauses with an interrupt instead of running it.

2. Your UI presents the proposed call and collects approve, edit, or reject.

3. Resume the graph with the decision. Approval runs the tool; edit runs it with modified arguments; reject skips it and tells the model.

4. Interrupts require a checkpointer. Without one you get MISSING_CHECKPOINTER at the worst possible moment.

5. Resume with the same thread id. A new thread id starts a new conversation and orphans the paused one.

6. Decide the default for unanswered interrupts: a paused run holding resources forever is a leak. Time them out or surface them in an ops view.

7. Test all three decisions. Edit is the one that breaks: the edited arguments must still validate against the tool schema.

## When to use this

- This covers exactly what the title says: Human-in-the-loop approvals.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Human-in-the-loop; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Human-in-the-loop behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_BTCff_kKSU9xDSRXLWIPtw). Version: `skv_PNUVwXWGw42eRgcH6v4g9Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
