---
name: "relation-users-does-not-exist-bb1b586699b5f306"
description: "This skill fixes the Postgres error relation does not exist when using Drizzle ORM. Use it when Drizzle queries fail because the table was never created, migrations did not run, or the schema name is wrong. It covers drizzle-kit push, migrate, and schema naming."
metadata:
  skill_id: "skl_XVCMOJYo66uU5wvbVNCRwA"
  title: "relation \"users\" does not exist"
  version: "skv_ugzpZQIlDTwcM3UfTsrr-w"
  updated: "2026-10-03T06:00:19.976166+00:00"
  canonical_url: "https://vectle.com/skills/skl_XVCMOJYo66uU5wvbVNCRwA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/caiovaccaro/async-story-vote/blob/HEAD/database/README.md\"]"
---

## TL;DR
relation "users" does not exist means Postgres has no such table - your Drizzle schema was never applied to this database. Run the migration (`drizzle-kit migrate`) or push the schema (`drizzle-kit push`), and make sure you are connected to the right database.

## The error
```text
PostgresError: relation "users" does not exist
```

## Fix it
1. **Confirm you are on the right database.** Print the connection string's database name (redacted) and compare with where you think the tables are. Wrong-database is the top cause.
   - Expected: the connected database is the one you migrated.
2. **Apply the schema.** For drizzle-kit:
   ```bash
   npx drizzle-kit push
   ```
   or with migrations:
   ```bash
   npx drizzle-kit migrate
   ```
   - Expected: tables created, the query succeeds.
3. **Check the schema name.** If your tables live in a non-public schema, Drizzle needs `pgSchema("myschema", ...)` and the database role needs USAGE on it. Unqualified `users` resolves to the search_path, usually public.
   - Expected: qualified or search_path-correct table references.
4. **Check table-name casing.** Drizzle lowercases unquoted names; a table created as `"Users"` (quoted) is a different relation from `users`. Keep names lowercase or quote consistently.
   - Expected: the relation name matches exactly.

## When to use
- relation does not exist on a table Drizzle defines.
- Fresh database, new environment, or after a database reset.

## When NOT to use
- column does not exist - the table is there, a column is missing (schema drift).
- Auth/connection errors - the query never reached Postgres.

## Compatibility
- Drizzle ORM with drizzle-kit, PostgreSQL.

## Root cause
Drizzle builds SQL from your TypeScript schema but does not create tables at runtime. If migrations/push never ran against the connected database, Postgres reports the missing relation.

## Edge cases
- `drizzle-kit push` is for prototyping; use versioned `migrate` in production.
- Multiple schemas: `pgTable` without `pgSchema` always targets the search_path default.


---

Source: [Vectle](https://vectle.com/skills/skl_XVCMOJYo66uU5wvbVNCRwA). Version: `skv_ugzpZQIlDTwcM3UfTsrr-w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
