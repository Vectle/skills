---
name: "terraform-azurerm-authenticate-with-ar-e9bdc82da8f87a22"
description: "Shows how to fix terraform azurerm: authenticate with ARM_ env vars, not az login leftovers. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_FwASqDkW4rgl1ANfqpbKMQ"
  title: "Terraform azurerm: authenticate with ARM_ env vars, not az login leftovers"
  version: "skv_w5WMoAlpi-2PhOziVGq56Q"
  updated: "2026-10-03T13:58:11.453533+00:00"
  canonical_url: "https://vectle.com/skills/skl_FwASqDkW4rgl1ANfqpbKMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://learn.microsoft.com/en-us/azure/developer/terraform/authenticate-to-azure\"]"
---

## TL;DR

An empty features block is required even if you set nothing. Major versions rename resources; unpinned upgrades break plans. - Backend auth.

## Steps

1. ```hcl
provider "azurerm" {
 features {}
 subscription_id = var.subscription_id
}
```

2. Auth options, in order of preference for automation:

3. **OIDC / federated credentials.** `ARM_USE_OIDC=true`, `ARM_CLIENT_ID`, `ARM_TENANT_ID`, plus the CI system's identity token. No secret to rotate. This is the current best practice for GitHub Actions.
2. **Service principal env vars.** ARM_CLIENT_ID, ARM_CLIENT_SECRET, ARM_TENANT_ID, ARM_SUBSCRIPTION_ID. Works everywhere; the secret expires, calendar it.
3. **Azure CLI.** `az login` then the provider uses the CLI token. Fine for local dev, banned in CI (non-reproducible, breaks when the token dies).
4. **Managed identity.** On an Azure VM / pipeline agent with identity: the provider picks it up.

4. - **features {} is mandatory.** An empty features block is required even if you set nothing. Missing it is a confusing provider error.
- **Provider version pin.** `required_providers { azurerm = { source = "hashicorp/azurerm", version = "~> 4.0" } }`. Major versions rename resources; unpinned upgrades break plans.
- **Backend auth.** The azurerm backend (state in Blob Storage) needs its own auth: same ARM_ vars or a SAS. A plan that authenticates fine but cannot read state is a backend-auth problem, not a provider problem.
- **Subscription in two places.** Provider subscription_id and backend storage account subscription can differ; set both explicitly.

5. Verify: `terraform plan` shows the expected subscription in the backend init output and no auth warnings, before apply.

## When to use

You are seeing this: ``hcl provider "azurerm" { features {} subscription\_id = var.subscription\_id } ` Auth options, in order of preference for automation: 1. Use this skill when you run into "Terraform azurerm: authenticate with ARM_ env vars, not az login leftovers".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_FwASqDkW4rgl1ANfqpbKMQ). Version: `skv_w5WMoAlpi-2PhOziVGq56Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
