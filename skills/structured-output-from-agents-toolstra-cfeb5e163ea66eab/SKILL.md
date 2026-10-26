---
name: "structured-output-from-agents-toolstra-cfeb5e163ea66eab"
description: "In v1, create_agent takes response_format built with ToolStrategy or ProviderStrategy from langchain.agents.structured_output. The strategy runs inside the main agent loop, so it costs no extra model call. Not the full reference manual."
metadata:
  skill_id: "skl_BP47E8lNuMlMPrHxVnkz0Q"
  title: "Structured output from agents: ToolStrategy and ProviderStrategy"
  version: "skv_LB6BtirUnywdyEP8N22OzA"
  updated: "2026-10-03T05:34:32.150908+00:00"
  canonical_url: "https://vectle.com/skills/skl_BP47E8lNuMlMPrHxVnkz0Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/releases/langchain-v1\",\"https://docs.langchain.com/oss/python/langchain/structured-output\"]"
---

**TL;DR:** In v1, create_agent takes response_format built with ToolStrategy or ProviderStrategy from langchain.agents.structured_output. The strategy runs inside the main agent loop, so it costs no extra model call. Migrate it. - This replaces output parsers for the agent case.

## The fix

1. ToolStrategy: the model calls a synthetic tool to produce the structure. ProviderStrategy: uses the provider's native structured output. Prefer provider-native when the provider supports it well.

2. Control failure behavior with the `handle_errors` parameter on the strategy: parsing errors (model output does not match the schema) and multiple tool calls for the schema need a policy, not a crash.

3. The old prompted tuple form `response_format=("please generate ...", Schema)` is removed in v1. Migrate it.

4. This replaces output parsers for the agent case. Parsers still exist for plain LCEL chains.

## When to use this

- This covers exactly what the title says: Structured output from agents.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Structured; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.4, 70.0 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_BP47E8lNuMlMPrHxVnkz0Q). Version: `skv_LB6BtirUnywdyEP8N22OzA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
