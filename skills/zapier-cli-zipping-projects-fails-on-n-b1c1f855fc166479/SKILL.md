---
name: "zapier-cli-zipping-projects-fails-on-n-b1c1f855fc166479"
description: "Shows how to fix zapier CLI zipping projects fails on nullish coalescing assignment modern syntax browserify. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_guHOx00kXRmrZXminK_xtg"
  title: "Zapier CLI zipping projects fails on nullish coalescing assignment modern syntax browserify"
  version: "skv_KDWEpfmofNiVDbJw-_W1aQ"
  updated: "2026-10-03T14:05:29.410156+00:00"
  canonical_url: "https://vectle.com/skills/skl_guHOx00kXRmrZXminK_xtg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_mnwSqXvGnIB2PZUCEHj1iA\",\"https://github.com/zapier/zapier-platform/issues/614\"]"
---

## TL;DR

Upgrade the CLI/core to v17 and modern syntax (??=, private fields/methods) bundles cleanly. Fixed in Zapier platform v17, which replaced browserify with esbuild for packaging.

## Steps

1. Fixed in Zapier platform v17, which replaced browserify with esbuild for packaging. Upgrade the CLI/core to v17 and modern syntax (??=, private fields/methods) bundles cleanly. If you are stuck on an older version, the workaround is to transpile down to older syntax in your Babel target so the legacy bundler can parse it.

## When to use

You are seeing this: After upgrading to Zapier platform v13 (Node 16) and targeting Node 16 in Babel, zapier push fails at "Zipping projects and dependencies", the browserify-based bundler cannot parse modern syntax like nullish coalescing assignment (??=) or private class... Use this skill when you run into "Zapier CLI zipping projects fails on nullish coalescing assignment modern syntax browserify".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_guHOx00kXRmrZXminK_xtg). Version: `skv_KDWEpfmofNiVDbJw-_W1aQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
