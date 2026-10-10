---
name: "neonctl-org-scoped-api-key-vs-user-sco-04d186c865045b4c"
description: "Explains neonctl permission failures from using the wrong API key scope. Use when commands fail with authorization errors even though the key is valid, especially across multiple projects or an org. Picks a user-scoped key for broad access or an org-scoped key for least privilege, and matches the key to the job. Not for invalid-key 401s."
metadata:
  skill_id: "skl_DcUZpnxxdu7HrW8EWgGwiA"
  title: "neonctl: org-scoped API key vs user-scoped API key"
  version: "skv_TFCTqxNnadnuQkroqW7gaw"
  updated: "2026-10-03T05:56:20.410263+00:00"
  canonical_url: "https://vectle.com/skills/skl_DcUZpnxxdu7HrW8EWgGwiA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# neonctl: org-scoped API key vs user-scoped API key

TL;DR: Neon issues API keys at different scopes: user-scoped keys act with your full account access, while org-scoped keys are limited to that organization. An org-scoped key used against a personal project (or the wrong org) fails authorization even though the key is valid. Check which scope your key has in the console, then use a user-scoped key for cross-org work or generate an org-scoped key inside the right org for least-privilege automation.

```text
neonctl authorization failures with a valid API key (wrong scope)
```

## Steps

1. In the Neon console, check the key's scope: user-level or organization-level.

2. If the command targets projects outside the key's org, switch to a user-scoped key (or a key scoped to the correct org).

3. For CI limited to one org's projects, prefer an org-scoped key from that org: least privilege, and a leak is contained.

4. Re-authenticate with the correctly scoped key and rerun. Expected: authorization succeeds.

## When this applies

- `not authorized` / permission errors with a key that passes the 401 check
- automation touching projects across multiple orgs
- choosing key scope for a new CI integration

## When it doesn't

- `Authentication failed` — the key is invalid, scope is irrelevant
- project-not-found for a project that genuinely does not exist
- SSO/browser login issues

## Compatibility

neonctl; Neon console API key scopes (user vs organization). Verified against the neon-pkgs agent notes.

## Variant phrasings

- neonctl org scoped api key
- neon api key scopes user vs org
- neonctl not authorized valid key

## Root cause

Authorization is checked against both key validity and key scope. A valid org-scoped key simply has no rights outside its org, so cross-org calls fail at the authorization layer with no hint that scope (not the key) is the problem.

## Edge cases

- a user-scoped key is powerful; store it as carefully as a password
- leaving an org can silently break automations built on your user-scoped key; prefer org keys for shared CI
- key scope is set at creation; you cannot widen a key later, only create a new one

---

Source: [Vectle](https://vectle.com/skills/skl_DcUZpnxxdu7HrW8EWgGwiA). Version: `skv_TFCTqxNnadnuQkroqW7gaw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
