---
name: "a0deploy-export-error-tenant-config-em-9bb065eb5405907a"
description: "a0deploy export error tenant config empty output fails"
metadata:
  skill_id: "skl_IZx3ZPcLV9BG4SDAtytuEg"
  title: "a0deploy export error tenant config empty output fails"
  version: "skv_KG8ajECPLRlL9VQgXC94oA"
  updated: "2026-11-17T01:55:52.153997+00:00"
  canonical_url: "https://vectle.com/skills/skl_IZx3ZPcLV9BG4SDAtytuEg"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Print the tenant domain the export is configured to use and confirm it is the tenant you expect.

Confirm the machine to machine application used for export is authorised for the Management API with read access to the resource types you expect in the output.

Run the export into a new empty output directory instead of reusing an old one.

Rerun with verbose logging enabled and read the first API error in the log, not the last line.

Check that the export format setting matches the output you are inspecting, directory or single file.

After fixing the domain or scopes, rerun the full export and count the resource folders in the output.

---

Source: [Vectle](https://vectle.com/skills/skl_IZx3ZPcLV9BG4SDAtytuEg). Version: `skv_KG8ajECPLRlL9VQgXC94oA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
