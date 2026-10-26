---
name: "terraform-workflow-safe-destroy-with-a-9d89e7371e72d579"
description: "terraform destroy is the most irreversible command in the toolchain. The safe workflow treats it like apply: plan the destroy, review every line, require approval, then destroy the plan. Not the full reference manual."
metadata:
  skill_id: "skl_EDYpqU1RLBRsFm8U0pvl4w"
  title: "Terraform workflow: safe destroy with a reviewed destroy plan"
  version: "skv_py-h56kF9ngRwdUg6Re3ag"
  updated: "2026-10-03T13:54:03.818102+00:00"
  canonical_url: "https://vectle.com/skills/skl_EDYpqU1RLBRsFm8U0pvl4w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/plan/\",\"https://opentofu.org/docs/cli/commands/apply/\"]"
---

**TL;DR:** terraform destroy is the most irreversible command in the toolchain. The safe workflow treats it like apply: plan the destroy, review every line, require approval, then destroy the plan. Never as a casual cleanup. Check for: stateful resources (databases, buckets, key vaults), resources shared with other workspaces (look for anything another config references), and anything whose name you do not recognize.

## The fix

**TL;DR:** terraform destroy is the most irreversible command in the toolchain. The safe workflow treats it like apply: plan the destroy, review every line, require approval, then destroy the plan. Never as a casual cleanup. Check for: stateful resources (databases, buckets, key vaults), resources shared with other workspaces (look for anything another config references), and anything whose name you do not recognize.

## When

Decommissioning an environment, removing an ephemeral workspace, tearing down a failed experiment. Never as a casual cleanup.

## Steps

1. `terraform plan -destroy -out=destroy.tfplan`. This is a full plan in destroy mode: every resource listed for deletion.
2. Review the destroy plan line by line. Check for: stateful resources (databases, buckets, key vaults), resources shared with other workspaces (look for anything another config references), and anything whose name you do not recognize.
3. Get explicit human approval for the destroy plan. This is the approval gate; the plan file is the artifact being approved.
4. Back up anything stateful first: snapshots, exports, bucket copies. "We can recreate it" is not a backup.
5. `terraform apply destroy.tfplan`. Watch it complete; do not walk away from a destroy.

## Rules for agents

1. Never `terraform destroy -auto-approve`. The flag exists; using it on destroy is never justified.
2. `-target` with destroy is for surgical removal of one resource, not for avoiding review. A targeted destroy still needs its own plan review.
3. If the destroy plan includes resources you did not expect, stop. Unexpected entries mean the config or workspace is not what you think; destroying first and asking later is irreversible.
4. After destroy, verify in the console that the critical resources are actually gone AND that nothing shared was affected. Then remove the workspace/config so nobody re-applies it by accident.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Terraform behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_EDYpqU1RLBRsFm8U0pvl4w). Version: `skv_py-h56kF9ngRwdUg6Re3ag`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
