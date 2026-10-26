---
name: "depot-cli-v2-102-file-merging-change-b-612d5176a1891352"
description: "Fixes depot-cli v2.102 breaking x-bake tag overrides by replacing compose override files with a native Bake target for generated overrides. Use when --file merging now appends tags instead of replacing them after upgrading depot-cli. Not for other depot bake failures."
metadata:
  skill_id: "skl_IPGOF10LMNI61gs_QEAbug"
  title: "depot-cli v2.102: --file merging change breaks x-bake tag overrides"
  version: "skv_UrJyCR9D0aDwwyVcm3mF2Q"
  updated: "2026-10-03T04:16:02.814383+00:00"
  canonical_url: "https://vectle.com/skills/skl_IPGOF10LMNI61gs_QEAbug"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_VkUO33CeP6sRl8FBoE5Vxw\",\"https://github.com/depot/cli/issues/553\"]"
---

## TL;DR

Stop using compose override files for generated tag overrides; use a native Bake target instead, e.g. `{"target": {"static": {"tags": [...]}}}`, which replaces the tags cleanly. depot-cli v2.102 upgraded compose-go, which switched x-* extensions from replace to standard Compose merge rules (arrays append).

## The problem

depot-cli v2.102 changed `--file` merging for `depot bake`: previously a compose override file completely replaced the `x-bake` tags array, but after the upgrade tags from both files are merged, so `--push` tries to push all tags instead of just the override's tag.

## Fix it

1. Confirm the version and symptom:
   ```bash
   depot --version
   ```
   Success check: v2.102+, and `depot bake --file base.yml --file override.yml --print` shows merged tags.

2. Replace the compose override file with a native Bake target for the generated overrides:
   ```json
   {"target": {"static": {"tags": ["your-tag"]}}}
   ```
   Success check: `--print` shows only the intended tags.

3. Run the bake with the native target file.
   Success check: `--push` pushes only the override's tag.

## When this applies

- depot-cli v2.102+ where `--file` override files now merge `x-bake` tags instead of replacing.
- `--push` pushing more tags than intended after the upgrade.

## When it does not apply

- depot-cli below v2.102; the old replace behavior still applies.
- Tag problems unrelated to override merging.

## Compatibility

- depot-cli v2.102+ (compose-go v2.1.3 to v2.14.0 upgrade). The merge behavior is the upstream Compose standard.

## Variant phrasings

- depot bake file merging tags
- depot-cli 2.102 x-bake tags merged
- depot bake override file tags append instead of replace

## Why it happens

compose-go switched `x-*` extension handling from replace to the standard Compose merge rules, where arrays append. depot-cli inherited the change via its compose-go upgrade, so override files now accumulate tags.

## Edge cases

- The native target form is the durable fix; do not rely on ordering tricks in override files.


---

Source: [Vectle](https://vectle.com/skills/skl_IPGOF10LMNI61gs_QEAbug). Version: `skv_UrJyCR9D0aDwwyVcm3mF2Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
