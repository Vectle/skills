---
name: "terraform-workflow-brownfield-import-o-dfd6ca03b9537155"
description: "Adopting click-ops infrastructure into Terraform means importing every object then converging config. The workflow: inventory, import blocks, generate config, converge to a clean plan. Not the full reference manual."
metadata:
  skill_id: "skl_1wqaXThMUwrIw7lWXb4DFg"
  title: "Terraform workflow: brownfield import of existing infrastructure"
  version: "skv_2QlrMItuyEDr0yVrpWa8ng"
  updated: "2026-10-03T14:07:05.574009+00:00"
  canonical_url: "https://vectle.com/skills/skl_1wqaXThMUwrIw7lWXb4DFg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/import/\",\"https://opentofu.org/docs/language/import/generating-config/\"]"
---

**TL;DR:** Adopting click-ops infrastructure into Terraform means importing every object then converging config. The workflow: inventory, import blocks, generate config, converge to a clean plan. Terraform workflow: brownfield import of existing infrastructure When Infrastructure exists (console, CloudFormation, another tool) and Terraform needs to adopt it without recreation. Write import blocks with verified IDs (see the import-ID diagnostic).

## When

Infrastructure exists (console, CloudFormation, another tool) and Terraform needs to adopt it without recreation.

## Steps

1. Inventory: list every real object in scope (console, CLI, tagging). You cannot import what you have not listed, and missed objects become drift later.
2. Write import blocks with verified IDs (see the import-ID diagnostic). Group by resource type. For many objects, `for_each` on import blocks beats hand-writing dozens.
3. Write minimal resource blocks to receive the imports, or use `-generate-config-out` to generate starting config. Generated config is a draft: review and normalize it (naming, tags, structure) before keeping.
4. `terraform plan`: the import preview shows what will be adopted. Then `terraform apply` performs the imports.
5. Converge: the post-import plan will show diffs (generated config rarely matches reality exactly). Iterate on config until `terraform plan` is clean. Config describes reality now.

## Rules for agents

1. Never import directly into the production workspace first. Practice the full loop on a copy or a non-prod account; import IDs and generated config always need one iteration.
2. Import in dependency order where it matters, or all at once with import blocks and let Terraform sort it out. Do not import half the objects and apply config changes in the same run.
3. The converged clean plan is the definition of done. "Imported" without a clean plan is half-adopted and will surprise the next apply.
4. After adoption, delete the import blocks or keep them as origin records, and set up the normal CI plan/apply flow. Brownfield done right ends as greenfield workflow.

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

Source: [Vectle](https://vectle.com/skills/skl_1wqaXThMUwrIw7lWXb4DFg). Version: `skv_2QlrMItuyEDr0yVrpWa8ng`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
