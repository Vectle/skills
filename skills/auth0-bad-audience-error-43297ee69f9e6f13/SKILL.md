---
name: "auth0-bad-audience-error-43297ee69f9e6f13"
description: "Shows how to fix auth0 Bad audience error. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_bxMBsCW5Mbr9G-lw2cQWkA"
  title: "Auth0 Bad audience error"
  version: "skv_H55--W4bPJW9PrWabUzulg"
  updated: "2026-10-04T01:12:26.819579+00:00"
  canonical_url: "https://vectle.com/skills/skl_bxMBsCW5Mbr9G-lw2cQWkA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/auth0/node-auth0/issues/787\"]"
---

## TL;DR

One, to call the Management API you have to use the Management API audience, not a custom API audience you created in the dashboard. Two, when granting scopes, the correct name is update:users_app_metadata, not update:users or update:users_metadata.

## Steps

1. Two things to check on a Bad audience error with node-auth0. One, to call the Management API you have to use the Management API audience, not a custom API audience you created in the dashboard. Two, when granting scopes, the correct name is update:users_app_metadata, not update:users or update:users_metadata. Check the Permissions tab of your API in the dashboard for the full list of valid scopes.

2. _Source: https://github.com/auth0/node-auth0/issues/787 (Auth0)_

## When to use

You are seeing this: Two things to check on a Bad audience error with node-auth0. Use this skill when you run into "Auth0 Bad audience error".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/auth0/node-auth0/issues/787


---

Source: [Vectle](https://vectle.com/skills/skl_bxMBsCW5Mbr9G-lw2cQWkA). Version: `skv_H55--W4bPJW9PrWabUzulg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
