---
name: "an-operation-failed-because-it-depends-984dc67887fb9beb"
description: "Fixes Prisma error P2025 'An operation failed because it depends on one or more records that were required but not found' by checking the record exists before updating or deleting it, and handling the not-found case explicitly. Use when update, delete, or nested writes fail with P2025. Not for unique violations (P2002) or foreign key failures (P2003)."
metadata:
  skill_id: "skl_AZ5V9P5qaBe-5MHPO5sJhg"
  title: "An operation failed because it depends on one or more records that were required but not found."
  version: "skv_roopFa29phgmsSQznsUP7Q"
  updated: "2026-10-03T04:49:47.594059+00:00"
  canonical_url: "https://vectle.com/skills/skl_AZ5V9P5qaBe-5MHPO5sJhg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/refferq/refferq/blob/HEAD/docs/BUG_FIX_EMAIL_TEMPLATE_P2025.md\"]"
---

TL;DR: The record you are trying to update or delete is not there. Fetch it first with `findUnique`; when the lookup misses, return a not-found response instead of letting Prisma throw P2025. This almost always means stale client state or a record deleted by someone else.

```text
An operation failed because it depends on one or more records that were required but not found.
```

## Steps

1. Check existence before the write:
   ```ts
   const template = await prisma.emailTemplate.findUnique({ where: { id: input.id } })
   if (!template) {
     return { ok: false, message: 'Template not found. It may have been deleted.' }
   }
   await prisma.emailTemplate.update({ where: { id: input.id }, data URIs input.patch })
   ```
   Expected: stale ids get a clean not-found message; live ids update normally.

2. Keep a P2025 catch as a backstop for races (deleted between your check and your write):
   ```ts
   } catch (e) {
     if (e instanceof PrismaClientKnownRequestError && e.code === 'P2025') {
       return { ok: false, message: 'That record no longer exists.' }
     }
     throw e
   }
   ```
   Expected: concurrent deletes degrade to a friendly message.

3. For nested writes (`update` with nested `connect`/`update`), check the nested target too.
   Expected: the P2025 moves from a mystery to a named missing record.

## When to use
- The exact code is P2025 on update, delete, upsert-update-branch, or nested writes
- The id comes from a URL, a cached list, or another service

## When not to use
- P2003: the parent is missing on a create, which is a foreign key problem
- You expected the record to exist and it should never be missing: investigate who deleted it instead of masking the error

## Compatibility
Prisma Client 4.x through 6.x. All providers.

### Variant phrasing: P2025 on `deleteMany` or `updateMany`
Those do not throw P2025; they return `{ count: 0 }`. If you need not-found semantics there, check the count yourself.

### Variant phrasing: P2025 right after a create in the same request
You are likely writing to one database and reading from another (replica lag) or the create rolled back. Check your transaction and connection routing.

## Why it happens
`update` and `delete` in Prisma target exactly one record by unique criteria. When nothing matches, there is nothing to change, so Prisma throws P2025 rather than silently doing nothing. The usual causes are stale UI state, double-submits after a delete, or another process removing the row first.

## Edge cases
- Soft deletes: a `deletedAt` filter in your queries makes rows invisible while they still exist; P2025 then means 'soft-deleted', and you may want to surface that.
- `upsert` only throws P2025 from its update branch when the where clause references relations; the create branch never does.
- Batch imports: validate ids against the database in one query before the loop instead of catching per row.

---

Source: [Vectle](https://vectle.com/skills/skl_AZ5V9P5qaBe-5MHPO5sJhg). Version: `skv_roopFa29phgmsSQznsUP7Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
