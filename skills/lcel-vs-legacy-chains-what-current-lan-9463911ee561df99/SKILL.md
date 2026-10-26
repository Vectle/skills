---
name: "lcel-vs-legacy-chains-what-current-lan-9463911ee561df99"
description: "Current LangChain composes runnables with the pipe operator (LCEL). LLMChain and the other legacy chains moved to langchain-classic in v1. Training data still presents LLMChain as the default, which is the main trap. Not the full reference manual."
metadata:
  skill_id: "skl_IKAAF5kLPReNL-mqo8SGSw"
  title: "LCEL vs legacy chains: what current LangChain code looks like"
  version: "skv_mV-fZ5pyBBOAVS9PnntVNw"
  updated: "2026-10-03T14:14:45.019532+00:00"
  canonical_url: "https://vectle.com/skills/skl_IKAAF5kLPReNL-mqo8SGSw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/migrate/langchain-v1\"]"
---

**TL;DR:** Current LangChain composes runnables with the pipe operator (LCEL). LLMChain and the other legacy chains moved to langchain-classic in v1. Chains are for straight pipelines; the moment the model needs to decide, that is an agent.

## The fix

1. For new code, use LCEL (`prompt | model | parser`). Do not reach for LLMChain in new code; it lives in langchain-classic now and only exists for old codebases.

2. LCEL runnables get `.invoke`, `.batch`, `.stream`, `.astream_events`, `.with_retry`, and `.with_fallbacks` for free. If you are hand-rolling retry loops around a chain, you are reimplementing built-ins.

3. Prefer create_agent over chains for anything with tools. Chains are for straight pipelines; the moment the model needs to decide, that is an agent.

## When to use this

- This covers exactly what the title says: LCEL vs legacy chains.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LCEL; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.4 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_IKAAF5kLPReNL-mqo8SGSw). Version: `skv_mV-fZ5pyBBOAVS9PnntVNw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
