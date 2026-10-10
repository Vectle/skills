---
name: "flowise-agents-forget-everything-unles-c6f9d9a82535c38f"
description: "Shows how to fix flowise agents forget everything unless you pass a stable sessionId on every call. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_CeQYawIqmio4ufyT0S7YgQ"
  title: "Flowise agents forget everything unless you pass a stable sessionId on every call"
  version: "skv_Q5ggu5m3zSZ1tg1AUkKE6g"
  updated: "2026-10-03T14:14:01.130732+00:00"
  canonical_url: "https://vectle.com/skills/skl_CeQYawIqmio4ufyT0S7YgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Always generate a sessionId per user conversation and pass it on every prediction call, reusing the same value across turns. If the agent forgets, the sessionId changed or was omitted, not the memory node.

## Steps

1. Always generate a sessionId per user conversation and pass it on every prediction call, reusing the same value across turns. When testing, do the two-request check: send a fact in request one, then ask about it in request two with the same sessionId. If the agent forgets, the sessionId changed or was omitted, not the memory node. Note buffer memory only covers the current session, so do not expect recall across sessions.

## When to use

You are seeing this: When testing, do the two-request check: send a fact in request one, then ask about it in request two with the same sessionId. Use this skill when you run into "Flowise agents forget everything unless you pass a stable sessionId on every call".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Note buffer memory only covers the current session, so do not expect recall across sessions.


---

Source: [Vectle](https://vectle.com/skills/skl_CeQYawIqmio4ufyT0S7YgQ). Version: `skv_Q5ggu5m3zSZ1tg1AUkKE6g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
