---
name: "version-3-11-was-not-found-in-the-loca-d008f9327bef2a15"
description: "Fixes actions/setup-python failing with 'Version X was not found in the local cache'. Use when the requested Python has no prebuilt binary for the runner OS/arch. Not for download timeouts."
metadata:
  skill_id: "skl_LAWCAsxE-dIoHxTMrkoI5g"
  title: "Version 3.11 was not found in the local cache (actions/setup-python)"
  version: "skv_EQ_cioa8hEhktXrI8tawYA"
  updated: "2026-10-03T05:38:35.708741+00:00"
  canonical_url: "https://vectle.com/skills/skl_LAWCAsxE-dIoHxTMrkoI5g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Use a Python version that actually has a prebuilt binary for your runner OS and architecture; check the versions manifest before pinning an exotic combo. setup-python only downloads builds that exist upstream; a version/arch with no installer (like old Pythons on Windows arm64) can never be satisfied.

```text
Version 3.11 was not found in the local cache
```

## The fix

1. Open the versions manifest and confirm your version/arch combo has a build: https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json
   Expected: You see whether the combo exists.

2. Pin python-version to one that exists for your runner (e.g. 3.11 on ubuntu x64, or a newer 3.12+ for Windows arm64).
   Expected: The setup step downloads and installs cleanly.

3. If you must have that exact version, install Python yourself (apt, pyenv, or a container image) and skip setup-python.
   Expected: python --version reports what you installed.

## When this applies

- actions/setup-python fails with Version X was not found in the local cache followed by a not-found error
- self-hosted runners or unusual architectures

## When it does NOT apply

- the download itself times out (that is network flake; re-run)
- the version exists but extraction fails (that is disk space or permissions)

## Compatibility

actions/setup-python v4/v5/v6 on GitHub-hosted and self-hosted runners, all OSes.

## Variants of this error

### `Error: The version '3.9' with architecture 'arm64' was not found`
The explicit arch form of the same failure. Same fix.

### `Version 3.12 with arch x64 not found`
Older form from when 3.12 had no stable build yet. Same fix: pick a released version.

## Why it happens

The runner's tool cache only holds what previous jobs put there; on a cold cache setup-python resolves the request against the python-versions manifest, and combos without upstream binaries (new architectures, brand-new or ancient versions) resolve to nothing.

## Edge cases and pitfalls

- Ephemeral self-hosted runners always have a cold cache, so they hit the manifest on every run; pin versions that exist.
- allow-prereleases: true can satisfy requests for beta versions.
- Specifying 3.11 lets the action pick the latest 3.11.x with a build; pinning 3.11.0 exactly is more fragile.

---

Source: [Vectle](https://vectle.com/skills/skl_LAWCAsxE-dIoHxTMrkoI5g). Version: `skv_EQ_cioa8hEhktXrI8tawYA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
