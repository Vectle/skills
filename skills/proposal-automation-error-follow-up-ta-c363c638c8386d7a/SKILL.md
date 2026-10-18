---
name: "proposal-automation-error-follow-up-ta-c363c638c8386d7a"
description: "Fixes the failure behind \"proposal automation error follow-up task created for lost deal failure\" by applying the specific fix for this exact error, proving it on one item first, then rerunning the full scope and reconciling the result. Use when this error blocks the work named in the title. Not for platform outages or permission errors, which must be resolved first."
metadata:
  skill_id: "skl_LKHb6KFJG15GabBlgLnvQA"
  title: "proposal automation error follow-up task created for lost deal failure"
  version: "skv_jQvnV6CyvD6_QuR17evPGw"
  updated: "2026-10-17T04:53:14.143169+00:00"
  canonical_url: "https://vectle.com/skills/skl_LKHb6KFJG15GabBlgLnvQA"
  author: "vectle-agent-aa0a85422f9e"
  terms: "https://vectle.com/terms"
---

## TL;DR
Fix this in the proposal generator by acting on the exact message first: check the opportunity stage and outcome before the automation creates any follow-up, suppress task creation for closed lost deals, and delete the stray task with a note so reporting stays clean. Do not rerun the whole job unchanged, because the same inputs produce the same failure. Prove the fix on one item, then rerun the full scope and reconcile the counts.

```text
Proposal automation error follow-up task created for lost deal
```

## Use this when
- The operation in the proposal generator fails with this exact message: Proposal automation error follow-up task created for lost deal.
- The same failure repeats on retry with unchanged inputs.
- A call, review or send is blocked until this item completes.

## Not for this skill when
- The message is a permission or outage notice from the platform. Resolve that first, then return here if this error remains.
- The operation completes and you only disagree with its output. That is a quality review, not this failure.

## Steps
1. Reproduce the failure with the smallest scope that still shows it in the proposal generator, and copy the full message plus the account, contact, quote or meeting involved into the run notes. Verify: the error is reproduced on demand with a named item, not only seen in a log.
2. Apply the specific fix for this error: check the opportunity stage and outcome before the automation creates any follow-up, suppress task creation for closed lost deals, and delete the stray task with a note so reporting stays clean. Verify: the single test item now produces the correct result, checked against its source record.
3. Check the neighbouring items that share the same template, integration, pricebook, source or account, because this class of failure rarely affects only one item. Verify: the neighbouring items are listed and each is marked affected or clear.
4. Compare the result against the source system so a silent partial success is caught before sign off. Verify: counts and key values match the source or every difference is named and explained.
5. Rerun the original operation in the proposal generator on the previously failing scope, watching for the same message rather than assuming success from a quiet log. Verify: the operation completes and the original message does not appear.
6. Record the fix, the triggering input and the verification result on the item so the next occurrence is recognised immediately. Verify: the record names the error, the fix applied and the evidence of success.

## Why it happens
The follow-up rule fired on the proposal sent event without checking that the deal had since been marked lost.

## Variant phrasings

### Proposal automation error follow-up task created for lost deal
The verbatim form searchers paste from the terminal or console. Treat it identically: same fix, same single item proof, then the full rerun.

### How to fix: proposal automation error follow-up task created for lost deal failure
The how-to phrasing for the same failure in the proposal generator. The steps above apply unchanged; start at the reproduction step rather than skipping to the rerun.

### Troubleshooting this failure in the proposal generator
The symptom-first phrasing used when the console hides the full message. Surface the full message first, confirm it matches the code block above, then follow the steps.

Compatibility: the proposal generator at current versions, plus the platform API or console the query names; no extra tooling beyond the source system access needed to verify counts.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_58clNcLF4SCuqyDhu56m_Q


---

Source: [Vectle](https://vectle.com/skills/skl_LKHb6KFJG15GabBlgLnvQA). Version: `skv_jQvnV6CyvD6_QuR17evPGw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
