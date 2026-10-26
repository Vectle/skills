---
name: "p1000-authentication-failed-against-da-f75e7711899b8560"
description: "Fixes Prisma error P1000 'Authentication failed against database server' when the database is reachable but rejects the credentials, most often because a native Postgres install already holds port 5432 while the app points at the Docker container. Use when P1000 names the right server. Not for unreachable servers (P1001) or missing databases (P1003)."
metadata:
  skill_id: "skl__wC39O_PIqWhjVnO9Y05Ww"
  title: "P1000: Authentication failed against database server"
  version: "skv_FLqj8MhVr4bF50ZY1iTNGg"
  updated: "2026-10-03T04:43:39.77326+00:00"
  canonical_url: "https://vectle.com/skills/skl__wC39O_PIqWhjVnO9Y05Ww"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/mjeffv2/printexchange\"]"
---

TL;DR: P1000 means the server is up but said no to your credentials, or you are talking to the wrong server. First check whether something else already owns the port (a native Postgres install is the classic), then fix the credentials or the port mapping.

```text
Error: P1000: Authentication failed against database server
```

## Steps

1. Check who actually owns the port:
   ```bash
   ss -ltnp | grep 5432
   ```
   Expected: if you see a native `postgres` process instead of docker-proxy, your app is authenticating against the wrong server. That is the cause.

2. Pick one fix:
   - Option A: map the container to a free port and update the connection string:
     ```yaml
     services:
       db:
         ports: ["5433:5432"]
     ```
     then use port `5433` in DATABASE_URL.
   - Option B: stop the native server (`brew services stop postgresql`, `sudo systemctl stop postgresql`) so the container owns 5432.
   Expected: `psql` with the same credentials you gave Prisma now connects.

3. Re-check the credentials themselves: user, password, and database name must match a real role. Special characters in the password must be URL-encoded in DATABASE_URL.
   Expected: connecting with a plain `psql` client using the same values succeeds.

4. Re-run your app.
   Expected: P1000 gone.

## When to use
- The exact code is P1000 and the server host is reachable
- Local Docker setups where a native database may also be installed

## When not to use
- P1001: the server is not reachable at all, fix host/port first
- `password authentication failed` from `psql` with the provider's own connection string: the password itself is wrong, reset it at the provider

## Compatibility
Prisma Client 4.x through 6.x. PostgreSQL and MySQL.

### Variant phrasing: P1000 on a managed provider after rotating the password
Re-copy the connection string from the dashboard. Stale strings with the old password keep failing until every consumer is updated.

### Variant phrasing: P1000 with special characters in the password
`@`, `/`, `#`, and `:` in a password break URL parsing. Percent-encode them (`%40`, `%2F`, `%23`, `%3A`).

## Why it happens
Authentication happens against whichever server answers on the host and port. When two servers can answer (native + container), the app silently talks to the wrong one and no password will ever be right. URL parsing mangling special characters is the second most common cause.

## Edge cases
- SCRAM vs md5: very old clients against new servers can fail auth even with the right password; update the client.
- Case sensitivity: role names are case-sensitive; `Postgres` is not `postgres`.
- If you use a connection pooler, the pooler user and the database user may differ; authenticate as the pooler user.

---

Source: [Vectle](https://vectle.com/skills/skl__wC39O_PIqWhjVnO9Y05Ww). Version: `skv_FLqj8MhVr4bF50ZY1iTNGg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
