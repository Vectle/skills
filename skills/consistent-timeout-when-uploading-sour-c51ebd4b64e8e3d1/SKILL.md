---
name: "consistent-timeout-when-uploading-sour-c51ebd4b64e8e3d1"
description: "Shows how to fix consistent timeout when uploading sourcemaps for next.js (turbopack). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_i_I3OoIj8h_xR6KiOzzLYA"
  title: "Consistent timeout when uploading sourcemaps for next.js (turbopack)"
  version: "skv_fZS4p2PXHk7A_hIFEl0WSw"
  updated: "2026-10-03T05:40:26.075762+00:00"
  canonical_url: "https://vectle.com/skills/skl_i_I3OoIj8h_xR6KiOzzLYA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/PostHog/posthog-js/issues/2240\"]"
---

## TL;DR

For "for stdout/stderr, the CLI is very verbose (it logs every chunk), so Node killed (SIGTERM) the child, surfacing as a timeout. Fix: increase": posthog-cli sourcemap upload fails with operation timed out at bulk\_start\_upload for Next.js Turbopack builds; the upload works fine when the same CLI commands are run manually from the terminal. Fix: increase maxBuffer (e.g.

```text
for stdout/stderr, the CLI is very verbose (it logs every chunk), so Node killed (SIGTERM) the child, surfacing as a timeout. Fix: increase
```

## Steps

1. `posthog-cli` sourcemap upload fails with `operation timed out` at `bulk_start_upload` for Next.js Turbopack builds; the upload works fine when the same CLI commands are run manually from the terminal.

2. Maintainer daibhin root-caused it: the Next.js config wrapper spawns `posthog-cli` via Node child_process, which has a small default `maxBuffer` for stdout/stderr, the CLI is very verbose (it logs every chunk), so Node killed (SIGTERM) the child, surfacing as a timeout. Fix: increase `maxBuffer` (e.g. 10x) when spawning verbose CLIs, or reduce CLI verbosity; PostHog also shipped quieter CLI logging so the maxBuffer bump shouldn't be needed anymore.

## When to use

You are seeing this: Maintainer daibhin root-caused it: the Next.js config wrapper spawns posthog-cli via Node child_process, which has a small default maxBuffer for stdout/stderr, the CLI is very verbose (it logs every chunk), so Node killed (SIGTERM) the child, surfacing as... Use this skill when you run into "Consistent timeout when uploading sourcemaps for next.js (turbopack)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_i_I3OoIj8h_xR6KiOzzLYA). Version: `skv_fZS4p2PXHk7A_hIFEl0WSw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
