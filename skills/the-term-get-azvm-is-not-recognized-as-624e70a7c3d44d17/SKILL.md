---
name: "the-term-get-azvm-is-not-recognized-as-624e70a7c3d44d17"
description: "Diagnoses the PowerShell error where Az module cmdlets like Get-AzVM are not found. Use when an agent sees this in Windows PowerShell or PowerShell 7. Covers installing the Az module, module autoload issues, and AzureRM vs Az confusion. Not for az CLI errors."
metadata:
  skill_id: "skl_ifqYO1YyYijkVj7WnbbPFw"
  title: "The term 'Get-AzVM' is not recognized as the name of a cmdlet"
  version: "skv_z-3f3dIqcs5ud45PNoHNrw"
  updated: "2026-10-03T04:53:11.264607+00:00"
  canonical_url: "https://vectle.com/skills/skl_ifqYO1YyYijkVj7WnbbPFw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/syncluv/azure-mastery-labs/blob/main/troubleshooting.md\"]"
---

# The term 'Get-AzVM' is not recognized as the name of a cmdlet

## TL;DR
The Az PowerShell module is not installed (or not loaded) in your session. Install it from the PowerShell Gallery, import it, and the cmdlets appear. Do not confuse this with the `az` CLI; they are different tools.

## The error
```
The term 'Get-AzVM' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

## Fix it
1. Install the module: `Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force`. Expected: the install completes without errors.
2. Import it: `Import-Module Az`. Expected: no output, meaning success.
3. Verify: `Get-Command Get-AzVM`. Expected: it resolves to the Az.Compute cmdlet.
4. Connect: `Connect-AzAccount`. Expected: interactive login succeeds.
5. Retry your command. Expected: `Get-AzVM` returns your VMs.

## When to use this
- An agent sees "not recognized as the name of a cmdlet" for any Get-Az*, New-Az*, or Set-Az* command.
- Fresh machines or CI agents running Azure PowerShell for the first time.

## When NOT to use this
- "'az' is not recognized". That is the Azure CLI, a separate install.
- AzureRM cmdlets (Get-AzureRmVM). Those are the retired module; migrate to Az.

## Compatibility
- PowerShell 5.1 and 7+, Az module (current). AzureRM is retired and should not be installed.

### Variant phrasings
- "The term 'Connect-AzAccount' is not recognized"
- Any "not recognized as the name of a cmdlet" for Az.* commands

## Root cause
Windows ships no Azure modules. The Az module comes from the PowerShell Gallery, and without it PowerShell has no idea what Get-AzVM is. CI agents and fresh VMs hit this on every first run until the module install becomes part of setup.

## Edge cases
- Both AzureRM and Az installed side by side cause conflicts. Uninstall AzureRM.
- Execution policy can block the install. `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` first if needed.


---

Source: [Vectle](https://vectle.com/skills/skl_ifqYO1YyYijkVj7WnbbPFw). Version: `skv_z-3f3dIqcs5ud45PNoHNrw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
