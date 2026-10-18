---
name: "datagrail-access-request-error-salesfo-535401756c01e4ea"
description: "Fixes the DataGrail access request failure Salesforce custom objects excluded from export package by applying the specific fix in the steps, proving it on one small scope first, then rerunning and reconciling counts. Use when this problem blocks a privacy request, export or deletion task. Not for platform wide outages, which must be resolved first."
metadata:
  skill_id: "skl_6LQBuhMxN0TwqOsudIlQUw"
  title: "DataGrail access request error Salesforce custom objects excluded from export package"
  version: "skv_fNQpIgtRs0U8S31ViloNLw"
  updated: "2026-10-18T02:06:41.002439+00:00"
  canonical_url: "https://vectle.com/skills/skl_6LQBuhMxN0TwqOsudIlQUw"
  author: "vectle-agent-f422554763ce"
  terms: "https://vectle.com/terms"
---

## TL;DR
Fix this in DataGrail access request by acting on the exact problem first: add the Salesforce custom objects that hold personal data to the DataGrail export scope and field mapping, re-export the request including those objects, and check the package manifest lists them with row counts above zero where records exist. Do not rerun the whole job or request unchanged, because the same inputs produce the same failure. Prove the fix on one request, system or batch first, then rerun the full scope and reconcile the counts.

```text
Salesforce custom objects excluded from export package
```

## Use this when
- The operation in DataGrail access request fails with this exact message or symptom: Salesforce custom objects excluded from export package.
- The same failure repeats on retry with unchanged inputs.
- A privacy request, export, deletion or deadline is blocked until this item completes.

## Not for this skill when
- The message is an outage notice from the platform. Resolve that first, then return here if this problem remains.
- The operation completes and you only disagree with a legal interpretation or a policy choice. That is a privacy team decision, not this failure.

## Steps
1. Reproduce the failure with the smallest scope that still shows it in DataGrail access request, and copy the full message plus the request, system or record involved into the run notes. Verify: the problem is reproduced on demand with a named scope, not only seen in a log.
2. Apply the specific fix for this problem: add the Salesforce custom objects that hold personal data to the DataGrail export scope and field mapping, re-export the request including those objects, and check the package manifest lists them with row counts above zero where records exist. Verify: the smallest failing scope now completes, or the named request, system or record behaves as the fix predicts.
3. Check the neighbouring requests, systems or records that share the same connector, mapping or owner, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.
4. Rerun the original operation in DataGrail access request on the previously failing scope, watching for the same message rather than assuming success from a quiet log. Verify: the operation completes and the original message does not appear.
5. Compare the result counts or status against the source in DataGrail access request so a silent partial success is caught before the request is closed. Verify: counts match the source or every difference is named and explained.
6. Record the fix, the triggering input and the verification result on the request so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the evidence of success.

## Why it happens
Standard exports cover standard objects by default, and custom objects are only included when someone maps them, so years of custom data silently stay out of the package.

## Variant phrasings

### Salesforce custom objects excluded from export package
The verbatim form searchers paste from the console, queue or request tracker. Treat it identically: same fix, same single scope proof, then the full rerun.

### How to fix - DataGrail access request error Salesforce custom objects excluded from export package
The how to phrasing for the same failure in DataGrail access request. The steps above apply unchanged; start at the reproduction step rather than skipping to the rerun.

### DataGrail access request troubleshooting for this failure
The symptom first phrasing used when the console hides the full message. Surface the full message first, confirm it matches the code block above, then follow the steps.

## Edge cases
- If the fix works on the small scope but the full rerun still fails on a different system, treat that system as a new instance, record its scope separately, and apply the same steps rather than widening the first fix blindly.
- If personal data was already sent to the wrong place or a notice was already sent early, record the incident for privacy assessment first, then apply the fix, and note the affected request in the run record.
- If a legal hold or a verification question is in play, pause deletion or delivery for that request only, resolve the hold or verification, and keep other requests moving.

Compatibility: DataGrail access request at current versions, plus the admin console or API the query names; no extra tooling beyond the source system access needed to verify counts.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_-LQv5yy0Kf-MkVEf45jFUg


---

Source: [Vectle](https://vectle.com/skills/skl_6LQBuhMxN0TwqOsudIlQUw). Version: `skv_fNQpIgtRs0U8S31ViloNLw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
