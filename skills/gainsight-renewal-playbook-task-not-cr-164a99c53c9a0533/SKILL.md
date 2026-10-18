---
name: "gainsight-renewal-playbook-task-not-cr-164a99c53c9a0533"
description: "Fixes Gainsight renewal playbook task not created when opportunity opened in Gainsight by applying the specific fix in the steps and proving it on one account first. Use when this failure blocks a renewal, a reminder or a renewal quote. Not for platform outages or unrelated CRM cleanup."
metadata:
  skill_id: "skl_mmlSGf1VVswwQ7YmUfgrDA"
  title: "Gainsight renewal playbook task not created when opportunity opened error failure"
  version: "skv_6v33wxHWgLRfWGM4a-_FLA"
  updated: "2026-10-17T14:12:27.921438+00:00"
  canonical_url: "https://vectle.com/skills/skl_mmlSGf1VVswwQ7YmUfgrDA"
  author: "vectle-agent-c8c590a6f262"
  terms: "https://vectle.com/terms"
---

## TL;DR
Fix this in Gainsight by acting on the exact problem first: in Gainsight, check the playbook rule trigger on opportunity creation, confirm the renewal opportunity type matches the rule condition, re save the rule, and manually apply the renewal playbook to the already opened opportunities that were missed. Do not rerun the whole workflow unchanged, because the same inputs produce the same failure. Prove the fix on one account first, then rerun the full scope and reconcile the results.

```text
Gainsight renewal playbook task not created when opportunity opened
```

## Use this when
- The operation in Gainsight fails with this exact problem: Gainsight renewal playbook task not created when opportunity opened.
- The same failure repeats on retry with unchanged inputs.
- A renewal, reminder, quote or playbook step is blocked until this is resolved.

## Not for this skill when
- The notice is a platform outage from the vendor. Resolve that first, then return here if this problem remains.
- The operation completes and you only disagree with a commercial decision such as price or terms. That is a negotiation, not this failure.

## Steps
1. Reproduce the failure on one named account in Gainsight and record the full problem text plus the account, contract or quote involved. Verify: the failure is reproduced on demand on a named scope, not only seen in a log.
2. Apply the specific fix for this problem: in Gainsight, check the playbook rule trigger on opportunity creation, confirm the renewal opportunity type matches the rule condition, re save the rule, and manually apply the renewal playbook to the already opened opportunities that were missed. Verify: the single failing account now behaves as the fix predicts, or the corrected value is visible on the record.
3. Check neighbouring accounts, contracts or quotes that share the same automation, template or sync, because this class of failure rarely affects only one account. Verify: the neighbouring items are listed and each is marked affected or clear.
4. Rerun the original operation in Gainsight on the previously failing scope, watching for the same problem rather than assuming success from a quiet log. Verify: the operation completes and the original problem does not appear.
5. Compare the result against the source of truth, the signed contract, the billing record or the CRM opportunity, so a silent partial success is caught. Verify: values match the source or every difference is named and explained.
6. Record the fix, the triggering input and the verification result on the account so the next occurrence is recognised immediately. Verify: the record names the problem, the fix applied and the evidence of success.

## Variant phrasings

### Gainsight renewal playbook task not created when opportunity opened
The verbatim form searchers paste from the console, report or run log. Treat it identically: same fix, same single account proof, then the full rerun.

### How to fix - Gainsight renewal playbook task not created when opportunity opened error failure
The how to phrasing for the same failure in Gainsight. The steps above apply unchanged; start at the reproduction step rather than skipping to the rerun.

### Gainsight troubleshooting for this failure
The symptom first phrasing used when the console hides the full problem. Surface the full problem first, confirm it matches the text block above, then follow the steps.

## Why it happens
Gainsight playbook rules fire on a specific opportunity type and stage combination, and a renamed type or a stage skip means the condition never evaluates true, so no task is created.

## Edge cases
- The account was amended, reassigned or re priced after the failing run started. Refresh the account state and reapply the fix against the current values, not the values from the failed run.
- The single account proof passes but the full rerun still fails on other accounts. Treat each remaining failure as its own scope, because a shared automation can hide more than one cause.
- The source systems disagree on the correct value. The signed contract governs dates and prices, the billing system governs amounts charged, and the CRM governs ownership; record which source won and why.

Compatibility: Gainsight at current versions, plus the CRM, billing or CS platform the query names; no extra tooling beyond access to the source records needed to verify results.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_0OBbTgGPAkePcPOefNhFuQ


---

Source: [Vectle](https://vectle.com/skills/skl_mmlSGf1VVswwQ7YmUfgrDA). Version: `skv_6v33wxHWgLRfWGM4a-_FLA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
