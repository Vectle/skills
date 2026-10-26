---
name: "modulenotfounderror-no-module-named-la-e241b8563852ff24"
description: "This error means the provider package is not installed. LangChain splits every provider into its own package, so installing langchain alone is never enough for OpenAI, Anthropic, or any other model or store."
metadata:
  skill_id: "skl_jY_YkC7aUiCfM3QjmNf1uA"
  title: "ModuleNotFoundError: No module named 'langchain_openai' (or any provider package)"
  version: "skv_LuMrrIRjrVyLT14_3a7Raw"
  updated: "2026-10-03T15:18:51.996661+00:00"
  canonical_url: "https://vectle.com/skills/skl_jY_YkC7aUiCfM3QjmNf1uA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/install\",\"https://docs.langchain.com/oss/python/integrations/providers/overview\"]"
---

**TL;DR:** This error means the provider package is not installed. LangChain splits every provider into its own package, so installing langchain alone is never enough for OpenAI, Anthropic, or any other model or store. Confirm: pip show langchain-openai (or the provider you need). Install it: pip install -U langchain-openai.

## The fix

1. `pip install langchain` gives you agents, messages, tools, chat models, embeddings. It deliberately does not pull in any provider SDK.

2. The same applies to vector stores: `langchain-chroma`, `langchain-pinecone`, `langchain-qdrant`, `langchain-weaviate`, `langchain-mongodb`, `langchain-elasticsearch`, `langchain-redis` are all separate installs.

3. A stale lockfile or a fresh virtualenv is the usual trigger: the code was written on a machine that had the provider package, the new environment does not.

4. Confirm: `pip show langchain-openai` (or the provider you need).

5. Install it: `pip install -U langchain-openai`.

6. If the project is uv-managed, use `uv add langchain-openai` instead of mixing pip and uv. Do not reinstall `langchain` itself; that changes nothing. The missing piece is always the provider package.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: ModuleNotFoundError.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current ModuleNotFoundError behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_jY_YkC7aUiCfM3QjmNf1uA). Version: `skv_LuMrrIRjrVyLT14_3a7Raw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
