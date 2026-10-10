---
name: "prisma-client-did-not-initialize-yet-p-eee6f87f226cac06"
description: "Fixes the runtime error '@prisma/client did not initialize yet. Please run prisma generate and try to import it again.' by running prisma generate after every fresh install or deploy and wiring it into the build. Use when the app crashes on startup with this exact message. Not for TypeScript type errors or migration failures."
metadata:
  skill_id: "skl_bZxMpSMdvXl9H-oabbMDiQ"
  title: "@prisma/client did not initialize yet. Please run \"prisma generate\" and try to import it again."
  version: "skv_g5Vk-6E2nZJr2w7QnILJNg"
  updated: "2026-10-03T04:40:23.934421+00:00"
  canonical_url: "https://vectle.com/skills/skl_bZxMpSMdvXl9H-oabbMDiQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Run `npx prisma generate` in your build, not just on your laptop. Add it to the build command (or a postinstall hook), redeploy, and the crash goes away. This error means the generated Prisma Client code was never produced in the deployed environment.

```text
error: @prisma/client did not initialize yet. Please run "prisma generate" and try to import it again.
```

## Steps

1. Reproduce locally to confirm the diagnosis:
   ```bash
   rm -rf node_modules/.prisma node_modules/@prisma/client
   npm install
   node -e "require('./node_modules/.prisma/client')"
   ```
   Expected: the same 'did not initialize yet' error, proving generate never ran.

2. Add generate to your build. The reliable form is a postinstall hook plus an explicit build step:
   ```json
   { "scripts": { "postinstall": "prisma generate", "build": "prisma generate && tsc" } }
   ```
   Expected: `npm run build` logs `Generated Prisma Client` with your Prisma version.

3. On hosted platforms (Render, Railway, Vercel), make generate part of the build command, not the start command:
   ```bash
   npm install && npx prisma generate && npm run build
   ```
   Expected: deploy logs show `Generated Prisma Client` before the app starts.

4. Redeploy and watch the boot logs.
   Expected: no init error; the app reaches `listening` / `ready` state.

## When to use
- The exact runtime message is `@prisma/client did not initialize yet` on a fresh install, CI build, or deploy
- The app works on your machine but crashes on the server

## When not to use
- `prisma generate` itself fails: that is a schema or network problem, fix that first
- You get this in tests only: check your test setup installs dev dependencies

## Compatibility
Prisma Client 4.x, 5.x, 6.x. npm, pnpm, yarn, bun.

### Variant phrasing: error after `npm ci` in Docker
`npm ci` wipes node_modules, which deletes the previously generated client. A postinstall `prisma generate` fixes it because npm runs postinstall after ci too.

### Variant phrasing: monorepo / workspace where generate ran in the wrong package
Run generate in the package that owns `schema.prisma`, or pass `--schema` explicitly.

## Why it happens
`@prisma/client` ships as a thin stub; the real query engine bindings and typed client are produced by `prisma generate` at install/build time. Fresh installs, `npm ci`, and clean Docker builds all start without those generated files, and most deploy pipelines never run generate.

## Edge cases
- If your start command runs generate but the platform caches node_modules between deploys, stale generated files can linger; make generate unconditional.
- pnpm users: the generated client lives under a virtual store path; do not import it by relative path.
- With Prisma 7 the generated client import path changed; follow the version's documented import, but the generate step is still the fix.

---

Source: [Vectle](https://vectle.com/skills/skl_bZxMpSMdvXl9H-oabbMDiQ). Version: `skv_g5Vk-6E2nZJr2w7QnILJNg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
