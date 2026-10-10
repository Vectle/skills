---
name: "why-transactions-don-t-work-in-this-ca-06e63a8be77bfbc0"
description: "Explains that MySQL DDL is not transactional, so CREATE TABLE statements cannot be rolled back inside a transaction, on PlanetScale or anywhere else. The maintainer's answer: schema-change safety comes from PlanetScale deploy requests with gated deployments. Use when DDL-in-transaction doesnt roll back. Not for DML transactions, which work normally."
metadata:
  skill_id: "skl_1ixP-sw9pp0oOxDslC6Pmg"
  title: "Why transactions don't work in this case"
  version: "skv_V5zDtIogbCy7y_kqCSNogw"
  updated: "2026-10-03T05:33:44.9028+00:00"
  canonical_url: "https://vectle.com/skills/skl_1ixP-sw9pp0oOxDslC6Pmg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: stop expecting DDL to roll back. MySQL DDL is not transactional, so CREATE TABLE statements cannot be rolled back inside a transaction, on PlanetScale or anywhere else.

1. Do not wrap DDL in transactions expecting atomic rollback; it will not work.
2. For schema-change safety, use a PlanetScale deploy request with gated deployments instead. The schema only applies once the deploy request is completed, which gives you the rollback story you were trying to get from transactions.

When to use: CREATE TABLE (or other DDL) inside a transaction doesnt roll back on PlanetScale.

When not to use: DML transactions (INSERT/UPDATE/DELETE roll back fine).

Compatibility: PlanetScale, @planetscale/database-js. Maintainer answer. Reported in planetscale/database-js#106.

Variants:
- "planetscale ddl transaction rollback"
- "mysql create table not transactional"
- "planetscale deploy request gated deployments"

Root cause: MySQL DDL is not transactional by design.

Edge cases: the report also had an empty-string query failing with 'Query was empty'; that is a separate issue from the DDL one.

---

Source: [Vectle](https://vectle.com/skills/skl_1ixP-sw9pp0oOxDslC6Pmg). Version: `skv_V5zDtIogbCy7y_kqCSNogw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
