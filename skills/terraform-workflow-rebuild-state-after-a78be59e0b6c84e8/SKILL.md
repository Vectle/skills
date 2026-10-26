---
name: "terraform-workflow-rebuild-state-after-a78be59e0b6c84e8"
description: "The state file is gone and there is no backup. The recovery workflow: inventory reality, reconstruct config, bulk import, converge to clean. Slow, methodical, and it works. Not the full reference manual."
metadata:
  skill_id: "skl_mzguZsPV2DAQ5pf8US0p_A"
  title: "Terraform workflow: rebuild state after state loss"
  version: "skv_6hoWZS0WIP3pAoin_E76XQ"
  updated: "2026-10-03T14:05:58.990881+00:00"
  canonical_url: "https://vectle.com/skills/skl_mzguZsPV2DAQ5pf8US0p_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/import/\",\"https://opentofu.org/docs/language/settings/backends/s3/\"]"
---

**TL;DR:** The state file is gone and there is no backup. The recovery workflow: inventory reality, reconstruct config, bulk import, converge to clean. Stop all applies and CI jobs touching this workspace. Inventory reality: list every object in the cloud account that the config should manage.

## When

The state file was deleted, the backend bucket was lost, or corruption is unrecoverable. No backup exists (if a backup exists, restore it; this workflow is the last resort).

## Steps

1. Stop all applies and CI jobs touching this workspace. Recovery and concurrent writes do not mix.
2. Inventory reality: list every object in the cloud account that the config should manage. Tagging discipline pays off here; without it this is manual.
3. Reconstruct the config to describe reality as it is now, not as it was historically. Write it fresh; do not try to reproduce the old config from memory.
4. Bulk import: import blocks with `for_each` where possible, verified IDs, `terraform plan` to preview, then apply. Work resource type by resource type.
5. Converge: iterate config until `terraform plan` is clean. The clean plan is the proof the state matches reality.
6. Set up what was missing: backend versioning, state backups, and restricted delete permissions on the state bucket so this never recurs.

## Rules for agents

1. This is the incident where patience matters most. Rushing the inventory produces a state file that disagrees with reality, which is worse than no state file.
2. Objects you cannot identify: do not import blindly. An imported mystery object becomes your responsibility; investigate first.
3. Secrets in the rebuilt state: assume the old state's secrets are burned if the loss involved unauthorized access. Rotate after recovery.
4. Write the postmortem: how the state was lost, why no backup existed, and the three concrete preventions now in place.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_mzguZsPV2DAQ5pf8US0p_A). Version: `skv_6hoWZS0WIP3pAoin_E76XQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
