---
name: "devcycle-expo-unable-to-resolve-class-6f57955db671e4ca"
description: "Fixes Expo SDK 50 bundling failing with 'Unable to resolve class-validator from @devcycle/types' after upgrading the DevCycle Expo SDK past 1.14. Use this when downgrading to 1.14 makes it go away. Not for other missing-module errors."
metadata:
  skill_id: "skl_12G58BvwecLXgy35UwOIXQ"
  title: "DevCycle Expo Unable to resolve class-validator from @devcycle/types"
  version: "skv_A0l-bL0shOAI41fwnyRNbg"
  updated: "2026-10-03T05:07:46.096617+00:00"
  canonical_url: "https://vectle.com/skills/skl_12G58BvwecLXgy35UwOIXQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_-sbfU28NVLNVeV-dBOTLfQ\",\"https://github.com/DevCycleHQ/js-sdks/issues/855\"]"
---

TL;DR: if bundling fails with `Unable to resolve "class-validator" from "node_modules/@devcycle/react-native-expo-client-sdk/node_modules/@devcycle/types/index.cjs.js"` after upgrading `@devcycle/react-native-expo-client-sdk` past 1.14 on Expo SDK 50, it is a DevCycle packaging bug introduced after 1.14 (something pulled class-validator into @devcycle/types). Upgrade past the affected versions; the reporter confirmed the fix resolved it. Pinned? Stay on 1.14 until you can upgrade.

```text
Unable to resolve "class-validator" from ".../@devcycle/types/index.cjs.js"
```

## Steps

1. Upgrade the DevCycle Expo client SDK past the affected versions.

   Expected: bundling succeeds. Success check: the app bundles with no class-validator error.

2. If pinned, stay on 1.14 as the temporary workaround.

## When to use this

- Expo SDK 50, error appeared right after the DevCycle upgrade past 1.14.

## When NOT to use this

- Other unresolvable modules; check your deps.
- You are on 1.14 and see it; something else is wrong.

## Compatibility

- @devcycle/react-native-expo-client-sdk fixed releases.

## Variant phrasings

- "devcycle expo class-validator unable to resolve"
- "devcycle types class-validator expo"

## Root cause

A transitive dependency leaked into the published @devcycle/types bundle.

## Edge cases

- None; the packaging fix is the whole story.

---

Source: [Vectle](https://vectle.com/skills/skl_12G58BvwecLXgy35UwOIXQ). Version: `skv_A0l-bL0shOAI41fwnyRNbg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
