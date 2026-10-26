---
name: "trigger-a-travis-ci-rebuild-without-pu-8707f6be72213ece"
description: "Shows how to fix trigger a Travis CI rebuild without pushing a commit. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_VFqx-lrpO-WSlpunrbnGkQ"
  title: "Trigger a Travis CI rebuild without pushing a commit"
  version: "skv_gDYzSJIUqpPRnPaxgISHjA"
  updated: "2026-10-04T02:19:07.72708+00:00"
  canonical_url: "https://vectle.com/skills/skl_VFqx-lrpO-WSlpunrbnGkQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/17606874/trigger-a-travis-ci-rebuild-without-pushing-a-commit\"]"
---

## TL;DR

With write access to the repo, open the build detail screen and use the Restart Build button, or the trigger-build item under More Options.

## Steps

1. With write access to the repo, open the build detail screen and use the Restart Build button, or the trigger-build item under More Options. Note two caveats: browser extensions like Ghostery can hide the restart button, so disable or whitelist if it is missing; and a restart re-runs the old .travis.yml, so if the config changed upstream you must push a commit or close/reopen the PR to pick it up.

## When to use

You are seeing this: The accepted answer gives the UI path and its caveats. Use this skill when you run into "Trigger a Travis CI rebuild without pushing a commit".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Note two caveats: browser extensions like Ghostery can hide the restart button, so disable or whitelist if it is missing; and a restart re-runs the old.travis.yml, so if the config changed upstream you must push a commit or close/reopen the PR to pick it up.

- The accepted answer gives the UI path and its caveats.


---

Source: [Vectle](https://vectle.com/skills/skl_VFqx-lrpO-WSlpunrbnGkQ). Version: `skv_gDYzSJIUqpPRnPaxgISHjA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
