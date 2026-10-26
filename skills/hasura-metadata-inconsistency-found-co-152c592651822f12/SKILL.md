---
name: "hasura-metadata-inconsistency-found-co-152c592651822f12"
description: "Fixes Hasura reboot-looping after upgrading to v2.49.5 with metadata inconsistency 'Found conflicting definitions for GraphQL type'. Use this when the naming_convention experimental feature with graphql-default is enabled. Not for other metadata errors."
metadata:
  skill_id: "skl_-H9TC5NMFbafCT7ex1Y5GA"
  title: "Hasura: metadata inconsistency 'Found conflicting definitions for GraphQL type' after upgrade to v2.49.5"
  version: "skv_SVDPfuTfq4q2ovzFiIxtQQ"
  updated: "2026-10-03T05:06:07.71492+00:00"
  canonical_url: "https://vectle.com/skills/skl_-H9TC5NMFbafCT7ex1Y5GA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_n6i0JPF-BdFWAym8FjF-QA\",\"https://github.com/hasura/graphql-engine/issues/10867\"]"
---

TL;DR: if upgrading hasura/graphql-engine from v2.49.4 to v2.49.5 puts the server in a reboot loop with `Found conflicting definitions for GraphQL type '[Type]' ... Former has definition: enum ... Latter has definition: scalar ...`, it is a v2.49.5 regression in the graphql-default naming convention handling. Upgrade to v2.50.0; the reporter confirmed the behavior is gone. If you must stay on v2.49.x, downgrade back to v2.49.4 as the temporary workaround. The signature: the conflict only appears with the naming_convention experimental feature plus graphql-default enabled, and metadata exported on the older version looks clean.

```text
Found conflicting definitions for GraphQL type
```

## Steps

1. Upgrade to Hasura v2.50.0+.

2. Restart and check the logs.

   Expected: no reboot loop. Success check: the server stays up and metadata is consistent.

## When to use this

- Reboot loop right after the v2.49.4 to v2.49.5 upgrade with the naming convention feature on.

## When NOT to use this

- Other metadata inconsistencies; those have their own causes.
- The feature is off; this regression does not apply.

## Compatibility

- hasura/graphql-engine v2.50.0+.

## Variant phrasings

- "hasura 2.49.5 conflicting definitions graphql type"
- "hasura metadata inconsistency upgrade"

## Root cause

The naming-convention rewrite in 2.49.5 generated conflicting enum/scalar definitions for the same type name.

## Edge cases

- Exported metadata looking clean on the old version is expected; the corruption happened at load time on the new one.

Source: https://github.com/hasura/graphql-engine/issues/10867

---

Source: [Vectle](https://vectle.com/skills/skl_-H9TC5NMFbafCT7ex1Y5GA). Version: `skv_SVDPfuTfq4q2ovzFiIxtQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
