---
name: "resource-protected-by-organization-sam-db68dbc1d0f44e44"
description: "Fixes 'Resource protected by organization SAML enforcement' by SSO-authorizing the personal access token for the org under Developer settings. Use when a token works elsewhere but one org 403s. Not for missing-scope or invalid-token errors."
metadata:
  skill_id: "skl_N-2lqgua5AFgtKFvYJFoJw"
  title: "Resource protected by organization SAML enforcement. You must grant your personal token access to this organization."
  version: "skv_tUk3LgxFirfP5YozCeaFFA"
  updated: "2026-10-03T05:58:42.646765+00:00"
  canonical_url: "https://vectle.com/skills/skl_N-2lqgua5AFgtKFvYJFoJw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/ganjardbc/ai-code-reviewer/blob/HEAD/docs-user/troubleshooting/github.md\"]"
---

Go to GitHub Settings, Developer settings, Personal access tokens, find your token, hit Configure SSO, and authorize it for the org. Then retry. Your token is fine, it just has not been introduced to that org's SAML setup yet.

```text
Resource protected by organization SAML enforcement. You must grant your personal token access to this organization.
```

## Fix it
1. Open github.com Settings, then Developer settings, then Personal access tokens.
   Success check: You see your token in the list.
2. Click Configure SSO next to the token.
   Success check: A list of organizations appears.
3. Click Authorize next to the organization that is blocking you, and complete the SAML sign-in.
   Success check: The org shows as authorized for the token.
4. Retry the gh command.
   Success check: The SAML enforcement error is gone.

## When this applies
- gh or API calls fail with 'Resource protected by organization SAML enforcement'
- the token works for personal repos but 403s on one specific org's repos

## When this does NOT apply
- the 403 names a missing scope instead (use gh auth refresh)
- the token itself is invalid (re-authenticate)

## Compatibility
gh CLI 2.x, github.com orgs with SAML SSO enforced. Applies to classic PATs and OAuth tokens from gh auth login.

## Variant phrasings
### The ambiguous 403
gh sometimes prints the SAML message AND a missing-scope hint together. Fix one, retry, then fix the other if it persists. Do not assume it is settled after one fix.

## Why it happens
Orgs with SAML SSO keep a per-token allowlist. A token that was never SSO-authorized is treated as an outsider for that org's resources even if its scopes are otherwise perfect. Authorizing links the token to your SAML identity for that org.

## Edge cases
- OAuth app tokens minted for you are auto-authorized; only PATs and gh CLI tokens need the manual step.
- Fine-grained PATs also need the org granted on the token itself, not just SSO authorization.
- gh prints both the SAML message and a scope hint at once; treat them as two separate suspects.

Source: https://github.com/ganjardbc/ai-code-reviewer/blob/HEAD/docs-user/troubleshooting/github.md

---

Source: [Vectle](https://vectle.com/skills/skl_N-2lqgua5AFgtKFvYJFoJw). Version: `skv_tUk3LgxFirfP5YozCeaFFA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
