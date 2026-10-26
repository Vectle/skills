---
name: "debian-buster-inrelease-changed-its-su-540e0a1db39c3601"
description: "Fixes apt failing in CI with the Debian buster Suite changed from stable to oldstable error. Use when apt-get update aborts on old Debian images. Not for 404 mirror errors."
metadata:
  skill_id: "skl_QRmWknO8vLPJWl5iQsYsnA"
  title: "Debian buster InRelease changed its Suite value from stable to oldstable in CI"
  version: "skv_IurZLrI5nDOvyMMsHlB5rw"
  updated: "2026-10-03T05:32:36.011634+00:00"
  canonical_url: "https://vectle.com/skills/skl_QRmWknO8vLPJWl5iQsYsnA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/68802802/repository-http-security-debian-org-debian-security-buster-updates-inrelease\"]"
---

TL;DR: Allow the release-info change for that one update run: apt-get update -o Acquire::AllowReleaseInfoChange::Suite=true, then install normally. Debian moved buster from stable to oldstable, and apt refuses to silently accept a changed Suite label; the flag tells apt you have seen and accept the rename.

```text
E: Repository 'http://security.debian.org/debian-security buster/updates InRelease' changed its 'Suite' value from 'stable' to 'oldstable'
```

## The fix

1. In the workflow step, run the update with the flag:
   ```bash
   sudo apt-get update -o Acquire::AllowReleaseInfoChange::Suite=true
   ```
   Expected: The update completes without the Suite error.

2. Then install as usual:
   ```bash
   sudo apt-get install -y unzip xvfb
   ```
   Expected: Packages install; the step exits 0.

3. Long term, move the job's container image off buster (bookworm or newer), since oldstable stops getting security updates.
   Expected: Future runs never hit the Suite rename again.

## When this applies

- apt-get update fails in CI with the changed Suite value error on Debian buster
- the job runs in a container based on an old Debian release

## When it does NOT apply

- the error is about a missing Release file or 404 (that is a dead mirror, not a Suite rename)
- you are on bookworm or newer (the flag is harmless but unnecessary)

## Compatibility

Any CI running apt on Debian buster containers or VMs, including GitHub Actions container jobs.

## Variants of this error

### `E: Repository 'http://deb.debian.org/debian buster InRelease' changed its 'Suite' value from 'stable' to 'oldstable'`
Same rename on the main repo URL. Same flag fixes it.

### `changed its 'Suite' value from 'stable-updates' to 'oldstable-updates'`
The updates pocket variant. Same flag fixes it.

## Why it happens

Each Debian release gets renamed stable to oldstable when the next stable ships. apt treats a Suite change as suspicious (it can signal a mirror hijack) and aborts unless you explicitly allow it.

## Edge cases and pitfalls

- Pinning to buster long-term is a security risk; oldstable security support ends about a year after release.
- The flag only affects that single apt-get invocation; add it wherever apt-get update runs.
- If you vendor your own base image, rebuild it on bookworm instead of patching every workflow.

---

Source: [Vectle](https://vectle.com/skills/skl_QRmWknO8vLPJWl5iQsYsnA). Version: `skv_IurZLrI5nDOvyMMsHlB5rw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
