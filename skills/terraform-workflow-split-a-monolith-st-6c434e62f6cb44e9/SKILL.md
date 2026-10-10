---
name: "terraform-workflow-split-a-monolith-st-6c434e62f6cb44e9"
description: "One giant state file means every plan touches everything and locks block everyone. The workflow: carve service boundaries, state mv resources into new configs, rewire with data sources. Not the full reference manual."
metadata:
  skill_id: "skl_ZzKLuL5FEodJSit0OMeYNg"
  title: "Terraform workflow: split a monolith state into per-service states"
  version: "skv__tlvb9-YdQdXrFLgjJEXwQ"
  updated: "2026-10-03T13:49:43.83285+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZzKLuL5FEodJSit0OMeYNg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** One giant state file means every plan touches everything and locks block everyone. The workflow: carve service boundaries, state mv resources into new configs, rewire with data sources. Create the new root configs (one per service), each with its own backend key. Replace cross-service references: what was a direct reference is now a terraform_remote_state data source or a parameter-store lookup.

## The fix

**TL;DR:** One giant state file means every plan touches everything and locks block everyone. The workflow: carve service boundaries, state mv resources into new configs, rewire with data sources. Create the new root configs (one per service), each with its own backend key. Replace cross-service references: what was a direct reference is now a terraform_remote_state data source or a parameter-store lookup.

## When

Plans take too long, applies lock out the whole team, or one service's change risks another's infrastructure. The monolith state has outlived its usefulness.

## Steps

1. Choose boundaries along blast radius and change cadence: network, data, app are the classic three. Draw the lines before moving anything.
2. Create the new root configs (one per service), each with its own backend key. Do not create new resources yet; these are empty shells with backend config.
3. Move state entries: `terraform state mv` (in the monolith) cannot move across configs directly, so the procedure is: `terraform state pull` from the monolith, and for each service, `terraform state mv` within a combined working setup OR use `terraform state mv -state-out` patterns. The practical approach most teams use: for each service, create its config containing the moved resource blocks, then `terraform state mv` from the monolith state file to the new state file with explicit `-state` and `-state-out` paths.
4. Replace cross-service references: what was a direct reference is now a `terraform_remote_state` data source or a parameter-store lookup. Update config accordingly.
5. Per service: `terraform plan` must be clean (moves only, no creates/destroys). Apply nothing until all services plan clean.

## Rules for agents

1. Back up the monolith state before starting. A failed split without a backup is a rebuild-everything event.
2. One service at a time. Splitting all services in one session multiplies the confusion when a plan misbehaves.
3. Apply order after the split is now load-bearing: network before data before app. Document it and enforce it in CI.
4. The monolith config shrinks as services leave. Do not delete the monolith until every service plans clean independently and the monolith plan is empty.

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

Source: [Vectle](https://vectle.com/skills/skl_ZzKLuL5FEodJSit0OMeYNg). Version: `skv__tlvb9-YdQdXrFLgjJEXwQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
