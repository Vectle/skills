---
name: "no-space-left-on-device-3fa620f56eb312f3"
description: "Why a GitHub Actions job fails with No space left on device on an otherwise green workflow, and how to reclaim disk on GitHub-hosted runners fast. Use when build or docker steps die with ENOSPC or write errors."
metadata:
  skill_id: "skl_xpLwnXb6hRrd1qO8ozi6Yg"
  title: "No space left on device"
  version: "skv_V-BvkIQqNpI2nDDpnEVCAA"
  updated: "2026-10-03T05:53:23.366683+00:00"
  canonical_url: "https://vectle.com/skills/skl_xpLwnXb6hRrd1qO8ozi6Yg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Add a step that shows disk usage with df -h, delete the big things you do not need (docker images, Android SDK, .NET, npm or pip caches), and rerun. If it still does not fit, move the job to a larger runner. GitHub-hosted ubuntu-latest runners ship about 14 GB of usable disk and Docker images plus SDK toolchains eat it fast.

```text
No space left on device
```

## The fix

1. Add a diagnostic step at the top of the job to see where the space went:
   ```bash
   df -h /
   sudo du -sh /usr/share/dotnet /usr/local/lib/android /opt/hostedtoolcache 2>/dev/null | sort -rh
   ```
   Expected: Filesystem shows the free space on / and the three biggest preinstalled dirs.

2. Delete what you do not need before the heavy step. A typical reclaim:
   ```bash
   sudo rm -rf /usr/share/dotnet
   sudo rm -rf /usr/local/lib/android
   sudo docker image prune --all --force
   df -h /
   ```
   Expected: df shows several GB freed.

3. If your own build produces the bulk (node_modules, target/, .gradle), clean caches between steps: npm cache clean --force, cargo clean, or stop gradle and remove the build cache.

4. Rerun the job and confirm the df line shows headroom; the failing step should pass unchanged. If the job genuinely needs more disk (large containers, Android emulator images), move it to a larger GitHub-hosted runner instead of fighting the small one.

## When this applies

- a previously green job fails with No space left on device
- build or docker build steps die with ENOSPC or write errors
- you added dependencies, caches, or artifacts and the job started failing

## When it does NOT apply

- the error is in your application code writing to a path that does not exist - that is a code bug, not disk
- self-hosted runners - resize or mount more disk on the host instead

## Compatibility

GitHub-hosted ubuntu-latest (about 14 GB usable); the reclaim step below is Linux-only, adjust paths on Windows and macOS images.

## Variants of this error

### `ENOSPC: no space left on device, write`
The errno form the same failure takes in Node and build tools.

### `write /dev/stdout: no space left on device`
What a shell step prints when the disk fills mid-write.

## Why it happens

The runner image comes with preinstalled toolchains (dotnet, Android, GHC, hostedtoolcache) that most workflows never use. Each docker pull and each cached dependency dir adds on top. When free space hits zero, the step writing at that moment throws - the error names the symptom, not the hog.

## Edge cases and pitfalls

- docker image prune only helps if the job actually pulls images; for pure language builds the SDK deletes matter more.
- Caches restore the same big cache every run - if a cache dir holds gigabytes of stale layers, delete and re-save the cache.
- Windows runners have more disk but slower deletes; do the cleanup before the heaviest step anyway.

---

Source: [Vectle](https://vectle.com/skills/skl_xpLwnXb6hRrd1qO8ozi6Yg). Version: `skv_V-BvkIQqNpI2nDDpnEVCAA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
