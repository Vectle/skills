---
name: "each-model-must-have-at-least-one-uniq-05aed3a47ba1ee88"
description: "Fixes the Prisma schema validation error 'Each model must have at least one unique criteria that has only required fields' (P1012) by giving the model a @id, @unique, or composite @@id/@@unique on required fields. Use when prisma validate or generate fails with this message. Not for database connection errors or migration failures."
metadata:
  skill_id: "skl_ofKQmSXU0Bj2Tdqhxd-1wg"
  title: "Each model must have at least one unique criteria that has only required fields."
  version: "skv_q8aUt9BbnD7JQehzxlNxHg"
  updated: "2026-10-03T04:45:12.298502+00:00"
  canonical_url: "https://vectle.com/skills/skl_ofKQmSXU0Bj2Tdqhxd-1wg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Add `@id`, `@unique`, or a composite `@@id`/`@@unique` to your model, on fields that are required (not optional). Then `npx prisma validate` passes. Prisma needs at least one unique way to address a single record.

```text
error: Each model must have at least one unique criteria that has only required fields.
```

## Steps

1. Find the model the error names and give it a unique criterion. Pick the first option that fits:
   ```prisma
   model User {
     id    Int    @id @default(autoincrement())
     email String @unique
   }
   ```
   or for composite keys:
   ```prisma
   model Membership {
     userId String
     orgId  String
     @@id([userId, orgId])
   }
   ```
   Expected: the criterion covers only required fields (no `?` on any of them).

2. Run validation:
   ```bash
   npx prisma validate
   ```
   Expected: `The schema at prisma/schema.prisma is valid`.

3. Regenerate the client and continue your migration:
   ```bash
   npx prisma generate
   ```
   Expected: `Generated Prisma Client` with no validation errors.

## When to use
- `prisma validate`, `prisma generate`, or `prisma migrate dev` fails with the exact unique-criteria message
- You are modeling a join table or a legacy table with no primary key

## When not to use
- The error is about a datasource URL or protocol: that is a different P1012 message
- You actually want keyless models (MongoDB): use `@@ignore` or the MongoDB connector rules instead

## Compatibility
Prisma schema validation, all versions 2.x through 7.x. PostgreSQL, MySQL, SQL Server, SQLite.

### Variant phrasing: `Each model must have at least one unique criteria that has only required fields` on a model where every field is optional
Making the unique field required is the point: `@unique` on an optional field still fails validation. Change the field to required or pick a different field.

## Why it happens
Prisma Client's `findUnique`, `update`, and `delete` need a guaranteed-unique lookup. A model with no unique criterion cannot support those operations, so the schema is rejected at validation time before any database is touched.

## Edge cases
- Legacy tables truly without a unique column: add a surrogate auto-increment id in the migration.
- Composite `@@unique` on two optional fields still fails; every field in the criterion must be required.
- Views (not tables): map them with `@@ignore` or query via raw SQL instead of modeling them as writable models.

---

Source: [Vectle](https://vectle.com/skills/skl_ofKQmSXU0Bj2Tdqhxd-1wg). Version: `skv_q8aUt9BbnD7JQehzxlNxHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
