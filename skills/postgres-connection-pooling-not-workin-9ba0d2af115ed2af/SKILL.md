---
name: "postgres-connection-pooling-not-workin-9ba0d2af115ed2af"
description: "Shows how to fix postgres connection pooling not working. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_X6RQtN8gf0CdeYBr5rhfDg"
  title: "Postgres connection pooling not working"
  version: "skv_1P7lEKLZ7oKAInU_QOX7AQ"
  updated: "2026-10-03T16:24:51.292087+00:00"
  canonical_url: "https://vectle.com/skills/skl_X6RQtN8gf0CdeYBr5rhfDg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set persistence.datastores.*.sql.maxConns and maxIdleConns explicitly. 1. cluster with 2k shards (I assume that's the culprit) 1. use Postgres v97 plugin (actual Postgres is v14, we still have to upgrade the plugin) 1.

## Steps

1. cluster with 2k shards (I assume that's the culprit)
 1. use Postgres v97 plugin (actual Postgres is v14, we still have to upgrade the plugin)
 1.

2. [tdeebswihart (contributor)]: The CPU/GC load from constant connection and TLS cert recreation comes from sqlx pool defaults (max 2 idle conns, unbounded pool). Set persistence.datastores.*.sql.maxConns and maxIdleConns explicitly. The reporter confirmed connection handling dropped out of the profiles after configuring it.

## When to use

You are seeing this: 2. [tdeebswihart (contributor)]: The CPU/GC load from constant connection and TLS cert recreation comes from sqlx pool defaults (max 2 idle conns, unbounded pool). Use this skill when you run into "Postgres connection pooling not working".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_X6RQtN8gf0CdeYBr5rhfDg). Version: `skv_1P7lEKLZ7oKAInU_QOX7AQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
