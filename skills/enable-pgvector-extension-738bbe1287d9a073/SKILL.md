---
name: "enable-pgvector-extension-738bbe1287d9a073"
description: "Enable pgvector extension. Verified on Neon: pgvector 0.8.6 enabled, migration recorded in `drizzle.__drizzle_migrations`, and `'[1,0]':vector [=] '[0,1]':vector` = 1. Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_KlAW_bopa3IATv8V1Ogy8w"
  title: "Enable pgvector extension"
  version: "skv_ptbjHqlOcOpDupUdimNkQw"
  updated: "2026-10-03T05:10:35.1081+00:00"
  canonical_url: "https://vectle.com/skills/skl_KlAW_bopa3IATv8V1Ogy8w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Verified on Neon: pgvector 0.8.6 enabled, migration recorded in `drizzle.__drizzle_migrations`, and `'[1,0]'::vector [=] '[0,1]'::vector` = 1.

## Fix

1. Verified on Neon: pgvector 0.8.6 enabled, migration recorded in `drizzle.__drizzle_migrations`, and `'[1,0]'::vector [=] '[0,1]'::vector` = 1.
   Expected: you can confirm this matches your situation.

## When to use

- You are dealing with this situation.
- The symptom matches: Enable pgvector extension.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source (mentions 0.8.6). Source: GitHub issue: https://github.com/aniketmandloi/anything-tonight/issues/5.

## Variant phrasings

### Enable pgvector extension

## Why it happens

GitHub issue aniketmandloi/anything-tonight#5 (closed, 2 comments, reported 2026-09-24): ## Goal Vector column support for embeddings and mood vectors. ## Scope - Migration `CREATE EXTENSION IF NOT EXISTS vector` ## Acceptance criteria - [ ] Extension present in DB ## Verification `select * from pg_extension where extname='vector'` returns a row. ## Depends on #4 _Work in small atomic commits referencing this issue. See `docs/PLAN.md`._

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/aniketmandloi/anything-tonight/issues/5

---

Source: [Vectle](https://vectle.com/skills/skl_KlAW_bopa3IATv8V1Ogy8w). Version: `skv_ptbjHqlOcOpDupUdimNkQw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
