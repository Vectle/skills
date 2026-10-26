---
name: "azure-cli-2-51-0-august-01-2023-introd-ed11c48ac893d4eb"
description: "Fixes the cryptography UserWarning on Azure CLI 2.51.0 ('You are using cryptography on a 32-bit Python on a 64-bit Windows OS') by migrating to the 64-bit Azure CLI. Use when Azure Pipelines fails with PowerShell RemoteException from the arcappliance extension warning. Not for other Python warnings or 64-bit installs."
metadata:
  skill_id: "skl_exylijJmm5cp-Yho6hx9KA"
  title: "Azure CLI 2.51.0 (August 01, 2023) introduces Python UserWarning of cryptography for extensions"
  version: "skv_ObToVdieVNtiQhMZLzQgrg"
  updated: "2026-10-03T04:10:25.46353+00:00"
  canonical_url: "https://vectle.com/skills/skl_exylijJmm5cp-Yho6hx9KA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/Azure/azure-cli/issues/27115\"]"
---

## TL;DR

The warning means the 32-bit Azure CLI is running on 64-bit Windows. Fix: migrate to the 64-bit Azure CLI (see the install docs section 'Migrate to 64-bit Azure CLI'). GitHub-hosted runner images now ship 64-bit by default, so updating the runner image also resolves it.

## The error

```text
UserWarning: You are using cryptography on a 32-bit Python on a 64-bit Windows Operating System. Cryptography will be significantly faster if you switch to using a 64-bit Python.
```

In Azure Pipelines this surfaces as a PowerShell `RemoteException` that fails the pipeline, typically when using the `arcappliance` extension.

## Fix it

1. Confirm you are on the 32-bit CLI:
   ```powershell
   az version
   ```
   Success check: the installed CLI is 2.51.0 (or nearby) and the warning mentions 32-bit Python.

2. Migrate to the 64-bit Azure CLI per the install docs ('Migrate to 64-bit Azure CLI').
   Success check: reinstall completes; `az version` no longer triggers the warning.

3. If you run on GitHub-hosted agents, update to a current runner image, which ships 64-bit by default.
   Success check: the pipeline step passes with no RemoteException.

4. As a short-term workaround, pin Azure CLI to 2.50.0 where the warning does not appear.
   Success check: pipeline goes green, but treat this as temporary.

## When this applies

- Azure CLI 2.51.0 on 64-bit Windows emitting the cryptography 32-bit UserWarning.
- Azure Pipelines failing with PowerShell RemoteException tied to the warning (arcappliance extension).

## When it does not apply

- You are already on the 64-bit CLI and still see warnings; the cause is different.
- Non-Windows agents, or warnings from a different Python package.
- Cryptography is genuinely slow for workload reasons rather than the 32-bit build.

## Compatibility

- Azure CLI 2.51.0 (August 2023) 32-bit Windows build. Fixed by migrating to 64-bit.
- GitHub-hosted runners: current images ship 64-bit.

## Variant phrasings

- Azure CLI 2.51.0 cryptography UserWarning 32-bit Python
- arcappliance extension RemoteException Azure Pipelines
- "You are using cryptography on a 32-bit Python on a 64-bit Windows"

## Why it happens

Azure CLI 2.51.0 shipped a 32-bit Python runtime on 64-bit Windows. The `cryptography` package detects the mismatch and warns; in PowerShell remoting contexts the warning becomes a RemoteException that fails the pipeline. The 64-bit CLI build removes the mismatch entirely.

## Edge cases

- Self-hosted agents need the manual 64-bit migration; only GitHub-hosted images updated automatically.
- Extensions other than arcappliance can trigger the same warning; the fix is identical.
- Source: https://github.com/Azure/azure-cli/issues/27115


---

Source: [Vectle](https://vectle.com/skills/skl_exylijJmm5cp-Yho6hx9KA). Version: `skv_ObToVdieVNtiQhMZLzQgrg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
