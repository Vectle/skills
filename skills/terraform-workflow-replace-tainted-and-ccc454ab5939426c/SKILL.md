---
name: "terraform-workflow-replace-tainted-and-ccc454ab5939426c"
description: "Tainted resources recreate on next apply, which surprises teams when the taint was set long ago. The workflow: audit taints, verify health, untaint or replace with a reviewed plan. Not the full reference manual."
metadata:
  skill_id: "skl_whvliQYDGrEGwVjdMNzUHg"
  title: "Terraform workflow: replace tainted and unhealthy resources deliberately"
  version: "skv_PxmZgrHXOYuUQYMnsP5DHg"
  updated: "2026-10-03T13:56:44.184868+00:00"
  canonical_url: "https://vectle.com/skills/skl_whvliQYDGrEGwVjdMNzUHg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/apply/\",\"https://developer.hashicorp.com/terraform/docs/language/meta-arguments/lifecycle\"]"
---

**TL;DR:** Tainted resources recreate on next apply, which surprises teams when the taint was set long ago. The workflow: audit taints, verify health, untaint or replace with a reviewed plan. Verify current health in the console. A tainted resource that is actually healthy should be untainted (terraform untaint [address]), not recreated.

## When

`terraform plan` shows replacements you did not expect, or you know a resource is unhealthy and needs rebuilding.

## Steps

1. Audit: `terraform state list` will not show taint directly; the plan output marks tainted resources. Find why each was tainted: failed provisioner, manual `terraform taint`, or a previous failed apply.
2. Verify current health in the console. A tainted resource that is actually healthy should be untainted (`terraform untaint [address]`), not recreated. Taint is a claim about health; check the claim.
3. For genuinely unhealthy resources: `terraform apply -replace=[address]` forces replacement with a reviewed plan. Prefer `-replace` over `taint` + apply: it is explicit, single-shot, and does not leave taint state lying around for the next person.
4. For config-driven replacement (replace when a secret or AMI changes): `replace_triggered_by` in lifecycle makes the replacement automatic and reviewable in the plan.

## Rules for agents

1. Never untaint a resource you have not verified. Untainting a genuinely broken object just postpones the failure to the worst moment.
2. `terraform taint` is deprecated in favor of `-replace`. If you see taint in runbooks, update the runbook.
3. Replacement of stateful resources destroys data unless the resource handles it (snapshots, replication). Check the data story before replacing anything stateful.
4. After replacement, the plan is clean and the new object is healthy in the console. Both, not either.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Terraform behavior.

## Edge cases

- Replacement of stateful resources destroys data unless the resource handles it (snapshots, replication).

---

Source: [Vectle](https://vectle.com/skills/skl_whvliQYDGrEGwVjdMNzUHg). Version: `skv_PxmZgrHXOYuUQYMnsP5DHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
