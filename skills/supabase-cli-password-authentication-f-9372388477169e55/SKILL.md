---
name: "supabase-cli-password-authentication-f-9372388477169e55"
description: "Fixes the Supabase CLI failing with password authentication failed for user \"postgres\". Use when supabase db push, supabase db pull, or link-time database operations fail on the postgres password while the CLI login itself works. Resets or corrects the database password and makes sure the CLI reads the current one. Not for Supabase dashboard login failures or pooler SCRAM handshake errors."
metadata:
  skill_id: "skl_FoiZ07jiYrn6NOJixuaOCg"
  title: "Supabase CLI: password authentication failed for user \"postgres\""
  version: "skv_52_DmARbgRuFeVadcmZYvQ"
  updated: "2026-10-03T05:39:36.221199+00:00"
  canonical_url: "https://vectle.com/skills/skl_FoiZ07jiYrn6NOJixuaOCg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sandeepsingh61935/_underscore/blob/HEAD/supabase/migrations/README.md\"]"
---

# Supabase CLI: password authentication failed for user "postgres"

TL;DR: the database password the CLI is using does not match the project's current DB password. Reset the database password in the Supabase dashboard (project settings > database), then update wherever the CLI reads it: the linked config and any PGPASSWORD or SUPABASE_DB_PASSWORD-style env var. This is the database password, not your dashboard login password — they are different.

```text
password authentication failed for user "postgres"
```

## Steps

1. Reset the database password in the Supabase dashboard under project settings > database. Copy the new password.

2. Update every place the CLI reads it: the stored link config and any password env var in your shell or .env file. Expected: no stale value remains.

3. Rerun the failing command (`supabase db push` or `supabase db pull`). Expected: authentication succeeds and the operation proceeds.

4. Still failing: verify you are pushing to the right project ref — a password from project A never works on project B.

## When this applies

- the exact `password authentication failed for user "postgres"` message on db push/pull
- password resets that were done in the dashboard but never updated in the CLI env
- a project that was paused and restored (passwords can be reset on restore)

## When it doesn't

- dashboard sign-in failures — that is your account password, not the DB password
- SCRAM handshake errors through the pooler (different failure, different fix)
- permission-denied errors after connecting — auth already succeeded

## Compatibility

Supabase CLI; dashboard database settings for password reset. Verified against the community Supabase migrations guide.

## Variant phrasings

- supabase password authentication failed for user postgres
- supabase db push password authentication failed
- supabase cli database password wrong

## Root cause

Postgres checks the password presented at connection time against pg_authid. The CLI's stored value goes stale whenever the dashboard password is reset, and the two passwords (dashboard login vs database) are independent, so fixing the wrong one changes nothing.

## Edge cases

- the dashboard login password and the database password are different; resetting one does not fix the other
- special characters in the new password must be URL-encoded in connection strings
- after a restore from backup, re-check which password is current

---

Source: [Vectle](https://vectle.com/skills/skl_FoiZ07jiYrn6NOJixuaOCg). Version: `skv_52_DmARbgRuFeVadcmZYvQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
