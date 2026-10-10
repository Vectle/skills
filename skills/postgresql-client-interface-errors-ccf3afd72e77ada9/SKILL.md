---
name: "postgresql-client-interface-errors-ccf3afd72e77ada9"
description: "Fixes QuestDB 8.2.0 PGWire corruption when text and binary protocol clients (e.g. JDBC and psql) connect concurrently. Workaround: set pg.legacy.mode.enabled to true; or upgrade to 8.2.1. Use when PostgreSQL client errors appear randomly under mixed clients. Not for single-client setups."
metadata:
  skill_id: "skl_22Sfd3a1mgcBIXHP5yxxOQ"
  title: "PostgreSQL client interface errors"
  version: "skv_-lXUoWxkotZS6FmZOS9GKg"
  updated: "2026-10-03T05:39:57.184442+00:00"
  canonical_url: "https://vectle.com/skills/skl_22Sfd3a1mgcBIXHP5yxxOQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: the PGWire corruption in QuestDB 8.2.0 happens when text and binary protocol clients (e.g. JDBC and psql) connect concurrently. Workaround it or upgrade.

1. Set pg.legacy.mode.enabled to true. The reporter confirmed no more issues after upgrading to 8.2.1, so upgrading is the cleaner fix.
2. Expected: the random client interface errors stop.

When to use: PostgreSQL client errors appear randomly when querying QuestDB with mixed text and binary protocol clients.

When not to use: a single client type (the corruption needs the concurrency).

Compatibility: QuestDB 8.2.0 (broken), 8.2.1 (fixed). Contributor mtopolnik. Reported in questdb/questdb#5202.

Variants:
- "questdb postgresql client interface errors"
- "questdb pgwire corruption"
- "questdb 8.2.0 jdbc psql concurrent"

Root cause: PGWire corruption under concurrent text and binary protocol clients.

Edge cases: the PG interface is exposed at port 8812 in the docker image; the bug is in the wire handling, not your client config.

---

Source: [Vectle](https://vectle.com/skills/skl_22Sfd3a1mgcBIXHP5yxxOQ). Version: `skv_-lXUoWxkotZS6FmZOS9GKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
