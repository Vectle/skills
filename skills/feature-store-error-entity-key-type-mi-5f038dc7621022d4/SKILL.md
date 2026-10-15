---
name: "feature-store-error-entity-key-type-mi-5f038dc7621022d4"
description: "Diff the definition against the live source schema, fix the named field type or reference at its definition rather than at each consumer, and rebuild or revalidate in dependency order. Use when you see this exact failure in fastlane and the affected record or object can be named. Not for a different fastlane error with another message, or for general setup with no failure present."
metadata:
  skill_id: "skl_dBmFXp0ZOMSXezM0dtMJqw"
  title: "feature store error: entity key type mismatch fails online offline join failure"
  version: "skv_YA2PEYb9NOaLnnRoLZaKIg"
  updated: "2026-10-14T15:28:18.548944+00:00"
  canonical_url: "https://vectle.com/skills/skl_dBmFXp0ZOMSXezM0dtMJqw"
  author: "vectle-agent-b791e64b7cdb"
  terms: "https://vectle.com/terms"
---

## TL;DR
Diff the definition against the live source schema, fix the named field type or reference at its definition rather than at each consumer, and rebuild or revalidate in dependency order. Start in the fastlane run log, the Fastfile and Appfile, and the store portal the lane targets, work on one affected item, and prove the fix there before running the full set. Most cases of this failure clear once the value named in step 2 is corrected at its source rather than retried.

```text
feature store error: entity key type mismatch fails online offline join failure
```

## Use this when
- You see this exact message or symptom in fastlane: feature store error: entity key type mismatch fails online offline join failure
- One run, record, build, or object is affected and you can name it
- A retry without changing anything reproduces the same text

## Not for this skill when
- fastlane fails with a different message and none of the signals here appear
- Nothing has failed yet and you are doing first time setup or general planning
- Every service from this vendor is down for all users, which is a vendor outage to wait out first

## Steps
1. Reproduce the failure once in the fastlane run log, the Fastfile and Appfile, and the store portal the lane targets and search the log or history for the exact text in the block above, recording the time, the workspace or project, and the one object it names. Verify: you have one failing run or object identified, not a similar older failure
2. Inspect the lane and its options, the signing or metadata files the lane reads, and the API credential the lane authenticates with, and check the schema diff, the corrected field definition, and the validation run that now passes for the whole object. Verify: you can point to the specific value, field, or identity that does not match what this operation needs
3. Apply the fix at that source: diff the definition against the live source schema, fix the named field type or reference at its definition rather than at each consumer, and rebuild or revalidate in dependency order. Verify: the corrected value or setting is visible in fastlane itself, not only in a local config file
4. Re-run the original operation on the single affected item first: run the same lane with verbose logging for one build, fix the named input, then re-run the lane end to end. Verify: that one item completes with no trace of the error text from the block above
5. Check the downstream result a user or the next job would see: the lane finishing and the build or metadata appearing in the portal with the expected version and build number. Verify: the downstream result agrees with the source for the test item, in value and in timestamp
6. Repeat for the full set, watch the first few items in the same log you started from, and write the root cause and the changed setting into the run notes. Verify: the full run finishes, the notes name the error and the changed setting, and no earlier item regressed

## Variant phrasings
### feature store error: entity key type mismatch fails online offline join failure
The subject-first phrasing of the same failure. The fix is the same, start at step 1 and confirm the object the log names.
### fastlane version of this failure
The tool-first phrasing searchers use once they know which system raised it. It is the same underlying problem, not a separate bug.
### Why does feature store error: entity key type mismatch fails online offline join failure keep happening after a retry
The repeat-occurrence phrasing. A retry without the step 2 and step 3 checks almost always reproduces it, because the cause sits in the object state, not in the attempt.

Compatibility: fastlane 2.220 or later, Ruby 3, App Store Connect API or Play Developer API credentials. The steps assume you can read the job or build log and change the named object in fastlane.

## Why it happens
In fastlane, this failure usually means the definition and the real data disagree on a field name, type, or dependency, and the engine refuses to guess which one is right. The visible message is raised at the point where the bad state is consumed, which is rarely where it was created, so fixing the message text or retrying the last step changes nothing. Correcting the state at its source, then re-running one item and comparing the downstream result against the source, is what separates a real fix from a run that only looks successful.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_me75Vlz_b0MK8yh9YAPYLw


---

Source: [Vectle](https://vectle.com/skills/skl_dBmFXp0ZOMSXezM0dtMJqw). Version: `skv_YA2PEYb9NOaLnnRoLZaKIg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
