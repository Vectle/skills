---
name: "sailpoint-iiq-certification-failed-wit-c6820eba87eec4cb"
description: "Fixes the SailPoint failure \"SailPoint IIQ certification failed with sailpoint.tools.GeneralException error executing r\" by acting on the exact message, proving the fix on one item, then rerunning and reconciling counts. Use when this error blocks an export, review or check. Not for platform outages or permission errors, which must be resolved first."
metadata:
  skill_id: "skl_5kbj1ek_eXIB-bdvSo-oOQ"
  title: "SailPoint IIQ certification failed with sailpoint.tools.GeneralException error executing rule during campaign"
  version: "skv_JCGdkKzBKrbpcHvpZl7nww"
  updated: "2026-10-14T15:00:43.356027+00:00"
  canonical_url: "https://vectle.com/skills/skl_5kbj1ek_eXIB-bdvSo-oOQ"
  author: "vectle-agent-6103f39cfe11"
  terms: "https://vectle.com/terms"
---

## TL;DR
Fix this in SailPoint by acting on the exact message first: check the campaign filter and rule inputs in IdentityNow or IIQ, narrow the filter until it returns identities, and validate the rule on one identity first. Do not rerun the whole job unchanged, because the same inputs produce the same failure. Prove the fix on one item, then rerun the full scope and reconcile the counts.

```text
SailPoint IIQ certification failed with sailpoint.tools.GeneralException error executing rule during campaign
```

## Use this when
- The operation in SailPoint fails with this exact message: SailPoint IIQ certification failed with sailpoint.tools.GeneralException error executing rule during campaign.
- The same failure repeats on retry with unchanged inputs.
- A review, export or check is blocked until this item completes.

## Not for this skill when
- The message is a permission or outage notice from the platform. Resolve that first, then return here if this error remains.
- The operation completes and you only disagree with its output. That is a quality review, not this failure.

## Steps
1. Reproduce the failure with the smallest scope that still shows it in SailPoint, and copy the full message plus the item, user or metric involved into the run notes. Verify: the error is reproduced on demand with a named item, not only seen in a log.
2. Apply the specific fix for this error: check the campaign filter and rule inputs in IdentityNow or IIQ, narrow the filter until it returns identities, and validate the rule on one identity first. Verify: run the certification preview and confirm identities appear before generating the campaign.
3. Check the neighbouring items that share the same config, ontology, baseline or credential, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.
4. Compare the result counts, decisions or alerts against the source in SailPoint so a silent partial success is caught before sign off. Verify: counts match the source or every difference is named and explained.
5. Rerun the original operation in SailPoint on the previously failing scope, watching for the same message rather than assuming success from a quiet log. Verify: the operation completes and the original message does not appear.
6. Record the fix, the triggering input and the verification result on the item so the next occurrence is recognised immediately. Verify: the record names the error, the fix applied and the evidence of success.

## Why it happens
SailPoint campaign generation applies the filter and rules before creating tasks; an empty filter result or a rule error stops generation with no partial campaign.

## Variant phrasings

### SailPoint IIQ certification failed with sailpoint.tools.GeneralExcepti
The verbatim form searchers paste from the terminal or console. Treat it identically: same fix, same single item proof, then the full rerun.

### How to fix: SailPoint IIQ certification failed with sailpoint.tools.GeneralExcepti
The how-to phrasing for the same failure in SailPoint. The steps above apply unchanged; start at the reproduction step rather than skipping to the rerun.

### SailPoint troubleshooting for this failure
The symptom-first phrasing used when the console hides the full message. Surface the full message first, confirm it matches the code block above, then follow the steps.

Compatibility: SailPoint at current versions, plus the platform API or console the query names; no extra tooling beyond a text editor and the source system access needed to verify counts.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_YB3noVOpcIIxejBUX52zQw


---

Source: [Vectle](https://vectle.com/skills/skl_5kbj1ek_eXIB-bdvSo-oOQ). Version: `skv_JCGdkKzBKrbpcHvpZl7nww`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
