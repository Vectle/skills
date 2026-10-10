---
name: "azcopy-exe-exited-with-non-zero-exit-c-f1b7e0ec72fa9770"
description: "Diagnoses Azure DevOps failures where AzCopy.exe exits non-zero during blob uploads, usually an AuthorizationPermissionMismatch on the storage account. Use when an agent sees this in AzureFileCopy tasks or standalone AzCopy runs. Covers granting Storage Blob Data Contributor, SAS token permissions, and reading the AzCopy log. Not for network failures."
metadata:
  skill_id: "skl_dXfLVP_S7gM0JRh5offPOg"
  title: "AzCopy.exe exited with non-zero exit code while uploading files to blob storage"
  version: "skv_62YR_x994pSDdG5ep9AjiQ"
  updated: "2026-10-03T04:50:52.331798+00:00"
  canonical_url: "https://vectle.com/skills/skl_dXfLVP_S7gM0JRh5offPOg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AzCopy.exe exited with non-zero exit code while uploading files to blob storage

## TL;DR
AzCopy authenticated fine but is not allowed to write to the container. The service connection's identity needs the Storage Blob Data Contributor role on the storage account. Grant the role, wait for propagation, rerun.

## The error
```
AzCopy.exe exited with non-zero exit code while uploading files to blob storage.
```
(often with `AuthorizationPermissionMismatch` in the AzCopy log.)

## Fix it
1. Open the AzCopy log from the failed task and search for the inner error. Expected: you find AuthorizationPermissionMismatch or a 403.
2. Grant the role: `az role assignment create --role "Storage Blob Data Contributor" --assignee [principal-id] --scope [storage-account-scope]`. Expected: the assignment is created.
3. Wait a few minutes for role propagation. Expected: no more 403 on retry.
4. If you use a SAS token instead of a managed identity, check the token has write and create permissions and is not expired. Expected: the SAS covers the operations AzCopy needs.
5. Rerun the copy. Expected: exit code 0.

## When to use this
- An agent sees AzCopy.exe non-zero exit codes in AzureFileCopy tasks or standalone AzCopy uploads.
- 403-style failures after successful authentication.

## When NOT to use this
- Network timeouts or DNS failures. Those fail before any permission check.
- "The term AzCopy is not recognized". That is a missing install, not permissions.

## Compatibility
- AzCopy v10, AzureFileCopy task v3 and later, Azure Blob Storage.

### Variant phrasings
- "AzCopy.exe exited with non-zero exit code"
- "AuthorizationPermissionMismatch"
- "This request is not authorized to perform this operation using this permission"

## Root cause
Azure RBAC separates control-plane from data-plane. Contributor on the storage account lets you manage it but not write blobs. AzCopy needs the data-plane role, and the classic miss is assuming Contributor is enough.

## Edge cases
- Storage firewall rules can 403 even with the right role. Check the networking blade if the role is correct.
- The AzureFileCopy task's service connection identity is what needs the role, not your user account.


---

Source: [Vectle](https://vectle.com/skills/skl_dXfLVP_S7gM0JRh5offPOg). Version: `skv_62YR_x994pSDdG5ep9AjiQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
