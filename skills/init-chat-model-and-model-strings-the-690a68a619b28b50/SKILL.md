---
name: "init-chat-model-and-model-strings-the-690a68a619b28b50"
description: "init_chat_model from langchain.chat_models is the unified way to build a chat model. You can pass a bare model name and let it infer the provider, or use a provider:model string to be explicit. Plain model classes from provider packages still work when you need provider-specific knobs. Not the full reference manual."
metadata:
  skill_id: "skl_6RoOnxzHAX_ZzDd3L9W4Gg"
  title: "init_chat_model and model strings: the current way to pick a model"
  version: "skv_CJMzC86jqPNodpLC1gmzlA"
  updated: "2026-10-03T14:36:56.098117+00:00"
  canonical_url: "https://vectle.com/skills/skl_6RoOnxzHAX_ZzDd3L9W4Gg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/models\",\"https://docs.langchain.com/oss/python/langchain/quickstart\"]"
---

**TL;DR:** init_chat_model from langchain.chat_models is the unified way to build a chat model. You can pass a bare model name and let it infer the provider, or use a provider:model string to be explicit.

## The fix

1. Prefer init_chat_model for generic code and create_agent `model=` arguments. Model strings like "openai:gpt-5.5" are what the docs use in agent examples.

2. Reach for the provider class when you need provider-only parameters (for example ChatOpenAI's use_responses_api, which picks the Responses vs Completions API).

3. For OpenAI-compatible endpoints (Together, vLLM), pass `model_provider="openai"` with a `base_url`. For routers like OpenRouter or LiteLLM, use the dedicated integrations instead: ChatOpenRouter from langchain-openrouter, or ChatLiteLLM / ChatLiteLLMRouter from langchain-litellm.

## When to use this

- This covers exactly what the title says: init_chat_model and model strings.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with init_chat_model; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_6RoOnxzHAX_ZzDd3L9W4Gg). Version: `skv_CJMzC86jqPNodpLC1gmzlA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
