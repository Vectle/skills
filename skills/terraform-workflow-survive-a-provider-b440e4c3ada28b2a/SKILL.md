---
name: "terraform-workflow-survive-a-provider-b440e4c3ada28b2a"
description: "Provider majors rename arguments, change defaults, and remove deprecated fields. The workflow: read the upgrade guide, stage the bump, review the full plan, roll forward environment by environment. Not the full reference manual."
metadata:
  skill_id: "skl_lSqstMlRC19xgVoL4KMO0A"
  title: "Terraform workflow: survive a provider major version upgrade"
  version: "skv_f9PXazbpY0MIYi4RR5Mqbg"
  updated: "2026-10-03T13:59:36.00893+00:00"
  canonical_url: "https://vectle.com/skills/skl_lSqstMlRC19xgVoL4KMO0A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developer.hashicorp.com/terraform/docs/language/providers/requirements\",\"https://opentofu.org/docs/cli/commands/validate/\"]"
---

**TL;DR:** Provider majors rename arguments, change defaults, and remove deprecated fields. The workflow: read the upgrade guide, stage the bump, review the full plan, roll forward environment by environment. Read the provider's upgrade guide end to end. Note every renamed/removed argument you use: grep your config for each one.

## When

A provider you depend on releases a new major (e.g. AWS provider 5.x to 6.x). The old major will eventually stop receiving updates; upgrading is a matter of scheduling, not if.

## Steps

1. Read the provider's upgrade guide end to end. Note every renamed/removed argument you use: `grep` your config for each one.
2. Update config for the breaking changes first, while still pinned to the old major. `terraform validate` should pass on the old version with the new-style config where the guide allows it.
3. Bump the version constraint to the new major. `terraform init -upgrade`. Read the lock file diff.
4. `terraform plan` in the lowest environment. Expect diffs from changed defaults; classify each as intended or suspicious.
5. Apply non-prod, bake, then promote. One environment at a time, with plan review at each step.

## Rules for agents

1. Never bump the major and "see what the plan says" without reading the guide. The plan shows diffs; the guide explains which diffs are dangerous.
2. Deprecated arguments removed in the major will fail `validate` immediately. Fix all of them before planning; a half-migrated config plans misleadingly.
3. Changed defaults are the silent killers: a default that flips from false to true will not error, it will just change your infrastructure. The upgrade guide lists them; check each against your config.
4. Keep the old-major pin in a branch until the upgrade is fully promoted. Rollback is "revert the bump", which only works if the revert is ready.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_lSqstMlRC19xgVoL4KMO0A). Version: `skv_f9PXazbpY0MIYi4RR5Mqbg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
