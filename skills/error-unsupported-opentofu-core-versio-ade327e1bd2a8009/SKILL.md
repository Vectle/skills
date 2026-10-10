---
name: "error-unsupported-opentofu-core-versio-ade327e1bd2a8009"
description: "Resolves OpenTofu's 'Error: Unsupported OpenTofu Core version' at tofu init by aligning the required_version constraint with the installed tofu binary. Use when init refuses right after a Terraform-to-OpenTofu migration or when CI installs a tofu version the config doesn't allow. Not for provider version or lock-file errors."
metadata:
  skill_id: "skl_q6Btsv1pd0nTI96GnGxmzA"
  title: "Error: Unsupported OpenTofu Core version"
  version: "skv_jlS4dY1wk8RsSEXDpB-CnQ"
  updated: "2026-10-03T05:29:20.272106+00:00"
  canonical_url: "https://vectle.com/skills/skl_q6Btsv1pd0nTI96GnGxmzA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Your `required_version` constraint excludes the tofu binary you have installed. Either install a tofu version the constraint allows, or widen the constraint. This bites hardest when migrating from Terraform, because constraints like `>= 1.14` follow Terraform's release line, which OpenTofu doesn't share.

```text
Error: Unsupported OpenTofu Core version

  on versions.tf line 2, in terraform:
   2:   required_version = ">= 1.14"

This configuration does not support OpenTofu version 1.11.5.
```

## Steps

1. Run `tofu version` and note the installed version.
   Expected: `OpenTofu v1.11.5` (or whatever you have).
2. Decide: upgrade tofu, or relax the constraint. If the constraint references Terraform's line (for example `>= 1.14` after a migration), edit `versions.tf` so it covers your tofu, e.g. `required_version = ">= 1.11"`.
   Expected: the constraint now includes your installed version.
3. If you'd rather keep the constraint, install a matching tofu with a version manager: `tofuenv install 1.12.6 && tofuenv use 1.12.6` (or the tenv equivalent).
   Expected: `tofu version` shows the new version.
4. Run `tofu init`.
   Expected: init proceeds past the version check.

## When this applies

- `tofu init` fails immediately, naming a `required_version` line, right after migrating a repo from Terraform.
- CI installs a pinned tofu version that the repo's constraint doesn't allow.

## When it doesn't apply

- `Error: Failed to install provider` is about provider versions, not the tofu binary.
- `Error: Inconsistent dependency lock file` is about provider pins, not the core version.

## Tool versions

All OpenTofu versions. The check runs on every init, plan, and apply.

## Why it happens

Version numbers diverged after the fork: Terraform and OpenTofu ship on separate cadences. A `required_version` written against Terraform's line (say `>= 1.14`) is meaningless on tofu's line (1.11.x, 1.12.x), so tofu refuses at init instead of running under a constraint it can't satisfy.

## Edge cases

- During a transition where a repo must work with both tools, pick a floor both lines satisfy, like `>= 1.6` (where OpenTofu forked), and tighten it once the migration is done.
- The error names the exact file and line, so you don't have to hunt; it's always the root module's `terraform` block.
- CI matrices should install the tofu version the repo declares. Pin it in one place (a `.opentofu-version` file read by tenv/tofuenv) so the number can't drift between local and CI.

---

Source: [Vectle](https://vectle.com/skills/skl_q6Btsv1pd0nTI96GnGxmzA). Version: `skv_jlS4dY1wk8RsSEXDpB-CnQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
