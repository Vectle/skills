---
name: "p1001-can-t-reach-database-server-at-y-d4a56ea505d5c863"
description: "Fixes Prisma error P1001 'Can't reach database server' by diagnosing which part of the connection path is wrong: host, port, pooler mode, or a server that is not actually running. Use when Prisma fails to open any connection at all. Not for authentication failures (P1000) or missing databases (P1003)."
metadata:
  skill_id: "skl_y_0StHMX7UOS9xAV7g0upQ"
  title: "P1001: Can't reach database server at `YOUR_HOST`:`5432`"
  version: "skv_zU3BmiliYjcbQoDHNaIkdA"
  updated: "2026-10-03T04:42:06.209331+00:00"
  canonical_url: "https://vectle.com/skills/skl_y_0StHMX7UOS9xAV7g0upQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Check the host and port in your connection string first, then whether the database is actually listening, then whether you are pointing at a pooler port by mistake. In most reports this error is a wrong host/port or a stopped server, not a Prisma bug.

```text
Error: P1001: Can't reach database server at `YOUR_HOST`:`5432`
```

## Steps

1. Verify the host and port are what you think:
   ```bash
   node -e "const u=new URL(process.env.DATABASE_URL); console.log(u.hostname+':'+u.port)"
   ```
   Expected: the host and port of your real database. A stale port (for example `5433` from an old setup) is the single most common cause.

2. Check the server is listening:
   ```bash
   nc -zv YOUR_HOST 5432
   ```
   Expected: `succeeded`. If it fails, start the database (for example `docker compose up -d db`) and retry.

3. If you connect through Supabase / a pooler, use the matching port and mode: session-mode pooler on port 5432 for Prisma Client, transaction-mode pooler on 6543 only with `?pgbouncer=true`. Mixing them produces P1001.
   Expected: with the right port and mode, `npx prisma db pull` connects.

4. Re-run your app or `npx prisma validate`.
   Expected: P1001 gone. If it becomes P1000, the host is reachable and the credentials are now the problem.

## When to use
- The exact code is P1001 `Can't reach database server`
- The failure is immediate on connect, not after a timeout (that would be P2024)

## When not to use
- P1000 (authentication failed): the server is reachable, your credentials are wrong
- P1003 (database does not exist): the server is reachable, the named database is missing

## Compatibility
Prisma Client 4.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: P1001 in Docker Compose where the host is the loopback address
Inside a container, the loopback address means the container itself. Use the service name (for example `db`) as the host instead.

### Variant phrasing: P1001 right after changing providers or regions
Connection strings go stale on migration. Re-copy the current connection string from the provider dashboard.

## Why it happens
P1001 means the TCP connection never opened: wrong host, wrong port, firewall, stopped server, or a pooler/direct mismatch. Prisma never got far enough to attempt authentication, which is why the fix is always in the network path or the server state.

## Edge cases
- IPv6-only hosts: some resolvers return an IPv6 address the client cannot route; try the IPv4 address explicitly.
- `sslmode` or `sslaccept` params do not cause P1001; they surface later in the handshake.
- Cloud SQL / RDS proxy endpoints change on failover; re-resolve the hostname.

---

Source: [Vectle](https://vectle.com/skills/skl_y_0StHMX7UOS9xAV7g0upQ). Version: `skv_zU3BmiliYjcbQoDHNaIkdA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
