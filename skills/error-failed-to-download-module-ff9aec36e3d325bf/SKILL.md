---
name: "error-failed-to-download-module-ff9aec36e3d325bf"
description: "Fixes OpenTofu's 'Error: Failed to download module' at tofu init by tracing the bad module source. Use when init names a module whose source URL, ref, or registry path doesn't resolve. Not for 'Module not installed' (you skipped init) or provider download errors."
metadata:
  skill_id: "skl_98qwIZc4m8OixfM1bUN1gA"
  title: "Error: Failed to download module"
  version: "skv_hrKidJpgSIa2F3Ku39I0ig"
  updated: "2026-10-03T06:05:46.681142+00:00"
  canonical_url: "https://vectle.com/skills/skl_98qwIZc4m8OixfM1bUN1gA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: `tofu init` can't fetch a module source. The error shows the module address and the exact source URL it tried. Check the source for typos, confirm the repo, ref, or registry path actually exists (and that you have access, for private ones), then re-init.

```text
Error: Failed to download module

Could not download module "ddn_exascaler" (modules/DDN-EXAScaler/main.tf:38) source code from
"git::https://github.com/DDNStorage/exascaler-cloud-terraform.git?ref=78deadb": error downloading
'https://github.com/DDNStorage/exascaler-cloud-terraform.git?ref=78deadb': /usr/bin/git exited with 128: Cloning into
'.terraform/modules/tmplustrefs.ddn_exascaler'...
remote: Repository not found.
fatal: repository 'https://github.com/DDNStorage/exascaler-cloud-terraform.git/' not found
```

## Steps

1. Copy the source URL from the error (the `git::[module source URL]` part, or the registry address).
   Expected: you have the exact string tofu tried.
2. Verify it exists: for git sources, `git ls-remote [url]`; for registry modules, open the registry page for that namespace/name/provider.
   Expected: either it resolves (access problem) or it doesn't (address problem).
3. Fix the cause:
   - Typo in the repo or module path: correct `source`.
   - Deleted branch/tag in `?ref=`: point at a ref that exists.
   - Private repo with no credentials: make sure git can auth (SSH agent, credential helper) in the environment running tofu.
   Expected: the source resolves by hand.
4. Run `tofu init` again.
   Expected: `- Installing [module]...` then `OpenTofu has been successfully initialized!`

## When this applies

- `tofu init` fails on `Downloading ...` / `Failed to download module`, naming a module and a source.
- Right after adding a module block or bumping its `version`/`ref`.

## When it doesn't apply

- `Error: Module not installed` means you never ran init; just run it.
- `Error: Failed to query available provider packages` is about providers, not modules.
- `Error: Unsupported argument` on a module block means the module downloaded fine but its inputs changed; check the registry Inputs tab for your pinned version.

## Tool versions

All OpenTofu versions. Module installer behavior (git, registry, local paths) is unchanged across 1.x.

## Why it happens

Module installation is just fetching: git clone, registry download, or local copy. Anything that breaks fetching (wrong address, deleted ref, missing credentials, no network) surfaces here, before tofu even reads the module's code.

## Edge cases

- `?ref=` pins are fragile: tags get deleted, branches get renamed. Prefer versioned registry modules (`source = "namespace/name/provider"` + `version`) over raw git URLs where you can.
- SSH vs HTTPS: CI runners often have one but not the other. Match the URL scheme to what the runner can authenticate.
- Registry modules with `version` constraints that match nothing fail differently (`no version matching`); that's a constraint problem, not a download problem.

---

Source: [Vectle](https://vectle.com/skills/skl_98qwIZc4m8OixfM1bUN1gA). Version: `skv_hrKidJpgSIa2F3Ku39I0ig`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
