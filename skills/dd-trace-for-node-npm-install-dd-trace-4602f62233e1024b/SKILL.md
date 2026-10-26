---
name: "dd-trace-for-node-npm-install-dd-trace-4602f62233e1024b"
description: "Node APM with dd-trace: npm install dd-trace, then require and init the tracer before any other import. Initialization order is the classic failure. Not the full reference manual."
metadata:
  skill_id: "skl_cBVlJ0Ap2lL_Y3zHT8dSLA"
  title: "dd-trace for Node: npm install dd-trace, require and init it before any app code"
  version: "skv_lf-ft4JxIdbTk36P7R53Sw"
  updated: "2026-10-03T05:13:02.443571+00:00"
  canonical_url: "https://vectle.com/skills/skl_cBVlJ0Ap2lL_Y3zHT8dSLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/tracing/setup/nodejs/\"]"
---

**TL;DR:** Node APM with dd-trace: npm install dd-trace, then require and init the tracer before any other import. Initialization order is the classic failure. dd-trace for Node: install it, then require it FIRST The Node tracer has one hard rule: it must be loaded before the modules it instruments. The tracer patches modules as they load, which is why it must be first.

# dd-trace for Node: install it, then require it FIRST

The Node tracer has one hard rule: it must be loaded before the modules it instruments. Get the order wrong and you get a running app with zero traces and no error.

## Setup

```sh
npm install dd-trace
```

At the very top of your entry file, before everything else:

```js
const tracer = require('dd-trace').init({
  service: 'my-service',
  env: 'prod',
  version: '1.2.3'
})
```

That is the whole integration for auto-instrumented frameworks (Express, Fastify, Nest, pg, redis, and the rest). The tracer patches modules as they load, which is why it must be first.

## The traps, in order of frequency

1. **Init after imports.** If your entry file imports express before requiring dd-trace, express never gets patched. Move the tracer require to line one. In ESM, use `--import dd-trace/register` or the loader hook so it runs before your code.
2. **No service/env/version.** Pass them to init or set `DD_SERVICE`, `DD_ENV`, `DD_VERSION`. Defaults guess and your service catalog turns to mush.
3. **Agent unreachable.** Default is the agent on the same host. In containers set `DD_AGENT_HOST` to the agent, or `DD_TRACE_AGENT_URL` to the full URL. Connection refused here is silent, traces just never arrive.
4. **Wrong site.** `DD_SITE` for non-US1 orgs, same as everything else Datadog.
5. **Major version jumps.** dd-trace has breaking changes across majors (the docs ship a migration guide for 0.x through 5.x). Pin the major in package.json.

## Verify

Start the app, hit an endpoint, check APM, Services. Also watch the tracer debug log on startup: it logs the agent endpoint it is using. If it says the wrong host, your env var did not take.

Serverless note: on Lambda, dd-trace works with the Datadog extension layer, but the init-first rule still applies inside the handler module.

## When to use this

- This covers exactly what the title says: dd-trace for Node.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with dd-trace; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_cBVlJ0Ap2lL_Y3zHT8dSLA). Version: `skv_lf-ft4JxIdbTk36P7R53Sw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
