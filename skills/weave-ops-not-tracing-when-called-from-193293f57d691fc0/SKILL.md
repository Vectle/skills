---
name: "weave-ops-not-tracing-when-called-from-193293f57d691fc0"
description: "Shows how to fix weave ops not tracing when called from Flask endpoints. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_rGwwyZUjNuWYsi7End_GUA"
  title: "Weave ops not tracing when called from Flask endpoints"
  version: "skv_YB9xGbRYHNQEVfj2imWP5w"
  updated: "2026-10-03T14:07:28.256162+00:00"
  canonical_url: "https://vectle.com/skills/skl_rGwwyZUjNuWYsi7End_GUA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_AKdDMUCuihbWwR_UPXbBXA\",\"https://github.com/wandb/weave/issues/1684\"]"
---

## TL;DR

Upgrade to the latest weave release if ops called under Flask produce no traces. This was a context-management bug in Weave: the trace context did not survive Flask's request dispatch.

## Steps

1. This was a context-management bug in Weave: the trace context did not survive Flask's request dispatch. The team reworked context management to play nicer with Flask (and other threaded environments like Google Colab). The fix landed via the PR linked in the issue; maintainers asked users to try the release containing it. Upgrade to the latest weave release if ops called under Flask produce no traces.

## When to use

You are seeing this: Functions decorated with @weave.op() do not trace when called from a Flask endpoint: the op runs but no trace appears in Weave. Use this skill when you run into "Weave ops not tracing when called from Flask endpoints".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_rGwwyZUjNuWYsi7End_GUA). Version: `skv_YB9xGbRYHNQEVfj2imWP5w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
