---
name: "speech-to-text-long-audio-sync-caps-at-76655a7671eb08d2"
description: "Shows how to fix speech-to-Text long audio: sync caps at 60s, async needs GCS for longer files. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Lu4TVztQzWfPfCnIbOWq4g"
  title: "Speech-to-Text long audio: sync caps at 60s, async needs GCS for longer files"
  version: "skv_fccvSjMDORroGKYppMf9kQ"
  updated: "2026-10-03T14:04:35.758987+00:00"
  canonical_url: "https://vectle.com/skills/skl_Lu4TVztQzWfPfCnIbOWq4g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use recognize for clips under 60 seconds and longrunningrecognize beyond that. Poll the returned operation name until done is true, or pass output_config with a GCS URI so the transcript lands in your bucket without polling.

## Steps

1. Use recognize for clips under 60 seconds and longrunningrecognize beyond that. Put audio longer than a minute in a GCS bucket first; a local file over 60 seconds errors even on async calls. Poll the returned operation name until done is true, or pass output_config with a GCS URI so the transcript lands in your bucket without polling.

## When to use

You are seeing this: Put audio longer than a minute in a GCS bucket first; a local file over 60 seconds errors even on async calls. Use this skill when you run into "Speech-to-Text long audio: sync caps at 60s, async needs GCS for longer files".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_Lu4TVztQzWfPfCnIbOWq4g). Version: `skv_fccvSjMDORroGKYppMf9kQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
