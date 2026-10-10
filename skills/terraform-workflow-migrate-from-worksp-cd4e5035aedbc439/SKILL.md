---
name: "terraform-workflow-migrate-from-worksp-cd4e5035aedbc439"
description: "Workspaces served until prod needed real isolation. The migration: new directory roots per env, state moved per workspace, backend configs separated, CI retargeted. Not the full reference manual."
metadata:
  skill_id: "skl_iDp_GfvQJEVsIqflFNO_Fw"
  title: "Terraform workflow: migrate from workspaces to directory-per-environment"
  version: "skv_r0c-tnB19HNPIpdLyXlR0Q"
  updated: "2026-10-03T13:45:23.948775+00:00"
  canonical_url: "https://vectle.com/skills/skl_iDp_GfvQJEVsIqflFNO_Fw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Workspaces served until prod needed real isolation. The migration: new directory roots per env, state moved per workspace, backend configs separated, CI retargeted. Create the directory structure: envs/dev, envs/staging, envs/prod, each a root module calling the shared child modules. Verify per env: terraform plan in the new directory must be clean against that env's state.

## When

`terraform workspace select` nearly (or actually) applied dev config to prod state. The team wants hard separation: different backends, different credentials, no shared mutable selector.

## Steps

1. Create the directory structure: `envs/dev`, `envs/staging`, `envs/prod`, each a root module calling the shared child modules. Extract the shared config into modules first if it is not already modular.
2. Per environment: copy the workspace's state to the new backend key. Procedure per env: `terraform workspace select [env]`, `terraform state pull > backup-[env].json`, configure the new directory's backend, `terraform init -migrate-state` answering with the backed-up state.
3. Verify per env: `terraform plan` in the new directory must be clean against that env's state. Do this for dev first, then staging, then prod.
4. Retarget CI: one job per directory, each with its own credentials and backend config. Delete the workspace-selection logic from the pipeline.
5. Only after all envs verify: remove the old workspace states (`terraform workspace delete` after selecting each, with the new dirs confirmed working).

## Rules for agents

1. One environment per session, lowest first. The prod migration happens last and gets the most review.
2. Keep the shared modules identical across envs during migration. Refactoring modules AND migrating layout in one change is two risks multiplied.
3. Different credentials per environment is the point of the exercise. If prod and dev still share credentials after migration, you moved deck chairs.
4. After migration, `terraform workspace` commands should have no workspaces left with real state. Verify; leftover workspaces are confusion waiting to happen.

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

Source: [Vectle](https://vectle.com/skills/skl_iDp_GfvQJEVsIqflFNO_Fw). Version: `skv_r0c-tnB19HNPIpdLyXlR0Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
