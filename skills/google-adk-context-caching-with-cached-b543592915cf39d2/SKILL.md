---
name: "google-adk-context-caching-with-cached-b543592915cf39d2"
description: "Shows how to fix google ADK: context caching with cached_content (constraints on tools and system instruction). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_IjMwQld1GvkZapva3kcCTQ"
  title: "Google ADK: context caching with cached_content (constraints on tools and system instruction)"
  version: "skv_pnKHdPxzOXsAvfNQu70TsA"
  updated: "2026-10-03T14:02:11.167333+00:00"
  canonical_url: "https://vectle.com/skills/skl_IjMwQld1GvkZapva3kcCTQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_BQa-70QHTRNE6-eCsb9VwQ\",\"https://github.com/google/adk-python/issues/211\"]"
---

## TL;DR

Separately, the adk web CLI in 1.51.1 had bugs loading cache configs, fixed on the main branch. If the adk web CLI does not load your cache config, update to the latest ADK (an older 1.51.x CLI had bugs fixed on main).

## Steps

1. Passing a `GenerateContentConfig(cached_content=cache.name)` to an ADK `LlmAgent` failed with a 400 INVALID_ARGUMENT error. The message said tool config, tools, and system instruction should not be set in the request when using cached content. The user wanted to inject an explicitly created cache into the agent, but ADK does not support injecting arbitrary cached content: it has specific requirements on what must be cached. Separately, the `adk web` CLI in 1.51.1 had bugs loading cache configs, fixed on the main branch.

2. What actually fixes it (verified in the thread):

3. Context caching is supported in ADK now (closed as supported by a maintainer). Two constraints apply: when using cached content, the request must not also set tool config, tools, or system instruction (the Gemini API rejects that combination), and ADK does not support injecting arbitrary cached content , ADK has specific requirements on what must be cached. If the `adk web` CLI does not load your cache config, update to the latest ADK (an older 1.51.x CLI had bugs fixed on main).

## When to use

You are seeing this: The situation: Passing a GenerateContentConfig(cached\_content=cache.name) to an ADK LlmAgent failed with a 400 INVALID_ARGUMENT error. Use this skill when you run into "Google ADK: context caching with cached_content (constraints on tools and system instruction)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 1.51.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_IjMwQld1GvkZapva3kcCTQ). Version: `skv_pnKHdPxzOXsAvfNQu70TsA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
