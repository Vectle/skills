---
name: "terraform-workflow-upgrade-a-registry-ad097646d2916ae6"
description: "Bumping a module version can rename resources and change defaults. The workflow: changelog, isolated bump, init -upgrade, full plan review, non-prod first. Not the full reference manual."
metadata:
  skill_id: "skl_HhRtLM8ABK2QvtV0eJZt9g"
  title: "Terraform workflow: upgrade a registry module version safely"
  version: "skv_OkIIEVI_pguizY_mR5gFSw"
  updated: "2026-10-03T14:02:00.349753+00:00"
  canonical_url: "https://vectle.com/skills/skl_HhRtLM8ABK2QvtV0eJZt9g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Bumping a module version can rename resources and change defaults. The workflow: changelog, isolated bump, init -upgrade, full plan review, non-prod first. Read the module's changelog/releases for the version range you are crossing. Note breaking changes, renamed resources, new required inputs, changed defaults.

## When

A registry module you depend on releases a new version with features, fixes, or a major with breaking changes. Dependabot-style blind bumps are how destroy/create pairs ship to prod.

## Steps

1. Read the module's changelog/releases for the version range you are crossing. Note breaking changes, renamed resources, new required inputs, changed defaults.
2. Bump the `version` constraint in the module block. One module per change.
3. `terraform init -upgrade` to install the new module version.
4. `terraform plan` and read every change. Classify each: expected (the reason you upgraded), neutral (renames with moved handling), suspicious (destroy/create on stateful resources, new resources you did not ask for).
5. Apply in the lowest environment first. Let it bake. Then promote through environments one at a time.

## Rules for agents

1. Major version bumps are projects, not edits. Budget time for the changelog, the plan review, and the bake period.
2. If the plan shows destroy/create pairs for stateful resources, check whether the module provides moved blocks or upgrade notes for the rename. If not, write the moved blocks yourself before applying.
3. Changed defaults are silent behavior changes: a new default encryption setting or instance type will not show as an error, only as a plan diff. Read defaults in the changelog, not just breaking changes.
4. After upgrading in one environment, the lock file and config change together. Commit both; a version bump without the lock file update is half a change.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_HhRtLM8ABK2QvtV0eJZt9g). Version: `skv_OkIIEVI_pguizY_mR5gFSw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
