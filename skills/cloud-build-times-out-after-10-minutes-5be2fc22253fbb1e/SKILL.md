---
name: "cloud-build-times-out-after-10-minutes-5be2fc22253fbb1e"
description: "Shows how to fix cloud Build times out after 10 minutes: raise the build timeout. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_281kjuoi-OXz00FFWpUmQQ"
  title: "Cloud Build times out after 10 minutes: raise the build timeout"
  version: "skv_X99E-rJ-k5J2dHG7dNnu3A"
  updated: "2026-10-03T14:05:17.512297+00:00"
  canonical_url: "https://vectle.com/skills/skl_281kjuoi-OXz00FFWpUmQQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Set the timeout field in cloudbuild.yaml to what the build really needs (the max is 24h); the default is only 600s. If you submit from the CLI, pass the --timeout flag, e.g. gcloud builds submit --timeout=1800s.

## Steps

1. Set the timeout field in cloudbuild.yaml to what the build really needs (the max is 24h); the default is only 600s. If you submit from the CLI, pass the --timeout flag, e.g. gcloud builds submit --timeout=1800s . Timeouts apply to the whole build, and individual steps can also carry their own timeout that must fit inside the build timeout. If builds keep timing out after raising it, the fix is not a bigger number but a faster build: cache dependencies and split slow steps.

## When to use

You are seeing this: The accepted answer gives the mechanism: 10 minutes is the default timeout, and it is configurable per build. Use this skill when you run into "Cloud Build times out after 10 minutes: raise the build timeout".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_281kjuoi-OXz00FFWpUmQQ). Version: `skv_X99E-rJ-k5J2dHG7dNnu3A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
