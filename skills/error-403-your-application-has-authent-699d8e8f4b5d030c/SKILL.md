---
name: "error-403-your-application-has-authent-699d8e8f4b5d030c"
description: "Fixes gcloud and API calls failing with Error 403: Your application has authenticated using end user credentials which are not supported. Use when application-default credentials from gcloud auth application-default login hit APIs that require a billing/quota project. Sets the quota project or switches to a service account. Not for invalid_grant, which is a dead refresh token, or IAM permission denied."
metadata:
  skill_id: "skl_dX-YbsBlLy1qKDaeSTe9Qw"
  title: "Error 403: Your application has authenticated using end user credentials which are not supported"
  version: "skv_5csLdDl2xg_nFeAcM8fe_g"
  updated: "2026-10-03T04:43:00.812067+00:00"
  canonical_url: "https://vectle.com/skills/skl_dX-YbsBlLy1qKDaeSTe9Qw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/googlecloudplatform/terraform-google-enterprise-genai/blob/HEAD/docs/TROUBLESHOOTING.md\"]"
---

# Error 403: Your application has authenticated using end user credentials which are not supported

TL;DR: some Google APIs refuse user credentials from ADC — they need a billing project attached to the call. Run `gcloud auth application-default set-quota-project [project]` once, or pass `--billing-project=[project]` on the command. Re-running `gcloud auth login` alone changes nothing.

```text
Error 403: Your application has authenticated using end user credentials from the Google Cloud SDK or Google Cloud Shell which are not supported by the API.
We recommend configuring the billing/quota_project setting in gcloud or using a service account through the auth/impersonate_service_account setting.
```

## Steps

1. Confirm the shape of the problem: the call 403s with the message above even though `gcloud auth application-default print-access-token` returns a token fine. The credential works — the API just wont bill it.

2. Attach a quota project to ADC:

```bash
gcloud auth application-default set-quota-project [project-id]
```

Expected: `Quota project [project-id] was added to ADC which can be used by Google client libraries for billing and quota.`

3. Or set it per command instead:

```bash
gcloud scc notifications describe [name] --organization [org-id] --billing-project=[project-id]
```

4. Or impersonate a service account (needs iam.serviceAccounts.getAccessToken on it):

```bash
gcloud ... --impersonate-service-account=[service account email]
```

5. Retry the original command. Expected: the 403 is gone.

## When this applies

- the exact 403 about end user credentials not being supported
- Cloud Shell or ADC user credentials calling APIs like securitycenter or accesscontextmanager
- terraform plan failing with this text when the provider uses your user-creds ADC

## When it doesnt

- `invalid_grant: Token has been expired or revoked` — dead refresh token, re-run `gcloud auth login`
- `API not enabled` without the end-user-credentials text — enable the API on the project
- plain permission denied — the credential is fine, the IAM role is missing

## Compatibility

Google Cloud SDK, all recent versions. ADC file: ~/.config/gcloud/application_default_credentials.json.

## Why it happens

ADC user credentials carry no quota project, so APIs that bill per call reject them outright. The gcloud CLI usually supplies the project from its own config, but ADC consumers — client libraries, terraform, and some gcloud paths in Cloud Shell — dont, so the call arrives unbilled and gets 403d.

## Edge cases

- you need the serviceusage.services.use permission on the quota project or the set-quota-project call fails
- the terraform Google provider has its own quota_project and impersonate_service_account settings for the same problem
- pick a project you own: the quota project gets billed for the API usage

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=gcloud+end+user+credentials+not+supported+quota+project'
```


---

Source: [Vectle](https://vectle.com/skills/skl_dX-YbsBlLy1qKDaeSTe9Qw). Version: `skv_5csLdDl2xg_nFeAcM8fe_g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
