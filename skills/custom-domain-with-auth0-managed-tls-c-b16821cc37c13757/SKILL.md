---
name: "custom-domain-with-auth0-managed-tls-c-b16821cc37c13757"
description: "A custom domain unifies branding and makes Auth0 cookies first-party. Auth0-managed certificates remove the renewal toil; the switchover order avoids breaking logins mid-migration. Not the full reference manual."
metadata:
  skill_id: "skl_t1ss7R2RMz4wqGdptxC07w"
  title: "Custom domain with Auth0-managed TLS: CNAME, verification, feature switchover"
  version: "skv_ws6qdD6G8_k-kDUqVKoDPQ"
  updated: "2026-10-03T05:06:44.851598+00:00"
  canonical_url: "https://vectle.com/skills/skl_t1ss7R2RMz4wqGdptxC07w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** A custom domain unifies branding and makes Auth0 cookies first-party. Auth0-managed certificates remove the renewal toil; the switchover order avoids breaking logins mid-migration. Add the domain Dashboard > Branding > Custom Domains > Add. Verify the domain first; do not point SDKs at it before verification completes.

# Custom domain setup

## 1. Add the domain

Dashboard > Branding > Custom Domains > Add. Enter `login.YOUR-DOMAIN`. Choose Auth0-managed certificates unless you have a reason to bring your own (managed = issuance + renewal handled).

## 2. DNS

Add the CNAME record Auth0 shows, pointing your hostname at the Auth0 edge. Then complete verification in the dashboard. Verification proves control of the domain.

## 3. Switchover order

1. Verify the domain first; do not point SDKs at it before verification completes.
2. Update SDK/API `domain` values to the custom domain.
3. Update Allowed Callback URLs, Logout URLs, and Web Origins to the custom domain (keep the canonical entries during the transition, remove after).
4. Check the feature-compatibility table in the docs: a few features still use the canonical domain. Do not assume everything moves.
5. Token `iss`: by default the issuer remains the canonical domain. API validators must accept the canonical issuer unless you change the issuer configuration. This is the number one post-migration 401 cause.

## Why bother

- Branding: users see your domain in the URL bar during login.
- First-party cookies: fixes Safari ITP silent-auth breakage with no code changes.
- Consistent security posture for enterprise customers inspecting URLs.

## Checklist

- Verified before cutover; both domains registered during transition.
- API issuer validation handles the canonical issuer.
- Renewal: managed certs auto-renew; self-managed need a calendar reminder.

## When to use this

- This covers exactly what the title says: Custom domain with Auth0-managed TLS.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Custom; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Custom behavior.

## Edge cases

- Choose Auth0-managed certificates unless you have a reason to bring your own (managed = issuance + renewal handled).
- API validators must accept the canonical issuer unless you change the issuer configuration.

---

Source: [Vectle](https://vectle.com/skills/skl_t1ss7R2RMz4wqGdptxC07w). Version: `skv_ws6qdD6G8_k-kDUqVKoDPQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
