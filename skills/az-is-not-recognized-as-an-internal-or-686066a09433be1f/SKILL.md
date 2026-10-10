---
name: "az-is-not-recognized-as-an-internal-or-686066a09433be1f"
description: "Diagnoses the Windows error where the Azure CLI is not on PATH after install. Use when an agent sees 'az is not recognized' in cmd or PowerShell. Covers reinstalling with PATH updates, fixing the PATH manually, and verifying with az version. Not for az login or authentication failures."
metadata:
  skill_id: "skl_5Pd62_kWnOuvbjd39Uy1LQ"
  title: "az' is not recognized as an internal or external command"
  version: "skv_chFFOe_qV8ejkuXjglSXnA"
  updated: "2026-10-03T04:51:32.910383+00:00"
  canonical_url: "https://vectle.com/skills/skl_5Pd62_kWnOuvbjd39Uy1LQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# az' is not recognized as an internal or external command

## TL;DR
The Azure CLI installed but its folder is not on your PATH, or the install did not finish. Reinstall with the PATH option checked, or add the install folder to PATH yourself, then open a fresh terminal.

## The error
```
'az' is not recognized as an internal or external command,
operable program or batch file.
```

## Fix it
1. Check whether it is actually installed: look for Azure CLI in Add or remove programs. Expected: you confirm it is there (or not).
2. If it is installed, find the install folder and add it to PATH. Open a NEW terminal after changing PATH. Expected: `az version` prints version info.
3. If it is not installed, or the folder is missing, reinstall from the official MSI and keep the "add to PATH" option checked. Expected: the installer completes and a fresh terminal finds `az`.
4. In PowerShell, check with `Get-Command az`. Expected: it resolves to the CLI executable.
5. Run `az version` to confirm. Expected: JSON output with the CLI version.

## When to use this
- An agent sees "'az' is not recognized" on Windows in cmd or PowerShell.
- Right after installing the Azure CLI.

## When NOT to use this
- `az login` failures. The CLI works there; auth is the problem.
- "The term 'az' is not recognized" inside Azure Cloud Shell. Cloud Shell always has it; that is a different issue.

## Compatibility
- Azure CLI on Windows (MSI install), cmd and PowerShell.

### Variant phrasings
- "az is not recognized as an internal or external command"
- "The term 'az' is not recognized as the name of a cmdlet"

## Root cause
The MSI installer optionally adds the CLI folder to PATH. Unchecking that option, or a terminal opened before the install finished, leaves `az` unresolvable. Opening a fresh terminal after fixing PATH is the step everyone skips.

## Edge cases
- 32-bit vs 64-bit installs land in different Program Files folders. Point PATH at the one that actually exists.
- Corporate images sometimes block the MSI's PATH change. Set it manually in System environment variables.


---

Source: [Vectle](https://vectle.com/skills/skl_5Pd62_kWnOuvbjd39Uy1LQ). Version: `skv_chFFOe_qV8ejkuXjglSXnA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
