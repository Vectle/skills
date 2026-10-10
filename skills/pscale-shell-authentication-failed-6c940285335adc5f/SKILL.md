---
name: "pscale-shell-authentication-failed-6c940285335adc5f"
description: "Fixes pscale shell failing with Authentication failed. Use when the PlanetScale CLI rejects your session even though you logged in before. Logs out and back in with pscale auth to refresh the expired token. Not for database-not-found errors or wrong-branch failures."
metadata:
  skill_id: "skl_g_GmAeL7lOn0u2tsTMNlYQ"
  title: "pscale shell: Authentication failed"
  version: "skv_SxGEucDNvJdbfhqwPvdCeg"
  updated: "2026-10-03T05:57:02.787903+00:00"
  canonical_url: "https://vectle.com/skills/skl_g_GmAeL7lOn0u2tsTMNlYQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# pscale shell: Authentication failed

TL;DR: your CLI session token expired or was revoked. Run `pscale auth logout` to clear the stale session, then `pscale auth login` to start a fresh browser login. Once the new session is stored, `pscale shell` connects again.

```text
Authentication failed
```

## Steps

1. Run `pscale auth logout`. Expected: the CLI confirms you are logged out and clears the session.

2. Run `pscale auth login` and complete the browser flow.

3. Rerun `pscale shell`. Expected: the MySQL shell opens instead of the auth error.

4. If it still fails, check the account still has access to the org/database — removed users get auth failures, not permission errors.

## When this applies

- the exact `Authentication failed` message on pscale shell
- sessions that worked last week and fail today
- CLI use after a password or SSO change on the PlanetScale account

## When it doesn't

- `database not found` — auth worked, the name is wrong
- branch or keyspace errors inside an open shell
- CI environments, which should use service tokens not browser login

## Compatibility

pscale CLI; pscale auth login/logout; browser-based session tokens. Verified against the pscale-database community skill.

## Variant phrasings

- pscale shell authentication failed
- planetscale cli authentication failed fix
- pscale auth logout login

## Root cause

pscale stores a session token from the browser login; tokens expire and are revoked on credential changes. The CLI cannot refresh it silently, so the explicit logout/login cycle is the supported reset.

## Edge cases

- `pscale auth login` needs a browser; on headless machines use service tokens
- logging out kills all pscale sessions on that machine, including scripts
- after SSO changes, old sessions die immediately; re-login before debugging further

---

Source: [Vectle](https://vectle.com/skills/skl_g_GmAeL7lOn0u2tsTMNlYQ). Version: `skv_SxGEucDNvJdbfhqwPvdCeg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
