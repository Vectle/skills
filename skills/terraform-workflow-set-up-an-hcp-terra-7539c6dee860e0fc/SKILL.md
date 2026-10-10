---
name: "terraform-workflow-set-up-an-hcp-terra-7539c6dee860e0fc"
description: "Connecting a workspace to version control gives speculative plans, run history, and policy checks. The setup workflow: VCS connection, working directory, variables, triggers, branch protections. Not the full reference manual."
metadata:
  skill_id: "skl_qjYaIueJcmPOJwme7UIqMQ"
  title: "Terraform workflow: set up an HCP Terraform VCS-driven workspace from scratch"
  version: "skv_kJALrUQicyKsMWrLCl75jQ"
  updated: "2026-10-03T14:03:14.884273+00:00"
  canonical_url: "https://vectle.com/skills/skl_qjYaIueJcmPOJwme7UIqMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Connecting a workspace to version control gives speculative plans, run history, and policy checks. The setup workflow: VCS connection, working directory, variables, triggers, branch protections. Create the workspace in the right project. Set the Terraform working directory to the config subdirectory if the repo is a monorepo.

## When

A new service or environment needs the full HCP workflow: plans on PRs, applies on merge, variable management, and policy checks.

## Steps

1. Create the workspace in the right project. Set the Terraform working directory to the config subdirectory if the repo is a monorepo.
2. Connect the VCS repo and set the trigger patterns: which branches and paths trigger runs. `main`-only applies with PR speculative plans is the standard.
3. Set the execution mode: Remote for consistency, Agent if runs need private network access. This decision is load-bearing; make it deliberately.
4. Add variables: non-sensitive as Terraform variables, secrets as sensitive variables or via a variable set shared across the project's workspaces.
5. Wire run triggers for upstream/downstream workspace ordering (network applies before app plans).
6. Enable speculative plans on PRs and cost estimation. Require the plan status check in branch protection.
7. Test the loop: open a no-op PR (whitespace), confirm the speculative plan runs and posts; merge, confirm the apply run triggers.

## Rules for agents

1. The working directory setting is the most common misconfiguration. A workspace pointed at the repo root when the config lives in `terraform/` plans nothing or plans the wrong thing.
2. Do not connect the workspace to a branch developers push to directly. The VCS flow assumes PR review; direct pushes bypass it.
3. Variable sets over per-workspace variables for anything shared. Per-workspace copies drift; this was decided in the variable-sets skill.
4. After setup, the workspace should never need local runs. If someone is running `terraform apply` locally against this workspace's state, the workflow is broken; fix the workflow, not the person.

## When to use this

- This covers exactly what the title says: Terraform workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Terraform; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_qjYaIueJcmPOJwme7UIqMQ). Version: `skv_kJALrUQicyKsMWrLCl75jQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
