---
name: "chatopenai-integration-parameters-and-69cbbbe38b38e709"
description: "The OpenAI integration ships in langchain-openai. Besides the model name it exposes a Responses-vs-Completions switch, a base URL override for OpenAI-compatible providers, and a proxy parameter. Router services get their own integration packages. Not the full reference manual."
metadata:
  skill_id: "skl_1xnNeFDfmh-FsKTQe7pdSA"
  title: "ChatOpenAI integration: parameters and OpenAI-compatible endpoint setup"
  version: "skv_bipUjRGxOaDSFTpps-ukmQ"
  updated: "2026-10-03T14:12:52.631604+00:00"
  canonical_url: "https://vectle.com/skills/skl_1xnNeFDfmh-FsKTQe7pdSA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** The OpenAI integration ships in langchain-openai. Besides the model name it exposes a Responses-vs-Completions switch, a base URL override for OpenAI-compatible providers, and a proxy parameter. Never paste a real key into code or chat. - For streaming token usage metadata from OpenAI, you must opt in on the integration; usage is not returned in streaming chunks by default.

## The fix

**TL;DR:** The OpenAI integration ships in langchain-openai. Besides the model name it exposes a Responses-vs-Completions switch, a base URL override for OpenAI-compatible providers, and a proxy parameter. Never paste a real key into code or chat. - For streaming token usage metadata from OpenAI, you must opt in on the integration; usage is not returned in streaming chunks by default.

## The fix

1. `use_responses_api` - picks the OpenAI Responses API vs the Chat Completions API.

2. `base_url` - point at an OpenAI-compatible endpoint (Together, vLLM, and similar) while keeping `model_provider="openai"` semantics. Provider-specific fields from routers may not be preserved through this path.

3. `openai_proxy` - HTTP proxy for deployments that need one.

4. `max_retries` / `timeout` - resilience (see the retry skill). Defaults: up to 6 retries on 429/5xx/network errors.

5. OpenRouter: `ChatOpenRouter` from `langchain-openrouter`

6. LiteLLM: `ChatLiteLLM` / `ChatLiteLLMRouter` from `langchain-litellm` Do not point ChatOpenAI at a router's base URL and expect router-specific fields to survive. The docs call this out explicitly.

7. The key comes from OPENAI_API_KEY in the environment. Never paste a real key into code or chat.

8. For streaming token usage metadata from OpenAI, you must opt in on the integration; usage is not returned in streaming chunks by default.

## When to use this

- This covers exactly what the title says: ChatOpenAI integration.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with ChatOpenAI; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_1xnNeFDfmh-FsKTQe7pdSA). Version: `skv_bipUjRGxOaDSFTpps-ukmQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
