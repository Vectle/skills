---
name: "azurefilecopy-failed-to-perform-auto-l-91875bf99750e528"
description: "Diagnoses the AzureFileCopy v6 pipeline failure 'Failed to perform Auto-login: json: cannot unmarshal object into Go struct field .Token of type string'. Use when an agent sees this in Azure DevOps releases using the PowerShell context. Covers the service connection token format problem and switching the task's login approach. Not for AzCopy permission errors."
metadata:
  skill_id: "skl_XvpsTKwVRSpr4dmb1baFVg"
  title: "AzureFileCopy: Failed to perform Auto-login (cannot unmarshal Go struct field .Token)"
  version: "skv_VXn3KfKv1CvVS95yA3XfTA"
  updated: "2026-10-03T04:52:22.071493+00:00"
  canonical_url: "https://vectle.com/skills/skl_XvpsTKwVRSpr4dmb1baFVg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/microsoft/azure-pipelines-tasks/issues/21053\"]"
---

# AzureFileCopy: Failed to perform Auto-login (cannot unmarshal Go struct field .Token)

## TL;DR
The AzureFileCopy task's auto-login hands AzCopy a token payload in a shape AzCopy does not expect, and AzCopy crashes parsing it. The fix is on the task configuration side: change how the task authenticates rather than debugging AzCopy itself.

## The error
```
Failed to perform Auto-login: json: cannot unmarshal object into Go struct field .Token of type string
```

## Fix it
1. Open the failing AzureFileCopy task in your pipeline and check the service connection it uses. Expected: you know which connection and auth scheme is in play.
2. Recreate or re-authorize the Azure Resource Manager service connection. Stale connection metadata is the usual trigger. Expected: the connection validates cleanly.
3. If the task offers a login-type or context option, switch away from the PowerShell auto-login context that produces the malformed token payload. Expected: the task logs in through the working path.
4. As a workaround, replace the task's copy step with an AzureCLI task that runs `azcopy` directly after `az login`. Expected: the copy succeeds outside the broken auto-login path.
5. Rerun the pipeline. Expected: no more unmarshal error.

## When to use this
- An agent sees the "cannot unmarshal object into Go struct field .Token" error from AzureFileCopy v6.
- Azure DevOps pipelines using the PowerShell login context.

## When NOT to use this
- AzCopy permission errors (AuthorizationPermissionMismatch). Those fail later, at the storage call.
- Generic AzCopy non-zero exits without the unmarshal message.

## Compatibility
- AzureFileCopy task v6, Azure DevOps Services, AzCopy v10.

### Variant phrasings
- "Failed to perform Auto-login"
- "cannot unmarshal object into Go struct field"

## Root cause
The task builds a token object for AzCopy's auto-login, but the shape does not match the Go struct AzCopy expects: an object arrives where a string was declared. It is a task-side serialization bug triggered by certain service connection configurations, which is why recreating the connection or changing the login path resolves it.

## Edge cases
- The error is intermittent across agents when the service connection was created long ago. Recreating it is still the fix.
- Service principal secret expiry in the connection produces different errors. This one is specifically the JSON shape mismatch.


---

Source: [Vectle](https://vectle.com/skills/skl_XvpsTKwVRSpr4dmb1baFVg). Version: `skv_VXn3KfKv1CvVS95yA3XfTA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
