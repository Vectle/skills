---
name: "deno-deploy-deno-env-get-returns-undef-2d97e3e14bab83bc"
description: "Fixes Deno.env.get() returning undefined at module top level on Deno Deploy. Use this when dashboard env vars work locally but not in deployment. Not for missing dashboard config."
metadata:
  skill_id: "skl_CiAGVk1qS60TshQhCjhayw"
  title: "Deno Deploy: Deno.env.get() returns undefined at module top level"
  version: "skv_nX0zQVYKo_3aXxfhmjiYWA"
  updated: "2026-10-03T05:33:17.378097+00:00"
  canonical_url: "https://vectle.com/skills/skl_CiAGVk1qS60TshQhCjhayw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_WL7bcjNngUqW2rlBeJWN4Q\",\"https://github.com/denoland/deploy_feedback/issues/574\"]"
---

TL;DR: if environment variables registered on the Deno Deploy dashboard read with `Deno.env.get()` at the top level of a module return `undefined` in deployment (while local `.env` works), on Deno Deploy dashboard env vars are not reliably available when top-level module code runs. Move any `Deno.env.get()` calls inside a function or component so they execute at request time instead of import time:

```ts
function getClient() {
  return createClient({
    url: Deno.env.get("turso_url"),
    authToken - Deno.env.get("turso_token"),
  });
}
```

The reporter confirmed wrapping the `createClient` call inside a function made the deployment work. Rule for Deno Deploy: never build clients or read env at module top level; do it lazily inside the request handler. Local dev with `.env` will not catch this because the timing is different.

```text
error: Uncaught (in promise) LibsqlError: URL_INVALID: The URL is not in a valid format
```

## Steps

1. Move `Deno.env.get()` calls into functions/handlers.

2. Redeploy.

   Expected: env resolves. Success check: the client builds with a valid URL.

## When to use this

- Deno Deploy, env undefined at module top level.

## When NOT to use this

- The var is genuinely unset on the dashboard; set it.
- Local dev; .env timing differs.

## Compatibility

- Deno Deploy.

## Variant phrasings

- "deno deploy env undefined module top level"
- "Deno.env.get undefined deploy"

## Root cause

Dashboard env vars are not available at module evaluation time.

## Edge cases

- Any lazy pattern works; the point is request-time evaluation, not import time.

---

Source: [Vectle](https://vectle.com/skills/skl_CiAGVk1qS60TshQhCjhayw). Version: `skv_nX0zQVYKo_3aXxfhmjiYWA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
