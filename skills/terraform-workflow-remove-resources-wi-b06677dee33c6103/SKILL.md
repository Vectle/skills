---
name: "terraform-workflow-remove-resources-wi-b06677dee33c6103"
description: "Deleting a config block destroys the object by default. When the object must live on unmanaged (or move to another tool), removed blocks untrack it safely and codify the intent. Not the full reference manual."
metadata:
  skill_id: "skl_crbdaqkzpW58KSTMvBctug"
  title: "Terraform workflow: remove resources without destroying with removed blocks"
  version: "skv_VXmnKUAai7bqRlF69z83Jw"
  updated: "2026-10-03T13:57:56.209289+00:00"
  canonical_url: "https://vectle.com/skills/skl_crbdaqkzpW58KSTMvBctug"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/resources/delete/\"]"
---

**TL;DR:** Deleting a config block destroys the object by default. When the object must live on unmanaged (or move to another tool), removed blocks untrack it safely and codify the intent. Replace the resource block with a removed block: destroy = false is the load-bearing line: without it, Terraform destroys the object. The plan must show the resource being forgotten, with NO destroy.

## When

A resource leaves Terraform management but must keep existing: handoff to another team, migration to another IaC tool, or decomposing a monolith config.

## Steps

1. Replace the resource block with a removed block:
   ```
   removed {
     from = aws_instance.legacy
     lifecycle {
       destroy = false
     }
   }
   ```
   `destroy = false` is the load-bearing line: without it, Terraform destroys the object.
2. `terraform plan`. The plan must show the resource being forgotten, with NO destroy. If it shows a destroy, stop: the lifecycle setting is wrong or in the wrong place.
3. `terraform apply`. Verify the object still exists in the console and no longer appears in `terraform state list`.
4. Keep the removed block as documentation, or delete it once the handoff is complete and everyone has applied past it.

## Rules for agents

1. Default `removed` without the lifecycle block destroys. This is the single most dangerous default in the removal workflow; double-check the block every time.
2. For resources with dependencies: removing a resource others reference breaks their config. Update or remove the references in the same change.
3. Data loss check: if the object holds state (database, bucket with data), confirm the new owner/management before untracking. Untracked and unowned is how data gets deleted by the next person who finds it.
4. Prefer removed blocks over `terraform state rm`: the block is in version control, reviewed, and replayable. state rm is invisible to the next reader.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_crbdaqkzpW58KSTMvBctug). Version: `skv_VXmnKUAai7bqRlF69z83Jw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
