---
name: "the-datasource-url-property-is-require-4d9afac445a5e737"
description: "Fixes the Prisma 7 error 'the datasource.url property is required in your prisma config file when using prisma migrate deploy' by adding a datasource url entry to prisma.config.ts at the project root and copying that file into Docker images. Use when the migrate deploy CLI fails with this exact message on Prisma 7. Not for Prisma 6 or earlier, and not for missing DATABASE_URL environment variable errors."
metadata:
  skill_id: "skl_moDVuxzKdxaKnU8Y5WvILQ"
  title: "the datasource.url property is required in your prisma config file when using prisma migrate deploy"
  version: "skv_EgwXRTeLLiF0tUKtWfV8OA"
  updated: "2026-10-03T04:37:05.84321+00:00"
  canonical_url: "https://vectle.com/skills/skl_moDVuxzKdxaKnU8Y5WvILQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Add a `datasource` url entry to `prisma.config.ts` at your project root, pointed at your real database URL, then re-run `npx prisma migrate deploy`. If you deploy with Docker, copy `prisma.config.ts` into the image too. This happens because Prisma 7 moved the CLI connection string out of `schema.prisma` into the config file, so the migrate CLI refuses to run without it.

```text
Error: the datasource.url property is required in your prisma config file when using prisma migrate deploy
```

## Steps

1. Create `prisma.config.ts` at the project root (not inside the prisma folder):
   ```ts
   import { defineConfig, env } from 'prisma/config'
   import 'dotenv/config'

   export default defineConfig({
     schema: 'prisma/schema.prisma',
     datasource: { url: env('DATABASE_URL') },
   })
   ```
   Expected: `npx prisma validate` prints that the schema is valid and that it loaded the Prisma config.

2. Docker users: copy the config file into the image next to the prisma folder:
   ```dockerfile
   COPY prisma.config.ts ./
   COPY prisma ./prisma
   ```
   Expected: the deploy container finds the config; the error disappears from the container logs.

3. Re-run the deploy:
   ```bash
   npx prisma migrate deploy
   ```
   Expected: `All migrations have been successfully applied.` or `No pending migrations to apply.`

## When to use
- You hit this exact error on `prisma migrate deploy`, `migrate dev`, or `db push` with Prisma 7 or later
- You upgraded from Prisma 5/6 and removed `url` from the datasource block

## When not to use
- Prisma 6 or earlier: there the URL still lives in `schema.prisma` and this error does not exist
- The failure is `Environment variable not found: DATABASE_URL` instead: that is a different fix (the env var itself is missing)

## Compatibility
Prisma 7.x CLI. Node 18+. Applies to `migrate deploy`, `migrate dev`, and `db push`.

### Variant phrasing: same error on `db push`
`db push` reads the same config file, so the fix is identical.

## Why it happens
Prisma 7 rejects `url` inside the `datasource` block of `schema.prisma` and expects the CLI connection string in `prisma.config.ts` instead. As a side effect, once the config file exists the CLI stops auto-loading `.env` on its own, which is why the config needs the `dotenv/config` import to keep working locally.

## Edge cases
- Wrong location: Prisma looks for `prisma.config.ts` at the project root (and parent dirs), not `prisma/config.ts`.
- `env()` comes from `prisma/config`; `process.env.DATABASE_URL` works too, but `env()` is the documented form.
- If you see `Prisma config detected, skipping environment variable loading`, that is expected Prisma 7 behavior, not an error.

---

Source: [Vectle](https://vectle.com/skills/skl_moDVuxzKdxaKnU8Y5WvILQ). Version: `skv_EgwXRTeLLiF0tUKtWfV8OA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
