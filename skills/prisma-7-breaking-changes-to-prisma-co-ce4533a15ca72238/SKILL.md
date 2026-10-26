---
name: "prisma-7-breaking-changes-to-prisma-co-ce4533a15ca72238"
description: "Fixes Prisma 7 breaking changes: the P1012 error 'The datasource property url is no longer supported in schema files' and seed failures, by moving config to prisma.config.ts with an explicit adapter. Use when upgrading to Prisma 7 breaks prisma generate, migrate deploy, or seeding. Not for Prisma 5/6 config issues."
metadata:
  skill_id: "skl_biwQKc_bojc8jhEJxWJKcg"
  title: "Prisma 7 breaking changes to Prisma config file, and prisma schema"
  version: "skv_gD7gVAZlF9vrgEaqOpsCGQ"
  updated: "2026-10-03T04:07:36.1426+00:00"
  canonical_url: "https://vectle.com/skills/skl_biwQKc_bojc8jhEJxWJKcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/prisma/orm/issues/28573\"]"
---

## TL;DR

Prisma 7 moved configuration out of `schema.prisma` into `prisma.config.ts`. Fix the P1012 validation error by removing `url` from the datasource block in your schema and defining it in `prisma.config.ts` instead. If seeding fails with "Cannot read properties of undefined", add an explicit database adapter in `prisma.config.ts` because Prisma 7 no longer auto-detects the provider.

## The error

```text
npx prisma generate
Loaded Prisma config from prisma.config.ts. Prisma schema loaded from prisma/schema.prisma
Error: Prisma schema validation - (get-config wasm)
Error code: P1012
error: The datasource property `url` is no longer supported in schema files.
```

Related failure on migrate deploy in Docker:

```text
error: The datasource property `url` is required in your Prisma config file
```

## Fix it

1. Remove `url` from the datasource block in `prisma/schema.prisma`.
   Success check: `npx prisma validate` no longer reports P1012.

2. Define the datasource URL in `prisma.config.ts`:
   ```ts
   import { defineConfig } from "prisma/config";
   export default defineConfig({
     datasource: { url: process.env.DATABASE_URL },
   });
   ```
   Success check: `npx prisma generate` completes without validation errors.

3. If seeding fails with "Cannot read properties of undefined (__internal)", add an explicit adapter in `prisma.config.ts` (Prisma 7 no longer auto-detects the provider):
   ```ts
   import { PrismaPg } from "@prisma/adapter-pg";
   export default defineConfig({
     datasource: { url: process.env.DATABASE_URL },
     // adapter wiring per your database driver
   });
   ```
   Success check: `prisma db seed` runs without the undefined-property error.

4. For Docker multi-stage builds, make sure `prisma.config.ts` is copied into the final image.
   Success check: `prisma migrate deploy` in the container finds the config and connects.

## When this applies

- Upgrading to Prisma 7 (from 5 or 6) breaks `prisma generate`, `migrate deploy`, or `db seed`.
- You see P1012 about the datasource `url` property, or "required in your Prisma config file".

## When it does not apply

- You are on Prisma 5 or 6; the old schema-based config still works there.
- The error is a different P-code (e.g. P1001 connection refused); that is a database reachability problem.
- `engine: 'classic'` errors on Prisma 7: the classic engine no longer exists; use the library engine default.

## Compatibility

- Prisma 7.x (breaking change introduced in 7.0). Prisma 5/6 unaffected.
- Node.js 18+. Docker multi-stage builds need the config file in the final stage.

## Variant phrasings

- error: prisma schema validation - (get-config wasm) error code: p1012
- The datasource property url is no longer supported in schema files
- Prisma 7 "datasource property url is required in your Prisma config file"
- Prisma 7 seed "Cannot read properties of undefined"

## Why it happens

Prisma 7 extracted all connection configuration from the schema file into `prisma.config.ts`, so the schema `url` property was removed and validation rejects it (P1012). The same move means the provider is no longer inferred from the schema datasource, so seeding needs an explicit adapter. Docker builds break when the new config file is not copied into the runtime image.

## Edge cases

- `engine: 'classic'` in config: the classic engine was removed; delete the setting and use the default.
- Monorepos: each Prisma schema needs its own `prisma.config.ts` or a shared config with per-schema datasource overrides.
- Source: https://github.com/prisma/orm/issues/28573


---

Source: [Vectle](https://vectle.com/skills/skl_biwQKc_bojc8jhEJxWJKcg). Version: `skv_gD7gVAZlF9vrgEaqOpsCGQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
