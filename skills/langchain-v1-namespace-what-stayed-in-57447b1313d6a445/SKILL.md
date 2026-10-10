---
name: "langchain-v1-namespace-what-stayed-in-57447b1313d6a445"
description: "LangChain 1.0 shrank the langchain package to agent building blocks. Legacy chains, retrievers, the indexing API, the hub module, and old community re-exports moved to a separate package called langchain-classic. Training data still teaches the old import paths, so agents write code that no longer imports. Not the full reference manual."
metadata:
  skill_id: "skl_8bzJi5f9OpTyjdrlSLA57A"
  title: "LangChain v1 namespace: what stayed in langchain and what moved to langchain-classic"
  version: "skv_V27T73ajzcQvB3jqzEXAAA"
  updated: "2026-10-03T14:05:42.305521+00:00"
  canonical_url: "https://vectle.com/skills/skl_8bzJi5f9OpTyjdrlSLA57A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** LangChain 1.0 shrank the langchain package to agent building blocks. Legacy chains, retrievers, the indexing API, the hub module, and old community re-exports moved to a separate package called langchain-classic.

## The fix

1. `langchain.agents` - create_agent, AgentState

2. `langchain.messages` - message types, trim_messages

3. `langchain.tools` - the @tool decorator, BaseTool

4. `langchain.chat_models` - init_chat_model

5. `langchain.embeddings` - init_embeddings What moved to `langchain-classic` (install it, then import from `langchain_classic`):

6. Legacy chains: LLMChain, ConversationChain, anything from the old `langchain.chains`

7. Retrievers from the old `langchain.retrievers` (MultiQueryRetriever etc.)

8. The indexing API (`langchain.indexes`)

9. The hub module for managing prompts programmatically

10. Embedding helpers like CacheBackedEmbeddings and the old community embeddings

11. Old `langchain-community` re-exports

12. If an import from `langchain` that your training data swears exists now fails, check whether it moved to `langchain_classic` before assuming a broken install. The old paths are not aliases; they are gone from the core package.

## When to use this

- This covers exactly what the title says: LangChain v1 namespace.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LangChain; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 1.0.0, 3.10 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_8bzJi5f9OpTyjdrlSLA57A). Version: `skv_V27T73ajzcQvB3jqzEXAAA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
