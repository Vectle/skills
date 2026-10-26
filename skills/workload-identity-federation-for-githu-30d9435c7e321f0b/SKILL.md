---
name: "workload-identity-federation-for-githu-30d9435c7e321f0b"
description: "Shows how to fix workload Identity Federation for GitHub Actions: CI with no stored keys. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ep5XGWsPrqsyeUabqSBdvA"
  title: "Workload Identity Federation for GitHub Actions: CI with no stored keys"
  version: "skv_z8oHNEQo7b1V0bc5ZqonlA"
  updated: "2026-10-03T13:54:18.457793+00:00"
  canonical_url: "https://vectle.com/skills/skl_ep5XGWsPrqsyeUabqSBdvA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/iam/docs/workload-identity-federation\",\"https://cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines\"]"
---

## TL;DR

Issuer is the GitHub OIDC issuer; set attribute mapping (google.subject from assertion.sub is the baseline) and an attribute condition to scope which repos can federate, e.g. assertion.repository == '[ORG]/[REPO]'.

## Steps

1. Goal: GitHub Actions deploys to GCP with zero long-lived keys.

2. Steps:
1. Create a workload identity pool:

```
gcloud iam workload-identity-pools create [POOL] --location global --display-name "[NAME]"
```

3. Create an OIDC provider for GitHub in the pool. Issuer is the GitHub OIDC issuer; set attribute mapping (google.subject from assertion.sub is the baseline) and an attribute condition to scope which repos can federate, e.g. assertion.repository == '[ORG]/[REPO]'.
3. Allow the federated identity to impersonate the target SA:

```
gcloud iam service-accounts add-iam-policy-binding [SA-EMAIL] --role roles/iam.workloadIdentityUser --member "principalSet://iam.googleapis.com/projects/[NUM]/locations/global/workloadIdentityPools/[POOL]/attribute.repository/[ORG]/[REPO]"
```

4. In the workflow, use google-github-actions/auth with the provider resource name and the SA email. No secrets needed.

5. Traps:
- Attribute condition too tight (or referencing a claim the token lacks) fails closed with unhelpful errors. Decode a real token and test the condition logic.
- The provider resource name in the workflow must match exactly, including projects/[NUM]/locations/global/workloadIdentityPools/[POOL]/providers/[PROVIDER].
- The federated identity still needs the workload's roles (storage.admin etc) via the SA it impersonates. Federation is auth, not authorization.
- Token lifetime: GitHub OIDC tokens are short-lived; long jobs that mint GCP tokens early can expire mid-run. Mint close to use.

6. Verify: run the workflow on a test branch, confirm the GCP step authenticates, and check audit logs show the federated principal.

## When to use

You are seeing this: Goal: GitHub Actions deploys to GCP with zero long-lived keys. Use this skill when you run into "Workload Identity Federation for GitHub Actions: CI with no stored keys".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_ep5XGWsPrqsyeUabqSBdvA). Version: `skv_z8oHNEQo7b1V0bc5ZqonlA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
