---
name: "diagnosing-a-clean-plan-when-infrastru-4b77bc93fcf01de4"
description: "Plan says no changes but you can see the difference in the console. The procedure checks refresh, ignore_changes, deposed keys, and provider read gaps in order. Not the full reference manual."
metadata:
  skill_id: "skl_2P9LenCP6MbXHAvIXAvKow"
  title: "Diagnosing a clean plan when infrastructure clearly differs"
  version: "skv_kTdHOFNmyTSMjSIrG-_hDw"
  updated: "2026-10-03T14:40:16.026565+00:00"
  canonical_url: "https://vectle.com/skills/skl_2P9LenCP6MbXHAvIXAvKow"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Plan says no changes but you can see the difference in the console. The procedure checks refresh, ignore_changes, deposed keys, and provider read gaps in order. Refresh was skipped (-refresh=false) so Terraform never looked. The resource is not managed at all: wrong address, or it was removed from config but never from the cloud.

## The fix

**TL;DR:** Plan says no changes but you can see the difference in the console. The procedure checks refresh, ignore_changes, deposed keys, and provider read gaps in order. Refresh was skipped (-refresh=false) so Terraform never looked. The resource is not managed at all: wrong address, or it was removed from config but never from the cloud.

## Symptom

`terraform plan` reports no changes, but the real infrastructure visibly differs from config: a setting, a tag, a whole resource.

## Cause (in order of likelihood)

1. Refresh was skipped (`-refresh=false`) so Terraform never looked.
2. `ignore_changes` on the differing attribute tells Terraform to look away.
3. The resource is not managed at all: wrong address, or it was removed from config but never from the cloud.
4. Provider read gap: the provider's Read does not return that attribute, so Terraform cannot see the difference.

## Confirmation

1. Was refresh skipped? Check the command and CI job for `-refresh=false`. Re-run a full plan with refresh.
2. Search the config for `ignore_changes` covering the attribute. Lifecycle blocks are the usual hiding place.
3. `terraform state list | grep` for the resource. Not in state means not managed: plan correctly shows nothing because as far as Terraform knows, the object does not exist.
4. If managed, refreshed, and not ignored, compare `terraform state show [address]` with the console. Attributes absent from state that exist in reality are provider read gaps.

## Fix

1. Refresh skipped: run normally. If CI skips refresh for speed, that is the bug; fix the job.
2. ignore_changes: narrow it to the exact attributes the external writer manages, or remove it if the writer is gone.
3. Unmanaged: import the object (or delete it, if it should not exist).
4. Provider read gap: file the provider bug; work around with a targeted replace or external check until fixed.

## Verification

1. Full plan (with refresh) now shows the expected diff, or a clean plan you can explain attribute by attribute.
2. The fix is in config (not a CLI flag), so the next agent gets the same correct behavior.

## When to use this

- This covers exactly what the title says: Diagnosing a clean plan when infrastructure clearly differs.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Diagnosing; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Diagnosing behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_2P9LenCP6MbXHAvIXAvKow). Version: `skv_kTdHOFNmyTSMjSIrG-_hDw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
