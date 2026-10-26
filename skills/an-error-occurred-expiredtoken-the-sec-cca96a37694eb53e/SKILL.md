---
name: "an-error-occurred-expiredtoken-the-sec-cca96a37694eb53e"
description: "Fixes the AWS CLI ExpiredToken error where temporary credentials (SSO, STS, or IAM role sessions) have passed their expiration. Use when aws commands fail with 'The security token included in the request is expired'. Not for InvalidClientTokenId (wrong keys) or AccessDenied (permissions)."
metadata:
  skill_id: "skl_T-6Q-lW4_i3_XICknVq_Og"
  title: "An error occurred (ExpiredToken): The security token included in the request is expired"
  version: "skv_i2DfCdZmYmYmslDVd1UzoA"
  updated: "2026-10-03T05:35:08.018086+00:00"
  canonical_url: "https://vectle.com/skills/skl_T-6Q-lW4_i3_XICknVq_Og"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://towardsthecloud.com/blog/aws-cli-switch-profiles\"]"
---

Your temporary AWS credentials ran out. Run `aws sso login --profile your-profile` to get a fresh session, then retry the command. If you are not on SSO, mint new temporary credentials (STS) or re-export fresh ones. The error is expected behavior, not a misconfiguration.

```text
An error occurred (ExpiredToken) when calling the ListBuckets operation: The security token included in the request is expired
```

## Fix

1. If you use AWS IAM Identity Center (SSO), refresh the session:
   ```bash
   aws sso login --profile your-profile
   ```
   Expected: a browser window opens, you approve, and the CLI prints `Successfully logged into Start URL`.

2. Verify the fresh identity works:
   ```bash
   aws sts get-caller-identity --profile your-profile
   ```
   Expected: JSON with your UserId, Account, and Arn. No error.

3. If you use STS temporary credentials (not SSO), get new ones and update `~/.aws/credentials` or your env vars, then retry.

4. If ExpiredToken appears *immediately* after a successful `aws sso login`, stale environment variables are overriding your profile. Check:
   ```bash
   env | grep AWS_
   ```
   If `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, or `AWS_SESSION_TOKEN` are set, unset them:
   ```bash
   unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
   ```
   Expected: `aws sts get-caller-identity --profile your-profile` now works.

## When this applies
- Any `aws` command fails with `(ExpiredToken)` and `The security token included in the request is expired`.
- You use `aws sso login`, assumed roles, `get-session-token`, or EC2/ECS task roles with cached creds.

## When it does NOT apply
- `InvalidClientTokenId` or `InvalidAccessKeyId`: those mean the keys are wrong or revoked, not expired. Re-enter credentials with `aws configure`.
- `AccessDenied`: the credentials are valid but lack permission. That is an IAM policy problem.
- `Unable to locate credentials`: nothing is configured at all.

## Compatibility
- AWS CLI v2 (all recent versions). SSO flow requires CLI v2; `aws configure sso` is not a v1 command.

## Why it happens
Temporary credentials have a fixed lifetime. SSO sessions typically last 8-12 hours, assumed-role sessions 1-12 hours depending on configuration. When the clock runs out, every API call fails with ExpiredToken until you re-authenticate. The CLI caches role credentials in `~/.aws/cli/cache`, so a revoked or expired cached session can also linger there.

## Edge cases
- Clock skew: if your system clock is far off, tokens can look expired early. Sync with NTP.
- CI jobs longer than the session duration: refresh mid-job or use a longer session duration on the role.
- `rm -r ~/.aws/cli/cache` forces the CLI to drop cached role credentials and fetch fresh ones.

---

Source: [Vectle](https://vectle.com/skills/skl_T-6Q-lW4_i3_XICknVq_Og). Version: `skv_i2DfCdZmYmYmslDVd1UzoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
