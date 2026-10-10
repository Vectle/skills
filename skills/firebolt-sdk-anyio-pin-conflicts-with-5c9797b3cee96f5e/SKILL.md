---
name: "firebolt-sdk-anyio-pin-conflicts-with-5c9797b3cee96f5e"
description: "Shows how to fix firebolt SDK anyio pin conflicts with MCP servers: fixed in 1.15.0. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_sLFjrUGUCPhZ9lYQ3BUrIQ"
  title: "Firebolt SDK anyio pin conflicts with MCP servers: fixed in 1.15.0"
  version: "skv_9rr6giFIKFwybky6oSrwKQ"
  updated: "2026-10-03T14:18:10.820722+00:00"
  canonical_url: "https://vectle.com/skills/skl_sLFjrUGUCPhZ9lYQ3BUrIQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

If an agent's venv fails to resolve firebolt-sqlalchemy together with an MCP server stack, the fix is to upgrade firebolt-sdk to 1.15.0 or later, which relaxed the anyio pin to be compatible with mcp.

## Steps

1. If an agent's venv fails to resolve firebolt-sqlalchemy together with an MCP server stack, the fix is to upgrade firebolt-sdk to 1.15.0 or later, which relaxed the anyio pin to be compatible with mcp. As a stopgap on older versions: install firebolt-sqlalchemy first, then run pip install -U anyio and accept the resolver warning, since the SDK works fine with newer anyio in practice. Pin floor versions in your agent environment specs rather than leaving firebolt-sdk unbounded.

Expected: The maintainer confirmed the pin was only to keep the SDK's test mocks working, gave a workaround of installing then force-upgrading anyio, and shipped the relaxed pin in firebolt-sdk 1.15.0, which the reporter confirmed fixed it.

## When to use

You are seeing this: Pin floor versions in your agent environment specs rather than leaving firebolt-sdk unbounded. Use this skill when you run into "Firebolt SDK anyio pin conflicts with MCP servers: fixed in 1.15.0".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 1.15.0, firebolt-sdk 1.6.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_sLFjrUGUCPhZ9lYQ3BUrIQ). Version: `skv_9rr6giFIKFwybky6oSrwKQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
