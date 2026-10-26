---
name: "incorrect-service-networking-config-fo-ceb4dbd61f1dfaa1"
description: "Shows how to fix incorrect Service Networking config for instance: xxxx:SERVICE_NETWORKING_NOT_ENABLED. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_X1UKnu5OynLEtwPMed0UCg"
  title: "Incorrect Service Networking config for instance: xxxx:SERVICE_NETWORKING_NOT_ENABLED"
  version: "skv_zeZ_1mr5I4sO0rkoc4waug"
  updated: "2026-10-03T14:03:18.251616+00:00"
  canonical_url: "https://vectle.com/skills/skl_X1UKnu5OynLEtwPMed0UCg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/66536427/incorrect-service-networking-config-for-instance-xxxxservice-networking-not-en\"]"
---

## TL;DR

If you see the following error: Error: Error, failed to create instance xxxx: googleapi: Error 400: Invalid request: Incorrect Service Networking config for instance: xxxx:xxxxx:SERVICE_NETWORKING_NOT_ENABLED., invalid Enable the Service Networking API: `` gcloud services enable servicenetworking.googleapis.com --project=[PSM\_PROJECT\_NUMBER] ` Getting Started with the Service Networking API Context: Stack Overflow #66536427 (accepted answer, 37 votes): I'm trying to replicate a SQL instance in GCP via terraform.

## Steps

1. If you see the following error: Error: Error, failed to create instance xxxx: googleapi: Error 400: Invalid request: Incorrect Service Networking config for instance: xxxx:xxxxx:SERVICE_NETWORKING_NOT_ENABLED., invalid Enable the Service Networking API:

``` gcloud services enable servicenetworking.googleapis.com --project=[PSM_PROJECT_NUMBER] ```

2. Getting Started with the Service Networking API

## When to use

You are seeing this: The active instance has a public IP, however subnets from a secondary project are shared with the project hosing the SQL instance, and the SQL instance is associated with the secondary project's network. Use this skill when you run into "Incorrect Service Networking config for instance: xxxx:SERVICE_NETWORKING_NOT_ENABLED".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_X1UKnu5OynLEtwPMed0UCg). Version: `skv_zeZ_1mr5I4sO0rkoc4waug`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
