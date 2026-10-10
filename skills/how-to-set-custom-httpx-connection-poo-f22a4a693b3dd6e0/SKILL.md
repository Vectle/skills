---
name: "how-to-set-custom-httpx-connection-poo-f22a4a693b3dd6e0"
description: "Walks through set custom httpx connection pool limits in modern-treasury python SDK, step by step. Use it when you need to do exactly this. Not a troubleshooting guide, so skip it if you are here because of an error."
metadata:
  skill_id: "skl_gIszfVWksQgThroi90j5hw"
  title: "How to set custom httpx connection pool limits in modern-treasury python SDK"
  version: "skv_YDs8H_YSbgw50CUjja-23Q"
  updated: "2026-10-03T22:19:44.708534+00:00"
  canonical_url: "https://vectle.com/skills/skl_gIszfVWksQgThroi90j5hw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

A maintainer later confirmed version 1.10 resolved the issue.

## Steps

1. Before 1.10 there was no public option , the documented workaround was to replace the internal HTTP client: build `custom_client = httpx.Client(base_url=standard_client.base_url, timeout=standard_client._timeout, headers=standard_client.headers, limits=httpx.Limits(max_connections=120, max_keepalive_connections=100, keepalive_expiry=20))` and assign it to `modern_treasury._client`. A maintainer confirmed version 1.10 resolved the issue, so upgrade and use whatever pool options the new release exposes. Source: https://github.com/Modern-Treasury/modern-treasury-python/issues/72

Expected: A maintainer confirmed version 1.10 resolved the issue, so upgrade and use whatever pool options the new release exposes.

## When to use

You are seeing this: The modern-treasury python SDK didn't expose httpx's limits kwarg for tuning the connection pool (max connections, keepalive). Use this skill when you run into "How to set custom httpx connection pool limits in modern-treasury python SDK".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 1.10. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/Modern-Treasury/modern-treasury-python/issues/72


---

Source: [Vectle](https://vectle.com/skills/skl_gIszfVWksQgThroi90j5hw). Version: `skv_YDs8H_YSbgw50CUjja-23Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
