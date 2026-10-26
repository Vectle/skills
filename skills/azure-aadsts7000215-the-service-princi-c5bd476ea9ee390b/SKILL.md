---
name: "azure-aadsts7000215-the-service-princi-c5bd476ea9ee390b"
description: "Microsoft Entra ID sign-in fails with AADSTS7000215 invalid client secret. Covers triaging expiry vs wrong secret vs wrong tenant, rotating safely, and replacing secrets with federated credentials. Not for certificate auth issues or consent errors."
metadata:
  skill_id: "skl_YueVBusbqTMRZPo_f2DJgQ"
  title: "Azure AADSTS7000215: the service principal secret is expired or wrong"
  version: "skv_iVt4ItK4BwDkfGKuYgfoCQ"
  updated: "2026-10-03T04:35:22.125543+00:00"
  canonical_url: "https://vectle.com/skills/skl_YueVBusbqTMRZPo_f2DJgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation\"]"
---

TL;DR: AADSTS7000215 means the app registration's secret expired (max 24 months) or you are using the wrong one. Check expiry in the portal under Certificates and secrets. Create a new secret, update the consumer, then DELETE the old one. Never delete first. The real fix is a federated credential (workload identity federation) so there is no secret to expire.

The error, verbatim:

```text
AADSTS7000215: Invalid client secret provided.
```

Steps:

1. Check expiry in the portal: Entra, App registrations, Certificates and secrets. Success: you can see the secret's expiry date. If it worked for months then broke overnight, this is it.
2. Rule out the wrong secret. App registrations can hold several; compare the secret's key id or hint in your config against the portal, never the value. Success: the hint matches exactly one current secret.
3. Rule out the wrong tenant. A secret from tenant A used against tenant B gives the same error shape. Success: the authority URL matches the app's tenant.
4. Create a new secret, update the consumer, then delete the old one. Do not delete first. Success: auth works and only the new secret exists.
5. Kill the pattern: add a federated credential for the CI workload so there is no secret at all (Entra, App registrations, Certificates and secrets, Federated credentials). Success: the workload authenticates with OIDC and no secret rotation is ever needed again.

When to use: AADSTS7000215 on any OAuth2 client-credentials flow against Microsoft Entra ID.

When not to use: certificate-based auth failures, consent/permission errors (those are different AADSTS codes), or user sign-in problems.

Compatibility: Microsoft Entra ID app registrations; GitHub Actions, Azure DevOps, and Terraform Cloud all support OIDC federation to Entra.

Variants:
- aadsts7000215 invalid client secret
- azure ad secret expired
- entra invalid client secret provided

Root cause: secrets max out at 24 months and something always forgets the rotation. The error also fires for wrong-secret and wrong-tenant, which is why step 1 is check, not rotate blindly.

Edge cases:
- Calendar rule: if you must keep secrets, set the expiry reminder for 30 days before, not the day of. The 2am page is the tax on skipping step 5.
- Multiple secrets on one registration are the classic wrong-secret trap. The key id or hint disambiguates; the value never should.

---

Source: [Vectle](https://vectle.com/skills/skl_YueVBusbqTMRZPo_f2DJgQ). Version: `skv_iVt4ItK4BwDkfGKuYgfoCQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
