---
name: "aws-sso-login-succeeds-but-every-comma-22bab400c02c20a8"
description: "Fixes the maddening case where aws sso login succeeds but every command still fails with ExpiredToken. Use when the login flow completes yet the error persists. The cause is stale AWS_ environment variables overriding the fresh SSO session. Not for genuinely expired sessions."
metadata:
  skill_id: "skl_BrGw-7x6pz_Z6mRCFw0e5g"
  title: "aws sso login succeeds but every command still fails with ExpiredToken"
  version: "skv_k8WLC2sgMIEgzxaQn6fFcw"
  updated: "2026-10-03T06:00:27.740254+00:00"
  canonical_url: "https://vectle.com/skills/skl_BrGw-7x6pz_Z6mRCFw0e5g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/matthewduke1/aws-onboarding/blob/HEAD/reference/troubleshooting.md\"]"
---

The login worked, but stale `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN` environment variables are overriding your fresh SSO session. Run `unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN`, then retry. Env vars always beat the config file.

```text
An error occurred (ExpiredToken) when calling the ListBuckets operation: The security token included in the request is expired
```

(The twist: you JUST ran `aws sso login` successfully and it still fails.)

## Fix

1. Check for overriding env vars:
   ```bash
   env | grep AWS_
   ```
   Expected culprits: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` set to old values.

2. Unset them (do not set them to empty strings):
   ```bash
   unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
   ```
   Expected: `env | grep AWS_` no longer shows them.

3. Retry with the profile:
   ```bash
   aws sts get-caller-identity --profile your-profile
   ```
   Expected: success, using the fresh SSO session.

4. Make it permanent: remove the exports from `~/.bashrc`, `~/.zshrc`, or your IDE's env config so new shells do not reintroduce the stale keys.

## When this applies
- `aws sso login` completes successfully but commands immediately fail with `ExpiredToken`.
- `aws configure list` shows credentials coming from `env` rather than the profile.

## When it does NOT apply
- The SSO session is genuinely expired (hours old): just `aws sso login` again.
- `InvalidClientTokenId`: the keys themselves are wrong, not merely stale.

## Compatibility
- AWS CLI v1 and v2. The env-over-file precedence is the same in both.

## Why it happens
The CLI's credential precedence is: env vars first, then config/credentials files, then SSO cache. `aws sso login` refreshes the cache, but if your shell exports old keys, the CLI never looks at the fresh session. This commonly comes from a `.bashrc` export added months ago for a different task.

## Edge cases
- `AWS_PROFILE` set to an empty string is a separate trap (`The config profile () could not be found`); `unset` it too if present.
- Tools like direnv or IDE run configs can inject these vars invisibly; check those if `env` looks clean in your terminal but the error persists in the tool.

---

Source: [Vectle](https://vectle.com/skills/skl_BrGw-7x6pz_Z6mRCFw0e5g). Version: `skv_k8WLC2sgMIEgzxaQn6fFcw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
