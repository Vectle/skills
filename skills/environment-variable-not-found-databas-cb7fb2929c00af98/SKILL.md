---
name: "environment-variable-not-found-databas-cb7fb2929c00af98"
description: "Fixes the Prisma error 'Environment variable not found: DATABASE_URL' by ensuring the DATABASE_URL is actually present in the environment where the Prisma command runs, commonly a CI job or Docker container that never received it. Use when Prisma validate, migrate, or generate fails with this exact message. Not for malformed URL errors or P1012 protocol errors."
metadata:
  skill_id: "skl_PyeY6BFb42-u8Zvtm9GIMQ"
  title: "Environment variable not found: DATABASE_URL."
  version: "skv_dHI-pwB2SBd0z3iHOVfueQ"
  updated: "2026-10-03T04:38:47.445262+00:00"
  canonical_url: "https://vectle.com/skills/skl_PyeY6BFb42-u8Zvtm9GIMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The DATABASE_URL value is not reaching the shell that runs Prisma. Export it or pass it into the CI job / container environment explicitly, then re-run your Prisma command. The variable almost always exists somewhere (your secret store); it just was never forwarded to the process that needs it.

```text
error: Environment variable not found: DATABASE_URL.
```

## Steps

1. Confirm the variable is missing in the failing environment:
   ```bash
   echo "${DATABASE_URL:+set}"
   ```
   Expected: empty output. If it prints `set`, your shell sees it and the real problem is elsewhere.

2. In CI (GitHub Actions and similar), forward the secret into the job:
   ```yaml
   jobs:
     deploy:
       env:
         DATABASE_URL: ${{ secrets.DATABASE_URL }}
   ```
   Expected: the Prisma step in the next run no longer fails at the env check.

3. In Docker / compose, declare it where the Prisma command runs:
   ```yaml
   services:
     app:
       environment:
         - DATABASE_URL=${DATABASE_URL}
   ```
   Expected: `docker compose exec app npx prisma validate` loads the config without the env error.

4. Re-run the original command (`npx prisma migrate deploy`, `prisma generate`, etc.).
   Expected: the env error is gone. A *different* error (bad password, unreachable host) means the variable now arrives but its value is wrong.

## When to use
- The exact message is `Environment variable not found: DATABASE_URL` on validate, migrate, generate, or db push
- The failure appears in CI, Docker, or any environment other than your local machine

## When not to use
- The message complains the URL must start with a protocol (P1012): that means the var exists but its value is malformed
- Local shell: if your own terminal lacks it, just export it or fix your .env loader instead of touching CI

## Compatibility
Prisma CLI 4.x through 7.x. Any CI provider or container runtime.

### Variant phrasing: `Environment variable not found: DIRECT_URL`
Same shape, different variable. Forward DIRECT_URL the same way.

### Variant phrasing: error appears during `prisma generate` in a Docker build
Build-time args do not become runtime env automatically. Pass DATABASE_URL as a build arg and also as a runtime environment entry.

## Why it happens
Prisma reads connection strings from `env()` in the config or from the process environment. Secrets stored in a CI provider or orchestrator are not injected into a job or container unless the pipeline config forwards them. So the variable can be perfectly configured in your dashboard and still invisible to the Prisma process.

## Edge cases
- Prisma 7 with `prisma.config.ts` skips auto-loading `.env`; add the dotenv import or export the variable for real in that shell.
- Shell quoting: a value containing `#` or `!` gets mangled by unquoted assignment; quote it.
- If the error persists after forwarding, check for a typo in the variable name (DATABASE_URL vs DATABASE_URLS).

---

Source: [Vectle](https://vectle.com/skills/skl_PyeY6BFb42-u8Zvtm9GIMQ). Version: `skv_dHI-pwB2SBd0z3iHOVfueQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
