---
name: "embeddings-in-v1-init-embeddings-and-p-93125a45d27e6d60"
description: "Embeddings live under langchain.embeddings in v1. Use init_embeddings for provider-agnostic setup, or the provider's embedding class directly. Old helpers like CacheBackedEmbeddings moved to langchain-classic. Not the full reference manual."
metadata:
  skill_id: "skl_crOys3ADQ1S46L_Lqb5hLA"
  title: "Embeddings in v1: init_embeddings and provider packages"
  version: "skv_c84Ax9ytrY0gFoA0m7NNWA"
  updated: "2026-10-03T14:38:59.485758+00:00"
  canonical_url: "https://vectle.com/skills/skl_crOys3ADQ1S46L_Lqb5hLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/migrate/langchain-v1\"]"
---

**TL;DR:** Embeddings live under langchain.embeddings in v1. Use init_embeddings for provider-agnostic setup, or the provider's embedding class directly.

## The fix

1. `init_embeddings` mirrors `init_chat_model`: bare names infer the provider, `provider:model` strings are explicit.

2. Embedding classes live in the provider packages (langchain-openai, langchain-google-genai, etc.), not in langchain core.

3. If old code imports CacheBackedEmbeddings or community embeddings from `langchain`, move those imports to `langchain_classic` and install langchain-classic. Do not rewrite working caching code to the new API unless you have a reason.

4. This covers exactly what the title says: Embeddings in v1.

5. You are setting this up for the first time, or auditing an existing setup.

6. You want the key gotchas in one place before you start.

7. You are doing a different workflow with Embeddings; these steps are specific to the title above.

8. You need the full reference docs; this is the short path, not the manual.

9. Not pinned to a specific version; follows current Embeddings behavior.

10. Do not rewrite working caching code to the new API unless you have a reason.

## When to use this

- This covers exactly what the title says: Embeddings in v1.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Embeddings; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_crOys3ADQ1S46L_Lqb5hLA). Version: `skv_c84Ax9ytrY0gFoA0m7NNWA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
