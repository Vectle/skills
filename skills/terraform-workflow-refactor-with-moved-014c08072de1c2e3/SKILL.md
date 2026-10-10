---
name: "terraform-workflow-refactor-with-moved-014c08072de1c2e3"
description: "Renaming resources or restructuring modules without moved blocks destroys and recreates. The workflow: add moved blocks, plan to confirm moves only, apply, keep the blocks as history. Not the full reference manual."
metadata:
  skill_id: "skl_nkAsUOQel_kymO99w3lblw"
  title: "Terraform workflow: refactor with moved blocks, zero recreation"
  version: "skv_76APjeolQ5hiHd4HzNH0-Q"
  updated: "2026-10-03T14:00:46.180685+00:00"
  canonical_url: "https://vectle.com/skills/skl_nkAsUOQel_kymO99w3lblw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Renaming resources or restructuring modules without moved blocks destroys and recreates. The workflow: add moved blocks, plan to confirm moves only, apply, keep the blocks as history. Anytime an address changes but the real object should not. Write the new config (new addresses) AND the moved blocks in the same change: 2. terraform plan.

## When

Renaming a resource, moving a resource into or out of a module, or restructuring module boundaries. Anytime an address changes but the real object should not.

## Steps

1. Write the new config (new addresses) AND the moved blocks in the same change:
   ```
   moved {
     from = aws_instance.web
     to   = module.web.aws_instance.main
   }
   ```
2. `terraform plan`. The plan must show moves, not destroy/create. Read every line: any destroy/create pair is a moved block that did not match.
3. Fix mismatches before applying: check `terraform state list` for the real `from` addresses. Typos are the usual cause.
4. `terraform apply`. Verify with `terraform state list` that only the new addresses exist.
5. Keep the moved blocks in config permanently (or at least until every collaborator and CI job has applied past the move). They are cheap and they document history.

## Rules for agents

1. One refactor per change. Mixing a rename with real infrastructure changes makes the plan unreadable and the rollback ambiguous.
2. For bulk renames (count to for_each, module restructuring), generate the moved blocks programmatically and review the generated list. Hand-writing twenty moved blocks invites typos.
3. `terraform state mv` achieves the same result imperatively. Prefer moved blocks in config because they are reviewable and replayable; use state mv only for moves the block syntax cannot express.
4. Never let a refactor plan with destroy/create pairs through review "because it is just a rename". A rename that recreates is a data-loss event for stateful resources.

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

Source: [Vectle](https://vectle.com/skills/skl_nkAsUOQel_kymO99w3lblw). Version: `skv_76APjeolQ5hiHd4HzNH0-Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
