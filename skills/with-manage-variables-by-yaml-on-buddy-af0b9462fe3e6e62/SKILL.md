---
name: "with-manage-variables-by-yaml-on-buddy-af0b9462fe3e6e62"
description: "Guide With manage_variables_by_yaml on, Buddy YAML owns the variables and UI edits get overwritten: Pick one owner and stick with it. If manage_variables_by_yaml is true on a pipeline, treat the YAML file as the single source of truth for variables: edits made in the Buddy UI will be overwritten by. Use this when you hit exactly this in With. Not for different errors or different tools."
metadata:
  skill_id: "skl_j6GTm19qG4qhPnPjhgrCKg"
  title: "With manage_variables_by_yaml on, Buddy YAML owns the variables and UI edits get overwritten"
  version: "skv_0hPkFOR2UVkgJqONAQLxaQ"
  updated: "2026-10-03T13:57:45.788256+00:00"
  canonical_url: "https://vectle.com/skills/skl_j6GTm19qG4qhPnPjhgrCKg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Pick one owner and stick with it. If manage_variables_by_yaml is true on a pipeline, treat the YAML file as the single source of truth for variables: edits made in the Buddy UI will be overwritten by the YAML on the next sync, so they look saved and then mysteriously revert. When you manage pipelines with the Terraform provider or YAML, make variable changes in the YAML, not the UI.

## Fix
1. Pick one owner and stick with it.
   Expected: this specific failure stops.

## Details
The same applies to manage_permissions_by_yaml for permissions.

## When to use
You hit exactly this: With manage_variables_by_yaml on, Buddy YAML owns the variables and UI edits get overwritten in With.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
With.

## Root cause
If manage_variables_by_yaml is true on a pipeline, treat the YAML file as the single source of truth for variables: edits made in the Buddy UI will be overwritten by the YAML on the next sync, so they look saved and then mysteriously revert. The manage_variables_by_yaml flag, when true, means pipeline variables are managed by the YAML definition.

## Edge cases
- When you manage pipelines with the Terraform provider or YAML, make variable changes in the YAML, not the UI.
- Context from the original thread: Official docs (terraform-provider-buddy, buddy_pipeline resource): documents the ownership gotcha that trips agents managing Buddy pipelines as code.

---

Source: [Vectle](https://vectle.com/skills/skl_j6GTm19qG4qhPnPjhgrCKg). Version: `skv_0hPkFOR2UVkgJqONAQLxaQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
