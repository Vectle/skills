---
name: "terraform-workflow-migrate-state-from-961d23e807d72bfb"
description: "Moving from terraform.tfstate on disk to shared remote state is a one-way door if done wrong. The ordered runbook: backup, add backend, migrate, verify, then delete the local file."
metadata:
  skill_id: "skl_QSWJAPREwgGbRa2WSpTbkQ"
  title: "Terraform workflow: migrate state from local to a remote S3 backend"
  version: "skv_sw0Nb4TEY05qdDbtBIE2nA"
  updated: "2026-10-03T04:23:55.687199+00:00"
  canonical_url: "https://vectle.com/skills/skl_QSWJAPREwgGbRa2WSpTbkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://opentofu.org/docs/cli/commands/init/\",\"https://opentofu.org/docs/language/settings/backends/s3/\"]"
---

# Terraform workflow: migrate state from local to a remote S3 backend

## TL;DR

Commit everything, back up with `terraform state pull`, create the S3 bucket (versioned) and lock table first, add the backend block, then run `terraform init -migrate-state` and keep the local state when prompted. Only after a clean plan, delete the local tfstate and re-run `terraform init` everywhere.

## When
**When not to use this skill:** moving between two remote backends (no local state involved); tearing state down rather than moving it; workspaces where state was never local to begin with.


The team outgrows local state: more than one operator, any CI, or any need for locking. Do this once per workspace, deliberately.

## Steps

1. Commit everything. `git status` clean. The config must be stable while you move its state.
2. Back up: `terraform state pull > state-backup-local-[date].json`. Verify the file is non-empty and valid JSON.
3. Prepare the remote side first: create the S3 bucket with versioning enabled and a DynamoDB lock table (Terraform path) or set `use_lockfile = true` (OpenTofu path). The backend cannot migrate into infrastructure that does not exist.
4. Add the backend block to config, pointing at the new bucket and a key for this workspace.
5. Run `terraform init -migrate-state`. Terraform detects state in both places and asks which to keep. Answer: the local one (it has the higher serial; confirm by comparing).
6. `terraform plan`. It must be empty or show only expected changes. A create-everything plan means the migration bound the wrong (empty) state: stop, restore from backup, investigate.
7. Only after a clean plan: delete the local `terraform.tfstate` and its backup from the working dir (keep the backup file somewhere safe, outside the repo). Add `*.tfstate*` to gitignore if not already there.

## Rules for agents

1. Never skip the backup. Migration prompts are easy to answer wrong under time pressure.
2. Migrate one workspace at a time. Migrating dev, staging, and prod in one session is how prod gets dev's state.
3. After migration, every operator and CI job re-runs `terraform init` to pick up the backend. Anyone still on local state will diverge silently.
4. Verify locking works: run two plans concurrently and confirm one waits. An unmigrated lock config is a corruption risk, not a cosmetic issue.

## Compatibility

- Terraform 1.x and OpenTofu. S3 backend with versioning; DynamoDB lock table (Terraform) or `use_lockfile = true` (OpenTofu).

## Variant phrasings

- terraform migrate state local to s3
- terraform init -migrate-state s3 backend
- move terraform tfstate to remote backend


---

Source: [Vectle](https://vectle.com/skills/skl_QSWJAPREwgGbRa2WSpTbkQ). Version: `skv_sw0Nb4TEY05qdDbtBIE2nA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
