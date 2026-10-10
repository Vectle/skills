---
name: "azure-key-vault-csi-multiple-user-assi-318051ab43df8706"
description: "Fixes the Azure Key Vault CSI driver failing with 'Multiple user assigned identities exist, please specify the clientId'. Use this when the node has more than one user-assigned managed identity. Not for other CSI errors."
metadata:
  skill_id: "skl_CzhbKb7S3bbGeAf7dHxAXw"
  title: "Azure Key Vault CSI Multiple user assigned identities exist please specify the clientId"
  version: "skv_Baq6FY4K2RzL510-9RF-UA"
  updated: "2026-10-03T05:34:30.379273+00:00"
  canonical_url: "https://vectle.com/skills/skl_CzhbKb7S3bbGeAf7dHxAXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if mounting Azure Key Vault secrets with the CSI driver fails with `Multiple user assigned identities exist, please specify the clientId / resourceId` when the node/VM has more than one user-assigned managed identity, the SecretProviderClass does not say which identity to use. Set `userAssignedIdentityID` to the client ID of the identity that has Key Vault access in your SecretProviderClass. The reporter confirmed this single change resolved the mount failure. The identity modes and this field are documented under the provider's user-assigned MSI mode configuration.

```text
Multiple user assigned identities exist, please specify the clientId
```

## Steps

1. Set `userAssignedIdentityID` in the SecretProviderClass to the client ID of the identity with Key Vault access.

2. Re-apply and re-mount.

   Expected: the mount succeeds. Success check: secrets appear at the mount path.

## When to use this

- Multiple user-assigned identities on the node, mount fails with this error.

## When NOT to use this

- Single identity; the driver picks it up.
- Other CSI errors; read the message.

## Compatibility

- Azure Key Vault provider with user-assigned MSI mode.

## Variant phrasings

- "key vault csi multiple user assigned identities"
- "key vault csi specify clientId"

## Root cause

Ambiguous identity selection when several managed identities exist.

## Edge cases

- The identity must actually have Key Vault access; the field only selects it.

---

Source: [Vectle](https://vectle.com/skills/skl_CzhbKb7S3bbGeAf7dHxAXw). Version: `skv_Baq6FY4K2RzL510-9RF-UA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
