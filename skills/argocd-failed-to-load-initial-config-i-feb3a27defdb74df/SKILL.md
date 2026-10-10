---
name: "argocd-failed-to-load-initial-config-i-feb3a27defdb74df"
description: "Routes argocd CLI corrupt-config failures. Use when every argocd command fails with failed to load initial config (invalid character / unexpected end of JSON). Not for auth or TLS errors."
metadata:
  skill_id: "skl_gGfuU63ixRq9fX_0H4WzgQ"
  title: "argocd: failed to load initial config: invalid character"
  version: "skv_nXBF67zcB16IuoezyAofjQ"
  updated: "2026-10-03T16:26:38.359604+00:00"
  canonical_url: "https://vectle.com/skills/skl_gGfuU63ixRq9fX_0H4WzgQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

The CLI config file at ~/.config/argocd/config got truncated or corrupted (killed write, disk-full, bad merge) - every command fails parsing it before doing anything. Move it aside and log in again; argocd recreates a clean config. Your clusters and servers are unaffected - only the local session cache is rebuilt.

## The error
```text
FATA[0000] failed to load initial config: invalid character 'x' looking for beginning of value
```

## What to do
1. Quarantine the broken file:
```bash
mv ~/.config/argocd/config ~/.config/argocd/config.broken
```
   Expected: No output.
2. Log in fresh:
```bash
argocd login [server] --grpc-web --username [user]
```
   Expected: Login succeeds; clean config written.
3. Re-add any other server contexts you used.
   Expected: All contexts restored.
4. Optional: diff the broken file to learn what corrupted it, then delete it.
   Expected: Cleanup done.

## When this applies
- the exact failed to load initial config message
- every argocd command failing identically
- after disk-full or killed-write incidents

## When it does NOT apply
- single commands failing (not a config parse issue)
- login failures with valid config (auth problem)

## Works with
argocd CLI 2.x/3.x

### failed to load initial config: unexpected end of JSON input
Same corruption, truncated file. Same move-aside fix.

## Why it happens
The CLI loads its JSON config on every invocation before parsing flags. A partially written file fails the JSON parse, and the error surfaces before any command logic runs.

## Edge cases
- Back up the config before bulk edits or disk-cleanup scripts touch ~/.config.
- Multiple contexts live in the one file - note which servers you used before deleting it.

## Resolved from
computingforgeeks argocd login guide - https://computingforgeeks.com/argocd-cli-login-authentication/

---

Source: [Vectle](https://vectle.com/skills/skl_gGfuU63ixRq9fX_0H4WzgQ). Version: `skv_nXBF67zcB16IuoezyAofjQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
