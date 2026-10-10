---
name: "prisma-on-alpine-arm64-missing-precomp-ff7af43e89027829"
description: "Shows how to fix prisma on Alpine ARM64: missing precompiled musl engines (fixed in 4.10.0). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_qnoXzXSkqB5ifTrXQiiK3w"
  title: "Prisma on Alpine ARM64: missing precompiled musl engines (fixed in 4.10.0)"
  version: "skv_wIM91n4OflZqeovxQGKOwg"
  updated: "2026-10-03T14:19:00.63146+00:00"
  canonical_url: "https://vectle.com/skills/skl_qnoXzXSkqB5ifTrXQiiK3w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "Query engine library for current platform "linux-musl-openssl-3.0.x" could not be found": upgrade to Prisma 4.10.0 or later, which ships native precompiled engines for Linux Alpine on ARM64. Prisma shipped the missing engines officially in version 4.10.0.

```text
Query engine library for current platform "linux-musl-openssl-3.0.x" could not be found
```

## Steps

1. Running Prisma inside an Alpine Docker container on ARM64 (M1/M2 Macs, Raspberry Pi, ARM cloud instances) failed because Prisma shipped no precompiled engines for the linux-musl-arm64 target. You get `Unknown binaryTarget linux-arm64-openssl-undefined` or `Query engine library for current platform "linux-musl-openssl-3.0.x" could not be found`. Prisma shipped the missing engines officially in version 4.10.0.

2. Upgrade to Prisma 4.10.0 or later, which ships native precompiled engines for Linux Alpine on ARM64. No emulation or custom builds are needed after the upgrade. If you must stay on an older version, use a Debian-based image like node:lts-slim instead of Alpine, or build with `docker buildx build --platform=linux/amd64` to run under emulation. For Alpine 3.17+ add `binaryTargets = ["native", "linux-musl-openssl-3.0.x"]` to your schema if you build images on one architecture and run on another. Source: https://github.com/prisma/orm/issues/8478

## When to use

You are seeing this: You get Unknown binaryTarget linux-arm64-openssl-undefined or Query engine library for current platform "linux-musl-openssl-3.0.x" could not be found. Use this skill when you run into "Prisma on Alpine ARM64: missing precompiled musl engines (fixed in 4.10.0)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 4.10.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/prisma/orm/issues/8478


---

Source: [Vectle](https://vectle.com/skills/skl_qnoXzXSkqB5ifTrXQiiK3w). Version: `skv_wIM91n4OflZqeovxQGKOwg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
