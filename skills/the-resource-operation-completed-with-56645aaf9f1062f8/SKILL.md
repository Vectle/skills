---
name: "the-resource-operation-completed-with-56645aaf9f1062f8"
description: "Diagnoses the Azure error 'The resource operation completed with terminal provisioning state Failed', which surfaces when a VM or resource deployment dies mid-provisioning. Use when an agent sees this during VM creation or ARM deployments. Covers reading the deployment operations for the real error, correlation IDs, and quota or image problems. Not for template validation errors."
metadata:
  skill_id: "skl_Ie7SR_2smKDWnCZNTIiAWw"
  title: "The resource operation completed with terminal provisioning state 'Failed'"
  version: "skv_bEAJFBxAZpRyUHb_qbdxnQ"
  updated: "2026-10-03T04:46:32.239968+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ie7SR_2smKDWnCZNTIiAWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/0a7v9a/supportarticles-docs/blob/HEAD/support/azure/virtual-machines/troubleshoot-deployment-new-vm-linux.md\"]"
---

# The resource operation completed with terminal provisioning state 'Failed'

## TL;DR
Something failed during resource provisioning, and this message is the wrapper, not the cause. Pull the deployment operations to find the inner error, then fix that. The correlation ID ties the whole trail together.

## The error
```
The resource operation completed with terminal provisioning state 'Failed'.
```

## Fix it
1. List the deployment operations to find the real error: `az deployment operation group list --resource-group [rg] --name [deployment-name]`. Expected: one operation shows a failed status with an inner error code.
2. Read the inner error. Common ones: quota exceeded, invalid image reference, or a policy violation. Expected: you have a specific code to work with, like SkuNotAvailable or AllocationFailed.
3. Copy the correlation ID from the failed operation. Support and log searches key off it. Expected: you can trace the failure across activity logs.
4. Fix the inner cause (raise quota, pick an available SKU, fix the image reference) and redeploy. Expected: provisioning completes.
5. If the inner error is AllocationFailed, try another region or VM size. Expected: the new size allocates successfully.

## When to use this
- An agent sees the terminal-provisioning-state message during VM creation or ARM deployment.
- A deployment fails with no useful detail at the top level.

## When NOT to use this
- Template validation errors (InvalidTemplate). Those fail before provisioning starts.
- DeploymentScriptError. That names the script; this message does not.

## Compatibility
- Azure Resource Manager, all resource types. The operations-list pattern is the same everywhere.

### Variant phrasings
- "provisioning state 'Failed'"
- "terminal provisioning state"

## Root cause
Azure reports provisioning asynchronously. The top-level message only says the operation reached a terminal failed state; the actual failure (bad SKU, quota, image, policy) is nested one level down in the deployment operations. People stare at the wrapper because the portal surfaces it first.

## Edge cases
- Transient platform failures produce this too. If the inner error is vague, one redeploy is a legitimate test before deep debugging.
- Policy denials look identical at the top level. Check the inner error for policy language before blaming quota.


---

Source: [Vectle](https://vectle.com/skills/skl_Ie7SR_2smKDWnCZNTIiAWw). Version: `skv_bEAJFBxAZpRyUHb_qbdxnQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
