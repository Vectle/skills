---
name: "deploymentscripterror-the-provided-scr-5873ae696c1a438d"
description: "Diagnoses the ARM DeploymentScriptError where a deployment script resource fails with multiple script errors. Use when an agent sees this during Bicep or ARM deployments that run inline scripts. Covers pulling the script logs with az deployment-scripts show-log and fixing the script itself. Not for generic DeploymentFailed wrappers."
metadata:
  skill_id: "skl_BQKgL0YG5N2WYggjEYZOrA"
  title: "DeploymentScriptError: The provided script failed with multiple errors"
  version: "skv_IkHtXbdKxYhHvS1BD88Ldg"
  updated: "2026-10-03T04:47:51.403119+00:00"
  canonical_url: "https://vectle.com/skills/skl_BQKgL0YG5N2WYggjEYZOrA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/Azure/azure-landing-zones/issues/3261\"]"
---

# DeploymentScriptError: The provided script failed with multiple errors

## TL;DR
The deployment script resource ran your script and the script itself failed. The fix is in the script, not the template. Pull the script logs, find what the script did wrong, fix it, and redeploy.

## The error
```
DeploymentScriptError: The provided script failed with multiple errors. Please check the deployment script logs.
```

## Fix it
1. Pull the script logs: `az deployment-scripts show-log --name [script-name] --resource-group [rg]`. Expected: the actual script output and errors appear.
2. Read the log from the top. The first error is usually the cause; later errors are fallout. Expected: you find the failing command.
3. Fix the script: missing tools in the script environment, wrong paths, auth failures inside the script. Expected: the script runs clean locally or in a matching container.
4. Check the script's timeout and cleanup settings. Long scripts can get killed and report as multiple errors. Expected: the timeout covers the script's real runtime.
5. Redeploy. Expected: the deployment script resource succeeds.

## When to use this
- An agent sees DeploymentScriptError during a Bicep or ARM deployment.
- Landing-zone or bootstrap templates that run Azure CLI or PowerShell inline.

## When NOT to use this
- Plain DeploymentFailed with no script involved. List the operations instead.
- Script failures outside ARM (pipeline tasks, local runs). Different tooling.

## Compatibility
- Azure deployment scripts (Microsoft.Resources/deploymentScripts), Bicep, ARM templates.

### Variant phrasings
- "DeploymentScriptError"
- "The provided script failed"

## Root cause
Deployment scripts run in a container with a time limit. The error aggregates whatever the script printed to stderr, so "multiple errors" usually means one root failure plus cascading follow-ons. The azure-landing-zones issue hit this on a bootstrap script and resolved it by reading the script logs and fixing the script content.

## Edge cases
- Scripts that need Azure access must use the managed identity the deployment script resource provides. A script that works locally with your login fails in the deployment without it.
- Log retention is limited. Pull logs soon after the failure.


---

Source: [Vectle](https://vectle.com/skills/skl_BQKgL0YG5N2WYggjEYZOrA). Version: `skv_IkHtXbdKxYhHvS1BD88Ldg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
