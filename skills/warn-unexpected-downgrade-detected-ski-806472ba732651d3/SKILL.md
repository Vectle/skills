---
name: "warn-unexpected-downgrade-detected-ski-806472ba732651d3"
description: "It appears to be isolated to `docker` versioning, which is used for the docker datasource and also for github actions. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_2z7_WNjH77Pf-UmwG6-u0Q"
  title: "WARN: Unexpected downgrade detected: skipping"
  version: "skv_g-q9pE__X60gQlTJFmmYbw"
  updated: "2026-10-03T04:31:15.481483+00:00"
  canonical_url: "https://vectle.com/skills/skl_2z7_WNjH77Pf-UmwG6-u0Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/renovatebot/renovate/issues/29919\"]"
---

## TL;DR

It appears to be isolated to `docker` versioning, which is used for the docker datasource and also for github actions.

## The error, verbatim

```text
WARN: Unexpected downgrade detected: skipping { "packageName": "ghcr.io/renovatebot/renovate" "currentValue": "37.440.0" "compareValue": "37.440.0" "currentVersion": "37.440.0" "update": { "bucket": "latest", "newVersion": "37.49.0", "newValue": "37.49.0", "newMajor": 37, "newMinor": 49, "newPatch": 0, "updateType": "patch" } "allVersionsLength": 5787 "filteredReleaseVersions": [ "37.49.0" ] }
```

## Fix

[maintainer viceice]: Saw it on our helm chart repo for renovate image ``` WARN: Unexpected downgrade detected: skipping { "packageName": "ghcr.io/renovatebot/renovate" "currentValue": "37.440.0" "compareValue": "37.440.0" "currentVersion": "37.440.0" "update": { "bucket": "latest", "newVersion": "37.49.0", "newValue": "37.49.0", "newMajor": 37, "newMinor": 49, "newPatch": 0, "updateType": "patch" } "allVersionsLength": 5787 "filteredReleaseVersions": [ "37.49.0" ] } ``` https://developer.mend.io/github/renovatebot/helm-charts/-/job/c23bc731-28f2-4222-89b3-4a44a521c064

Context: Issue renovatebot/renovate#29919 (closed, 41 comments): ### Describe the proposed change(s). Renovate in some cases is creating PRs to update dependencies where it's actually a downgrade. It appears to be isolated to `docker` versioning, which is used for the docker datasource and also for github actions. Discussion: #29901 Unfortunately we are not yet able to reproduce it Update: we have added code to suppress such workarounds and log a message `WARN: Unexpected downgrade detected: skipping` instead, so I have updated the title of this Issue to match

## Matched source
Source: Published skill
Original query: "WARN: Unexpected downgrade detected: skipping"
Key terms: detected, downgrade, skipping, unexpected, warn

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_2z7_WNjH77Pf-UmwG6-u0Q). Version: `skv_g-q9pE__X60gQlTJFmmYbw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
