---
name: "p1017-server-has-closed-the-connection-1f4f5f623a3d7bd0"
description: "This skill fixes Prisma error P1017, where the database server closes the connection mid-query. Use it when Prisma throws P1017 with PgBouncer, RDS Proxy, Neon, or Supabase poolers, or after idle periods. It covers pooler timeouts, stale connections, and connection_limit tuning."
metadata:
  skill_id: "skl_UpMY-ZRXxp5KRrbe1tXAxQ"
  title: "P1017: Server has closed the connection"
  version: "skv_OPnWkLklDvvSZu-ok8n60Q"
  updated: "2026-10-03T05:42:35.640178+00:00"
  canonical_url: "https://vectle.com/skills/skl_UpMY-ZRXxp5KRrbe1tXAxQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sagarsys/bengalivo-redesign/blob/HEAD/@docs/MIGRATION_TROUBLESHOOTING.md\"]"
---

## TL;DR
P1017 means the database server hung up on Prisma mid-query. This almost always happens with a connection pooler (PgBouncer, RDS Proxy, Neon pooled) that closes idle connections, or when the server restarts. Point Prisma at the pooler correctly, shorten Prisma's idle handling, or raise the pooler's idle timeout.

## The error
```text
Error: P1017
Server has closed the connection
```

## Fix it
1. **Check whether you are behind a pooler.** If your connection string uses port 6543 (Supabase), a `-pooler` host (Neon), or PgBouncer/RDS Proxy, the pooler is the prime suspect. Confirm with your provider's dashboard that idle connections get closed after N seconds.
   - Expected: you find an idle-timeout setting (often 60-300s) on the pooler.
2. **Set `connection_limit` and `pool_timeout` in your datasource URL.** Add query params so Prisma recycles connections before the pooler kills them:
   ```prisma
   datasource db {
     provider = "postgresql"
     url      = env("DATABASE_URL")
   }
   ```
   ```text
   postgresql://HOST:5432/DB?connection_limit=5&pool_timeout=10
   ```
   - Expected: `prisma db pull` or your app no longer throws P1017 on idle-then-query patterns.
3. **For PgBouncer in transaction mode, keep transactions short.** Long interactive transactions get killed first. Break work into smaller transactions.
   - Expected: P1017 stops appearing on long-running jobs.
4. **If it happens on deploys/restarts, add retry on P1017.** Wrap the query in a retry with backoff for this code specifically; a fresh connection succeeds.
   - Expected: transient P1017s during rolling restarts no longer fail the request.

## When to use
- P1017 appears after periods of inactivity, behind PgBouncer/RDS Proxy/Neon pooler/Supabase pooler.
- P1017 spikes during deployments or database restarts.

## When NOT to use
- The error is P1001 (can't reach server at all) or P1008 (operations timed out) - different fixes.
- Every query fails immediately, even the first one - that is a credentials/network issue, not closed idle connections.

## Compatibility
- Prisma ORM 2.x-6.x, PostgreSQL and MySQL. Pooler-specific settings vary by provider (Supabase, Neon, RDS).

## Root cause
The server or pooler terminates a TCP connection Prisma thought was alive (idle timeout, server restart, max lifetime). Prisma only discovers this when it tries to reuse the connection, and surfaces P1017.

## Edge cases
- Neon scale-to-zero closes connections; use the pooled connection string and expect cold starts.
- `pool_timeout=0` disables the timeout and can hang forever - keep it small but nonzero.
- Serverless (Lambda, Vercel) with many concurrent invocations can exhaust the pool; lower `connection_limit` per instance.


---

Source: [Vectle](https://vectle.com/skills/skl_UpMY-ZRXxp5KRrbe1tXAxQ). Version: `skv_OPnWkLklDvvSZu-ok8n60Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
