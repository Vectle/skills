---
name: "checkov-attribute-reference-e6346946b8a05395"
description: "depending on what you want to achieve you can use .*."
metadata:
  skill_id: "skl_OfD1QB1AmUpwC8jTyClw3g"
  title: "Checkov attribute reference"
  version: "skv_b6dvusKSDqCoLZAGz8kIbA"
  updated: "2026-10-03T05:42:18.617137+00:00"
  canonical_url: "https://vectle.com/skills/skl_OfD1QB1AmUpwC8jTyClw3g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Checkov attribute reference

## TL;DR

In the process, I am also writing my own policies. I would like to write a policy that checks the content inside "managed_rule_set". I know how to reference the attributes from the terraform-file correctly, but not how to do it in this particular case.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

In the process, I am also writing my own policies. I would like to write a policy that checks the content inside "managed_rule_set". I know how to reference the attributes from the terraform-file correctly, but not how to do it in this particular case. I define the custom policies via a yaml-file and orient myself on the documentation of checkov. Terraform-file: tf-file ``` resource "azurerm_web_application_firewall_policy" "waf_network" { name = "waf-${var.tag_project}-network-${var.tag_environment}" resource_group_name = azurer


---

Source: [Vectle](https://vectle.com/skills/skl_OfD1QB1AmUpwC8jTyClw3g). Version: `skv_b6dvusKSDqCoLZAGz8kIbA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
