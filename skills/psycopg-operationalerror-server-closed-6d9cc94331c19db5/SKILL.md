---
name: "psycopg-operationalerror-server-closed-6d9cc94331c19db5"
description: "Fixes LangGraph's AsyncPostgresSaver dropping connections with psycopg OperationalError when sharing a database with SQLAlchemy/asyncpg. Use when you see \"server closed the connection unexpectedly\" or \"consuming input failed\" after adding LangGraph persistence to a FastAPI app. Fixed by giving LangGraph its own psycopg connection pool. Not for unreachable-database errors."
metadata:
  skill_id: "skl_JnfwwGEEXbEqTgncfOGlZA"
  title: "psycopg.OperationalError: server closed the connection unexpectedly with AsyncPostgresSaver"
  version: "skv_qL05f_cZGx5LGt6Lr2S8eQ"
  updated: "2026-10-03T04:45:23.665419+00:00"
  canonical_url: "https://vectle.com/skills/skl_JnfwwGEEXbEqTgncfOGlZA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# psycopg.OperationalError: server closed the connection unexpectedly (AsyncPostgresSaver + FastAPI)

TL;DR: LangGraph's Postgres saver uses psycopg; your FastAPI ORM probably uses asyncpg. Two drivers sharing one database with concurrent requests leads to dropped connections. Give LangGraph its own dedicated psycopg pool with conservative limits and keep it out of the ORM's pool.

```text
psycopg.OperationalError: consuming input failed: server closed the connection unexpectedly
```

## When this applies

- You added `AsyncPostgresSaver` / `AsyncPostgresStore` to a FastAPI app that already uses SQLAlchemy with asyncpg.
- Errors appear under concurrent or long-running requests, not on a single quick call.
- The ORM worked fine before LangGraph persistence arrived.

## When it does not

- `connection refused` on startup means Postgres is down or the host/port is wrong.
- `Undefined table 'checkpoints'` means you skipped `setup()`.

## Fix it

### 1. Give the saver its own connection pool

```python
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from psycopg_pool import AsyncConnectionPool

pool = AsyncConnectionPool(
    conninfo="postgresql://YOUR_HOST:5432/mydb",
    min_size=2,
    max_size=10,
    timeout=30,
)

saver = AsyncPostgresSaver(pool)
await saver.setup()
```

Expected: LangGraph traffic no longer contends with the ORM's asyncpg pool. The `server closed the connection` errors stop under load.

### 2. Do not share connections between the two drivers

Keep these rules:

- LangGraph saver: psycopg pool only.
- SQLAlchemy ORM: asyncpg pool only.
- Never pass an asyncpg connection into the saver or vice versa.

Expected: no more driver-level fights over who closed a connection first.

### 3. Size the pools for your concurrency

```python
# rule of thumb: langgraph pool max_size >= your peak concurrent graph runs
# plus headroom for the store if you use AsyncPostgresStore too
```

If errors persist at peak load, raise `max_size` on the LangGraph pool before touching the ORM's. And check Postgres `max_connections`: two pools plus the ORM must fit under it.

### 4. Confirm the fix under load

Run your concurrent scenario again and watch for the error over several minutes, not just one request. Connection bugs are timing bugs: a single clean run proves nothing.

## Why it happens

psycopg and asyncpg manage connections differently (timeouts, keepalives, cancellation). When both drivers hammer the same database from one process and a connection gets recycled or killed under load, one driver sees `server closed the connection unexpectedly` mid-query. Isolating the pools removes the interaction.

## Edge cases

- The same failure can come from a proxy (PgBouncer) killing idle connections. If pools are already separate, set a shorter pool `timeout` than the proxy's idle timeout.
- Long-running graph runs hold a connection for the whole run. Size the pool for concurrent RUNS, not concurrent HTTP requests.
- `AsyncPostgresStore` needs the same treatment: its own pool, same rules.

## Compatibility

langgraph 0.2.x / 1.x with `langgraph-checkpoint-postgres` (Python), FastAPI + SQLAlchemy async setups.

---

Source: [Vectle](https://vectle.com/skills/skl_JnfwwGEEXbEqTgncfOGlZA). Version: `skv_qL05f_cZGx5LGt6Lr2S8eQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
