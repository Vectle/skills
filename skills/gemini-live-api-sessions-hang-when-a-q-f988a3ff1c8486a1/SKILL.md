---
name: "gemini-live-api-sessions-hang-when-a-q-f988a3ff1c8486a1"
description: "Shows how to fix gemini Live API sessions hang when a query should trigger a function call. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_iDQk4pDuP7R6AU0g-tKsJw"
  title: "Gemini Live API sessions hang when a query should trigger a function call"
  version: "skv_nLRtzy1rpTu0IVtAzlHZEQ"
  updated: "2026-10-03T14:20:07.998891+00:00"
  canonical_url: "https://vectle.com/skills/skl_iDQk4pDuP7R6AU0g-tKsJw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

We are experiencing a critical issue with the Gemini Live API using the gemini-2.0-flash-live-001 model, specifically when attempting to use function calling.

## Steps

1. We are experiencing a critical issue with the Gemini Live API using the gemini-2.0-flash-live-001 model, specifically when attempting to use function calling. Starting approximately on Tuesday, May 13, 2025, around 4:00 AM UTC+3, API sessions began to hang indefinitely when a query is made that should trigger a function call. Symptoms: API Hangs: When a prompt intended to trigger a declared function is sent, the API session stops responding.

2. Gemini Live API sessions that used to work suddenly hanging on function calls, with the socket staying open, was a Google server-side incident on gemini-2.0-flash-live-001, fixed about two days after the report with no client change needed. Reusable lesson: reproduce the same call in AI Studio; if it hangs there too, it's a service-side incident, not your code, so file it and wait. Client-side, add reconnect with backoff on hung sessions so your app recovers on its own once the backend is fixed.

## When to use

You are seeing this: Starting approximately on Tuesday, May 13, 2025, around 4:00 AM UTC+3, API sessions began to hang indefinitely when a query is made that should trigger a function call. Use this skill when you run into "Gemini Live API sessions hang when a query should trigger a function call".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_iDQk4pDuP7R6AU0g-tKsJw). Version: `skv_nLRtzy1rpTu0IVtAzlHZEQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
