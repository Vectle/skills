---
name: "the-table-public-user-does-not-exist-i-d2e34b551d64c1bf"
description: "Fixes Prisma error P2021 'The table does not exist in the current database' by applying the missing migrations or pushing the schema so the table actually gets created. Use when queries fail with P2021 after a deploy or a schema change. Not for drift errors or failed migrations."
metadata:
  skill_id: "skl__SgJSF85CoEg9YRJKDWa6A"
  title: "The table `public.User` does not exist in the current database."
  version: "skv_l2pjgPgyOsjdqJhs8RSOlQ"
  updated: "2026-10-03T05:09:49.37129+00:00"
  canonical_url: "https://vectle.com/skills/skl__SgJSF85CoEg9YRJKDWa6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/braedonsaunders/bidwright/commit/5a4b2e8f16ff6237494006b5e8311d32bea9fac6\"]"
---

TL;DR: The table was never created in this database. Run `prisma migrate deploy` (or `prisma db push` if you do not use migration history here) against the database your app actually connects to, and the table appears. P2021 means the schema and the database disagree, and the database is the one behind.

```text
The table `public.User` does not exist in the current database.
```

## Steps

1. Check what Prisma thinks is pending:
   ```bash
   npx prisma migrate status
   ```
   Expected: it lists unapplied migrations, or reports the database is in sync (which means you are pointed at the wrong database).

2. Apply the migrations to the right database:
   ```bash
   npx prisma migrate deploy
   ```
   Expected: `All migrations have been successfully applied.`

3. If this environment does not use migration history (prototypes, `db push` workflows):
   ```bash
   npx prisma db push
   ```
   Expected: `Your database is now in sync with your Prisma schema.` Missing tables are created.

4. Re-run the failing query.
   Expected: P2021 gone; the query returns rows.

## When to use
- The exact code is P2021 naming a table your schema defines
- After a deploy, a new environment, or adding a model without generating a migration

## When not to use
- The table exists but the query still fails: check the schema name (`public.` vs your schema) and the connection string
- `migrate status` says everything is applied: you are connected to the wrong database; fix DATABASE_URL

## Compatibility
Prisma Client and Migrate 2.x through 6.x. All providers.

### Variant phrasing: P2021 right after adding a model to schema.prisma
You added the model but never ran `migrate dev --name`. Generate and apply the migration.

### Variant phrasing: P2021 only in production, fine locally
The production deploy skipped `migrate deploy` (the Dockerfile ran only `prisma generate`). Add migrate deploy to the container entrypoint or release command.

## Why it happens
`prisma generate` creates client code but touches no database. Tables only appear when a migration runs (`migrate deploy`, `migrate dev`) or the schema is pushed (`db push`). Any pipeline that generates without migrating ships code that references tables that do not exist.

## Edge cases
- Marking a migration applied without running it (a bad baseline) produces exactly this: history says done, tables say otherwise. Use `db push` to reconcile, as the source commit did.
- Multi-schema Postgres: the table may exist in another schema; check `@@schema` mappings.
- `db push` with `--accept-data-loss` can drop columns; prefer `migrate deploy` wherever history exists.

---

Source: [Vectle](https://vectle.com/skills/skl__SgJSF85CoEg9YRJKDWa6A). Version: `skv_l2pjgPgyOsjdqJhs8RSOlQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
