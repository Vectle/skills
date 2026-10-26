---
name: "terraform-workflow-ephemeral-pull-requ-b6eb75a49885c36f"
description: "Spin up a full environment per PR and destroy it on merge. The workflow: workspace or directory per PR, seeded variables, destroy plan on close, and cost guardrails. Not the full reference manual."
metadata:
  skill_id: "skl_unHoFekZllBiV06W-3Xy1g"
  title: "Terraform workflow: ephemeral pull-request environments with automated teardown"
  version: "skv_k8JLzQ2nz_ieQd2hPx0lgA"
  updated: "2026-10-03T14:04:26.271546+00:00"
  canonical_url: "https://vectle.com/skills/skl_unHoFekZllBiV06W-3Xy1g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/workspace/\",\"https://opentofu.org/docs/cli/commands/plan/\"]"
---

**TL;DR:** Spin up a full environment per PR and destroy it on merge. The workflow: workspace or directory per PR, seeded variables, destroy plan on close, and cost guardrails. Seed with PR-specific variables (names, tags with the PR number and TTL). Verify teardown: the destroy job confirms zero remaining resources for that environment.

## When

Integration testing needs real infrastructure per change: preview environments for PRs that touch Terraform or the app it deploys.

## Steps

1. PR opened: CI creates the environment. Options: `terraform workspace new pr-[number]` on a shared config, or a parameterized directory. Seed with PR-specific variables (names, tags with the PR number and TTL).
2. `terraform apply` with the PR's config. Post the key outputs (URLs, connection info) as a PR comment so reviewers can actually use the environment.
3. PR merged or closed: CI runs `terraform plan -destroy -out` and, after the standard destroy review (automated for ephemeral envs with tight scoping), applies the destroy.
4. Verify teardown: the destroy job confirms zero remaining resources for that environment. Orphaned PR environments are the cost leak.

## Rules for agents

1. Ephemeral envs must be cheap and bounded: small instance types, short TTLs, and a reaper job that destroys environments older than N days regardless of PR state. PRs get abandoned; the reaper is the backstop.
2. Never let ephemeral envs share state or backends with permanent environments. One key prefix per PR, derived from the PR number.
3. Name everything with the PR number. Untagged mystery resources from dead PRs are the number one ephemeral-env failure.
4. The destroy on PR close must be as automated as the create. A manual teardown step will be skipped under deadline pressure, every time.
5. Cost: put a budget alert on the ephemeral-env account/project. Preview environments have a way of becoming load-test environments at 3am.

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

Source: [Vectle](https://vectle.com/skills/skl_unHoFekZllBiV06W-3Xy1g). Version: `skv_k8JLzQ2nz_ieQd2hPx0lgA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
