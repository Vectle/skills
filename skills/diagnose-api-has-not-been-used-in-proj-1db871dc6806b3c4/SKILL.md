---
name: "diagnose-api-has-not-been-used-in-proj-1db871dc6806b3c4"
description: "Shows how to fix diagnose: API has not been used in project before or it is disabled. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_FY0INLpJi4Hi-qIlhSfrRg"
  title: "Diagnose: API has not been used in project before or it is disabled"
  version: "skv_geeqQDIIelWNM86zyvcbaA"
  updated: "2026-10-03T13:44:48.555758+00:00"
  canonical_url: "https://vectle.com/skills/skl_FY0INLpJi4Hi-qIlhSfrRg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/apis/docs/getting-started\"]"
---

## TL;DR

Enable it by visiting... then retry." Cause: the API is not enabled on that project. Symptom: "[SERVICE] has not been used in project [P] before or it is disabled.

## Steps

1. Symptom: "[SERVICE] has not been used in project [P] before or it is disabled. Enable it by visiting ... then retry."

2. Cause: the API is not enabled on that project. Nothing about your code or IAM is wrong yet.

3. Confirm:
1. Copy the API name from the error exactly (it is like storage.googleapis.com, not a friendly name).
2. `gcloud services list --enabled --project [P] | grep [API]` - absent confirms it.
3. Check you are looking at the right project: `gcloud config list` core/project vs the [P] in the error. Agents often enable the API on the wrong project.

```
gcloud services enable [API] --project [P]
```

4. Then wait 1-2 minutes for propagation before retrying. Immediate retry can still fail; that is propagation, not a new problem.

5. If the enable call itself 403s: your identity lacks serviceusage.services.use on the project. That is a separate IAM grant (Service Usage Admin), not a problem with the API name.

6. Terraform path: add a google_project_service resource for the API so enablement is in state and ordered before resources that need it.

7. Verify: the API appears in the enabled list, then the original call succeeds. If it still fails with the same message after 5 minutes, re-check the project id character by character.

## When to use

You are seeing this: Nothing about your code or IAM is wrong yet. Use this skill when you run into "Diagnose: API has not been used in project before or it is disabled".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_FY0INLpJi4Hi-qIlhSfrRg). Version: `skv_geeqQDIIelWNM86zyvcbaA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
