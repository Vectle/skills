---
name: "p3018-a-migration-failed-to-apply-new-0349fe4460abdf1f"
description: "Fixes Prisma error P3018 'A migration failed to apply' by deciding whether the failed migration's changes actually landed, then marking it rolled back or applied with migrate resolve. Use when migrate deploy stops with P3018 and new migrations are blocked. Not for P3006 shadow database failures or P3005 non-empty schema errors."
metadata:
  skill_id: "skl_iSxa_kV6rcMpgT732pEFDQ"
  title: "P3018: A migration failed to apply. New migrations cannot be applied before the error is recovered from."
  version: "skv_cZ79gR4zeoKD6VRc_cASYg"
  updated: "2026-10-03T04:55:59.063423+00:00"
  canonical_url: "https://vectle.com/skills/skl_iSxa_kV6rcMpgT732pEFDQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/devwithabhishek/kridha/blob/HEAD/docs/LEARNINGS.md\"]"
---

TL;DR: A migration died halfway and Prisma froze the history until you resolve it. Check whether its changes actually landed in the database, fix the partial state by hand, then run `prisma migrate resolve --rolled-back "[name]"` (or `--applied` if the changes did land) and redeploy.

```text
Error: P3018: A migration failed to apply. New migrations cannot be applied before the error is recovered from.
```

## Steps

1. Find the failed migration:
   ```bash
   npx prisma migrate status
   ```
   Expected: it names the failed migration and shows everything after it as blocked.

2. Inspect what actually landed. Compare the migration SQL against the real database (for example, check whether the table or column exists).
   Expected: you can answer yes or no to 'did the failed migration's changes get applied?'

3. Resolve it honestly:
   - Changes did NOT land: repair any partial state manually, then
     ```bash
     npx prisma migrate resolve --rolled-back "20240102_add_orders"
     ```
   - Changes DID land (the failure was after the DDL, e.g. in a data step):
     ```bash
     npx prisma migrate resolve --applied "20240102_add_orders"
     ```
   Expected: `Migration 20240102_add_orders marked as rolled back.` (or applied).

4. Fix the migration file if it was buggy, then redeploy:
   ```bash
   npx prisma migrate deploy
   ```
   Expected: the fixed migration applies and later ones follow.

## When to use
- The exact code is P3018 and `migrate status` shows a failed migration blocking the queue
- A deploy died mid-migration (OOM, statement timeout, bad SQL)

## When not to use
- P3006: the failure was on the shadow database, the real database is untouched
- You want to undo a migration that applied cleanly: write a new migration instead, Prisma has no down migrations

## Compatibility
Prisma Migrate 3.x through 6.x. PostgreSQL, MySQL, SQL Server.

### Variant phrasing: P3018 with `database error: relation already exists`
The DDL half-applied before the crash. Drop the partially created objects by hand, then resolve as rolled back.

## Why it happens
Prisma records each migration as failed in `_prisma_migrations` and refuses to run anything newer until a human declares the outcome. `--rolled-back` means 'I cleaned up, pretend it never ran'; `--applied` means 'the changes are really there, record it as done'. Picking the wrong one corrupts the history, so the manual inspection in step 2 is the whole job.

## Edge cases
- Never edit a failed migration file and re-run deploy without resolving: Prisma checksums the file and the history row stays failed.
- On production, practice the manual repair on a restored copy first.
- If the failed migration is the very first one and the database is otherwise empty, `migrate reset` on a scratch database is simpler than surgery.

---

Source: [Vectle](https://vectle.com/skills/skl_iSxa_kV6rcMpgT732pEFDQ). Version: `skv_cZ79gR4zeoKD6VRc_cASYg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
