---
name: "heroku-pg-copy-fails-after-a-few-start-ab9a76c3bf8bf1b9"
description: "Shows how to fix `heroku pg:copy` fails after a few `starting copy` logs. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_52gR2OptfYc_tVDYeix-EQ"
  title: "`heroku pg:copy` fails after a few `starting copy` logs"
  version: "skv_NQrmPU3Psb2-fcb0TsJuvw"
  updated: "2026-10-03T14:15:05.589539+00:00"
  canonical_url: "https://vectle.com/skills/skl_52gR2OptfYc_tVDYeix-EQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/heroku/cli/issues/3146\"]"
---

## TL;DR

Run with HEROKU_DEBUG=1 and HEROKU_DEBUG_HEADERS=1 to see where the copy stalls, and consider pinning the CLI version in your CI install step if a newer release broke it.

## Steps

1. Do you want to request a *feature* or report a *bug*? ----------------------------------------------------- We are running on the latest version. We use `curl https://cli-assets.heroku.com/install-ubuntu.sh | sh` to install the heroku cli.

2. If heroku pg:copy fails after a few 'starting copy' logs on the latest CLI, one reporter resolved it by downgrading the Heroku CLI to 9.5.1. Run with HEROKU_DEBUG=1 and HEROKU_DEBUG_HEADERS=1 to see where the copy stalls, and consider pinning the CLI version in your CI install step if a newer release broke it.

## When to use

You are seeing this: Do you want to request a feature or report a bug? ----------------------------------------------------- We are running on the latest version. Use this skill when you run into "`heroku pg:copy` fails after a few `starting copy` logs".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 9.5.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://cli-assets.heroku.com/install-ubuntu.sh


---

Source: [Vectle](https://vectle.com/skills/skl_52gR2OptfYc_tVDYeix-EQ). Version: `skv_NQrmPU3Psb2-fcb0TsJuvw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
