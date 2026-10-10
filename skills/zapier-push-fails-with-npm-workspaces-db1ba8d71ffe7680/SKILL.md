---
name: "zapier-push-fails-with-npm-workspaces-db1ba8d71ffe7680"
description: "Shows how to fix zapier push fails with npm workspaces. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_pjr6vawKjYr_-fyhZM4m-g"
  title: "zapier push fails with npm workspaces"
  version: "skv_kn_uwcWn_pwqozY8NDy8hw"
  updated: "2026-10-03T14:05:31.240512+00:00"
  canonical_url: "https://vectle.com/skills/skl_pjr6vawKjYr_-fyhZM4m-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

zapier push failing with 'Looks like you're missing a local installation of zapier-platform-core' in an npm workspaces monorepo: the CLI does not resolve workspace-installed packages.

## Steps

1. zapier push failing with 'Looks like you're missing a local installation of zapier-platform-core' in an npm workspaces monorepo: the CLI does not resolve workspace-installed packages. Reporter's workaround: temporarily remove the workspace entry from the root package.json, then from the adapter directory run npm install, npm run build, and npx zapier push.

2. _Source: https://github.com/zapier/zapier-platform/issues/648 (Zapier)_

## When to use

Use this skill when you run into "zapier push fails with npm workspaces".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://github.com/zapier/zapier-platform/issues/648


---

Source: [Vectle](https://vectle.com/skills/skl_pjr6vawKjYr_-fyhZM4m-g). Version: `skv_kn_uwcWn_pwqozY8NDy8hw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
