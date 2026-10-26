---
name: "p3006-migration-20240101-init-failed-t-06cf8441b55f52cb"
description: "Fixes Prisma error P3006 'Migration failed to apply cleanly to the shadow database' by finding the SQL in the migration that the empty shadow database cannot run, usually generated columns, extensions, or permissions, and rewriting it. Use when migrate dev or migrate deploy fails with P3006. Not for P3018 failed migrations on the real database."
metadata:
  skill_id: "skl_Un2KBy6KWRegkMHGpf893w"
  title: "P3006: Migration `20240101_init` failed to apply cleanly to the shadow database."
  version: "skv_cO_xiC2Wmz1nq0eCuWdGZQ"
  updated: "2026-10-03T04:54:32.625449+00:00"
  canonical_url: "https://vectle.com/skills/skl_Un2KBy6KWRegkMHGpf893w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/devwithabhishek/kridha/blob/HEAD/docs/LEARNINGS.md\"]"
---

TL;DR: P3006 is about the *shadow* database, not your real one. Some statement in the migration cannot run against a completely empty database. Find it, rewrite it so it works from empty, and the migration proceeds.

```text
Error: P3006: Migration `20240101_init` failed to apply cleanly to the shadow database.
```

## Steps

1. Read the full error output. Prisma prints the failing statement and the database's complaint below the P3006 line.
   Expected: you can name the exact statement, for example a `GENERATED ALWAYS AS` column or a `CREATE EXTENSION` call.

2. Fix the usual suspects in the migration SQL:
   - Generated columns referencing functions unavailable in the shadow database: simplify the expression or create it in a later migration.
   - `CREATE EXTENSION`: the shadow database role may lack permission; pre-create the extension on the shadow database or move it to a manual setup step.
   - Statements assuming existing data or tables: guard them or split them into a second migration.
   Expected: the migration file now contains only statements that run on an empty database.

3. Re-run:
   ```bash
   npx prisma migrate dev
   ```
   Expected: `Your database is now in sync with your schema` instead of P3006.

## When to use
- The exact code is P3006 during `migrate dev` or `migrate deploy`
- The migration works on your dev database but fails in CI or on a teammate's machine

## When not to use
- The migration failed on the real database: that is P3018, and the recovery is different
- The error is about drift between schema and history: that is the drift error, not P3006

## Compatibility
Prisma Migrate 3.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: P3006 mentioning `permission denied for database`
The shadow database user cannot do what the migration asks. Grant the permission on the shadow database or remove the privileged statement from the migration.

## Why it happens
Before applying a migration for real, Prisma replays it on a temporary empty shadow database to validate it. Anything that assumes a non-empty database, special permissions, or extensions not present there fails the replay, even though the same SQL worked on your lived-in dev database.

## Edge cases
- `SHADOW_DATABASE_URL` unset: Prisma creates the shadow database automatically, but on some providers you must supply one explicitly.
- Editing a migration that already applied to production is forbidden; only fix migrations that have never left your machine.
- If the statement is genuinely needed and shadow-hostile, some teams set `shadowDatabaseUrl` to a database where they pre-install the extension.

---

Source: [Vectle](https://vectle.com/skills/skl_Un2KBy6KWRegkMHGpf893w). Version: `skv_cO_xiC2Wmz1nq0eCuWdGZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
