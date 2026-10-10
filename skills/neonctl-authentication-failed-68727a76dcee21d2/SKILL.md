---
name: "neonctl-authentication-failed-68727a76dcee21d2"
description: "Fixes neonctl failing with Authentication failed. Use when neon/neonctl commands reject your credentials even though the key looks right. Replaces a revoked or expired API key with a fresh one from the Neon console and re-authenticates. Not for project-not-found errors or network failures."
metadata:
  skill_id: "skl_oYpU0ncbG2IkIcEzPZtC7g"
  title: "neonctl: Authentication failed"
  version: "skv_CyRIp5_5Qz63FzVgE8E4jQ"
  updated: "2026-10-03T05:53:12.054977+00:00"
  canonical_url: "https://vectle.com/skills/skl_oYpU0ncbG2IkIcEzPZtC7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# neonctl: Authentication failed

TL;DR: the API key neonctl is sending is revoked, expired, or belongs to a different account. Generate a new API key in the Neon console (account settings > API keys), store it with `neonctl auth` or as NEON_API_KEY, and retry. Do not keep retrying the old key — a 401 never turns into a 200 on retry.

```text
Authentication failed
```

## Steps

1. In the Neon console, open account settings > API keys and create a new key. Copy it immediately.

2. Authenticate the CLI: run `neonctl auth` and paste the new key, or export NEON_API_KEY with the new value. Expected: the CLI confirms authentication.

3. Rerun the failing command. Expected: it executes instead of failing auth.

4. If it still fails, confirm you are using the key from the right Neon account — keys from account A never work when the CLI targets account B's project.

## When this applies

- the exact `Authentication failed` message from neon/neonctl
- a key that worked yesterday and fails today (rotated or revoked)
- keys copied with a trailing space or newline

## When it doesn't

- `project not found` or `branch not found` — auth succeeded, the resource is the problem
- network/DNS errors reaching the Neon API
- browser-based OAuth flows hanging (use the API-key path here instead)

## Compatibility

neonctl; Neon console API keys; NEON_API_KEY env var. Verified against the neonctl community issue thread.

## Variant phrasings

- neonctl authentication failed fix
- neonctl api key invalid
- neon cli auth failed

## Root cause

The Neon API checks the presented key on every call; revoked or mistyped keys fail with a flat Authentication failed. Because the check is stateless, retrying or waiting never helps — only a valid key does.

## Edge cases

- console keys show once at creation; if you lost it, create a new one instead of hunting
- revoke the old key after replacing it so a leaked copy dies
- service accounts and personal keys have different scopes; match the key to the job

---

Source: [Vectle](https://vectle.com/skills/skl_oYpU0ncbG2IkIcEzPZtC7g). Version: `skv_CyRIp5_5Qz63FzVgE8E4jQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
