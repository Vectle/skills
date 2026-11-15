---
name: "skill-package-validation-fails-with-mi-dd5aec03dc4d63b1"
description: "skill package validation fails with \"missing description\" error publish rejected"
metadata:
  skill_id: "skl_lBXGKHSQdLN_98xMq0uqag"
  title: "skill package validation fails with \"missing description\" error publish rejected"
  version: "skv_dxr9ZiWkF8vcald7E55TyA"
  updated: "2026-11-15T13:55:26.798107+00:00"
  canonical_url: "https://vectle.com/skills/skl_lBXGKHSQdLN_98xMq0uqag"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Open the main skill file the publisher validates and check its top frontmatter block before anything else.

Add a description if absent, written in third person, stating what the skill does and when to use it.

Check the frontmatter syntax: delimiters on their own lines, a colon and space after the field name, and no unquoted special characters that break parsing.

Trim the description to the validator limit if it is very long, keeping the what and when triggers.

Remove duplicate or conflicting description fields elsewhere in the package that could shadow the main one.

Run the package validator locally or with a dry-run publish and confirm the missing description error is gone.

Publish again and confirm the listing shows the description text.

---

Source: [Vectle](https://vectle.com/skills/skl_lBXGKHSQdLN_98xMq0uqag). Version: `skv_dxr9ZiWkF8vcald7E55TyA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
