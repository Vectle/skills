---
name: "uploadcare-google-drive-breaks-when-th-b2b6e336aedf0823"
description: "Shows how to fix uploadcare: Google Drive breaks when the widget uses the tabs option. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_NY_hYGiC8jDBKVAaHK4XPw"
  title: "Uploadcare: Google Drive breaks when the widget uses the tabs option"
  version: "skv_sQXcnDYHeAF7JKj1nL0ujA"
  updated: "2026-10-04T08:13:42.524513+00:00"
  canonical_url: "https://vectle.com/skills/skl_NY_hYGiC8jDBKVAaHK4XPw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

The cause was on Uploadcare's side: the Google Drive iframe required more width to render its UI and silently failed without it. Fixed server-side by Uploadcare: the Drive iframe width was restored, so no widget update is needed.

## Steps

1. Fixed server-side by Uploadcare: the Drive iframe width was restored, so no widget update is needed. The team asked the reporter to revert the iframe width to its previous value and confirmed the integration works again, then closed the issue.

## When to use

You are seeing this: Using the uploadcare widget with the tabs option (e.g. tabs: 'file gdrive dropbox onedrive box url'), the Google Drive integration breaks: Drive shows as connected, but My Files, Shared with me, Starred, and Team drives do nothing when clicked. Use this skill when you run into "Uploadcare: Google Drive breaks when the widget uses the tabs option".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The cause was on Uploadcare's side: the Google Drive iframe required more width to render its UI and silently failed without it.


---

Source: [Vectle](https://vectle.com/skills/skl_NY_hYGiC8jDBKVAaHK4XPw). Version: `skv_sQXcnDYHeAF7JKj1nL0ujA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
