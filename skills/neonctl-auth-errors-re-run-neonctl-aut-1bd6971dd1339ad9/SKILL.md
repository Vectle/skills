---
name: "neonctl-auth-errors-re-run-neonctl-aut-1bd6971dd1339ad9"
description: "Fixes recurring neonctl auth errors caused by stale cached credentials. Use when commands that used to work start failing auth with no config change, or after switching Neon accounts. Clears the stale credential cache with a fresh neonctl auth. Not for first-time setup or revoked API keys."
metadata:
  skill_id: "skl_vWO_vmqsBGB6LaLOJhqqlQ"
  title: "neonctl auth errors: re-run neonctl auth to re-authenticate"
  version: "skv_fgaiqD6Xnsk3LKYZ8SG3hA"
  updated: "2026-10-03T05:55:37.900121+00:00"
  canonical_url: "https://vectle.com/skills/skl_vWO_vmqsBGB6LaLOJhqqlQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/rev4nchist/continuous-claude-v3/blob/HEAD/.claude/skills/neonctl/SKILL.md\"]"
---

# neonctl auth errors: re-run neonctl auth to re-authenticate

TL;DR: neonctl caches credentials locally, and the cache goes stale when keys rotate, accounts switch, or sessions expire. Re-run `neonctl auth` to redo the login flow and overwrite the cache with fresh credentials. If errors persist, delete the cached credential files so nothing stale survives, then authenticate again.

```text
neonctl auth errors after previously working
```

## Steps

1. Run `neonctl auth` and complete the login flow. Expected: the CLI confirms the new authentication.

2. Rerun the failing command. Expected: auth succeeds.

3. Still failing: remove the cached credentials (the CLI's local credential store) and run `neonctl auth` once more from clean state.

4. If you switched accounts, confirm the new login matches the account that owns the target project.

## When this applies

- auth errors appearing with no config change on a previously working setup
- failures right after switching Neon accounts in the browser
- `Authentication failed` that survives a key check (the cache may hold the old key)

## When it doesn't

- first-time setup where no credentials were ever stored
- keys revoked server-side — re-auth with the same dead key changes nothing
- CI environments, which should use NEON_API_KEY instead of cached auth

## Compatibility

neonctl; the local credential cache; neonctl auth. Verified against the community neonctl skill notes.

## Variant phrasings

- neonctl re-authenticate
- neonctl auth errors fix
- neonctl stale credentials

## Root cause

The CLI reads credentials from its local cache first. When the cached value no longer matches the account state (rotation, expiry, account switch), every call fails until the cache is refreshed — the config files you keep checking were never the problem.

## Edge cases

- two CLIs (neon vs neonctl) can keep separate caches; fix the one you actually invoke
- NEON_API_KEY in the environment overrides the cache, which can mask a stale cache locally
- on shared machines, the cache belongs to the OS user; sudo runs see a different one

---

Source: [Vectle](https://vectle.com/skills/skl_vWO_vmqsBGB6LaLOJhqqlQ). Version: `skv_fgaiqD6Xnsk3LKYZ8SG3hA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
