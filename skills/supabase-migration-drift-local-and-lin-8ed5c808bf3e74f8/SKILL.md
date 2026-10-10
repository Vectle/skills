---
name: "supabase-migration-drift-local-and-lin-8ed5c808bf3e74f8"
description: "supabase db push fails or pushes against a database whose real schema no longer matches migration history, usually from dashboard hotfixes or ad-hoc SQL. Covers diffing, deciding source of truth, repairing history, and prevention rules. Not for migration syntax errors or fresh-project setup."
metadata:
  skill_id: "skl_htuOYgPNGBP6PQ1_HlZUfg"
  title: "Supabase migration drift: local and linked project disagree, diff before you push"
  version: "skv_disGi6gtMEKJIoUxmu2gGg"
  updated: "2026-10-03T04:41:19.182649+00:00"
  canonical_url: "https://vectle.com/skills/skl_htuOYgPNGBP6PQ1_HlZUfg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The migration history table says one thing and the database says another, usually because someone changed the schema by hand in the dashboard or ran ad-hoc SQL. Stop and diff with `supabase db diff` against the linked project, decide per change whether the database or the migrations are the source of truth, repair the history with `supabase migration repair` if the history rows are wrong, and only push when the diff is empty. Never push blind.

What it looks like:

```text
supabase db push fails, or succeeds against a database whose real schema no
longer matches the migration history.
```

Steps:

1. Confirm the drift: `supabase db diff` against the linked project. Read the diff carefully; it shows what the migrations would change, which tells you what is out of sync. Success: you can name the drifting objects.
2. Decide per change whether the database or the migrations are the source of truth. Dashboard hotfixes belong in a new migration (capture them with `supabase db diff` into a migration file). Local-only experiments that never shipped should be reverted. Success: every diff hunk is classified.
3. If the history table is wrong (migrations marked applied that were not, or vice versa), use `supabase migration repair` to fix the history rows. Repair edits history, not schema; run it only after step 2. Success: history matches reality.
4. Re-run `supabase db diff`. Empty diff is the only acceptable state before pushing. Success: diff is empty.
5. Push, then diff again. A clean round trip is the verification. Success: still empty.

When to use: push failures, surprise schema on the linked project, or migrations that "already ran" but the objects are missing.

When not to use: migration SQL syntax errors, brand-new project setup, or local-only development with no linked project.

Compatibility: Supabase CLI, Postgres.

Variants:
- supabase migration history mismatch
- supabase db push drift
- supabase migration repair

Root cause: out-of-band schema changes. Someone clicked in the dashboard, ran ad-hoc SQL, or applied a migration locally without committing it. The history table and the real schema diverge silently until a push exposes it.

Edge cases:
- Rules that prevent recurrence: every schema change goes through a migration file, reviewed and committed. The dashboard SQL editor is for reads and emergencies; any emergency write gets a follow-up migration the same day.
- Agents that just fix it in the dashboard are the number one drift source. If your agent has dashboard access, this skill is the guardrail.

---

Source: [Vectle](https://vectle.com/skills/skl_htuOYgPNGBP6PQ1_HlZUfg). Version: `skv_disGi6gtMEKJIoUxmu2gGg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
