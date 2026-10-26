---
name: "prisma-query-engine-missing-after-sst-6ae4d0d882c83348"
description: "Shows how to fix prisma query engine missing after SST v3.3.16: copy the .so and set PRISMA_QUERY_ENGINE_LIBRARY. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl__CF5Sn9kwh3aGv9qL7rKNg"
  title: "Prisma query engine missing after SST v3.3.16: copy the .so and set PRISMA_QUERY_ENGINE_LIBRARY"
  version: "skv_u8FLgayhBSMDqo8cgGPYEg"
  updated: "2026-10-03T14:12:06.79153+00:00"
  canonical_url: "https://vectle.com/skills/skl__CF5Sn9kwh3aGv9qL7rKNg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/anomalyco/sst/issues/5077\"]"
---

## TL;DR

For "Prisma Client could not locate the Query Engine for runtime rhel-openssl-3.0.x. This is likely caused by a bundler that has not copied libqu": prisma query engine missing after SST v3.3.16: copy the.so and set PRISMA_QUERY_ENGINE_LIBRARY What was going on Issue anomalyco/sst#5077 (closed, 33 comments): After upgrading SST to v3.3.16, Prisma bundling in an SST Function broke: "Prisma Client could not locate the Query Engine for runtime rhel-openssl-3.0.x.

```text
Prisma Client could not locate the Query Engine for runtime rhel-openssl-3.0.x. This is likely caused by a bundler that has not copied libquery_engine-rhel-openssl-3.0.x.so.node next to the result.
```

## Steps

1. Prisma query engine missing after SST v3.3.16: copy the .so and set PRISMA_QUERY_ENGINE_LIBRARY

2. What was going on
Issue anomalyco/sst#5077 (closed, 33 comments): After upgrading SST to v3.3.16, Prisma bundling in an SST Function broke: "Prisma Client could not locate the Query Engine for runtime rhel-openssl-3.0.x. This is likely caused by a bundler that has not copied libquery_engine-rhel-openssl-3.0.x.so.node next to the result." The same setup worked before the release.

3. The fix
Reporter-verified fix, no esbuild fiddling needed. Point the function at the query engine binary explicitly: in your SST Function config add a copyFiles entry from node_modules/.prisma/client/libquery_engine-rhel-openssl-3.0.x.so.node to .prisma/client/libquery_engine-rhel-openssl-3.0.x.so.node, and set the PRISMA_QUERY_ENGINE_LIBRARY environment variable to .prisma/client/libquery_engine-rhel-openssl-3.0.x.so.node. That tells the Prisma client exactly where the engine binary lives in the bundle, and the reporter confirmed Prisma works in a monorepo SST Function with this setup.

## When to use

You are seeing this: This is likely caused by a bundler that has not copied libquery_engine-rhel-openssl-3.0.x.so.node next to the result." The same setup worked before the release. Use this skill when you run into "Prisma query engine missing after SST v3.3.16: copy the .so and set PRISMA_QUERY_ENGINE_LIBRARY".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: SST v3.3.16. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl__CF5Sn9kwh3aGv9qL7rKNg). Version: `skv_u8FLgayhBSMDqo8cgGPYEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
