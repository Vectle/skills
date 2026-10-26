---
name: "macos-tailscale-logs-out-after-less-th-279fe9314bc5d853"
description: "Shows how to fix macOS tailscale logs out after less than 5 mins of signing in. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_S-yO5dYsP8jUge_XVtbASg"
  title: "macOS tailscale logs out after less than 5 mins of signing in"
  version: "skv_9k6v3k0u5K8nNYe6kltGCg"
  updated: "2026-10-03T14:12:51.403108+00:00"
  canonical_url: "https://vectle.com/skills/skl_S-yO5dYsP8jUge_XVtbASg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/tailscale/tailscale/issues/8220\"]"
---

## TL;DR

Tailscale on macOS logging out within minutes of signing in (introduced around 1.40.0) was fixed in Tailscale 1.52: the client now restarts itself when the system kills it.

## Steps

1. Tailscale on macOS logging out within minutes of signing in (introduced around 1.40.0) was fixed in Tailscale 1.52: the client now restarts itself when the system kills it. If you're on 1.40.x-1.51 and see 'Please log in' loops, upgrade to 1.52 or later.

2. _Source: https://github.com/tailscale/tailscale/issues/8220 (Tailscale)_

## When to use

Use this skill when you run into "macOS tailscale logs out after less than 5 mins of signing in".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: around 1.40.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/tailscale/tailscale/issues/8220


---

Source: [Vectle](https://vectle.com/skills/skl_S-yO5dYsP8jUge_XVtbASg). Version: `skv_9k6v3k0u5K8nNYe6kltGCg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
