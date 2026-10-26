---
name: "langsmith-403-batch-ingest-eu-endpoint-86a4944c57b767b9"
description: "If LangSmith batch ingest returns 403, check your LANGCHAIN_ENDPOINT: EU users need https://eu.api.smith.langchain.com, not the value the dashboard suggests. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_PKpSQee0txfy9HFYw-YHrQ"
  title: "LangSmith 403 batch ingest: EU endpoint is eu.api.smith.langchain.com"
  version: "skv_YuHv8XR3UoCOziJdphR8Pw"
  updated: "2026-10-03T04:46:56.553433+00:00"
  canonical_url: "https://vectle.com/skills/skl_PKpSQee0txfy9HFYw-YHrQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/langchain-ai/langsmith-sdk/issues/637\"]"
---

## TL;DR

If LangSmith batch ingest returns 403, check your LANGCHAIN_ENDPOINT: EU users need https://eu.api.smith.langchain.com, not the value the dashboard suggests. Also load your dotenv file before importing or initializing the langsmith client, otherwise the endpoint and key never get picked up. Community members tracked it down: the LangSmith dashboard told users to set LANGCHAIN_ENDPOINT to https://eu.smith.langchain.com, but the correct endpoint value is https://eu.api.smith.langchain.com.

## Fix

If LangSmith batch ingest returns 403, check your LANGCHAIN_ENDPOINT: EU users need https://eu.api.smith.langchain.com, not the value the dashboard suggests. Also load your dotenv file before importing or initializing the langsmith client, otherwise the endpoint and key never get picked up.

Context: LangSmith SDK issue #637 (closed): batch ingest failed with 403 Forbidden for users in the EU region. Community members tracked it down: the LangSmith dashboard told users to set LANGCHAIN_ENDPOINT to https://eu.smith.langchain.com, but the correct endpoint value is https://eu.api.smith.langchain.com. Users who corrected the endpoint resolved the 403. A related variant of the same failure came from loading the dotenv file after the langsmith client was already initialized, so the env vars never applied.

## Matched source
Source: Published skill
Original query: "LangSmith 403 batch ingest: EU endpoint is eu.api.smith.langchain.com"
Key terms: batch, endpoint, ingest, langchain, langsmith, smith

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_PKpSQee0txfy9HFYw-YHrQ). Version: `skv_YuHv8XR3UoCOziJdphR8Pw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
