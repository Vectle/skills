---
name: "search-attributes-registration-is-lost-f0410a94823ec773"
description: "Shows how to fix search attributes registration is lost after successfully adding. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl__KMSCCW3eABnOVtroV7AsQ"
  title: "Search attributes registration is lost after successfully adding"
  version: "skv_in3cPHY4m4UzyjCT9kYJ6A"
  updated: "2026-10-03T14:17:07.300675+00:00"
  canonical_url: "https://vectle.com/skills/skl__KMSCCW3eABnOVtroV7AsQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/temporalio/temporal/issues/4160\"]"
---

## TL;DR

E.g. in this integ test failure: https://github.com/indeedeng/iwf/actions/runs/4682724673/jobs/8297177058 In dump docker logs you can see: `` You are about to add search...

## Steps

1. What was reported:
Issue temporalio/temporal#4160 (closed, 12 comments): ## Expected Behavior
The search attributes should never got lost after registering

2. Sometimes it will get lost

3. This is the script that I used to register search attributes automatically after service is up running in docker. 
It happens occasionally that one of the three (randomly) will be lost after the CLI command show up the registering is succeeded.

4. E.g. in this integ test failure: https://github.com/indeedeng/iwf/actions/runs/4682724673/jobs/8297177058

5. In dump docker logs you can see:
```
 You are about to add search...

6. What works:
Register all search attributes in a single CLI call using the Temporal CLI (not the deprecated `tctl`):

7. temporal search-attribute create --namespace default \
 --name CustomKeywordField --type Keyword \
 --name CustomIntField --type Int

8. Two things from the thread: the `tctl` code path was out of date relative to Temporal CLI, so switching CLIs matters; and search-attribute caches refresh about once a minute, while the `list` command reads persistence directly, so use it to verify. Known edge case: adding several same-type attributes at once could lose one; a fix PR (#4273) was proposed but not confirmed merged, so the single-call pattern above is the safe approach.

## When to use

You are seeing this: This is the script that I used to register search attributes automatically after service is up running in docker. Use this skill when you run into "Search attributes registration is lost after successfully adding".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Edge cases

- Known edge case: adding several same-type attributes at once could lose one; a fix PR (#4273) was proposed but not confirmed merged, so the single-call pattern above is the safe approach.

## Sources

- https://github.com/indeedeng/iwf/actions/runs/4682724673/jobs/8297177058


---

Source: [Vectle](https://vectle.com/skills/skl__KMSCCW3eABnOVtroV7AsQ). Version: `skv_in3cPHY4m4UzyjCT9kYJ6A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
