---
name: "standard-content-blocks-the-provider-a-c4f9ad0cae0ae744"
description: "LangChain v1 added message.content_blocks, a unified accessor for modern model output like reasoning and tool calls. It only works on the integrations that implement it; message.content still works everywhere. Not the full reference manual."
metadata:
  skill_id: "skl_2UFs4lmIuwRHjHW1Uw6foA"
  title: "Standard content blocks: the provider-agnostic way to read model output"
  version: "skv_dbgJgEjftZbXXgUh0ysBHw"
  updated: "2026-10-03T14:43:56.819046+00:00"
  canonical_url: "https://vectle.com/skills/skl_2UFs4lmIuwRHjHW1Uw6foA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/releases/langchain-v1\",\"https://docs.langchain.com/oss/python/langchain/streaming\"]"
---

**TL;DR:** LangChain v1 added message.content_blocks, a unified accessor for modern model output like reasoning and tool calls. It only works on the integrations that implement it; message.content still works everywhere. Use content_blocks when you need structured access to what the model produced (text parts, reasoning parts, tool calls) without provider-specific parsing.

## The fix

1. Use `content_blocks` when you need structured access to what the model produced (text parts, reasoning parts, tool calls) without provider-specific parsing.

2. Fall back to `message.content` when the provider does not implement blocks yet. It remains valid and is not deprecated.

3. In streaming, `stream_mode="messages"` gives you message chunks; filter for reasoning content blocks when you want thinking tokens.

4. This covers exactly what the title says: Standard content blocks.

5. You are setting this up for the first time, or auditing an existing setup.

6. You want the key gotchas in one place before you start.

7. You are doing a different workflow with Standard; these steps are specific to the title above.

8. You need the full reference docs; this is the short path, not the manual.

9. Not pinned to a specific version; follows current Standard behavior.

## When to use this

- This covers exactly what the title says: Standard content blocks.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Standard; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_2UFs4lmIuwRHjHW1Uw6foA). Version: `skv_dbgJgEjftZbXXgUh0ysBHw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
