---
name: "diagnose-streaming-filters-on-node-nam-08b847b99b16960b"
description: "Shows how to fix diagnose: streaming filters on node name 'agent' match nothing in v1. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_9LyQyweSN0acab5EhJFQvQ"
  title: "Diagnose: streaming filters on node name 'agent' match nothing in v1"
  version: "skv_AHIJpcbZptXiCr3qKORS1Q"
  updated: "2026-10-03T14:14:42.41154+00:00"
  canonical_url: "https://vectle.com/skills/skl_9LyQyweSN0acab5EhJFQvQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Update every filter, match, and branch that references the old node name: - "agent" -> "model" in stream chunk filtering. Re-run the stream and confirm your handler now receives the model-step events.

## Steps

1. v1 renamed the streaming node from `"agent"` to `"model"` as part of the create_agent migration.

2. Update every filter, match, and branch that references the old node name:

3. - `"agent"` -> `"model"` in stream chunk filtering.

4. Re-run the stream and confirm your handler now receives the model-step events. Grep the codebase for other `"agent"` string literals tied to streaming; the rename is easy to miss in helper functions.

## When to use

You are seeing this: After upgrading to LangChain v1, your stream-event filtering by node name "agent" stops matching. Use this skill when you run into "Diagnose: streaming filters on node name 'agent' match nothing in v1".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

v1 renamed the streaming node from "agent" to "model" as part of the create_agent migration.


---

Source: [Vectle](https://vectle.com/skills/skl_9LyQyweSN0acab5EhJFQvQ). Version: `skv_AHIJpcbZptXiCr3qKORS1Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
