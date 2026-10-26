---
name: "token-auth-failing-depending-on-userna-99fecafdee3846da"
description: "Fixes SurrealDB scoped token auth failing intermittently depending on the username (signin works, the returned token sometimes doesnt) by upgrading to a nightly build containing the fix. Use when token auth is username-dependent. Not for scope definition errors."
metadata:
  skill_id: "skl_YDBuwRUvlTUSyKuo-XZ2PA"
  title: "Token auth failing depending on username: fixed in nightly"
  version: "skv_EuIZJEF9QUE8noNT_BWqEA"
  updated: "2026-10-03T05:11:45.542997+00:00"
  canonical_url: "https://vectle.com/skills/skl_YDBuwRUvlTUSyKuo-XZ2PA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/surrealdb/surrealdb/issues/2963\"]"
---

Fix first: this was a server bug, not your scope definition. The fixing PR was merged and shipped in the next nightly, so upgrade to a nightly build that includes it.

```text
token authentication intermittently fails depending on the username
```

1. Upgrade SurrealDB to a nightly build containing the fix.
2. Sign in and authenticate with the returned token across several usernames. Expected: tokens authenticate regardless of username.

When to use: on a websocket connection, after signin, the token sometimes fails depending on which username was used.

When not to use: tokens that never work for any user (check your SIGNUP/SIGNIN scope definitions first).

Compatibility: SurrealDB nightly (fix merged after the report). Reported in surrealdb/surrealdb#2963.

Variants:
- "surrealdb token auth fails username"
- "surrealdb signin token intermittent"
- "surrealdb scope token authentication"

Root cause: a server-side bug in scoped token authentication that made it username-dependent.

Edge cases: dont rewrite your SIGNUP/SIGNIN scopes chasing this; they were never the problem.

---

Source: [Vectle](https://vectle.com/skills/skl_YDBuwRUvlTUSyKuo-XZ2PA). Version: `skv_EuIZJEF9QUE8noNT_BWqEA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
