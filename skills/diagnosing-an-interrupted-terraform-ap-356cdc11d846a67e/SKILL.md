---
name: "diagnosing-an-interrupted-terraform-ap-356cdc11d846a67e"
description: "Killed applies leave unknown state. The procedure: refresh, plan, compare against reality, and reconcile each half-created resource before the next apply. Not the full reference manual."
metadata:
  skill_id: "skl_3MS3nzpVYjvo5RiaTe1O2g"
  title: "Diagnosing an interrupted Terraform apply: what actually got created"
  version: "skv_1Z9NNUswNDyWdCI-j9wRzA"
  updated: "2026-10-03T15:14:36.060514+00:00"
  canonical_url: "https://vectle.com/skills/skl_3MS3nzpVYjvo5RiaTe1O2g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/plan/\",\"https://opentofu.org/docs/cli/commands/apply/\"]"
---

**TL;DR:** Killed applies leave unknown state. The procedure: refresh, plan, compare against reality, and reconcile each half-created resource before the next apply. Resources it never reached show as creates. Resources created but not in state (crash between API success and state write): import them or let the next apply recreate, never both.

# Diagnosing an interrupted Terraform apply

## Symptom

An apply was killed: CI timeout, Ctrl-C, runner eviction, network drop. You do not know which resources were created, which failed, and what the state file recorded.

## Cause

Terraform writes state after each resource operation completes. A kill between operations leaves a consistent but partial state: everything before the kill is recorded, everything after is not. The danger is not corruption, it is not knowing where the boundary is.

## Confirmation

1. `terraform refresh` (or `terraform plan -refresh-only`) to reconcile state with reality. This is read-only and safe.
2. `terraform plan` and read every proposed change. Resources the killed run created show as no-change. Resources it never reached show as creates.
3. For anything ambiguous, check the cloud console/API directly. State is a cache; the API is truth.

## Fix

1. Resources created but not in state (crash between API success and state write): `import` them or let the next apply recreate, never both. If the next apply would create a duplicate, import first.
2. Resources half-configured (created but setup steps failed): `terraform apply -replace=[address]` to rebuild cleanly, or fix in place if the resource supports it.
3. Tainted resources from the failed run: `terraform untaint` only if you have verified the object is healthy; otherwise replace.

## Verification

1. A final `terraform plan` shows zero changes. That is the definition of done.
2. Spot-check critical resources in the console: the plan being clean plus the objects existing and configured is the full verification.

## When to use this

- This covers exactly what the title says: Diagnosing an interrupted Terraform apply.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Diagnosing behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_3MS3nzpVYjvo5RiaTe1O2g). Version: `skv_1Z9NNUswNDyWdCI-j9wRzA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
