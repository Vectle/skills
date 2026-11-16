---
name: "terraform-init-reconfigure-vs-migrate-53279e79d7d2ccda"
description: "terraform init reconfigure vs migrate-state error backend changes fails"
metadata:
  skill_id: "skl_GeFua5emz4erTSZYzt49Xw"
  title: "terraform init reconfigure vs migrate-state error backend changes fails"
  version: "skv_602-FfbOU1X56e2VyZ1RCA"
  updated: "2026-11-16T13:54:26.847535+00:00"
  canonical_url: "https://vectle.com/skills/skl_GeFua5emz4erTSZYzt49Xw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Decide whether the state itself moved. A new bucket, account, key prefix, or backend type means it moved.

Back up the current state by pulling it while the old configuration still works, if it still works.

If state moved and the old backend is still reachable, run init with the migrate-state flag and confirm the copy prompt.

If state did not move, or the old backend no longer exists, run init with the reconfigure flag instead.

Run terraform plan and read the result carefully before any apply.

If the plan wants to recreate everything, stop. That means init pointed at an empty backend.

---

Source: [Vectle](https://vectle.com/skills/skl_GeFua5emz4erTSZYzt49Xw). Version: `skv_602-FfbOU1X56e2VyZ1RCA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
