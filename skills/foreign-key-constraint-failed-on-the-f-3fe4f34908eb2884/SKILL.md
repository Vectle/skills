---
name: "foreign-key-constraint-failed-on-the-f-3fe4f34908eb2884"
description: "Fixes Prisma error P2003 'Foreign key constraint failed on the field' by verifying the referenced parent record exists before creating the child, and returning a clear not-found message when it does not. Use when creating or linking records fails with P2003. Not for unique violations (P2002) or missing records on update (P2025)."
metadata:
  skill_id: "skl_CrcilKTeDpPquGr8aqWp8w"
  title: "Foreign key constraint failed on the field: `authorId`"
  version: "skv_RFKwGxcufcLz2aK_EUZXAg"
  updated: "2026-10-03T04:48:10.459155+00:00"
  canonical_url: "https://vectle.com/skills/skl_CrcilKTeDpPquGr8aqWp8w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/im-ushan-ikshana/fuel-quota-management/blob/HEAD/backend/docs/PRISMA_ERROR_HANDLING.md\"]"
---

TL;DR: Look up the parent record before you create the child. If the parent lookup misses, return a clear not-found message instead of letting the database throw P2003. The error means the id you are linking to does not exist.

```text
Foreign key constraint failed on the field: `authorId`
```

## Steps

1. Read the field name in the error. `authorId` tells you the relation that failed: the author you referenced does not exist.

2. Verify the parent exists before creating the child:
   ```ts
   const author = await prisma.user.findUnique({ where: { id: input.authorId } })
   if (!author) {
     return { ok: false, message: 'Author not found.' }
   }
   await prisma.post.create({ data URIs { title: input.title, authorId: input.authorId } })
   ```
   Expected: a bad author id returns your clean message; a good one creates the post.

3. Still catch P2003 as a backstop for races (the parent can be deleted between your check and your write):
   ```ts
   } catch (e) {
     if (e instanceof PrismaClientKnownRequestError && e.code === 'P2003') {
       return { ok: false, message: 'The linked record no longer exists.' }
     }
     throw e
   }
   ```
   Expected: concurrent deletes produce a friendly message, not a 500.

## When to use
- The exact code is P2003 on a create, update, or connect that references another record
- The referenced id comes from user input, a URL param, or another service

## When not to use
- P2002: that is a duplicate value, not a missing parent
- You are deleting a parent with children: that is a cascade / restrict policy question, set `onDelete` in the schema

## Compatibility
Prisma Client 4.x through 6.x. All relational providers.

### Variant phrasing: P2003 on `connect: { id }` in a nested write
Same fix: verify the id exists before the nested write, or catch P2003 around it.

### Variant phrasing: P2003 in a seed script
Seeds run in order; the parent seed must run (and commit) before the child seed. Check your seed order.

## Why it happens
The foreign key in the database guarantees the child always points at a real parent row. When the app sends an id that is not there (typo, stale client state, deleted parent), the database rejects the write and Prisma reports P2003. Checking first turns a database rejection into an application-level message.

## Edge cases
- `onDelete: Cascade` vs `Restrict`: deleting a parent with children fails differently; choose the policy your domain needs.
- UUID vs integer ids: a malformed id string can fail parsing before it ever reaches the constraint check.
- Multi-tenant apps: the parent may exist but belong to another tenant; scope the lookup by tenant, not just by id.

---

Source: [Vectle](https://vectle.com/skills/skl_CrcilKTeDpPquGr8aqWp8w). Version: `skv_RFKwGxcufcLz2aK_EUZXAg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
