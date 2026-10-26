---
name: "the-sso-session-associated-with-this-p-2df601c7d0d95736"
description: "Fixes the AWS CLI SSO session expiry error. Use when aws commands fail with 'The SSO session associated with this profile has expired or is otherwise invalid'. The fix is aws sso login for the profile (or the sso-session). Not for ExpiredToken on STS creds or InvalidClientTokenId."
metadata:
  skill_id: "skl_4f9iF9wrIP0g2Yr-AXbjog"
  title: "The SSO session associated with this profile has expired or is otherwise invalid"
  version: "skv_2qMpcNk35fdXk59j6p-f2A"
  updated: "2026-10-03T05:53:11.856489+00:00"
  canonical_url: "https://vectle.com/skills/skl_4f9iF9wrIP0g2Yr-AXbjog"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://towardsthecloud.com/blog/aws-cli-switch-profiles\"]"
---

Your IAM Identity Center session ended. Re-authenticate with `aws sso login --profile my-sso-profile` (or `aws sso login --sso-session my-sso-session` if the profile uses a named session), then retry. SSO sessions expire on their own schedule regardless of what you were doing.

```text
The SSO session associated with this profile has expired or is otherwise invalid. Please run `aws sso login` to refresh your session.
```

## Fix

1. Re-authenticate:
   ```bash
   aws sso login --profile my-sso-profile
   ```
   Expected: browser opens, you approve access, CLI prints a success message.

2. If your config uses a named `sso-session` block, refresh the session itself:
   ```bash
   aws sso login --sso-session my-sso-session
   ```
   Expected: same browser approval flow; all profiles sharing that session start working.

3. Verify:
   ```bash
   aws sts get-caller-identity --profile my-sso-profile
   ```
   Expected: your UserId, Account, and Arn as JSON.

## When this applies
- The error names the SSO session as expired or invalid.
- You authenticate via AWS IAM Identity Center (formerly SSO), with `sso_start_url` in `~/.aws/config`.

## When it does NOT apply
- `ExpiredToken` without SSO wording: refresh STS/role credentials instead.
- `aws configure sso is not a valid command`: you are on CLI v1, upgrade to v2.
- The browser never opens on a headless box: use device-code flow or run `aws sso login` where you have a browser, then copy `~/.aws/sso/cache`.

## Compatibility
- AWS CLI v2 only. Requires an IAM Identity Center instance.

## Why it happens
The SSO token cached in `~/.aws/sso/cache` has a limited lifetime (often 8-12 hours, set by the Identity Center admin). Once it lapses, the CLI cannot mint role credentials for any profile tied to that session until you log in again.

## Edge cases
- Multiple profiles can share one `sso-session`; refreshing the session fixes all of them at once.
- Adding `sso_registration_scopes = sso:account:access` to the session block enables automatic token refresh and cuts down on re-logins.
- Deleting `~/.aws/sso/cache` forces a clean re-login if the cached token is corrupt.

---

Source: [Vectle](https://vectle.com/skills/skl_4f9iF9wrIP0g2Yr-AXbjog). Version: `skv_2qMpcNk35fdXk59j6p-f2A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
