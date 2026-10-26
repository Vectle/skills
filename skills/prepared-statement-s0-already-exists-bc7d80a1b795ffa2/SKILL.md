---
name: "prepared-statement-s0-already-exists-bc7d80a1b795ffa2"
description: "Fixes the Prisma error 'prepared statement already exists' (Postgres code 42P05) when connecting through PgBouncer in transaction mode, by adding pgbouncer=true to the connection string so Prisma stops using prepared statements. Use when queries fail with this error behind Supabase, Heroku, Railway, or any PgBouncer pooler. Not for direct connections or P2024 pool timeouts."
metadata:
  skill_id: "skl_83yMhigbfTF8B52AW7jg7Q"
  title: "prepared statement \"s0\" already exists"
  version: "skv_wclUuQ7xUMzz4VHJClnlTQ"
  updated: "2026-10-03T05:02:00.842452+00:00"
  canonical_url: "https://vectle.com/skills/skl_83yMhigbfTF8B52AW7jg7Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://supabase.com/docs/guides/troubleshooting/error-prepared-statement-xxx-already-exists-3laqeM\"]"
---

TL;DR: Add `?pgbouncer=true` to your DATABASE_URL. PgBouncer in transaction mode cannot do prepared statements, and that one parameter tells Prisma to stop using them. Keep a separate direct connection (no pooler) for migrations.

```text
Error: prepared statement "s0" already exists
```

## Steps

1. Confirm you are behind PgBouncer in transaction mode: your connection string points at a pooler port (for example Supabase port 6543) or your provider says 'transaction mode'.
   Expected: the error appears on queries, with Postgres code 42P05 in the logs.

2. Add the Prisma PgBouncer flag to the app's connection string:
   ```
   postgresql://YOUR_HOST:6543/postgres?pgbouncer=true
   ```
   Keep your real username, password, and host; only the parameter is new.
   Expected: Prisma logs no longer prepare statements on this datasource.

3. Keep migrations on a direct connection. Set a separate variable for them:
   ```
   DIRECT_URL="postgresql://YOUR_HOST:5432/postgres"
   ```
   Expected: `prisma migrate deploy` runs against the direct port, the app runs against the pooler.

4. Re-run the failing queries.
   Expected: the 'already exists' errors stop.

## When to use
- The error is `prepared statement ... already exists` with code 42P05 and you connect through PgBouncer / Supavisor / a pooler
- Supabase, Heroku, Railway, or any hosted Postgres with a transaction-mode pooler

## When not to use
- Direct connections to Postgres: prepared statements work fine there, so this error means something else
- P2024 pool timeouts: that is pool exhaustion, not prepared statements

## Compatibility
Prisma Client 4.x through 6.x. Any PgBouncer deployment in transaction pooling mode.

### Variant phrasing: `prepared statement "$z" already exists`
Same error, different generated statement name. The fix is identical.

### Variant phrasing: error only in production, not locally
Local dev usually connects directly (no pooler), so the bug only appears where the pooler sits. That mismatch is expected.

## Why it happens
Prisma names its prepared statements per connection. PgBouncer in transaction mode reuses server connections across clients, so a statement name prepared by one client collides with the same name from another, and Postgres rejects the duplicate with 42P05. The `pgbouncer=true` flag makes Prisma use simple query protocol instead, which needs no prepared statements.

## Edge cases
- Session-mode poolers (Supabase port 5432) support prepared statements; you only need the flag for transaction mode.
- The flag must be on the URL the Prisma Client uses, not just the migration URL.
- Some providers need `&statement_cache_size=0` style extras on other drivers; for Prisma the single flag is the documented fix.

---

Source: [Vectle](https://vectle.com/skills/skl_83yMhigbfTF8B52AW7jg7Q). Version: `skv_wclUuQ7xUMzz4VHJClnlTQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
