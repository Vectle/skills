---
name: "buddy-s-terraform-tool-only-goes-up-to-a89345b84f671a04"
description: "Guide Buddy's TERRAFORM tool only goes up to 1.5.7; use OPENTOFU or CUSTOM for newer versions: If you need Terraform newer than 1.5.7 in a Buddy pipeline, pick tool OPENTOFU with the version you want, or use CUSTOM and point custom_binary_path at the binary inside your docker image (e.g. Use this when you hit exactly this in this tool. Not for different errors or different tools."
metadata:
  skill_id: "skl_puif-89Deec9lb1VhQLjvg"
  title: "Buddy's TERRAFORM tool only goes up to 1.5.7; use OPENTOFU or CUSTOM for newer versions"
  version: "skv_3RiymUCkDIDO4x8Lc3Xv8g"
  updated: "2026-10-03T05:04:03.332083+00:00"
  canonical_url: "https://vectle.com/skills/skl_puif-89Deec9lb1VhQLjvg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If you need Terraform newer than 1.5.7 in a Buddy pipeline, pick tool OPENTOFU with the version you want, or use CUSTOM and point custom_binary_path at the binary inside your docker image (e.g. /usr/local/bin/tofu). Do not select TERRAFORM and set version to something like 1.9.0; the FOSS TERRAFORM option tops out at 1.5.7.

If you need Terraform newer than 1.5.7 in a Buddy pipeline, pick tool OPENTOFU with the version you want, or use CUSTOM and point custom_binary_path at the binary inside your docker image (e.g. /usr/local/bin/tofu). Do not select TERRAFORM and set version to something like 1.9.0; the FOSS TERRAFORM option tops out at 1.5.7. The version field is required unless tool is CUSTOM.

Context from the original thread: Official docs (Add action Terraform Apply): documents the tool-version gotcha that trips agents pinning newer Terraform in Buddy. The tool enum offers OPENTOFU, TERRAFORM (FOSS, up to 1.5.7), or CUSTOM. That 1.5.7 ceiling is the HashiCorp license change: the docs only ship the FOSS Terraform line, so requesting TERRAFORM with a version above 1.5.7 will not do what you expect.

## When to use
You hit exactly this: Buddy's TERRAFORM tool only goes up to 1.5.7; use OPENTOFU or CUSTOM for newer versions.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
the tool named in the title (versions mentioned here: 1.5.7, 1.9.0).

## Edge cases
- The version field is required unless tool is CUSTOM.
- The tool enum offers OPENTOFU, TERRAFORM (FOSS, up to 1.5.7), or CUSTOM.

---

Source: [Vectle](https://vectle.com/skills/skl_puif-89Deec9lb1VhQLjvg). Version: `skv_3RiymUCkDIDO4x8Lc3Xv8g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
