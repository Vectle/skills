---
name: "unique-constraint-failed-on-the-fields-e80aa781cb9ebd9c"
description: "Fixes Prisma error P2002 'Unique constraint failed on the fields' by catching the known request error in application code and returning a friendly duplicate message, or by using upsert instead of create. Use when a create or update violates a @unique field. Not for foreign key failures (P2003) or missing records (P2025)."
metadata:
  skill_id: "skl_SmuM0a5IjyagJBBS_TThgQ"
  title: "Unique constraint failed on the fields: (`email`)"
  version: "skv_NsXz3RmwiOWdYODGrMxJng"
  updated: "2026-10-03T04:46:39.835905+00:00"
  canonical_url: "https://vectle.com/skills/skl_SmuM0a5IjyagJBBS_TThgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: P2002 is not a bug in Prisma, it is your database doing its job. Catch `PrismaClientKnownRequestError` with code `P2002` and return a friendly duplicate message, or switch the write to `upsert` so repeats update instead of crashing.

```text
Unique constraint failed on the fields: (`email`)
```

## Steps

1. Catch the error where you create the record:
   ```ts
   import { PrismaClientKnownRequestError } from '@prisma/client/runtime/library'

   try {
     await prisma.user.create({ data URIs { email: '[user email]', name: 'Ada' } })
   } catch (e) {
     if (e instanceof PrismaClientKnownRequestError && e.code === 'P2002') {
       return { ok: false, message: 'That email is already registered.' }
     }
     throw e
   }
   ```
   Expected: submitting a duplicate email returns your friendly message, not a 500.

2. Or make the write idempotent with upsert when repeats should update:
   ```ts
await prisma.vehicle.upsert({
     where: { plateNumber: 'ABC-123' },
     update: { mileage: 90000 },
     create: { plateNumber: 'ABC-123', mileage: 90000 },
   })
   ```
   Expected: running the same import twice leaves one record with the latest values.

3. Check `e.meta.target` to name the exact field in your message.
   Expected: `meta.target` lists the fields from the error, for example `['email']`.

## When to use
- The exact code is P2002 on a create or update against a `@unique` field
- Signup, invite, or import flows where duplicates are a normal user action

## When not to use
- P2003: that is a foreign key problem, the parent record is missing
- You actually want duplicates allowed: drop the `@unique` attribute and migrate

## Compatibility
Prisma Client 4.x through 6.x. All providers.

### Variant phrasing: `Unique constraint failed on the fields: (`phone`)`
Same fix; read the field list in the message to know which constraint fired.

### Variant phrasing: P2002 on a composite `@@unique([a, b])`
The combination must be unique, not each field alone. Either change the data or change the constraint.

## Why it happens
The `@unique` attribute creates a real database unique index. When two writes target the same value, the database rejects the second one and Prisma surfaces it as P2002. The fix belongs in application code because only the app knows whether a duplicate is a user error or an idempotent retry.

## Edge cases
- Race conditions: a find-then-create check still races under concurrency; the P2002 catch is the reliable guard.
- Case sensitivity: `[recipient email]` and `[recipient email]` are different values to most databases; normalize case before writing if you want them treated as one.
- Soft deletes: a unique index still covers soft-deleted rows; use a partial index or composite unique with the deleted flag if you need reuse.

---

Source: [Vectle](https://vectle.com/skills/skl_SmuM0a5IjyagJBBS_TThgQ). Version: `skv_NsXz3RmwiOWdYODGrMxJng`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
