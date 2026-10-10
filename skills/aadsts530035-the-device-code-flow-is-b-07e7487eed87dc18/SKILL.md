---
name: "aadsts530035-the-device-code-flow-is-b-07e7487eed87dc18"
description: "Diagnoses Entra ID error AADSTS530035, where Conditional Access blocks the device code flow. Use when an agent sees this during az login with --use-device-code or any device-code auth on a hardened tenant. Covers switching to interactive browser login, using a service principal, or asking the admin for a policy exception. Not for general Conditional Access blocks."
metadata:
  skill_id: "skl_do8naHIr1SfCEArlSu-7qQ"
  title: "AADSTS530035: The device code flow is blocked in your organization"
  version: "skv_iEZxeDdavUNfNjCJnLpmyg"
  updated: "2026-10-03T04:44:36.587971+00:00"
  canonical_url: "https://vectle.com/skills/skl_do8naHIr1SfCEArlSu-7qQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# AADSTS530035: The device code flow is blocked in your organization

## TL;DR
Your tenant's Conditional Access policy explicitly blocks device code authentication. Do not fight the policy. Use interactive browser login instead, or authenticate as a service principal for automation.

## The error
```
AADSTS530035: The device code flow has been blocked due to Conditional Access policies.
```

## Fix it
1. For interactive use, drop the device code flag and run plain `az login`. Expected: a browser window opens and sign-in succeeds.
2. For automation, switch to a service principal: `az login --service-principal -u [app-id] -p [client-secret] --tenant [tenant-id]`. Expected: auth succeeds without any user interaction.
3. On a machine with no browser, use `az login --use-device-code` only if the policy allows it. If it does not, authenticate from a machine with a browser, or use the service principal route. Expected: you stop retrying a flow the policy will never allow.
4. If device code flow is genuinely needed (remote SSH sessions), ask the tenant admin for a Conditional Access exception for your account. Expected: the admin scopes an exception, then the flow works.
5. Verify with `az account show`. Expected: the command returns your subscription details.

## When to use this
- An agent sees AADSTS530035 during `az login --use-device-code` or any device-code auth.
- Automation on a headless box fails where interactive login works.

## When NOT to use this
- Other Conditional Access blocks (MFA required, compliant device required). Those name different codes and need different fixes.
- AADSTS50034 or AADSTS90002. The account and tenant are fine here; the flow is the problem.

## Compatibility
- Microsoft Entra ID tenants with Conditional Access policies, Azure CLI, MSAL device code flow.

### Variant phrasings
- "AADSTS530035" on its own
- "device code flow has been blocked"

## Root cause
Device code flow is a common phishing vector, so security-conscious tenants block it outright in Conditional Access. The block is intentional. The fix is to use a flow the policy permits, not to work around the policy.

## Edge cases
- WSL and SSH sessions often push people toward device code flow. Service principals are the durable answer there.
- Some tenants block device code flow only for guests or only for risky sign-ins. The sign-in log shows which policy fired.


---

Source: [Vectle](https://vectle.com/skills/skl_do8naHIr1SfCEArlSu-7qQ). Version: `skv_iEZxeDdavUNfNjCJnLpmyg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
