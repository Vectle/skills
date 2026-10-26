---
name: "the-token-in-default-is-invalid-to-re-3494ecfac520dbe8"
description: "Fixes 'The token in default is invalid' from the gh CLI by re-running gh auth login for the host. Use when stored gh credentials expire or are revoked. Not for env-var-overridden auth or scope errors."
metadata:
  skill_id: "skl_Y6rNnN6CP16crmjNFVfomQ"
  title: "The token in default is invalid. To re-authenticate, run: gh auth login -h github.com"
  version: "skv_1FFXBocoE_U6XkXQJiZx6Q"
  updated: "2026-10-03T05:57:25.29379+00:00"
  canonical_url: "https://vectle.com/skills/skl_Y6rNnN6CP16crmjNFVfomQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/genxsirai/jloop/blob/HEAD/cron-headless-github-auth.md\"]"
---

Your stored gh token stopped working (expired or revoked). Run gh auth login -h github.com and complete the login flow again. Takes a minute and every gh command starts working again.

```text
The token in default is invalid. To re-authenticate, run: gh auth login -h github.com
```

## Fix it
1. Run gh auth status to confirm which account and host is broken.
   Success check: The failing host shows the invalid-token message.
2. Run gh auth login -h github.com (or your enterprise hostname).
   Success check: The interactive login or device-code flow starts.
3. Complete the browser or device-code authorization.
   Success check: gh prints that authentication succeeded.
4. Re-run the command that failed.
   Success check: No more invalid-token error.

## When this applies
- gh prints 'The token in default is invalid'
- gh auth status shows the account but commands fail

## When this does NOT apply
- a GH_TOKEN or GITHUB_TOKEN env var is set (that overrides stored auth; unset it instead)
- the error is about scopes rather than validity

## Compatibility
gh CLI 2.x on macOS, Linux, Windows. github.com and GHES hostnames.

## Why it happens
gh stores OAuth tokens in the system keyring or config file. Tokens expire, get revoked by an admin, or die when SSO sessions lapse. gh detects the dead token on the next API call and tells you exactly how to replace it.

## Edge cases
- If GH_TOKEN is set in the environment, gh never reads the keyring, so re-logging in changes nothing until you unset it.
- On shared machines, make sure you re-authenticate the right account: gh auth login has no --user flag, it binds whoever approves in the browser.
- After re-auth, run gh auth setup-git if git operations also need the new credential.

Source: https://github.com/genxsirai/jloop/blob/HEAD/cron-headless-github-auth.md

---

Source: [Vectle](https://vectle.com/skills/skl_Y6rNnN6CP16crmjNFVfomQ). Version: `skv_1FFXBocoE_U6XkXQJiZx6Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
