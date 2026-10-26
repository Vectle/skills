---
name: "p1003-database-mydb-does-not-exist-on-03d1db6ed0394f57"
description: "Fixes Prisma error P1003 'Database does not exist on the database server' by creating the missing database and then running migrations against it. Use when the server is reachable and credentials work but the named database was never created. Not for unreachable servers (P1001) or auth failures (P1000)."
metadata:
  skill_id: "skl_ffZEXSlHyTNW7DjNX3zFDg"
  title: "P1003: Database `mydb` does not exist on the database server at `YOUR_HOST:5432`."
  version: "skv_aSpc6Wfv1zqRfA4g-jmWQg"
  updated: "2026-10-03T04:58:57.385491+00:00"
  canonical_url: "https://vectle.com/skills/skl_ffZEXSlHyTNW7DjNX3zFDg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/rhymion/app-generator/blob/HEAD/docs/knowledge/troubleshooting.md\"]"
---

TL;DR: The server is fine, the database just was never created. Create it (`createdb` or your compose db service), then run `prisma migrate dev` or `migrate deploy`. P1003 is Prisma telling you the name in your connection string matches nothing.

```text
Error: P1003: Database `mydb` does not exist on the database server at `YOUR_HOST:5432`.
```

## Steps

1. Confirm the database is really missing:
   ```bash
   psql -h YOUR_HOST -U postgres -lqt | cut -d '|' -f 1 | grep -w mydb
   ```
   Expected: no output. If it prints the name, your connection string points at the wrong server.

2. Create it. Pick the one that matches your setup:
   ```bash
   createdb -h YOUR_HOST -U postgres mydb
   ```
   or start the compose service that owns it:
   ```bash
   docker compose up -d db
   ```
   Expected: the name now appears in the database list.

3. Build the schema inside it:
   ```bash
   npx prisma migrate deploy
   ```
   Expected: `All migrations have been successfully applied.` P1003 is gone.

## When to use
- The exact code is P1003 and you can connect to the server itself
- Fresh setups, new branches, or restored servers where the database was never created

## When not to use
- P1001: you cannot reach the server at all
- P1000: the server rejects your credentials before the database name even matters

## Compatibility
Prisma Client and Migrate 4.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: P1003 in tests that use a separate test database
Create the test database in your test setup script before migrations run, not after.

### Variant phrasing: P1003 after dropping the database by hand
Recreate it and re-run `migrate deploy`; there is no shortcut around the missing database.

## Why it happens
Prisma connects to the server first, then selects the database named in the connection string. `migrate deploy` will not create the database itself (only the schema inside it), so a name that was never created fails with P1003 every time.

## Edge cases
- Case sensitivity: `MyDB` and `mydb` are different names on most servers; match the connection string exactly.
- Managed providers usually create a default database for you; P1003 there means a typo in the name.
- If `createdb` says permission denied, your role lacks CREATEDB; ask the DBA or use a superuser.

---

Source: [Vectle](https://vectle.com/skills/skl_ffZEXSlHyTNW7DjNX3zFDg). Version: `skv_aSpc6Wfv1zqRfA4g-jmWQg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
