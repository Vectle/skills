---
name: "error-inconsistent-dependency-lock-fil-5d559c4231c39d75"
description: "Fixes OpenTofu's 'Error: Inconsistent dependency lock file' by re-resolving provider versions with tofu init -upgrade. Use when tofu init, plan, or apply refuses because .terraform.lock.hcl doesn't match the providers in your configuration. Not for registry network failures or unknown provider sources."
metadata:
  skill_id: "skl_R4UbmyScrRWSvQZt_y77Zg"
  title: "Error: Inconsistent dependency lock file"
  version: "skv_WQ00OOS4-WXeV9tndMzpog"
  updated: "2026-10-03T06:21:59.553147+00:00"
  canonical_url: "https://vectle.com/skills/skl_R4UbmyScrRWSvQZt_y77Zg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Run `tofu init -upgrade`. It re-resolves your providers against the current configuration and rewrites `.terraform.lock.hcl` so the recorded selections match. You hit this when a provider was added to the config, or its version constraint changed, after the lock file was written.

```text
Error: Inconsistent dependency lock file

The following dependency selections recorded in the lock file are
inconsistent with the current configuration:
  - provider registry.opentofu.org/hashicorp/random: required by this
    configuration but no version is selected

To update the locked dependency selections to match a changed
configuration, run:
  tofu init -upgrade
```

## Steps

1. Run `tofu init -upgrade` in the root module directory.
   Expected: tofu downloads the missing providers and prints `- Installing hashicorp/random v[version]...`, ending with `OpenTofu has been successfully initialized!`
2. Confirm `.terraform.lock.hcl` now lists the provider with a selected version and hashes.
   Expected: a `provider "registry.opentofu.org/hashicorp/random"` block with `version` and `hashes` entries.
3. Commit the updated lock file so CI and teammates get the same pins.
   Expected: `git diff --stat` shows `.terraform.lock.hcl` modified.
4. Re-run your original command (`tofu plan` / `tofu apply`).
   Expected: no lock error; the plan proceeds.

## When this applies

- Right after adding a provider, or a resource from a new provider, to your config.
- After changing a `version` constraint in `required_providers`.
- CI fails on `tofu init` or `tofu plan` while it works on your machine (stale committed lock file).

## When it doesn't apply

- `Error: Failed to query available provider packages` means tofu can't reach the registry or the provider doesn't exist. That's a network or naming problem, not a lock mismatch.
- `Error: Failed to install provider` with checksum complaints means the lock file hashes don't match the downloads. Different fix.

## Tool versions

OpenTofu 1.6 and later. The lock file mechanism is inherited from Terraform 0.14 and up; tofu writes the same `.terraform.lock.hcl` format.

## Why it happens

The lock file records the exact provider versions chosen at the last successful init. When the configuration changes (new provider, new constraint), the recorded selections no longer describe the config, and tofu refuses to guess. `-upgrade` tells it to pick fresh versions inside your constraints instead of reusing the recorded ones.

## Edge cases

- Don't just delete the lock file and re-init. That works locally but throws away the pins your team relies on for reproducible builds. Prefer `-upgrade`.
- Multi-platform teams: after `-upgrade` on one OS, run `tofu providers lock -platform=linux_amd64 -platform=darwin_amd64 -platform=darwin_arm64` so runners on other platforms don't hit hash mismatches.
- If the lock file is gitignored, every fresh clone can hit this. Either commit it, or make `tofu init -upgrade` part of your setup script.

---

Source: [Vectle](https://vectle.com/skills/skl_R4UbmyScrRWSvQZt_y77Zg). Version: `skv_WQ00OOS4-WXeV9tndMzpog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
