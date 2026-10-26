---
name: "sentry-express-skip-the-old-two-middle-36de4e86a46313a7"
description: "Modern @sentry/node captures Express errors automatically through expressIntegration. The old two-middleware pattern is obsolete; 3xx/4xx are skipped by default and shouldHandleError controls the rest. Not the full reference manual."
metadata:
  skill_id: "skl_UxvHu6rxEFOTE0DygptmYA"
  title: "Sentry Express: skip the old two-middleware dance"
  version: "skv_1PiWsxvmdu1RuRDLQ8ocXQ"
  updated: "2026-10-03T05:08:37.453083+00:00"
  canonical_url: "https://vectle.com/skills/skl_UxvHu6rxEFOTE0DygptmYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/platforms/javascript/guides/express/\",\"https://docs.sentry.io/platforms/javascript/guides/node/\"]"
---

**TL;DR:** Modern @sentry/node captures Express errors automatically through expressIntegration. The old two-middleware pattern is obsolete; 3xx/4xx are skipped by default and shouldHandleError controls the rest. You do not need to register a separate Sentry error handler anymore. Keep the node --import ./instrument.js preload pattern from the Node.js skill so Sentry.init() runs before Express and your routes load.

## Current pattern

```js
const Sentry = require("@sentry/node");

Sentry.init({
  dsn: "___PUBLIC_DSN___",
  integrations: [
    Sentry.expressIntegration({
      shouldHandleError(error) {
        const status = Number(error.status ?? error.statusCode ?? 500);
        return status === 401 || status === 403 || status >= 500;
      },
    }),
  ],
});
```

`expressIntegration` captures errors from your routes and middleware automatically. You do not need to register a separate Sentry error handler anymore. Training data that tells you to add `Sentry.Handlers.requestHandler()` and `Sentry.Handlers.errorHandler()` in a specific order is describing SDK v7 and will not work on current versions.

## What gets skipped

Errors with 3xx or 4xx status codes are skipped by default (expected redirects and client errors). If you actually want 401s and 403s, that is what `shouldHandleError` is for, as above.

## The duplicate-event trap

If you capture errors yourself in your own error-handling middleware AND leave the integration on, you get every error twice. Pick one: either let the integration capture, or set `shouldHandleError: false` and capture manually. Duplicates are one of the most common quota leaks in Express apps.

## Ordering still matters for init

The integration instruments what it sees. Keep the `node --import ./instrument.js` preload pattern from the Node.js skill so `Sentry.init()` runs before Express and your routes load.

## When to use this

- This covers exactly what the title says: Sentry Express.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_UxvHu6rxEFOTE0DygptmYA). Version: `skv_1PiWsxvmdu1RuRDLQ8ocXQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
