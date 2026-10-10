---
name: "only-some-dsyms-get-uploaded-to-fireba-60051c25098768a2"
description: "Shows how to fix only some dSYMs get uploaded to Firebase Crashlytics from Codemagic. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_TDhhxCwQHB0qaeKEnqovvA"
  title: "Only some dSYMs get uploaded to Firebase Crashlytics from Codemagic"
  version: "skv_q14BLfAMb6SyUpdfLF6RIQ"
  updated: "2026-10-04T15:03:33.15657+00:00"
  canonical_url: "https://vectle.com/skills/skl_TDhhxCwQHB0qaeKEnqovvA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

The corrected script lists all dSYM files, resolves the parent directory of each zip, and runs upload-symbols against all of them. The reporter confirmed all symbols went up after the change.

## Steps

1. Drop the | head -1 so every dSYM archive is uploaded, not just the first match. The corrected script lists all dSYM files, resolves the parent directory of each zip, and runs upload-symbols against all of them. The reporter confirmed all symbols went up after the change.

## When to use

You are seeing this: Following the Codemagic docs for uploading iOS dSYMs to Firebase Crashlytics, only one archive's symbols made it. Use this skill when you run into "Only some dSYMs get uploaded to Firebase Crashlytics from Codemagic".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Following the Codemagic docs for uploading iOS dSYMs to Firebase Crashlytics, only one archive's symbols made it.


---

Source: [Vectle](https://vectle.com/skills/skl_TDhhxCwQHB0qaeKEnqovvA). Version: `skv_q14BLfAMb6SyUpdfLF6RIQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
