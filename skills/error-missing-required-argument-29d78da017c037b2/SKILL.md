---
name: "error-missing-required-argument-29d78da017c037b2"
description: "Fixes OpenTofu's 'Error: Missing required argument' inside encryption key_provider blocks, usually a missing passphrase on pbkdf2. Use when tofu 1.7+ rejects your state-encryption config naming a required argument. Not for 'Unsupported block type encryption' on older tofu."
metadata:
  skill_id: "skl_cSdNsMJeRb0ci0_wT-DWzg"
  title: "Error: Missing required argument"
  version: "skv_Ojet3cdSkBt54Q5HiWMZuw"
  updated: "2026-10-03T06:04:52.109166+00:00"
  canonical_url: "https://vectle.com/skills/skl_cSdNsMJeRb0ci0_wT-DWzg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Your `encryption` block's `key_provider` is missing a required argument. The error names it (for `pbkdf2` it's `passphrase`). Add the argument to the `key_provider` block. If you configure encryption via the `TF_ENCRYPTION` environment variable, it must contain the full nested block, not just the inner `key_provider`.

```text
Error: Missing required argument

  on main.tf line 3, in terraform:
   3:     key_provider "pbkdf2" "main" {

The argument "passphrase" is required, but no definition was
found.
```

## Steps

1. Open the `terraform` block and find the `encryption` -> `key_provider` block the error points at.
   Expected: you see the block missing the named argument.
2. Add the required argument. For `pbkdf2`, that's a passphrase of at least 16 characters:
   ```hcl
   terraform {
     encryption {
       key_provider "pbkdf2" "main" {
         passphrase = "[your passphrase, 16+ chars]"
       }
       method "aes_gcm" "main" {
         keys = key_provider.pbkdf2.main
       }
       state {
         method = method.aes_gcm.main
       }
     }
   }
   ```
   Expected: the block now defines every required argument.
3. If you use `TF_ENCRYPTION`, export the FULL nested block (terraform -> encryption -> key_provider), not just the inner `key_provider` alone. A bare `key_provider` at the top of the env var value fails with `Unsupported block type` or drops required arguments.
   Expected: `tofu plan` no longer complains about the encryption config.
4. Run `tofu plan` to verify.
   Expected: plan proceeds; no encryption errors.

## When this applies

- OpenTofu 1.7 or later with a `terraform { encryption { ... } }` block.
- The error names a specific argument (`passphrase`, `key_id`, etc.) inside a `key_provider` or `method` block.

## When it doesn't apply

- `Error: Unsupported block type "encryption"` means your tofu is older than 1.7; upgrade instead.
- `Error: Failed to retrieve key from key provider` means the config parsed but the key itself couldn't be loaded; that's a credentials problem, not a missing argument.

## Tool versions

OpenTofu 1.7+, which introduced state encryption. Each `key_provider` type (`pbkdf2`, `aws_kms`, `gcp_kms`, `openbao`, `azure_key_vault`) has its own required arguments; check the docs for the one you use.

## Why it happens

Encryption key providers need real secrets to derive data keys, so their arguments are required, not optional. A missing argument fails closed at config load: tofu would rather refuse than silently run with unencrypted state.

## Edge cases

- Don't commit a real passphrase in the config file. Use `TF_ENCRYPTION` or a separate vars file excluded from version control.
- `pbkdf2` needs 16+ characters; shorter values fail validation with a different error.
- Changing encryption settings on a backend that already holds state requires migrating the state; read the encryption docs' migration section before flipping it on an existing workspace.

---

Source: [Vectle](https://vectle.com/skills/skl_cSdNsMJeRb0ci0_wT-DWzg). Version: `skv_Ojet3cdSkBt54Q5HiWMZuw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
