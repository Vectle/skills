---
name: "hawkscan-cli-unexpectedly-requests-git-8ccf07897d8201c6"
description: "Shows how to fix hawkScan CLI unexpectedly requests Git password or token when running a scan. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_GwxhIi9fnvxLlXccUy2XOg"
  title: "HawkScan CLI unexpectedly requests Git password or token when running a scan"
  version: "skv_JnEsrikHTvIOsI3P2i6-Uw"
  updated: "2026-10-04T04:30:10.202135+00:00"
  canonical_url: "https://vectle.com/skills/skl_GwxhIi9fnvxLlXccUy2XOg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://help.stackhawk.com/en/articles/6197544-hawkscan-cli-unexpectedly-requests-git-password-or-token-when-running-a-scan\"]"
---

## TL;DR

Unset GIT_URL and rerun hawk scan. Cause: the GIT_URL environment variable is set in the shell that launched the CLI version of HawkScan, causing HawkScan to attempt to pull from the git repo in that variable.

## Steps

1. The GIT_URL env var in your shell makes HawkScan try to clone from it. Unset GIT_URL and rerun hawk scan.

## When to use

You are seeing this: The GIT_URL env var in your shell makes HawkScan try to clone from it. Use this skill when you run into "HawkScan CLI unexpectedly requests Git password or token when running a scan".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_GwxhIi9fnvxLlXccUy2XOg). Version: `skv_JnEsrikHTvIOsI3P2i6-Uw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
