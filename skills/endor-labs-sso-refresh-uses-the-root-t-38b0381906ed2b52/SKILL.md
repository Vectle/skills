---
name: "endor-labs-sso-refresh-uses-the-root-t-38b0381906ed2b52"
description: "Guide Endor Labs SSO refresh uses the root tenant segment, not your child namespace: Set ENDOR_NAMESPACE or pass -n on the workflow CLI you run after auth. [Official Endor Labs SDK docs (endor-auth-setup)]: `endor-auth refresh -n [tenant. Use this when you hit exactly this in Endor Labs SSO. Not for different errors or different tools."
metadata:
  skill_id: "skl_jhYICcxTd8mv9eXHSymi9A"
  title: "Endor Labs SSO refresh uses the root tenant segment, not your child namespace"
  version: "skv_H4hqnPbSJhrJ9fgnTuv-ig"
  updated: "2026-10-03T05:35:36.538185+00:00"
  canonical_url: "https://vectle.com/skills/skl_jhYICcxTd8mv9eXHSymi9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/endorlabs/endorlabs-sdk/blob/HEAD/agent-knowledge/skills/endor-auth-setup/SKILL.md\"]"
---

TL;DR: Set ENDOR_NAMESPACE or pass -n on the workflow CLI you run after auth. [Official Endor Labs SDK docs (endor-auth-setup)]: `endor-auth refresh -n [tenant.child]`

## Fix
1. Set ENDOR_NAMESPACE or pass -n on the workflow CLI you run after auth.
   Expected: this specific failure stops.
2. uses only the root segment of the tenant for the IdP login, while report workflows use the full namespace path for list scope.
   Expected: the request routes instead of erroring.

## Details
[Official Endor Labs SDK docs (endor-auth-setup)]: `endor-auth refresh -n [tenant.child]` logs in against the root segment (tenant) only, so do not assume a child namespace passed to refresh becomes your API list path. Precedence for SSO: the refresh flag, then ENDOR_NAMESPACE in shell, then .env, then endorctl config.yaml. Token lifetime gotchas: one Client instance holds its bearer token in memory, expiry prints a one-time stderr warning within 30 minutes, and an expired token fails closed with UnauthorizedError. Refresh does not touch .env or os.environ, and child shells never inherit the in-memory token, so rerun `endor-auth refresh` in each new process. Context: Official docs (endor-auth-setup SKILL.md): documents two SSO gotchas that trip agents. `endor-auth refresh`

## When to use
You hit exactly this: Endor Labs SSO refresh uses the root tenant segment, not your child namespace in Endor Labs SSO.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Endor Labs SSO.

## Edge cases
- Also, a refreshed bearer token lives in memory only: child shells do not inherit it and the SDK client never writes it to disk.

---

Source: [Vectle](https://vectle.com/skills/skl_jhYICcxTd8mv9eXHSymi9A). Version: `skv_H4hqnPbSJhrJ9fgnTuv-ig`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
