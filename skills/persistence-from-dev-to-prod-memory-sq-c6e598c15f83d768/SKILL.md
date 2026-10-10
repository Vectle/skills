---
name: "persistence-from-dev-to-prod-memory-sq-c6e598c15f83d768"
description: "Start with InMemorySaver, move to SQLite for local durable runs, and Postgres for production. The API is the same; only the saver and the package change. Thread ids and time travel work at every level. Not the full reference manual."
metadata:
  skill_id: "skl_HzKblCNcaeucs7wwK_S86g"
  title: "Persistence from dev to prod: memory, SQLite, Postgres checkpointers"
  version: "skv_G0a7p2zBFN3DyZ4i2Dd3lA"
  updated: "2026-10-03T13:59:47.074247+00:00"
  canonical_url: "https://vectle.com/skills/skl_HzKblCNcaeucs7wwK_S86g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Start with InMemorySaver, move to SQLite for local durable runs, and Postgres for production. The API is the same; only the saver and the package change. Build your "retry this turn" and "edit and resume" UX on it. - Postgres is what LangSmith itself uses; treat it as the production default. Read the backward-compatibility guide before changing state schemas in production.

## The fix

1. Async graphs need the async variants: AsyncSqliteSaver, AsyncPostgresSaver. Sync savers in async graphs fail.

2. Every invoke/stream needs `{"configurable": {"thread_id": "..."}}`. The thread is the unit of persistence; without it, history is not resumable.

3. Time travel (`get_state`, `update_state`, re-invoke from a past checkpoint) works on any checkpointer. Build your "retry this turn" and "edit and resume" UX on it.

4. Postgres is what LangSmith itself uses; treat it as the production default. SQLite is for local workflows and experiments.

5. Deploying new graph code against old checkpoints: LangGraph runs the latest code against persisted state, so every deploy is a state-migration event. Read the backward-compatibility guide before changing state schemas in production.

## When to use this

- This covers exactly what the title says: Persistence from dev to prod.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Persistence; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Persistence behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_HzKblCNcaeucs7wwK_S86g). Version: `skv_G0a7p2zBFN3DyZ4i2Dd3lA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
