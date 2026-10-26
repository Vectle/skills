---
name: "the-config-profile-my-profile-could-no-cf0ffb8b662ff4a5"
description: "Fixes the AWS CLI 'The config profile could not be found' error. Use when aws rejects a --profile name or AWS_PROFILE value. Covers the missing [profile ] prefix in ~/.aws/config, typos, and the empty-string AWS_PROFILE trap. Not for credential errors."
metadata:
  skill_id: "skl_xCPz5-SAoP4mHly2OAG_7g"
  title: "The config profile (my-profile) could not be found"
  version: "skv_GsPhj9yTk2hWn3uERXxGFA"
  updated: "2026-10-03T05:53:10.800882+00:00"
  canonical_url: "https://vectle.com/skills/skl_xCPz5-SAoP4mHly2OAG_7g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://towardsthecloud.com/blog/aws-cli-switch-profiles\"]"
---

The profile name does not match anything in your config. List your profiles with `aws configure list-profiles`, fix the typo, and make sure named profiles in `~/.aws/config` use the `[profile my-profile]` header (only `[default]` goes bare). If `AWS_PROFILE` is set to an empty string, `unset` it entirely.

```text
The config profile (my-profile) could not be found
```

## Fix

1. List the profiles the CLI actually sees:
   ```bash
   aws configure list-profiles
   ```
   Expected: the profile name you want appears exactly, character for character.

2. If it is missing, check `~/.aws/config`. Named profiles need the prefix:
   ```ini
   [profile my-profile]
   region = us-east-1
   ```
   Only `[default]` goes without the `profile` prefix. Fix the header, save, retry.

3. Check the right file: SSO, `role_arn`, and `source_profile` settings belong in `~/.aws/config`; static IAM keys belong in `~/.aws/credentials`. A profile split across the wrong files will not resolve.

4. If the error shows empty parentheses - `The config profile () could not be found` - your `AWS_PROFILE` is set to an empty string, which counts as a profile name. Fix it:
   ```bash
   unset AWS_PROFILE
   ```
   Expected: `aws sts get-caller-identity` falls back to the default profile and works.

## When this applies
- Any `aws` command fails with `The config profile (name) could not be found`, including the empty-parens variant.
- You just edited `~/.aws/config` or set `AWS_PROFILE` in a new shell.

## When it does NOT apply
- `Unable to locate credentials`: the profile resolves but has no credentials.
- `ExpiredToken` / `InvalidClientTokenId`: the profile resolves but the credentials are bad.

## Compatibility
- AWS CLI v1 and v2. The `[profile name]` header rule applies to `~/.aws/config` in both.

## Why it happens
The CLI looks up the profile name in `~/.aws/config` (and `~/.aws/credentials` for keys). A typo, a missing `profile` prefix in the section header, or an `AWS_PROFILE` value that does not exist anywhere means the lookup finds nothing. The empty-string case is sneaky: `export AWS_PROFILE=""` sets a real (empty) name instead of clearing the variable.

## Edge cases
- `AWS_CONFIG_FILE` / `AWS_SHARED_CREDENTIALS_FILE` env vars can point the CLI at different files than the ones you edited. Check them with `env | grep AWS_`.
- Profile names are case-sensitive.
- On Windows, the files live under `%UserProfile%\.aws`.

---

Source: [Vectle](https://vectle.com/skills/skl_xCPz5-SAoP4mHly2OAG_7g). Version: `skv_GsPhj9yTk2hWn3uERXxGFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
