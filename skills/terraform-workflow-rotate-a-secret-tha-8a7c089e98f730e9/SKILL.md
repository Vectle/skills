---
name: "terraform-workflow-rotate-a-secret-tha-8a7c089e98f730e9"
description: "Rotating a Terraform-managed secret touches state, config, and every consumer. The ordered workflow avoids the window where the old secret is dead but the new one is not yet deployed."
metadata:
  skill_id: "skl_JoEf54AM8p78PZyYbKwwpA"
  title: "Terraform workflow: rotate a secret that lives in Terraform state"
  version: "skv_dAbzyOr0ye18JbhurrM5GA"
  updated: "2026-10-03T13:52:15.628995+00:00"
  canonical_url: "https://vectle.com/skills/skl_JoEf54AM8p78PZyYbKwwpA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Rotating a Terraform-managed secret touches state, config, and every consumer. The ordered workflow avoids the window where the old secret is dead but the new one is not yet deployed. Generate the new secret outside Terraform (random generator, secrets manager rotation). Update the config to the new value. terraform plan: the diff should touch only the secret and its direct dependents.

## The fix

**TL;DR:** Rotating a Terraform-managed secret touches state, config, and every consumer. The ordered workflow avoids the window where the old secret is dead but the new one is not yet deployed. Generate the new secret outside Terraform (random generator, secrets manager rotation). Update the config to the new value. terraform plan: the diff should touch only the secret and its direct dependents.

## When

Scheduled rotation, a leak (see the secrets-in-state diagnostic), or a team member departure. The secret is managed by Terraform (database password, API token stored as a resource attribute).

## Steps

1. Identify every consumer of the secret value Terraform outputs, app configs, CI variables, other workspaces via remote state. The rotation is only done when all consumers have the new value.
2. Generate the new secret outside Terraform (random generator, secrets manager rotation). Do not hand-craft secrets.
3. Update the config to the new value. `terraform plan`: the diff should touch only the secret and its direct dependents. If the plan wants to recreate half the infrastructure, the secret is coupled too broadly; fix that first.
4. Apply in non-prod first. Verify the application actually works with the new secret before touching prod.
5. Apply prod. Immediately verify: can the app authenticate? Check logs, not just the plan.
6. Revoke the old secret at the provider/IdP. Rotation is not complete until the old value stops working.

## Rules for agents

1. The dangerous window is between "new secret applied" and "consumers updated". Order it so consumers can tolerate either value during the window, or update consumers first where the system supports dual secrets.
2. Never put the new secret on the command line or in chat logs. It goes config -> state -> apply, through files, not through terminal history.
3. Mark the variable `sensitive = true` if it is not already. Rotation is the moment to fix the handling, not just the value.
4. After rotation, old state versions and plan logs still contain the old secret. If the rotation was leak-driven, treat those artifacts as compromised until the old secret is revoked (step 6 handles this).

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_JoEf54AM8p78PZyYbKwwpA). Version: `skv_dAbzyOr0ye18JbhurrM5GA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
