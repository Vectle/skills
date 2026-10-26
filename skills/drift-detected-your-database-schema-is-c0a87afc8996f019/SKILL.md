---
name: "drift-detected-your-database-schema-is-c0a87afc8996f019"
description: "Fixes the Prisma 'Drift detected: Your database schema is not in sync with your migration history' error by deciding whether the database or the migration history is the source of truth, then reconciling the two. Use when migrate dev refuses to run because of drift. Not for failed migrations (P3018) or non-empty databases (P3005)."
metadata:
  skill_id: "skl_0_lIlZsWXDQf6I_JfFmmLg"
  title: "Drift detected: Your database schema is not in sync with your migration history"
  version: "skv_XmAE0ns4IV7O2MwkPjBn5w"
  updated: "2026-10-03T04:57:26.304106+00:00"
  canonical_url: "https://vectle.com/skills/skl_0_lIlZsWXDQf6I_JfFmmLg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/digohq/app-starter/blob/HEAD/docs/troubleshooting.md\"]"
---

TL;DR: Something changed the database without going through migrations. Decide which side is right: if the database changes were intentional, turn them into a migration; if they were accidental, reset the database back to the history. Then `migrate dev` works again.

```text
Drift detected: Your database schema is not in sync with your migration history.
```

## Steps

1. See exactly what drifted:
   ```bash
   npx prisma migrate diff --from-migrations ./prisma/migrations --to-schema-datamodel prisma/schema.prisma --shadow-database-url "$SHADOW_DATABASE_URL"
   ```
   Expected: a diff showing the statements that differ between history and schema.

2. If the database changes were INTENTIONAL (a hotfix applied by hand, a DBA change):
   ```bash
   npx prisma migrate dev --name capture_manual_changes
   ```
   Expected: Prisma generates a migration from the drift and applies it; history and database agree again.

3. If the changes were ACCIDENTAL (someone ran db push, a script wrote DDL):
   ```bash
   npx prisma migrate reset
   ```
   Expected: the dev database is rebuilt from the migration history; drift gone. Only do this where data loss is acceptable.

4. Re-run `npx prisma migrate dev`.
   Expected: no drift error; normal migration flow resumes.

## When to use
- The exact message is `Drift detected` on `migrate dev`
- Someone edited the database directly, ran `db push`, or restored a dump over the dev database

## When not to use
- Production: never `migrate reset` there; capture the drift as a migration or reconcile by hand
- The message is P3018 instead: a migration failed, which is a different recovery

## Compatibility
Prisma Migrate 3.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: drift after a teammate ran `prisma db push`
`db push` changes the database without writing history. The push was probably intentional, so capture it with `migrate dev --name` as in step 2.

## Why it happens
Prisma Migrate treats the migration history as the single source of truth. Any DDL that bypasses it (manual SQL, db push, restores) makes the database disagree with history, and `migrate dev` stops rather than build on a foundation it cannot verify.

## Edge cases
- `db push` accepts data loss by design; teams that mix push and migrate hit drift constantly. Pick one workflow per environment.
- If drift reappears on every run, something in your pipeline writes DDL outside migrations; find it before reconciling again.
- Shadow database URL problems can masquerade as drift; make sure the diff command actually ran before trusting its output.

---

Source: [Vectle](https://vectle.com/skills/skl_0_lIlZsWXDQf6I_JfFmmLg). Version: `skv_XmAE0ns4IV7O2MwkPjBn5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
