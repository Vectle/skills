---
name: "supabase-cli-failed-sasl-auth-invalid-f4bb9525bcb8054e"
description: "Fixes the Supabase CLI failing with failed SASL auth (invalid SCRAM server-final-message received from server) on db push/pull. Use when pooler connections fail while direct connections work, or right after a password change or special-character password. Switches to the direct connection or URL-encodes the password. Not for plain wrong-password errors or network timeouts."
metadata:
  skill_id: "skl_CUzO2XtKFUEdDUISG_RULQ"
  title: "Supabase CLI: failed SASL auth (invalid SCRAM server-final-message received from server)"
  version: "skv_TEIAXLbKKEr0-J6wChyL8g"
  updated: "2026-10-03T05:38:45.71109+00:00"
  canonical_url: "https://vectle.com/skills/skl_CUzO2XtKFUEdDUISG_RULQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://supabase.com/docs/guides/troubleshooting/supabase-cli-failed-sasl-auth-or-invalid-scram-server-final-message\"]"
---

# Supabase CLI: failed SASL auth (invalid SCRAM server-final-message received from server)

TL;DR: the SCRAM handshake is breaking, which usually means the connection is going through the pooler (Supavisor) in the wrong mode, or the password has special characters that were not URL-encoded in the connection string. Use the direct database connection instead of the pooler URL for db push/pull, or re-encode the password. If you changed the DB password recently, update the stored password everywhere the CLI reads it.

```text
failed SASL auth (invalid SCRAM server-final-message received from server)
```

## Steps

1. Find which connection string the CLI uses: check for a pooler host (port 6543) vs the direct host (port 5432). Switch db push/pull to the direct connection string.

2. If the password contains characters like @, #, %, or /, URL-encode them in the connection string. Expected: the SASL error disappears on the next attempt.

3. If you recently reset the database password, update it in the CLI config and in any stored connection string, then retry.

4. Still failing: confirm the plain password works via the dashboard SQL editor. If it works there, the issue is the connection string, not the credential.

## When this applies

- the exact `failed SASL auth (invalid SCRAM server-final-message received from server)` message
- db push / db pull failing right after a password reset or when the password has special characters
- pooler (port 6543) connections failing while direct (port 5432) works

## When it doesn't

- `password authentication failed for user postgres` — the password itself is wrong, fix that first
- connection timeouts / DNS failures reaching the host
- RLS or permission errors after connecting successfully

## Compatibility

Supabase CLI db push/pull; Supavisor pooler (transaction/session modes) and direct Postgres connections. Verified against the Supabase CLI troubleshooting docs.

## Variant phrasings

- supabase failed SASL auth invalid SCRAM
- supabase cli scram server final message
- supabase pooler SASL auth failed fix

## Root cause

SCRAM authentication hashes the password on both sides; if the client sends a password mangled by URL parsing (unencoded special chars) or talks SCRAM to an endpoint expecting a different flow, the server's final message does not verify and the handshake aborts.

## Edge cases

- transaction-mode pooler plus prepared statements is a separate failure class; use session mode for migrations
- passwords changed in the dashboard take a moment to propagate; retry before rebuilding strings
- storing the raw connection string in shell history leaks the password; prefer env files with tight perms

---

Source: [Vectle](https://vectle.com/skills/skl_CUzO2XtKFUEdDUISG_RULQ). Version: `skv_TEIAXLbKKEr0-J6wChyL8g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
