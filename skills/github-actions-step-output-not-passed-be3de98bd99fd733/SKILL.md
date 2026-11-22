---
name: "github-actions-step-output-not-passed-be3de98bd99fd733"
description: "github actions step output not passed error next job empty bug"
metadata:
  skill_id: "skl_UX_kuTbFbJoc3tpYhWIG1Q"
  title: "github actions step output not passed error next job empty bug"
  version: "skv_BLGI-e6o8aWgJuSJDfflew"
  updated: "2026-11-22T01:55:51.599048+00:00"
  canonical_url: "https://vectle.com/skills/skl_UX_kuTbFbJoc3tpYhWIG1Q"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the step writes to the output file, not the deprecated stdout command.

Confirm the producing job maps the step output at job level.

Confirm the consuming job declares the dependency.

Read the value through the needs context, not the steps context.

Watch for multiline and special-character values.

---

Source: [Vectle](https://vectle.com/skills/skl_UX_kuTbFbJoc3tpYhWIG1Q). Version: `skv_BLGI-e6o8aWgJuSJDfflew`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
