---
name: "drive-api-shared-drive-files-404-witho-1a5f94d62528166f"
description: "Shows how to fix drive API: shared-drive files 404 without supportsAllDrives. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_vJf90-AUiC6k20zG_oP8uA"
  title: "Drive API: shared-drive files 404 without supportsAllDrives"
  version: "skv_541Hc_nS5gl4QbmILLoP6w"
  updated: "2026-10-03T14:01:20.037577+00:00"
  canonical_url: "https://vectle.com/skills/skl_vJf90-AUiC6k20zG_oP8uA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/anthropics/claude-tag-plugins/blob/HEAD/google-drive/skills/google-drive-api/SKILL.md\"]"
---

## TL;DR

When Drive API calls 404 on a file you can open in the browser, or list calls silently miss team files, add supportsAllDrives=true first. And always set fields explicitly on list calls, or youll never see the nextPageToken and will stop after the first page.

## Steps

1. When Drive API calls 404 on a file you can open in the browser, or list calls silently miss team files, add supportsAllDrives=true first. Shared-drive content is opt-in per call. And always set fields explicitly on list calls, or youll never see the nextPageToken and will stop after the first page.

## When to use

You are seeing this: Shared-drive content is opt-in per call. Use this skill when you run into "Drive API: shared-drive files 404 without supportsAllDrives".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Also, the default fields subset omits nextPageToken, so always pass fields explicitly.


---

Source: [Vectle](https://vectle.com/skills/skl_vJf90-AUiC6k20zG_oP8uA). Version: `skv_541Hc_nS5gl4QbmILLoP6w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
