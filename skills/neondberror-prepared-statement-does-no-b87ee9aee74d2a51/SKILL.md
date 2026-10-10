---
name: "neondberror-prepared-statement-does-no-b87ee9aee74d2a51"
description: "Serverless: neonDbError: prepared statement does not exist. The verified fix is Fixed server-side; reporter confirmed no failures on the new version, rolling out with the weekly compute release. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl_TK9NzkmxbKl_OmBnjEC6gg"
  title: "NeonDbError: prepared statement does not exist"
  version: "skv_6iP4y4KSS75slI_AY1mBAA"
  updated: "2026-10-03T06:06:59.839214+00:00"
  canonical_url: "https://vectle.com/skills/skl_TK9NzkmxbKl_OmBnjEC6gg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fixed server-side; reporter confirmed no failures on the new version, rolling out with the weekly compute release. No SDK change needed.

## The error

```text
However when performing multiple calls in parallel, the request sometimes fails with the following errors:
error: NeonDbError: prepared statement "s257" does not exist
```

## Fix

1. Fixed server-side; reporter confirmed no failures on the new version, rolling out with the weekly compute release.
2. No SDK change needed.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in serverless.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in serverless, even a similar-looking one.
- General serverless setup or credential questions.

## Compatibility

- Serverless (neondatabase/serverless)

## Variant phrasings

- How to fix "neonDbError: prepared statement does not exist" in serverless
- serverless: neonDbError: prepared statement does not exist

## Root cause

[conradludgate (Neon proxy engineer)]: Root cause found in Neon's proxy code: for RLS the proxy runs 'discard all' between user sessions for security, which discarded the cached prepared statements the proxy uses for Postgres type mapping of enum/composite types.

## Edge cases

- [conradludgate (Neon proxy engineer)]: Root cause found in Neon's proxy code: for RLS the proxy runs 'discard all' between user sessions for security, which discarded the cached prepared statements the proxy uses for Postgres type mapping of enum/composite types.

## Source

- https://github.com/neondatabase/serverless/issues/144

---

Source: [Vectle](https://vectle.com/skills/skl_TK9NzkmxbKl_OmBnjEC6gg). Version: `skv_6iP4y4KSS75slI_AY1mBAA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
