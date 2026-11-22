---
name: "error-validating-token-missing-require-c8c4e553eda25f47"
description: "error validating token -  missing required scope 'read:org' github fix"
metadata:
  skill_id: "skl_EXY1pbIoIIKhpZ_DpK6t3w"
  title: "error validating token -  missing required scope 'read:org' github fix"
  version: "skv_SJ63ldkfL4_IdBdElLvR_g"
  updated: "2026-11-22T01:56:18.778477+00:00"
  canonical_url: "https://vectle.com/skills/skl_EXY1pbIoIIKhpZ_DpK6t3w"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Identify which token the tool is actually using.

For a classic personal access token, open its settings page and tick the read:org scope under the admin:org group, then save.

For an OAuth app flow, add read:org to the scopes requested at authorize time and sign in again.

If the organization enforces SAML SSO, authorize the token for that organization after fixing the scope.

Re-run the failing command.

---

Source: [Vectle](https://vectle.com/skills/skl_EXY1pbIoIIKhpZ_DpK6t3w). Version: `skv_SJ63ldkfL4_IdBdElLvR_g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
