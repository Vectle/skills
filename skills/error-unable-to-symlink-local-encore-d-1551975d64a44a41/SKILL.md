---
name: "error-unable-to-symlink-local-encore-d-1551975d64a44a41"
description: "Fixes Encore version update failures on Windows ('unable to symlink local encore.dev' with pnpm) by running the Encore install script directly in a fresh PowerShell terminal. Use when encore version update fails on Windows. Not for macOS/Linux installs or non-symlink update errors."
metadata:
  skill_id: "skl_Cbm3mmfUhVkK4TdnEurSlw"
  title: "Error unable to symlink local encore.dev using pnpm"
  version: "skv_DcfR7O0FN9FZgF12Axcb3A"
  updated: "2026-10-03T04:09:44.531489+00:00"
  canonical_url: "https://vectle.com/skills/skl_Cbm3mmfUhVkK4TdnEurSlw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

If `encore version update` fails on Windows with a symlink error, skip it and run the install script directly in a fresh PowerShell terminal. The reporter confirmed this worked when the in-place update did not.

## The error

```text
Error: unable to symlink local encore.dev
```

Seen when running `pnpm i` or `encore version update` on Windows.

## Fix it

1. Open a fresh PowerShell terminal (not the one where the update failed).
   Success check: a new terminal window with no Encore processes running in it.

2. Run the Encore install script directly:
   ```powershell
   iwr https://encore.dev/install.ps1 -useb | iex
   ```
   Success check: the script completes and reports the installed version.

3. Verify the install:
   ```powershell
   encore version
   ```
   Success check: prints the new version with no errors.

## When this applies

- `encore version update` fails on Windows with a symlink-related error.
- pnpm-based Encore installs on Windows that cannot self-update.

## When it does not apply

- macOS or Linux; use the standard update path there.
- The failure is a network or permission error rather than a symlink error.
- Fresh installs (not updates) failing for other reasons.

## Compatibility

- Windows 10/11, PowerShell 5.1+.
- Encore CLI installed via pnpm or the install script.

## Variant phrasings

- encore version update fails Windows
- unable to symlink local encore.dev pnpm
- encore update symlink error

## Why it happens

On Windows, the running Encore binary holds a lock on its own symlink, so the in-place updater cannot replace it. Running the install script in a fresh terminal avoids the locked files and lays down a clean install.

## Edge cases

- Run PowerShell as Administrator if the script reports access denied.
- Close any terminal running `encore run` before updating.
- Source: https://github.com/encoredev/encore/issues/1658


---

Source: [Vectle](https://vectle.com/skills/skl_Cbm3mmfUhVkK4TdnEurSlw). Version: `skv_DcfR7O0FN9FZgF12Axcb3A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
