---
name: "unable-to-locate-credentials-you-can-c-e6110275cdac243c"
description: "Fixes the AWS CLI error Unable to locate credentials by walking the credential chain in order: env vars, shared credentials file, SSO, instance profile. Use when any aws command fails with this error on a machine that should be authenticated. Not for InvalidClientTokenId, which is a bad key, or AccessDenied, which is a missing IAM permission."
metadata:
  skill_id: "skl_exYinwSKhaEhAfwKm7cKqQ"
  title: "Unable to locate credentials. You can configure credentials by running 'aws configure'"
  version: "skv_11vG3JZ7QmVSJ2xRdizSLg"
  updated: "2026-10-03T04:42:25.627651+00:00"
  canonical_url: "https://vectle.com/skills/skl_exYinwSKhaEhAfwKm7cKqQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/abdullahbinamin/devops-training-practical-notes/blob/HEAD/terraform/Day-01-Terraform-Fundamentals-and-Setup/04-aws-cli-setup.md\"]"
---

# Unable to locate credentials. You can configure credentials by running 'aws configure'

TL;DR: the CLI found no credentials anywhere it looks. Run `aws configure` and enter your access key pair, or if your org uses SSO run `aws sso login --profile [profile]`. Nine times out of ten the fix is either never having run aws configure, or AWS_PROFILE pointing at a profile that doesnt exist.

```text
Unable to locate credentials. You can configure credentials by running "aws configure".
```

## Steps

1. Confirm the failure:

```bash
aws sts get-caller-identity
```

Expected on success: JSON with UserId, Account, and Arn. If it errors the same way, keep going.

2. Check which profile is active and where values come from:

```bash
aws configure list
```

Expected: shows the profile name and the source of each value (env, config file, or none).

3. Set credentials. Static keys:

```bash
aws configure
```

Expected: prompts for AWS Access Key ID, AWS Secret Access Key, region, and output format. SSO instead:

```bash
aws sso login --profile [your profile]
```

Expected: browser opens for SSO, then the CLI reports a successful login.

4. Verify:

```bash
aws sts get-caller-identity
```

Expected: returns your identity with no error.

## When this applies

- any aws command fails with the exact `Unable to locate credentials` error
- fresh install where `aws configure` was never run
- new shell where the env vars were not exported, or AWS_PROFILE names a profile with no keys
- SSO session expired

## When it doesnt

- `InvalidClientTokenId: The security token included in the request is invalid` — the key is deleted, deactivated, or mistyped; recreate it in IAM and re-run aws configure
- `ExpiredToken` — refresh SSO or the temporary credentials
- `AccessDenied` on a specific call — identity is fine, the IAM policy is missing the action

## Compatibility

AWS CLI v2 (v1 from distro repos is retired). Same chain on Linux, macOS, and Windows.

## Why it happens

The CLI checks credentials in a fixed order: environment variables, the shared credentials file, SSO cache, then container or instance metadata. If none yields a key it raises this instead of guessing. The classic traps: AWS_PROFILE pointing nowhere, env vars set in one terminal but not another, and an SSO login that expired silently.

## Edge cases

- `~/.aws/credentials` stores the secret in plain text: chmod 600 it and never commit it
- a typo in the env var name is a top cause — it must be exactly AWS_SECRET_ACCESS_KEY
- system clock skew shows up as SignatureDoesNotMatch, not this error
- in containers and EC2, prefer IAM roles over static keys so there is nothing to locate

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=aws+unable+to+locate+credentials'
```


---

Source: [Vectle](https://vectle.com/skills/skl_exYinwSKhaEhAfwKm7cKqQ). Version: `skv_11vG3JZ7QmVSJ2xRdizSLg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
