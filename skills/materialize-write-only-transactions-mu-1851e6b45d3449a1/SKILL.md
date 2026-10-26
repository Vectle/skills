---
name: "materialize-write-only-transactions-mu-1851e6b45d3449a1"
description: "Fix for Materialize write only transactions must hit one table or commit fails: In Materialize every INSERT inside a single transaction block must hit the same table as the first INSERT, or COMMIT dies with 'internal error, wrong set of locks acquired' and rolls back everything. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_fkamCMazWuNgT0EWC2Qx9Q"
  title: "Materialize write only transactions must hit one table or commit fails"
  version: "skv_otSMSD3bV7dYMaAUfAhb6A"
  updated: "2026-10-03T04:41:45.13462+00:00"
  canonical_url: "https://vectle.com/skills/skl_fkamCMazWuNgT0EWC2Qx9Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/materializeinc/agent-skills/blob/HEAD/.agents/skills/materialize-docs/sql/begin/index.md\"]"
---

TL;DR: In Materialize every INSERT inside a single transaction block must hit the same table as the first INSERT, or COMMIT dies with 'internal error, wrong set of locks acquired' and rolls back everything. Keep write-only transactions to one table. The fix is to split multi-table writes into separate transaction blocks rather than assuming Postgres-style multi-table transactions.

```text
Materialize write only transactions must hit one table or commit fails
```

Keep write-only transactions to one table. In Materialize every INSERT inside a single transaction block must hit the same table as the first INSERT, or COMMIT dies with 'internal error, wrong set of locks acquired' and rolls back everything. The fix is to split multi-table writes into separate transaction blocks rather than assuming Postgres-style multi-table transactions.

Context: Materialize docs BEGIN (materializeinc/agent-skills .agents/skills/materialize-docs/sql/begin/index.md): In Materialize, a write-only transaction may contain only INSERT statements, and every INSERT must target the same table. If a later statement in the block writes to a different table than the first, COMMIT fails with 'internal error, wrong set of locks acquired' and rolls the whole transaction back.

## When to use
You hit exactly this: Materialize write only transactions must hit one table or commit fails.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title.

---

Source: [Vectle](https://vectle.com/skills/skl_fkamCMazWuNgT0EWC2Qx9Q). Version: `skv_otSMSD3bV7dYMaAUfAhb6A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
