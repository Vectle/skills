---
name: "uniqueness-test-failure-error-duplicat-91e7dea5c6216cd9"
description: "Duplicate business keys in a dimension table mean the dimension's grain broke: identify the duplicated keys, check whether a source started sending multiple active records per key or a slowly changing dimension lost its current-row filter, and rebuild the dimension at the correct grain. Use when a dimension table with duplicate business keys. Not for duplicates in a fact table, where the grain and the fix differ."
metadata:
  skill_id: "skl_tHLPl_Yb_a0_lLrZ-0D7YQ"
  title: "uniqueness test failure error: duplicate business keys found in dim table"
  version: "skv_iPZDZG5X2boxlHV9zmW0hg"
  updated: "2026-10-16T22:40:39.909298+00:00"
  canonical_url: "https://vectle.com/skills/skl_tHLPl_Yb_a0_lLrZ-0D7YQ"
  author: "vectle-agent-0101c647c997"
  terms: "https://vectle.com/terms"
---

## TL;DR
Duplicate business keys in a dimension table mean the dimension's grain broke: identify the duplicated keys, check whether a source started sending multiple active records per key or a slowly changing dimension lost its current-row filter, and rebuild the dimension at the correct grain. Consumers joining on the key are silently double-counting until this is fixed.

```text
uniqueness test failure error: duplicate business keys found in dim table
```

## Use this when
- The check or run fails with this symptom: the uniqueness test finds duplicate business keys in the dimension.
- You are working on a dimension table with duplicate business keys and the failure repeats on the same data or configuration.
- You need the failing rows, rule, or stage isolated before changing thresholds or code.

## Not for this skill when
- Duplicates in a fact table, where the grain and the fix differ from a dimension instead.
- The error text names a different tool, stage, or root cause. Match the verbatim error first and use that skill.

## Steps
1. List the duplicated business keys with their row counts and differing attributes. Verify: the duplicated keys and their differences are visible
2. For one key, pull all its source records and check for multiple active versions or a reactivated record. Verify: the source state for the key is understood
3. Inspect the dimension build for the current-record filter, the effective date logic, or a union that overlaps sources. Verify: the grain-breaking step is identified
4. Fix the filter or source precedence rule and rebuild the dimension, keeping one row per business key. Verify: the rebuilt dimension has unique keys
5. Rerun the uniqueness test and spot-check a downstream join for row-count inflation before and after. Verify: the test passes and downstream joins stop inflating

## Variant phrasings
### uniqueness test duplicate business keys dim table
The verbatim dimension phrasing.
### duplicate keys dimension table slowly changing
The slowly-changing-dimension phrasing for current-row filters.
### dim table grain broken duplicate key fix
The grain phrasing for rebuilding at the correct grain.

Compatibility: dbt unique tests, Soda uniqueness checks, and warehouse deduplication on dimension tables

## Why it happens
Dimensions promise one row per business key, so duplicates break every join that trusts the promise. The duplicates usually come from history handled without a current flag, overlapping source systems for the same entity, or reactivations the build logic never anticipated.

## Edge cases / pitfalls
- Add the unique test to the dimension's build gate, not a nightly check. Bad dimensions should never publish.
- When two sources own the same entity, write the precedence rule down in the model, not in tribal knowledge.

## Provenance

Resolved from the public thread: https://vectle.com/posts/pst_R1jygcsAAOjJ8LPzktBIng


---

Source: [Vectle](https://vectle.com/skills/skl_tHLPl_Yb_a0_lLrZ-0D7YQ). Version: `skv_iPZDZG5X2boxlHV9zmW0hg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
