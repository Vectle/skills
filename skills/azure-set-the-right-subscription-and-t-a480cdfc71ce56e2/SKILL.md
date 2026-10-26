---
name: "azure-set-the-right-subscription-and-t-a480cdfc71ce56e2"
description: "Shows how to fix azure: set the right subscription and tenant before you create anything. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_A7HODTksoe-4kvFt5Aeq9A"
  title: "Azure: set the right subscription and tenant before you create anything"
  version: "skv_81UG_xtlmiVIYL6QJ10s1g"
  updated: "2026-10-03T14:07:08.407517+00:00"
  canonical_url: "https://vectle.com/skills/skl_A7HODTksoe-4kvFt5Aeq9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli\"]"
---

## TL;DR

Pass --subscription on every mutating command, or set the ARM\_SUBSCRIPTION\_ID environment variable. Azure CLI commands silently run against whatever subscription is marked default, and az login without a tenant flag lands in the first tenant it finds.

## Steps

1. Azure CLI commands silently run against whatever subscription is marked default, and `az login` without a tenant flag lands in the first tenant it finds. Agents trip on this constantly.

2. Check where you are before doing anything that creates or bills:

```
az account show --output table
```

3. Look at `name`, `id`, and `tenantId`. If any of them is wrong, fix it:

```
az account list --output table # see everything you can reach
az account set --subscription "My Subscription" # or pass the subscription id
az login --tenant [tenant-id] # when you have access to several tenants
```

4. Rules that save loops:

5. - Never trust the default in a script. Pass `--subscription` on every mutating command, or set the ARM_SUBSCRIPTION_ID environment variable. A script that ran fine on your dev sub will happily create a production resource group if the default changed.
- Service principals are tenant-scoped. If login works but every command says the subscription does not exist, you are in the wrong tenant. Re-login with --tenant.
- `az account show` caches. After a subscription is moved or disabled, re-run `az account list --refresh` before concluding it is gone.
- In Terraform, the azurerm provider reads ARM_SUBSCRIPTION_ID / ARM_TENANT_ID env vars. Same confusion, different surface: set them explicitly in CI instead of relying on whatever the runner's az login did.
- Billing surprise guard: `az account list --query "[?isDefault].{name:name}"` in the first line of any automation that provisions resources, and fail loudly if it is not the expected subscription.

6. When a resource "disappears", the checklist is: right subscription, right tenant, right resource group, then panic. The first two explain most of it.

## When to use

You are seeing this: Agents trip on this constantly. Use this skill when you run into "Azure: set the right subscription and tenant before you create anything".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_A7HODTksoe-4kvFt5Aeq9A). Version: `skv_81UG_xtlmiVIYL6QJ10s1g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
