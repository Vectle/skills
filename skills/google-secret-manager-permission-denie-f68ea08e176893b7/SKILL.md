---
name: "google-secret-manager-permission-denie-f68ea08e176893b7"
description: "Shows how to fix google Secret Manager PERMISSION_DENIED API has not been used in project wrong project number. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Y0gTGkFz6Z8Yf0MeVW2JEw"
  title: "Google Secret Manager PERMISSION_DENIED API has not been used in project wrong project number"
  version: "skv_cttO7oP_WTOqkqBbdErg3w"
  updated: "2026-10-03T13:55:52.16643+00:00"
  canonical_url: "https://vectle.com/skills/skl_Y0gTGkFz6Z8Yf0MeVW2JEw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Check that your project ID is actually being injected (a misnamed.env file or an unset env var produces exactly this) and always pass the fully-qualified secret name.

## Steps

1. Calling the Secret Manager API fails with: Error: 7 PERMISSION_DENIED: Secret Manager API has not been used in project 698910892233 before or it is disabled, but that project number is not the caller's project. The credentials belong to a different project, which makes the error message misleading.

2. What actually fixes it (verified in the thread):

3. This misleading error means the secret name you passed is not a full resource path. Secret names must be the full path like projects/PROJECT/secrets/SECRET/versions/latest, a bare or partial name makes the API resolve against the wrong project. Check that your project ID is actually being injected (a misnamed .env file or an unset env var produces exactly this) and always pass the fully-qualified secret name.

## When to use

You are seeing this: The credentials belong to a different project, which makes the error message misleading. Use this skill when you run into "Google Secret Manager PERMISSION_DENIED API has not been used in project wrong project number".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_Y0gTGkFz6Z8Yf0MeVW2JEw). Version: `skv_cttO7oP_WTOqkqBbdErg3w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
