---
name: "bug-miniflarecoreerror-err-runtime-fai-9fa389992ac6a946"
description: "Fixes 'MiniflareCoreError [ERR_RUNTIME_FAILURE]: The Workers runtime failed to start' by downgrading wrangler to 3.57.1 as a workaround. Use when wrangler fails to start the Workers runtime on a newer version, e.g. when creating a second application. Not for other Miniflare errors or runtime crashes after startup."
metadata:
  skill_id: "skl_G2cWBJ-LtDeKZkUq7nW0cQ"
  title: "\ud83d\udc1b BUG: MiniflareCoreError [ERR_RUNTIME_FAILURE]: The Workers runtime failed to start."
  version: "skv_ikA5ZuDEGYjVLSEMjlctQA"
  updated: "2026-10-03T04:12:42.816988+00:00"
  canonical_url: "https://vectle.com/skills/skl_G2cWBJ-LtDeKZkUq7nW0cQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Downgrade wrangler to 3.57.1 as a workaround: the reporter confirmed that version cleared the runtime startup failure. The bug hits newer wrangler versions when starting the Workers runtime (e.g. creating a second application).

## The error

```text
MiniflareCoreError [ERR_RUNTIME_FAILURE]: The Workers runtime failed to start.
```

## Fix it

1. Check your wrangler version:
   ```bash
   wrangler --version
   ```
   Success check: the version is newer than 3.57.1, confirming you are affected.

2. Downgrade wrangler to 3.57.1:
   ```bash
   npm i -g wrangler@3.57.1
   ```
   Success check: `wrangler --version` reports 3.57.1.

3. Retry the command that failed (e.g. creating the second application).
   Success check: the Workers runtime starts with no MiniflareCoreError.

## When this applies

- `MiniflareCoreError [ERR_RUNTIME_FAILURE]` on wrangler newer than 3.57.1.
- The failure happens at runtime startup, e.g. when scaffolding a second application.

## When it does not apply

- The runtime starts but your worker crashes; that is an application bug.
- A different Miniflare error code.
- You are already on 3.57.1 or older and still see the failure.

## Compatibility

- wrangler 3.57.1 (workaround version). Affected: newer 3.x versions at the time of the report.
- miniflare 3.20231218.1, workerd 1.20231218.0, Node 16+.

## Variant phrasings

- MiniflareCoreError ERR_RUNTIME_FAILURE
- wrangler Workers runtime failed to start
- Miniflare runtime failed to start second application

## Why it happens

A regression in newer wrangler 3.x broke Miniflare's runtime startup path in some configurations. Version 3.57.1 predates the regression, so downgrading restores the working startup sequence.

## Edge cases

- Pin the version in CI so a fresh install does not pull the broken release.
- Watch the upstream issue for a fixed release, then upgrade past it.
- Source: https://github.com/cloudflare/workers-sdk/issues/4709


---

Source: [Vectle](https://vectle.com/skills/skl_G2cWBJ-LtDeKZkUq7nW0cQ). Version: `skv_ikA5ZuDEGYjVLSEMjlctQA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
