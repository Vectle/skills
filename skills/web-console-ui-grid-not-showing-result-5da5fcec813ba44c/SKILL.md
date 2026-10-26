---
name: "web-console-ui-grid-not-showing-result-5da5fcec813ba44c"
description: "Fixes the QuestDB 7.1 web console grid showing column headers but no rows ('Cannot read properties of undefined (reading digest)') by downgrading to 7.0.1, or by running a local HTTP proxy so the web console URL is YOUR_HOST or the loopback address. A 7.1 regression from the improved grid features. Use when the grid is empty but queries run. Not for query errors."
metadata:
  skill_id: "skl_0akEjBf2FfFAg2VNZphyLA"
  title: "web console UI grid not showing results"
  version: "skv_5w4e457QzqtKE0LRiuk9Tw"
  updated: "2026-10-03T05:30:55.972369+00:00"
  canonical_url: "https://vectle.com/skills/skl_0akEjBf2FfFAg2VNZphyLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/questdb/questdb/issues/3168\"]"
---

Fix first: this is a 7.1 regression from the improved grid features, not your query. Two maintainer-provided workarounds:

```text
Uncaught TypeError: Cannot read properties of undefined (reading 'digest')
```

1. Downgrade to QuestDB 7.0.1. Expected: the grid shows rows again.
2. Or run a local HTTP proxy so the web console URL is YOUR_HOST or the loopback address. Expected: the grid renders.

When to use: any query in the QuestDB 7.1 web console shows the number of columns but the grid is always empty.

When not to use: queries that error (that is the database, not the grid).

Compatibility: QuestDB 7.1 (broken), 7.0.1 (fine). Reported in questdb/questdb#3168.

Variants:
- "questdb web console grid empty"
- "questdb grid not showing results"
- "questdb cannot read properties of undefined reading digest"

Root cause: a 7.1 regression in the updated grid component.

Edge cases: the proxy workaround suggests the bug is URL/host dependent; if you already access via the loopback address and still see it, downgrade.

---

Source: [Vectle](https://vectle.com/skills/skl_0akEjBf2FfFAg2VNZphyLA). Version: `skv_5w4e457QzqtKE0LRiuk9Tw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
