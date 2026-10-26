---
name: "jest-fails-with-cannot-find-module-fas-eb7b67b43c28b49f"
description: "Shows how to fix jest fails with Cannot find module 'fastly:secret-store' for Fastly Compute@Edge app. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl__MM1RrUIZfagAZKfCHqDIg"
  title: "Jest fails with Cannot find module 'fastly:secret-store' for Fastly Compute@Edge app"
  version: "skv_HoVVX2_mWw2J50-XG53-Gg"
  updated: "2026-10-03T14:14:10.358176+00:00"
  canonical_url: "https://vectle.com/skills/skl__MM1RrUIZfagAZKfCHqDIg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_rIMGAbw33e3H90R76knL1A\",\"https://github.com/fastly/js-compute-runtime/issues/597\"]"
---

## TL;DR

Jest cannot resolve the fastly: namespace imports because those modules only exist inside the Compute@Edge runtime.

## Steps

1. Importing fastly:secret-store (or other fastly: namespaced modules) fails under Jest with Cannot find module 'fastly:secret-store' even though the app builds and deploys fine. Jest cannot resolve the fastly: namespace imports because those modules only exist inside the Compute@Edge runtime. Maintainers from Fastly recommend using the community jest preset ysugimoto/jest-preset-fastly-js-compute, which maps the fastly: imports to local mocks; the maintainer explicitly called it the exact integration they recommend for Fastly JS apps under Jest. The reporter confirmed that PR 9 on that preset resolved their issue and the thread was closed.

2. What actually fixes it (verified in the thread):

3. Use the jest preset ysugimoto/jest-preset-fastly-js-compute in your jest config: it maps fastly: namespaced imports to local mocks so tests can run outside the Compute@Edge runtime. This is the integration Fastly's own maintainer recommends for Jest users, and the reporter confirmed that a preset update (PR 9) fixed their failing tests. Source: https://github.com/fastly/js-compute-runtime/issues/597

## When to use

You are seeing this: The situation: Importing fastly:secret-store (or other fastly: namespaced modules) fails under Jest with Cannot find module 'fastly:secret-store' even though the app builds and deploys fine. Use this skill when you run into "Jest fails with Cannot find module 'fastly:secret-store' for Fastly Compute@Edge app".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/fastly/js-compute-runtime/issues/597


---

Source: [Vectle](https://vectle.com/skills/skl__MM1RrUIZfagAZKfCHqDIg). Version: `skv_HoVVX2_mWw2J50-XG53-Gg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
