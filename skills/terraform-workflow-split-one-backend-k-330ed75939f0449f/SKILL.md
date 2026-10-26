---
name: "terraform-workflow-split-one-backend-k-330ed75939f0449f"
description: "One state file per backend key served until the blast radius got scary. The workflow moves resource groups to new keys with state mv and per-key backend configs. Not the full reference manual."
metadata:
  skill_id: "skl_MSJvlwTogtZZ7G_rbY5lbQ"
  title: "Terraform workflow: split one backend key into many without downtime"
  version: "skv_1spKD-JiZu-nxqocyWxYvg"
  updated: "2026-10-03T14:08:32.009286+00:00"
  canonical_url: "https://vectle.com/skills/skl_MSJvlwTogtZZ7G_rbY5lbQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://developer.hashicorp.com/terraform/docs/cli/commands/state/mv\",\"https://opentofu.org/docs/language/state/remote-state-data/\"]"
---

**TL;DR:** One state file per backend key served until the blast radius got scary. The workflow moves resource groups to new keys with state mv and per-key backend configs. Create the new root configs, one per key, each with its own backend block pointing at its key. Move the corresponding resource blocks into each config.

## When

A single `terraform.tfstate` key holds unrelated resource groups and every plan refreshes all of them. Split by service or lifecycle: things that change together stay together.

## Steps

1. Decide the key layout: one key per service group, e.g. `network/terraform.tfstate`, `data/terraform.tfstate`, `app/terraform.tfstate`. Fewer, stable keys beat many clever ones.
2. Create the new root configs, one per key, each with its own backend block pointing at its key. Move the corresponding resource blocks into each config.
3. Back up the original state: `terraform state pull > backup-monolith-[date].json`.
4. For each new config: `terraform init`, then move entries from the old state file to the new one with explicit state paths:
   `terraform state mv -state=[old-state-file] -state-out=[new-state-file] [address] [address]`
   (Pull the old state to a local file first so the moves are explicit and reviewable.)
5. Push each new state file to its backend key, then per config: `terraform plan` must be clean (moves only).
6. Replace cross-key references with `terraform_remote_state` data sources or parameter lookups.

## Rules for agents

1. Moves are by address, and addresses must match the new config exactly. `terraform state list` on the old state is your source of truth for what exists.
2. One key per change. Splitting three keys in one session triples the chance of moving an address to the wrong key.
3. After the split, the old key should be empty. Verify with a plan against the old config (should propose nothing or be retired), then decommission the old config directory.
4. Apply order between keys is now manual: document network -> data -> app and enforce it in CI. The monolith ordered things for free; the split does not.

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

Source: [Vectle](https://vectle.com/skills/skl_MSJvlwTogtZZ7G_rbY5lbQ). Version: `skv_1spKD-JiZu-nxqocyWxYvg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
