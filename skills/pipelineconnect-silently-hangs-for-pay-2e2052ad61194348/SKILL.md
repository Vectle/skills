---
name: "pipelineconnect-silently-hangs-for-pay-2e2052ad61194348"
description: "Serverless: pipelineConnect silently hangs for payloads in ~32KB-42KB range on pool reconnection. The verified fix is Fix: [jawj (maintainer)]: Bug is in Neon's proxy code, not the npm package: with `pipelineConnect`, a first query of roughly 65-84KB wire size (Prisma sends UPSERT data twice - once for INSERT, once for UPDATE branch) silently hung. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl_48h_sz9IlIKHNbeeTDym2w"
  title: "pipelineConnect silently hangs for payloads in ~32KB-42KB range on pool reconnection"
  version: "skv_T4h3GwOaMDNd61cFd25VSg"
  updated: "2026-10-03T05:10:50.377101+00:00"
  canonical_url: "https://vectle.com/skills/skl_48h_sz9IlIKHNbeeTDym2w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: [jawj (maintainer)]: Bug is in Neon's proxy code, not the npm package: with `pipelineConnect`, a first query of roughly 65-84KB wire size (Prisma sends UPSERT data twice - once for INSERT, once for UPDATE branch) silently hung. Fixed server-side on production; no package update needed.

## The error

```text
Issue neondatabase/serverless#209 (closed, 5 comments): ## Bug: `pipelineConnect` silently hangs for payloads in ~32KB - 42KB range on pool reconnection
```

## Fix

1. [jawj (maintainer)]: Bug is in Neon's proxy code, not the npm package: with `pipelineConnect`, a first query of roughly 65-84KB wire size (Prisma sends UPSERT data twice - once for INSERT, once for UPDATE branch) silently hung.
2. Fixed server-side on production; no package update needed.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in serverless.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in serverless, even a similar-looking one.
- General serverless setup or credential questions.

## Compatibility

- Serverless (neondatabase/serverless)

## Variant phrasings

- How to fix "pipelineConnect silently hangs for payloads in ~32KB-42KB range on pool reconnection" in serverless
- serverless: pipelineConnect silently hangs for payloads in ~32KB-42KB range on pool reconnection

## Source

- https://github.com/neondatabase/serverless/issues/209

---

Source: [Vectle](https://vectle.com/skills/skl_48h_sz9IlIKHNbeeTDym2w). Version: `skv_T4h3GwOaMDNd61cFd25VSg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
