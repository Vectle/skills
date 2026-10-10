---
name: "error-failed-to-query-available-provid-474a3f5a75363ae4"
description: "Fixes OpenTofu's 'Error: Failed to query available provider packages' during tofu init, most often caused by a misspelled resource type prefix that makes tofu request a nonexistent provider. Use when init names a provider you never declared. Not for lock-file mismatches or download failures."
metadata:
  skill_id: "skl_TDzj51vWYP5Hd8zqbbuP5g"
  title: "Error: Failed to query available provider packages"
  version: "skv_2ee9KANQZ9-dA8TkMtGtvA"
  updated: "2026-10-03T05:30:21.800764+00:00"
  canonical_url: "https://vectle.com/skills/skl_TDzj51vWYP5Hd8zqbbuP5g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: tofu init is naming a provider that doesn't exist in the registry. Nine times out of ten this is a typo'd resource prefix: `azure_` instead of `azurerm_` makes tofu go looking for a `hashicorp/azure` provider that was never published. Fix the prefix (or the `source` in `required_providers`), then re-init.

```text
Error: Failed to query available provider packages

Could not retrieve the list of available versions for provider
hashicorp/azure: provider registry.opentofu.org/hashicorp/azure was not
found
```

## Steps

1. Read the provider name in the error. Ask: did you declare that provider? If not, find what implied it: `grep -rn 'resource "azure_' .` (swap in the prefix from your error).
   Expected: one or more resources with the wrong type prefix.
2. Fix the prefix, e.g. `resource "azure_resource_group"` becomes `resource "azurerm_resource_group"`.
   Expected: the grep from step 1 finds nothing anymore.
3. If the provider IS declared, check `required_providers` for a typo'd `source` address.
   Expected: the source matches a real registry address, like `hashicorp/azurerm`.
4. Run `tofu init`.
   Expected: `Initializing provider plugins...` followed by `- Installing hashicorp/azurerm v[...]...`.

## When this applies

- `tofu init` fails naming a provider you never asked for, or a provider with a slightly-off name.
- Right after renaming resources or copying config between projects.

## When it doesn't apply

- `Error: Inconsistent dependency lock file` is a lock mismatch; fix with `tofu init -upgrade`.
- `Error: Failed to install provider` means the provider exists but the download failed; that's network or disk.

## Tool versions

All OpenTofu versions. Provider inference from resource type prefixes works the same across the 1.x line.

## Why it happens

tofu infers required providers from resource type prefixes: anything starting `azurerm_` implies the `hashicorp/azurerm` provider. A wrong prefix implies a wrong provider, and tofu only discovers the mistake when it asks the registry for a provider that was never published.

## Edge cases

- If EVERY provider fails the same way at once, suspect network or proxy, not naming. A single bogus provider name points at a typo; all of them failing points at connectivity.
- Private registries and network mirrors: check the CLI config file's host credentials and mirror blocks before blaming the config.
- Modules can imply providers too. If the root config looks clean, grep inside `.terraform/modules` or your module sources for the bad prefix.

---

Source: [Vectle](https://vectle.com/skills/skl_TDzj51vWYP5Hd8zqbbuP5g). Version: `skv_2ee9KANQZ9-dA8TkMtGtvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
