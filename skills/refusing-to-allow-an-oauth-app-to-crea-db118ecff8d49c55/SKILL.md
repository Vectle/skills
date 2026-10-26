---
name: "refusing-to-allow-an-oauth-app-to-crea-db118ecff8d49c55"
description: "Fixes the git push rejection 'refusing to allow an OAuth App to create or update workflow'. Use when a push over HTTPS fails only on .github/workflows files. Not for SSH push failures or general 403s."
metadata:
  skill_id: "skl_sGzoChr8h26Bx1KCSKssQw"
  title: "refusing to allow an OAuth App to create or update workflow on git push"
  version: "skv_FFIi9xTLliKEuO0y27C--A"
  updated: "2026-10-03T06:11:48.239325+00:00"
  canonical_url: "https://vectle.com/skills/skl_sGzoChr8h26Bx1KCSKssQw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/64059610/how-to-resolve-refusing-to-allow-an-oauth-app-to-create-or-update-workflow-on\"]"
---

TL;DR: Regenerate your personal access token with the workflow scope checked, then push again with the new token. GitHub refuses to let any OAuth token touch files under .github/workflows unless the token carries the workflow scope, so a token that works everywhere else still gets rejected on workflow files.

```text
refusing to allow an OAuth App to create or update workflow
```

## The fix

1. Create a new token with the workflow scope. For a classic PAT, tick the workflow checkbox. For a fine-grained PAT, grant Actions read and write on the repo.
   Expected: The token summary lists the workflow scope.

2. Clear the cached credential so git asks for the new token on the next push, then paste the new token when prompted.
   ```bash
   printf 'protocol=https\nhost=github.com\n' | git credential reject
   ```
   Expected: The next git push prompts for a username and password; the push completes.

3. Push again.
   ```bash
   git push origin main
   ```
   Expected: The push completes instead of the refusing error.

## When this applies

- git push over HTTPS fails only when the push includes .github/workflows files
- you authenticate with a personal access token or OAuth app token

## When it does NOT apply

- the push has no workflow files (then it is a different auth problem)
- you push over SSH (scopes do not apply there)

## Compatibility

GitHub.com and GitHub Enterprise Server. Applies to PAT classic, fine-grained PATs, and OAuth app tokens used for git over HTTPS.

## Variants of this error

### `refusing to allow an OAuth App to create or update workflow without `workflow` scope`
Same error with the missing scope named. Same fix: reissue the token with that scope.

## Why it happens

Workflow files can execute arbitrary code with access to repository secrets, so GitHub treats them as privileged. The workflow scope is a separate opt-in so a compromised token cannot silently install a secret-stealing workflow.

## Edge cases and pitfalls

- If a CI system or password manager holds the old token, rotate it there too or the next push fails the same way.
- Fine-grained PATs do not have a checkbox literally named workflow; use Actions read and write permissions.
- Inside Actions itself, GITHUB_TOKEN already has workflow-file access in its own repo; this error is about pushing from your machine.

---

Source: [Vectle](https://vectle.com/skills/skl_sGzoChr8h26Bx1KCSKssQw). Version: `skv_FFIi9xTLliKEuO0y27C--A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
