---
name: "cloud-sql-proxy-error-during-createeph-004f957992d6f03f"
description: "Shows how to fix cloud SQL Proxy: \"Error during createEphemeral ... Error 403: The client is not authorized to make this request\". Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_FVfknsv9ERJ_wBRUSEM39w"
  title: "Cloud SQL Proxy: \"Error during createEphemeral ... Error 403: The client is not authorized to make this request\""
  version: "skv_R5Uqw0vtfqRh_kxSqNVSRA"
  updated: "2026-10-03T13:57:08.839138+00:00"
  canonical_url: "https://vectle.com/skills/skl_FVfknsv9ERJ_wBRUSEM39w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_crWGpb4ZbifUfz0AeRqbtg\",\"https://github.com/GoogleCloudPlatform/cloud-sql-proxy/issues/37\"]"
---

## TL;DR

Remove the Cloud SQL Client role from the failing service account in IAM & Admin > IAM (uncheck it and Save), verify the account disappears from the list, then Add it back with the Cloud SQL Client role and Save.

## Steps

1. The Cloud SQL proxy failed at startup with: couldn't connect to "PROJECT:REGION:INSTANCE": ensure that the account has access ... Error during createEphemeral for PROJECT:REGION:INSTANCE: googleapi: Error 403: The client is not authorized to make this request., notAuthorized. The instance connection name was correct and the service account already had the Cloud SQL Client role , in one case two identically-configured service accounts behaved differently, one working and one failing.

2. What actually fixes it (verified in the thread):

3. This is a known IAM propagation quirk, not a proxy bug: re-grant the role to force it to take effect. Remove the Cloud SQL Client role from the failing service account in IAM & Admin > IAM (uncheck it and Save), verify the account disappears from the list, then Add it back with the Cloud SQL Client role and Save. Multiple users confirmed this fixed the identical 403 createEphemeral error, with one reporting the fix was still relevant two years later. Also double-check the connection name for typos , project IDs use dashes, not underscores, which was the original reporter's first mistake. Source: https://github.com/GoogleCloudPlatform/cloud-sql-proxy/issues/37

## When to use

You are seeing this: The situation: The Cloud SQL proxy failed at startup with: couldn't connect to "PROJECT:REGION:INSTANCE": ensure that the account has access... Use this skill when you run into "Cloud SQL Proxy: "Error during createEphemeral ... Error 403: The client is not authorized to make this request"".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Also double-check the connection name for typos , project IDs use dashes, not underscores, which was the original reporter's first mistake.

## Sources

- https://github.com/GoogleCloudPlatform/cloud-sql-proxy/issues/37


---

Source: [Vectle](https://vectle.com/skills/skl_FVfknsv9ERJ_wBRUSEM39w). Version: `skv_R5Uqw0vtfqRh_kxSqNVSRA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
