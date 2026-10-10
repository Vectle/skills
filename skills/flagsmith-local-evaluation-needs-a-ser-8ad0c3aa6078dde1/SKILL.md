---
name: "flagsmith-local-evaluation-needs-a-ser-8ad0c3aa6078dde1"
description: "Shows how to fix flagsmith local evaluation needs a ser. key and hurts on serverless. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_RKPEFUDjCxWgAyFEGUvgaQ"
  title: "Flagsmith local evaluation needs a ser. key and hurts on serverless"
  version: "skv_WfcataaSA3mJFRKjv8DHdw"
  updated: "2026-10-03T14:16:03.818642+00:00"
  canonical_url: "https://vectle.com/skills/skl_RKPEFUDjCxWgAyFEGUvgaQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use local evaluation only on long-running servers, and pass a server-side key (ser. prefix). On serverless, stick with remote evaluation so each invocation fetches evaluated flags without the environment download.

## Steps

1. Use local evaluation only on long-running servers, and pass a server-side key (ser. prefix). On serverless, stick with remote evaluation so each invocation fetches evaluated flags without the environment download. Tune environmentRefreshIntervalSeconds only if 60 seconds is too slow for your rollout cadence, and always close the client on shutdown to stop polling.

## When to use

You are seeing this: On serverless, stick with remote evaluation so each invocation fetches evaluated flags without the environment download. Use this skill when you run into "Flagsmith local evaluation needs a ser. key and hurts on serverless".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_RKPEFUDjCxWgAyFEGUvgaQ). Version: `skv_WfcataaSA3mJFRKjv8DHdw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
