---
name: "flowise-in-memory-vector-store-not-wor-06105004ebdca689"
description: "Shows how to fix flowise In Memory Vector Store not working after docker image update. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_MIXYQpgaExtgWHs-KBXMaw"
  title: "Flowise In Memory Vector Store not working after docker image update"
  version: "skv_K8Pb8Impz__gy5PWVCKoew"
  updated: "2026-10-03T14:09:25.274842+00:00"
  canonical_url: "https://vectle.com/skills/skl_MIXYQpgaExtgWHs-KBXMaw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The maintainer pushed the fix in release 1.8.1, so the answer is to upgrade to 1.8.1 or later and pull the new image. A maintainer responded on the thread and the reporter confirmed it was fixed.

## Steps

1. My chatflows used the In Memory Vector Store and everything was fine until I pulled the latest Flowise docker image, after which the vector store just stopped working. The issue was closed in May 2024. A maintainer responded on the thread and the reporter confirmed it was fixed.

2. What actually fixes it (verified in the thread):

3. This was a regression in the Flowise docker build that broke the In Memory Vector Store. The maintainer pushed the fix in release 1.8.1, so the answer is to upgrade to 1.8.1 or later and pull the new image. The reporter thanked them and confirmed it worked, so theres no config workaround, just the version.

## When to use

You are seeing this: The situation: My chatflows used the In Memory Vector Store and everything was fine until I pulled the latest Flowise docker image, after which the vector store just stopped working. Use this skill when you run into "Flowise In Memory Vector Store not working after docker image update".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 1.8.1. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_MIXYQpgaExtgWHs-KBXMaw). Version: `skv_K8Pb8Impz__gy5PWVCKoew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
