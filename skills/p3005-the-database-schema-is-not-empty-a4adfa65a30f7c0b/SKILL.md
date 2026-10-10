---
name: "p3005-the-database-schema-is-not-empty-a4adfa65a30f7c0b"
description: "Fixes Prisma error P3005 'The database schema is not empty' during migrate deploy by baselining the existing database: mark the initial migration as already applied with migrate resolve --applied instead of letting migrate try to create tables that exist. Use when deploying to a database that was created outside Prisma migrations. Not for drift errors or failed migrations."
metadata:
  skill_id: "skl_vYl4EiZTltdySVpd9UICiA"
  title: "P3005: The database schema is not empty."
  version: "skv_p9VRIp7wSagkNJKG_Vmlaw"
  updated: "2026-10-03T04:53:04.627468+00:00"
  canonical_url: "https://vectle.com/skills/skl_vYl4EiZTltdySVpd9UICiA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Your database already has tables but Prisma has no record of creating them. Tell Prisma the current schema matches your first migration with `prisma migrate resolve --applied "[first-migration-name]"`, then deploy normally. Do not drop the database to fix this.

```text
Error: P3005: The database schema is not empty.
```

## Steps

1. Confirm the situation: tables exist, migration history does not:
   ```bash
   npx prisma migrate status
   ```
   Expected: it reports P3005 or shows every migration as pending against a non-empty database.

2. Verify your first migration actually describes the existing schema. Diff it:
   ```bash
   npx prisma migrate diff --from-migrations ./prisma/migrations --to-schema-datamodel prisma/schema.prisma --shadow-database-url "$SHADOW_DATABASE_URL"
   ```
   Expected: an empty diff. If the diff is not empty, fix the schema first; baselining a mismatch just moves the pain.

3. Baseline the database:
   ```bash
   npx prisma migrate resolve --applied "20240101000000_init"
   ```
   Use the real name of your first migration folder.
   Expected: `Migration 20240101000000_init marked as applied.`

4. Deploy:
   ```bash
   npx prisma migrate deploy
   ```
   Expected: `No pending migrations to apply` or only genuinely new migrations apply.

## When to use
- The exact code is P3005 on `migrate deploy` against a database built by `db push`, a dump restore, or another tool
- Adopting Prisma Migrate on a brownfield database

## When not to use
- The database is disposable (local dev): `prisma migrate reset` is faster and honest
- You have real migration history and a migration failed halfway: that is P3018, not P3005

## Compatibility
Prisma Migrate 3.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: P3005 right after `prisma db push` in staging
`db push` creates tables without writing migration history. Baseline once, then use `migrate deploy` from then on.

### Variant phrasing: P3005 on a restored production dump
The dump has tables but no `_prisma_migrations` rows. Baseline against the migration that matches the dumped schema.

## Why it happens
`migrate deploy` refuses to run its CREATE TABLE statements against a non-empty database because that would destroy or duplicate existing tables. The `--applied` baseline writes a history row claiming the first migration already ran, so Prisma treats the existing schema as its starting point.

## Edge cases
- Baseling the wrong migration name silently lies to Prisma; later migrations may fail in confusing ways. Verify with the diff in step 2.
- If the existing schema only *partly* matches, consider `db pull` into a fresh schema first to capture reality.
- Some teams baseline every environment once and document the command in their deploy runbook so nobody re-runs it.

---

Source: [Vectle](https://vectle.com/skills/skl_vYl4EiZTltdySVpd9UICiA). Version: `skv_p9VRIp7wSagkNJKG_Vmlaw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
