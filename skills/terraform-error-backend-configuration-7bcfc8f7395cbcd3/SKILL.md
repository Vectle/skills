---
name: "terraform-error-backend-configuration-7bcfc8f7395cbcd3"
description: "terraform error backend configuration changed run init -migrate-state fails"
metadata:
  skill_id: "skl_odsD4tntXvmc_68H5f7-vA"
  title: "terraform error backend configuration changed run init -migrate-state fails"
  version: "skv_doOMyDWtZz-r9h6rtAA72w"
  updated: "2026-11-27T01:52:13.207325+00:00"
  canonical_url: "https://vectle.com/skills/skl_odsD4tntXvmc_68H5f7-vA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Diff the backend block in your configuration against version control to see exactly what changed.

Check whether state already exists in the new backend location with terraform state pull after a reconfigure in a scratch copy, or by listing the new storage location.

If the new location is empty and the state should move, run terraform init with the -migrate-state flag and confirm the copy prompt.

If the state should not move, run terraform init with the -reconfigure flag instead, which keeps the state where it is and only updates the local backend record.

Run terraform init with no flags, then terraform plan.

---

Source: [Vectle](https://vectle.com/skills/skl_odsD4tntXvmc_68H5f7-vA). Version: `skv_doOMyDWtZz-r9h6rtAA72w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
