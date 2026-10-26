---
name: "finding-the-correct-terraform-import-i-1fc61d512c1fbfdc"
description: "Import IDs are provider-specific and the docs bury them. The procedure: provider docs, then the resource's read path, then a trial import into a scratch config, never straight into production state."
metadata:
  skill_id: "skl__178vdZNCUgO72U5ntAzQg"
  title: "Finding the correct Terraform import ID for any resource"
  version: "skv_IXHKWPTMzEKQWXQxEx01Yw"
  updated: "2026-10-03T15:19:46.62718+00:00"
  canonical_url: "https://vectle.com/skills/skl__178vdZNCUgO72U5ntAzQg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/language/import/\"]"
---

**TL;DR:** Import IDs are provider-specific and the docs bury them. The procedure: provider docs, then the resource's read path, then a trial import into a scratch config, never straight into production state. Finding the correct Terraform import ID for any resource Symptom You need to import an existing object and do not know what id (Terraform) or identity (OpenTofu) value the provider expects. Copy it verbatim.

## Symptom

You need to import an existing object and do not know what `id` (Terraform) or `identity` (OpenTofu) value the provider expects.

## Cause

Import IDs are arbitrary per provider: sometimes the plain ID (`i-abc123`), sometimes a composite (`vpc-id/subnet-id`), sometimes the ARN, sometimes the name. There is no universal rule.

## Confirmation

1. Provider registry docs for the resource, section "Import". This documents the exact ID format. Copy it verbatim.
2. If the docs are unclear, look at how the provider's Read function identifies the object: the ID is usually the primary identifier the API uses.
3. Trial in a scratch config: a minimal config with the import block (or `terraform import` CLI) against a non-production copy first. `terraform plan` with an import block shows what will be imported before anything changes.

## Fix

1. Write the import block with the verified ID format. For bulk imports, `for_each` on import blocks handles many objects of the same type.
2. Run `terraform plan`: the import section of the plan confirms each object resolves. Fix ID formats here, not during apply.
3. After apply, the next plan must be clean. If it is not, the config does not match the imported object; adjust config, not state.

## Verification

1. `terraform state list` shows the imported addresses.
2. Clean plan afterwards. An import that leaves a perpetual diff imported the wrong object or the wrong ID format.
3. Delete the scratch trial config. Import blocks can stay as documentation or be removed; either is fine, but be deliberate.

## When to use this

- This covers exactly what the title says: Finding the correct Terraform import ID for any resource.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Finding; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Finding behavior.

---

Source: [Vectle](https://vectle.com/skills/skl__178vdZNCUgO72U5ntAzQg). Version: `skv_IXHKWPTMzEKQWXQxEx01Yw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
