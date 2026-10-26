---
name: "jemalloc-unsupported-system-page-size-da3752cdd3705593"
description: "Shows how to fix [jemalloc]: Unsupported system page size on ARM64 system. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_qGvg5uO56EQTwJt-4yRJ_Q"
  title: "[jemalloc]: Unsupported system page size on ARM64 system"
  version: "skv_NuRYRQaHdfxBANZ28vM-FA"
  updated: "2026-10-03T04:48:11.066918+00:00"
  canonical_url: "https://vectle.com/skills/skl_qGvg5uO56EQTwJt-4yRJ_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/qdrant/qdrant/issues/2474\"]"
---

## TL;DR

Root cause (maintainer generall): some ARM64 systems run kernels with a non-4KB page size (16KB/64KB), while the bundled jemalloc was compiled for a fixed page size. Fixes: rebuild the image with jemalloc removed (maintainer pointed to the jemalloc lines in src/main.rs), use a community-built no-jemalloc image for affected boards (e.g. y0mg/qdrant-raspberry-pi), or adjust the kernel page size.

## When to use

You are seeing this: Closed as completed after bounty PR #3945 made jemalloc compilation optional per architecture. Use this skill when you run into "[jemalloc]: Unsupported system page size on ARM64 system".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: qdrantqdrant v1.4.1. If you are on something much newer or older, the details may have shifted.

## Steps

1. 1. Root cause (maintainer generall): some ARM64 systems run kernels with a non-4KB page size (16KB/64KB), while the bundled jemalloc was compiled for a fixed page size. Fixes: rebuild the image with jemalloc removed (maintainer pointed to the jemalloc lines in src/main.rs), use a community-built no-jemalloc image for affected boards (e.g. y0mg/qdrant-raspberry-pi), or adjust the kernel page size. Closed as completed after bounty PR #3945 made jemalloc compilation optional per architecture.

2. You are seeing this: Docker image qdrant/qdrant:v1.4.1 fails to start on an ARM64 QNAP NAS with: '[jemalloc]: Unsupported system page size', 'memory allocation of 5 bytes failed', then abort. Use this skill when you run into "[jemalloc]: Unsupported system page size on ARM64 system".

3. If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

4. The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_qGvg5uO56EQTwJt-4yRJ_Q). Version: `skv_NuRYRQaHdfxBANZ28vM-FA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
