---
name: "an-error-occurred-invalidclienttokenid-ec8e9a3ceb7a83c9"
description: "Fixes the AWS CLI InvalidClientTokenId error, meaning the access key is wrong, revoked, or belongs to a different account. Use when the error says 'The security token included in the request is invalid'. The fix is re-entering correct credentials, not refreshing a session. Not for ExpiredToken."
metadata:
  skill_id: "skl_SjHSAOv3yum_Tt7lKSnmuA"
  title: "An error occurred (InvalidClientTokenId): The security token included in the request is invalid"
  version: "skv_at6DDpqYSmA9OgTpwc5q6w"
  updated: "2026-10-03T05:56:43.081983+00:00"
  canonical_url: "https://vectle.com/skills/skl_SjHSAOv3yum_Tt7lKSnmuA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Your access key is wrong, deleted, or from a different account. Re-enter credentials with `aws configure --profile my-profile` (or regenerate the key pair in the IAM console first if the key was deleted or deactivated). This is not a session expiry, so `aws sso login` alone will not help unless you are on SSO.

```text
An error occurred (InvalidClientTokenId) when calling the ListBuckets operation: The security token included in the request is invalid.
```

## Fix

1. Confirm which identity is actually being used:
   ```bash
   aws sts get-caller-identity --profile my-profile
   ```
   Expected on success: your UserId, Account, Arn. If this fails, the credentials for that profile are bad.

2. Check the obvious: open `~/.aws/credentials` and look for copy/paste damage (trailing spaces, truncated keys, keys pasted into the wrong profile section).

3. If the key was deleted or deactivated in IAM, create a fresh access key pair in the IAM console, then:
   ```bash
   aws configure --profile my-profile
   ```
   Paste the new key ID and secret when prompted. Expected: `aws sts get-caller-identity --profile my-profile` succeeds.

4. If you are on SSO rather than static keys, re-authenticate instead:
   ```bash
   aws sso login --profile my-profile
   ```

## When this applies
- The error is `(InvalidClientTokenId)` with `The security token included in the request is invalid`.
- Commands worked before and broke after a key rotation, or never worked with these keys.

## When it does NOT apply
- `ExpiredToken`: the key is fine, the temporary session lapsed. Refresh the session.
- `SignatureDoesNotMatch`: the secret is wrong but the key ID exists. Re-enter the secret carefully.
- `AccessDenied`: credentials are valid, permissions are missing.

## Compatibility
- AWS CLI v1 and v2.

## Why it happens
AWS cannot find the access key ID in its records for the target account. Usual causes: the key was deleted or deactivated, it belongs to a different account than the one being called, or it was mistyped during `aws configure`.

## Edge cases
- `AWS_ACCESS_KEY_ID` env vars override the credentials file; a stale exported key produces this error even with a correct file. Check `env | grep AWS_`.
- Keys are per-account: a key from account A used against account B resources fails this way.
- After `aws configure`, old sessions cached in `~/.aws/cli/cache` can linger; clear the cache if the error persists with fresh keys.

---

Source: [Vectle](https://vectle.com/skills/skl_SjHSAOv3yum_Tt7lKSnmuA). Version: `skv_at6DDpqYSmA9OgTpwc5q6w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
