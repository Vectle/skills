---
name: "locks-aren-t-being-released-when-an-er-fd942a5fbaef86ca"
description: "Fixes @planetscale/database holding locks for 20 seconds after a transaction error. The package was not rolling back correctly on error. Upgrade to v1.10.0 or later; the release fixed it and the reporter confirmed their previously failing tests passed. Use when locks linger after transaction errors. Not for other lock issues."
metadata:
  skill_id: "skl_0MH2_aVhx8QjJiy0zxNlNw"
  title: "Locks aren't being released when an error is thrown inside a transaction!"
  version: "skv_caj3bvvU_HyMpbnbiuLARA"
  updated: "2026-10-03T05:29:45.119091+00:00"
  canonical_url: "https://vectle.com/skills/skl_0MH2_aVhx8QjJiy0zxNlNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/planetscale/database-js/issues/124\"]"
---

Fix first: upgrade to v1.10.0 or later. The package was not rolling back correctly on error.

1. Upgrade @planetscale/database to v1.10.0+.
2. Re-run the failing tests. Expected: locks release on error; the reporter confirmed their previously failing tests passed.

When to use: @planetscale/database holds locks for 20 seconds after a transaction error.

When not to use: other lock issues (different causes).

Compatibility: @planetscale/database v1.10.0+. Reported in planetscale/database-js#124.

Variants:
- "planetscale locks not released"
- "planetscale transaction rollback"
- "database-js 124"

Root cause: the package wasnt rolling back correctly on error.

Edge cases: none; the fix is version-bound.

---

Source: [Vectle](https://vectle.com/skills/skl_0MH2_aVhx8QjJiy0zxNlNw). Version: `skv_caj3bvvU_HyMpbnbiuLARA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
