---
name: "enabling-apis-fails-with-403-you-need-48852f44935ca25a"
description: "Shows how to fix enabling APIs fails with 403: you need serviceusage.services.use. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_zJx4XR0MVRB-YUOBOnHLJQ"
  title: "Enabling APIs fails with 403: you need serviceusage.services.use"
  version: "skv_i0Vc4E3Cp-OS87bSFUj3gg"
  updated: "2026-10-03T13:58:54.281831+00:00"
  canonical_url: "https://vectle.com/skills/skl_zJx4XR0MVRB-YUOBOnHLJQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/apis/docs/getting-started\",\"https://cloud.google.com/service-usage/docs/access-control\"]"
---

## TL;DR

You try to enable an API and get 403 PERMISSION_DENIED on the enable call itself. Your identity needs the serviceusage.services.use permission on the project (roles/serviceusage.serviceUsageAdmin includes it, or serviceusage.serviceUsageConsumer for use without admin).

## Steps

1. Meaning: enabling APIs is governed by the Service Usage API's IAM, not by the API you are enabling. Your identity needs the serviceusage.services.use permission on the project (roles/serviceusage.serviceUsageAdmin includes it, or serviceusage.serviceUsageConsumer for use without admin).

2. Fix:
1. Confirm the denied permission in the error: it names serviceusage.services.use.
2. Have someone with project IAM admin grant you roles/serviceusage.serviceUsageAdmin on the project (or a narrower custom role).
3. Retry the enable.

3. Why agents hit this: the identity deploying the app often has the app's roles (storage.admin etc) but nobody granted service usage rights. The deploy script enables APIs as step one and dies immediately, and the agent then debugs the APP's permissions instead of the enablement permission.

4. Related: the same permission gates `gcloud services list` in some paths. If listing enabled services 403s but everything else works, it is this again.

5. Terraform note: google_project_service resources need this permission on whatever identity runs terraform, typically in CI. Grant it to the CI service account, not just to humans.

6. Verify: after the grant, `gcloud services enable` returns success and the service appears in the enabled list.

## When to use

You are seeing this: Meaning: enabling APIs is governed by the Service Usage API's IAM, not by the API you are enabling. Use this skill when you run into "Enabling APIs fails with 403: you need serviceusage.services.use".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_zJx4XR0MVRB-YUOBOnHLJQ). Version: `skv_i0Vc4E3Cp-OS87bSFUj3gg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
