---
name: "aws-secrets-manager-can-t-find-the-spe-327c688357cc5127"
description: "Shows how to fix aWS Secrets Manager can't find the specified secret (AWS Secrets Manager). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_nsZMHnuB8YA20HCpp_2zfA"
  title: "AWS Secrets Manager can't find the specified secret (AWS Secrets Manager)"
  version: "skv_0aJVTSgn6rvM2sbfOdp4Cg"
  updated: "2026-10-04T04:15:27.916316+00:00"
  canonical_url: "https://vectle.com/skills/skl_nsZMHnuB8YA20HCpp_2zfA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

However, it is imperfect because partial ARNs could collide. If you are fetching secrets within the same account, you can just use the secret name (the part after secret - and excluding the dash 6 character -GUID) instead of the full ARN.

## Steps

1. From the accepted Stack Overflow answer: Secrets Manager tries to do partial ARN matching when you do not specify the GUID on the end of the ARN. However, it is imperfect because partial ARNs could collide. If you are fetching secrets within the same account, you can just use the secret name (the part after secret - and excluding the dash 6 character -GUID) instead of the full ARN. But using the full ARN, when you have it, is always best.

## When to use

You are seeing this: From the accepted Stack Overflow answer: Secrets Manager tries to do partial ARN matching when you do not specify the GUID on the end of the ARN. Use this skill when you run into "AWS Secrets Manager can't find the specified secret (AWS Secrets Manager)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_nsZMHnuB8YA20HCpp_2zfA). Version: `skv_0aJVTSgn6rvM2sbfOdp4Cg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
