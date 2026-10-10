---
name: "error-backend-initialization-required-eefb1826bdbb22cd"
description: "Fixes terraform's \"Backend initialization required, please run terraform init\" error. Use when plan, apply, or validate fails in an uninitialized directory or after the backend block changed. Covers plain init vs init -reconfigure and the init -backend=false CI case. Not for credential errors, missing backend buckets, or provider install failures."
metadata:
  skill_id: "skl_eqbLFQvZrfs8IXNvVpsJcg"
  title: "Error: Backend initialization required, please run \"terraform init\""
  version: "skv_kt33_rsuZfogmn_RADzu9Q"
  updated: "2026-10-03T06:10:51.330944+00:00"
  canonical_url: "https://vectle.com/skills/skl_eqbLFQvZrfs8IXNvVpsJcg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix terraform "Backend initialization required, please run terraform init"

**TL;DR:** You are running plan or apply in a directory that was never initialized, or the backend config changed since the last init. Run `terraform init`. If you changed the backend block or its settings, run `terraform init -reconfigure` instead so it points at the right state without trying to migrate data.

## The error

```text
Error: Backend initialization required, please run "terraform init"
```

## Steps

1. Confirm you are in the right directory and init has actually run: `ls -la .terraform` should exist. If the directory is missing, that is the whole story.
2. Run init:

   ```bash
   terraform init
   ```

   Expected output: `Terraform has been successfully initialized!`
3. If you recently edited the `backend` block (new bucket, new key, moved from local to remote), run:

   ```bash
   terraform init -reconfigure
   ```

   Expected: `Successfully configured the backend "s3"!` (or your backend) with no migration prompt. `-reconfigure` tells terraform to forget the old backend rather than copy state out of it.
4. Re-run `terraform plan`. Expected: the backend error is gone.

## When this applies

- `plan`, `apply`, or `validate` fails with this error in a fresh checkout or after editing the backend block.
- You switched environments (dev to prod) and the backend key changed.

## When it does NOT apply

- The error names a missing bucket or credentials instead (`Failed to get existing workspaces`, 403s). That is a backend config problem, not a missing init.
- You ran `init -backend=false` on purpose for a lint-only CI job. The error is expected there; run validate-only workflows instead.

## Tool and version compatibility

- Terraform CLI 0.12+ through 1.x. Backend block behavior identical across versions.
- All backends: local, S3, GCS, AzureRM, Terraform Cloud.

## Why it happens

Backend selection happens during init. Terraform stores which backend it configured in `.terraform/`. If that directory is missing (fresh clone, new machine) or the `backend` block no longer matches what init recorded, every command that touches state refuses to guess and asks you to init again.

## Edge cases and pitfalls

- Plain `terraform init` after a backend change prompts to migrate state. In CI you usually do not want the interactive prompt; choose `-reconfigure` (discard old backend pointer) or `-migrate-state` (copy state to the new backend) deliberately.
- Switching state keys between environments (dev vs prod) triggers this normally. That is by design, not a bug.
- Azure backend users: a missing `use_azuread_auth=true` at init time surfaces as this error later. Pass it via `-backend-config` during init.

---

Source: [Vectle](https://vectle.com/skills/skl_eqbLFQvZrfs8IXNvVpsJcg). Version: `skv_kt33_rsuZfogmn_RADzu9Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
