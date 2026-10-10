---
name: "workflow-schema-diff-before-restore-or-7d02ac5a53ebed5d"
description: "Use Neon's schema diff to see exactly what a restore or migration will change before it changes it. The diff is the approval gate."
metadata:
  skill_id: "skl_AtS-ZDE7V8F--9_KOfNmHg"
  title: "Workflow: schema diff before restore or migration"
  version: "skv_1TpXmPNaqRkjGLQ9sXVDEA"
  updated: "2026-10-03T20:51:30.465521+00:00"
  canonical_url: "https://vectle.com/skills/skl_AtS-ZDE7V8F--9_KOfNmHg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# Workflow: schema diff before restore or migration

## TL;DR

No restore or migration runs without a human- or CI-readable summary of what it changes. The last three restores/migrations each have a diff attached to their change record, and at least one caught an unintended change.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Steps

1. Before an instant restore, run a schema diff between the current branch and the restore target (the Console offers a side-by-side comparison; the CLI has a diff command).

   Success check: the expected output above appears and the command exits 0.

2. Before a migration, diff the schema-only rehearsal branch against production.

3. Attach the diff to the change record (PR, incident ticket): tables added/dropped, columns changed, indexes touched.

   Success check: the expected output above appears and the command exits 0.

4. Only proceed when the diff matches the intended change and nothing else.

   Success check: the expected output above appears and the command exits 0.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Workflow: schema diff as an approval gate

## Goal

## Ordering constraints

- Diff before the operation, not after; after is an autopsy.

## Traps

- Data-only changes do not show in a schema diff; pair it with row-count checks for restores.
- Auto-generated migration diffs can hide destructive steps inside friendly names; read the actual DDL.

## Verify


---

Source: [Vectle](https://vectle.com/skills/skl_AtS-ZDE7V8F--9_KOfNmHg). Version: `skv_1TpXmPNaqRkjGLQ9sXVDEA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
