---
name: "endor-labs-auth-never-mix-bearer-token-a4881fe8964dd6f5"
description: "Guide Endor Labs auth: never mix bearer token and API key in one env (dual_mode_conflict): `endor-auth check --tenant [namespace]` [Official Endor Labs SDK docs (endor-auth-setup)]: Single auth mode is a hard rule: unset ENDOR_TOKEN or unset both API key vars to clear dual_mode_conflict. Use this when you hit exactly this in Endor Labs auth. Not for different errors or different tools."
metadata:
  skill_id: "skl_jOU18jroN1fl6lfPiNzSqg"
  title: "Endor Labs auth: never mix bearer token and API key in one env (dual_mode_conflict)"
  version: "skv_5hRzSEX8zBm7TgLh05EQuQ"
  updated: "2026-10-03T04:48:24.545328+00:00"
  canonical_url: "https://vectle.com/skills/skl_jOU18jroN1fl6lfPiNzSqg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: `endor-auth check --tenant [namespace]` [Official Endor Labs SDK docs (endor-auth-setup)]: Single auth mode is a hard rule: unset ENDOR_TOKEN or unset both API key vars to clear dual_mode_conflict. Probe with

[Official Endor Labs SDK docs (endor-auth-setup)]: Single auth mode is a hard rule: unset ENDOR_TOKEN or unset both API key vars to clear dual_mode_conflict. Probe with `endor-auth check --tenant [namespace]` (exit 0 when ready). whoami fails with 401 means the bearer token expired, rerun `endor-auth refresh` to get a new one. 403 means the wrong tenant or insufficient scope, fix ENDOR_NAMESPACE or the credential access. For CI/automation use the API key pair instead of browser refresh, since refresh opens YOUR_HOST:30000 and needs a human present.

Context: Official docs (endor-auth-setup SKILL.md): documents the single-auth-mode gotcha that trips agents when ENDOR_TOKEN and the API key pair (ENDOR_API_CREDENTIALS_KEY / ENDOR_API_CREDENTIALS_SECRET) are both set in one environment. SDK, endorctl, and MCP must pick one credential mode per env or per .env file, never both.

## When to use
You hit exactly this: Endor Labs auth: never mix bearer token and API key in one env (dual_mode_conflict) in Endor Labs auth.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Endor Labs auth.

---

Source: [Vectle](https://vectle.com/skills/skl_jOU18jroN1fl6lfPiNzSqg). Version: `skv_5hRzSEX8zBm7TgLh05EQuQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
