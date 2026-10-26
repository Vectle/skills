---
name: "error-failed-to-install-provider-967e68fa72d2f5be"
description: "Fixes terraform's \"Error: Failed to install provider\" during terraform init. Use when provider installation fails with a sub-error naming the real cause: disk full, lock-file checksum mismatch, network or proxy failure, or missing platform package. Not for \"Failed to query available provider packages\" (version/registry access) or provider authentication errors at plan time."
metadata:
  skill_id: "skl_E17qpcxTWLhmsSbiggjb6A"
  title: "Error: Failed to install provider"
  version: "skv_4nX9X_CjrLIuIrqu3PW0CA"
  updated: "2026-10-03T06:05:54.289271+00:00"
  canonical_url: "https://vectle.com/skills/skl_E17qpcxTWLhmsSbiggjb6A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://discuss.hashicorp.com/t/error-when-installing-terraform-cloudstack-provider-plugin/59691\"]"
---

# Fix terraform "Error: Failed to install provider"

**TL;DR:** `terraform init` could not download or verify a provider plugin. Read the line *under* the error; it names the real cause (network timeout, checksum mismatch, no space left, missing platform package). Fix that cause, then re-run `terraform init`. Most cases are transient network failures or a stale `.terraform.lock.hcl`.

## The error

```text
Error: Failed to install provider

Error while installing hashicorp/aws v6.47.0: write
.terraform/providers/registry.terraform.io/hashicorp/aws/6.47.0/linux_amd64/terraform-provider-aws_v6.47.0_x5: no space left on
device
```

(Your sub-line will differ. Common ones: checksum mismatch against the lock file, TLS handshake timeout, registry unreachable.)

## Steps

1. Read the sub-error. It is the actual diagnosis. Categorize it:
   - `no space left on device`: free disk space.
   - `doesn't match any of the checksums previously recorded in the dependency lock file`: lock file conflict.
   - `TLS handshake timeout` / `connection refused` / `Could not retrieve the list of available versions`: network or proxy.
   - `does not have a package available for your current platform`: wrong arch (e.g. 32-bit).
2. For lock-file checksum conflicts, regenerate the lock file:

   ```bash
   rm .terraform.lock.hcl
   terraform init
   ```

   Expected: providers install, and a fresh lock file is written. Commit it.
3. For network failures, check reachability and retry. Behind a corporate proxy, export the proxy vars first:

   ```bash
   curl -s https://registry.terraform.io/.well-known/terraform.json
   export HTTPS_PROXY=YOUR_PROXY_HOST
   export HTTP_PROXY=YOUR_PROXY_HOST
   terraform init
   ```

   Expected: the registry answers and the install proceeds.
4. For repeated flakiness (GitHub CDN TLS timeouts on community providers), retry once or twice; these are usually transient. Expected: a later `init` succeeds with no config change.

## When this applies

- `terraform init` fails at the "Installing ..." step with any sub-error.
- You changed provider versions, platforms, or the lock file.

## When it does NOT apply

- Init fails earlier at "Finding ... versions" with `Failed to query available provider packages`. That is version-constraint or registry-access, a different fix.
- The provider installs but `plan` fails with auth errors. That is provider configuration, not installation.

## Tool and version compatibility

- Terraform CLI 0.13+ (provider source model) through 1.x.
- registry.terraform.io and community providers hosted on GitHub releases.

## Why it happens

Init downloads each provider binary for your platform and verifies it against `.terraform.lock.hcl` checksums. Anything that breaks that chain (no disk, no network, a lock file written on another platform, a registry namespace that moved like zscaler.com/zpa to zscaler/zpa) fails the whole install.

## Edge cases and pitfalls

- Deleting the lock file and re-running init on a different platform than your team (M1 Mac vs Linux CI) writes platform-specific hashes. Regenerate for all target platforms with `terraform providers lock -platform=linux_amd64 -platform=darwin_arm64` and commit the result.
- Fully offline environments: download the provider zip, unpack it into the local plugin dir layout, and init works without the network.
- Do not hand-edit checksums in the lock file. Regenerate it.

---

Source: [Vectle](https://vectle.com/skills/skl_E17qpcxTWLhmsSbiggjb6A). Version: `skv_4nX9X_CjrLIuIrqu3PW0CA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
