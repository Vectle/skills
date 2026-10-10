---
name: "diagnosing-a-terraform-plan-that-takes-6a9f74ad7bf8930b"
description: "Plans that hang or crawl have three usual causes: too many resources refreshing, a slow provider API, or dependency chains serializing everything. The procedure isolates which one. Not the full reference manual."
metadata:
  skill_id: "skl_NpUxHwQtPQrFNbEJBL9bfA"
  title: "Diagnosing a Terraform plan that takes forever"
  version: "skv_nndbPU81akhqF5nuL4I_Vg"
  updated: "2026-10-03T14:16:43.248736+00:00"
  canonical_url: "https://vectle.com/skills/skl_NpUxHwQtPQrFNbEJBL9bfA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Plans that hang or crawl have three usual causes: too many resources refreshing, a slow provider API, or dependency chains serializing everything. The procedure isolates which one. Run with TF_LOG=INFO and watch which provider calls take the longest. Fix the call pattern first.

## Symptom

`terraform plan` runs for tens of minutes or appears hung. CI timeouts kill it.

## Cause

1. Refresh fan-out: hundreds of resources each needing an API read, some paginated or throttled.
2. Provider API slowness: one data source or resource with an expensive query (list-all calls, cross-region reads).
3. Serialization: long `depends_on` chains or module dependencies forcing sequential operations that could be parallel.

## Confirmation

1. Run with `TF_LOG=INFO` and watch which provider calls take the longest. The log timestamps per API call; the slow ones stand out.
2. `terraform plan -refresh=false`: if this is fast, the cost is in refresh (cause 1 or 2). If still slow, the cost is in planning logic or serialization (cause 3).
3. Count resources: `terraform state list | wc -l`. Hundreds of resources with per-object API reads is inherently slow; that is a design fact, not a bug.

## Fix

1. Refresh cost: split the config into smaller workspaces so each plan refreshes less. There is no flag that makes 2000 API reads fast.
2. Slow data source: narrow it (specific IDs instead of list-all with filters), or replace a data source with a variable when the value is stable.
3. Serialization: remove unnecessary `depends_on` (references already imply ordering). Break long module chains with data sources where the dependency is read-only.
4. `-parallelism` exists but raising it against a throttling API makes things worse. Fix the call pattern first.

## Verification

1. Time the plan before and after. "Faster" needs a number.
2. `terraform plan -refresh=false` vs full plan timings tell you whether refresh is still the dominant cost.
3. The plan output must be identical in content, just faster. Speedups that change the plan are not speedups.

## When to use this

- This covers exactly what the title says: Diagnosing a Terraform plan that takes forever.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Diagnosing behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_NpUxHwQtPQrFNbEJBL9bfA). Version: `skv_nndbPU81akhqF5nuL4I_Vg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
