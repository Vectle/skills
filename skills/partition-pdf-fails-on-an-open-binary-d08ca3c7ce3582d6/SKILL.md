---
name: "partition-pdf-fails-on-an-open-binary-d08ca3c7ce3582d6"
description: "Fixes partition_pdf throwing on an already-opened binary file handle with the hi_res strategy by upgrading to a build that includes PR #3395, which fixed the binary-file loading path. Use when passing an open handle to partition_pdf. Not for path-based calls, or for other strategies."
metadata:
  skill_id: "skl_X3u2We_dRo2jZhFkDeE1Bg"
  title: "partition_pdf fails on an open binary file handle: fixed by PR 3395"
  version: "skv_1K-8oQucqNBqhnomQz_6EA"
  updated: "2026-10-03T04:47:39.477164+00:00"
  canonical_url: "https://vectle.com/skills/skl_X3u2We_dRo2jZhFkDeE1Bg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/Unstructured-IO/unstructured/issues/3097\"]"
---

Fix first: upgrade to a build that includes PR #3395, which fixed the binary-file loading path.

```text
partition_pdf throws when passed an already-opened binary file handle (hi_res strategy)
```

1. Upgrade unstructured to a build containing PR #3395.
2. Retry partition_pdf with the open binary handle and the hi_res strategy. Expected: it partitions instead of throwing.

When to use: partition_pdf throws when you pass it an already-opened binary file handle with hi_res.

When not to use: passing a file path (never affected), or strategies other than hi_res.

Compatibility: unstructured, hi_res strategy. Reported in Unstructured-IO/unstructured#3097, fixed by PR #3395.

Variants:
- "partition_pdf open file handle"
- "partition_pdf hi_res binary handle"
- "unstructured partition_pdf throws file handle"

Root cause: the binary-file loading path didnt handle an already-opened handle under hi_res.

Edge cases: if you cant upgrade, passing a path instead of a handle sidesteps the bug.

---

Source: [Vectle](https://vectle.com/skills/skl_X3u2We_dRo2jZhFkDeE1Bg). Version: `skv_1K-8oQucqNBqhnomQz_6EA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
