---
name: "sentry-node-js-esm-vs-cjs-match-the-in-b8db0f324d43d380"
description: "ESM and CommonJS need different instrument files and preload flags. Pick the wrong pair and the SDK loads too late or not at all."
metadata:
  skill_id: "skl_K0DQH29ZEwCTEyRFgIJuSA"
  title: "Sentry Node.js ESM vs CJS: match the instrument file to the module system"
  version: "skv_qQxa_QHrRQBPl9GZxhbKNw"
  updated: "2026-10-03T04:44:55.508549+00:00"
  canonical_url: "https://vectle.com/skills/skl_K0DQH29ZEwCTEyRFgIJuSA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.sentry.io/platforms/javascript/guides/node/\"]"
---

**TL;DR:** ESM and CommonJS need different instrument files and preload flags. Pick the wrong pair and the SDK loads too late or not at all. Move it earlier via the preload flag.

## The pairs

CommonJS:

```
// instrument.js
const Sentry = require("@sentry/node");
Sentry.init({ dsn: "___PUBLIC_DSN___" });
```

```
node --import ./instrument.js app.js
```

ESM (`"type": "module"` in package.json):

```
// instrument.mjs
import * as Sentry from "@sentry/node";

// Ensure to call this before importing any other modules!
Sentry.init({ dsn: "___PUBLIC_DSN___" });
```

```
node --import ./instrument.mjs app.mjs
```

## How this breaks

- ESM app with `instrument.js` (CJS): the `require` call fails or the file loads in the wrong context, and init never runs. No errors in Sentry, obviously, because Sentry is the thing that is broken.
- Forgetting `--import` and instead importing instrument from app code: by the time your import runs, Express, Prisma, and everything else already loaded without instrumentation. You get errors but no traces, and the gap is confusing.
- TypeScript projects: the instrument file must be compiled or run through your TS loader with the same `--import` registration order. `ts-node` users need the loader flag pointing at the instrument file, not the app entry.

## The check

If error events arrive but spans are missing for libraries you expect (http, pg, redis), init ran but too late. Move it earlier via the preload flag. If nothing arrives at all, the file pair is wrong or the flag is missing from the start command (check the Dockerfile CMD and the process manager config, not just package.json scripts).

## When to use this

- This covers exactly what the title says: Sentry Node.js ESM vs CJS.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Sentry; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Sentry behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_K0DQH29ZEwCTEyRFgIJuSA). Version: `skv_qQxa_QHrRQBPl9GZxhbKNw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
