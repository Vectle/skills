---
name: "timed-out-fetching-a-new-connection-fr-b4e94f3b419ee09c"
description: "Fixes Prisma error P2024 'Timed out fetching a new connection from the connection pool' by finding the connection leak or pool exhaustion: use a single PrismaClient instance, size connection_limit to the workload, and route serverless traffic through a pooler. Use when queries intermittently fail with P2024 under load. Not for unreachable servers (P1001) or auth failures (P1000)."
metadata:
  skill_id: "skl_i_bGDFwkS0zlxrqvmrNBYw"
  title: "Timed out fetching a new connection from the connection pool."
  version: "skv_Hp_N4S9EvSXxkXxE0WWdVw"
  updated: "2026-10-03T04:51:33.066445+00:00"
  canonical_url: "https://vectle.com/skills/skl_i_bGDFwkS0zlxrqvmrNBYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sheesha-labs/indus-hydraulics/commit/336456f1c638e51df2b47681c5e37cf6f0fc43ff\"]"
---

TL;DR: Something is holding connections and not giving them back, or the pool is just too small. Use one shared `PrismaClient` instance, set `connection_limit` to match your database, raise `pool_timeout` for slow cold starts, and put serverless traffic behind a pooler like PgBouncer or Supavisor.

```text
Timed out fetching a new connection from the connection pool. (Current connection pool timeout: 10, connection limit: 5)
```

## Steps

1. Make sure you create exactly one client and reuse it:
   ```ts
   // lib/prisma.ts
   import { PrismaClient } from '@prisma/client'
   const globalForPrisma = globalThis as unknown as { prisma?: PrismaClient }
   export const prisma = globalForPrisma.prisma ?? new PrismaClient()
   if (process.env.NODE_ENV !== 'production') globalForPrisma.prisma = prisma
   ```
   Expected: connection count on the database stops climbing with every request.

2. Size the pool in the connection string:
   ```
   postgresql://YOUR_HOST:5432/mydb?connection_limit=10&pool_timeout=20
   ```
   Expected: `pool_timeout=20` gives slow queries twice as long to get a connection before P2024 fires.

3. Serverless (Vercel, Lambda): point DATABASE_URL at your pooler in transaction mode with `?pgbouncer=true`, and keep a direct URL for migrations.
   Expected: P2024 under burst traffic drops sharply because the pooler multiplexes.

4. Find the leak: log `prisma.$queryRaw` connection counts or watch `pg_stat_activity` during the failure window.
   Expected: you see connections stuck in `idle in transaction`, which means a transaction was opened and never committed or rolled back.

## When to use
- The exact code is P2024, intermittent, worse under load or cold starts
- Connection count on the database climbs until queries start timing out

## When not to use
- P1001: nothing connects at all, the server is unreachable
- Every query is slow: that is a query performance problem, not pool exhaustion

## Compatibility
Prisma Client 4.x through 6.x. PostgreSQL and MySQL. Supabase, Neon, RDS.

### Variant phrasing: P2024 only during `next build` / prerender
Build-time data fetching opens many parallel connections. Raising `pool_timeout` for the build environment is the documented quick fix.

### Variant phrasing: P2024 with `connection_limit=1`
A limit of 1 serializes everything; any concurrent request waits. Raise it to at least your framework's concurrency.

## Why it happens
Prisma keeps a pool of database connections capped at `connection_limit`. Each query borrows one and returns it when done. If clients multiply (one per request), transactions leak, or the limit is smaller than your concurrency, new queries wait longer than `pool_timeout` and Prisma throws P2024.

## Edge cases
- Long-running transactions hold a connection for their whole life; keep transactions short.
- `connection_limit` counts per client instance, so two instances double your real connections.
- Statement timeouts on the database side surface as different errors; P2024 is specifically the pool wait expiring.

---

Source: [Vectle](https://vectle.com/skills/skl_i_bGDFwkS0zlxrqvmrNBYw). Version: `skv_Hp_N4S9EvSXxkXxE0WWdVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
