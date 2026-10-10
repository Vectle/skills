---
name: "langgraph-setup-and-checkpointer-packa-12e6e5828b517fa5"
description: "pip install langgraph gets the graph runtime and the in-memory checkpointer. SQLite and Postgres checkpointers are separate packages you install only when you need durable persistence. Not the full reference manual."
metadata:
  skill_id: "skl__xWwwiWynJa_L86d9sXr0A"
  title: "LangGraph setup and checkpointer packages: what ships in the box"
  version: "skv_vHb4mMG1-YHNNxUNCWYE1w"
  updated: "2026-10-03T14:16:26.860841+00:00"
  canonical_url: "https://vectle.com/skills/skl__xWwwiWynJa_L86d9sXr0A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** pip install langgraph gets the graph runtime and the in-memory checkpointer. SQLite and Postgres checkpointers are separate packages you install only when you need durable persistence.

## The fix

1. In-memory (dev, tests): `from langgraph.checkpoint.memory import InMemorySaver` - ships inside the langgraph package, nothing else to install.

2. SQLite (local workflows): SqliteSaver / AsyncSqliteSaver - install `langgraph-checkpoint-sqlite` separately.

3. Postgres (production): PostgresSaver / AsyncPostgresSaver - install `langgraph-checkpoint-postgres` separately.

4. Persistence only works if you pass a checkpointer to `compile()`. Without one you get MISSING_CHECKPOINTER the moment you use persistence features.

5. Pass a `thread_id` in the config (`{"configurable": {"thread_id": "..."}}`) so conversations checkpoint per thread. No thread id, no resumable history.

6. Async graphs need the async checkpointer variants. Mixing a sync saver into an async graph fails.

## When to use this

- This covers exactly what the title says: LangGraph setup and checkpointer packages.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LangGraph; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current LangGraph behavior.

---

Source: [Vectle](https://vectle.com/skills/skl__xWwwiWynJa_L86d9sXr0A). Version: `skv_vHb4mMG1-YHNNxUNCWYE1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
