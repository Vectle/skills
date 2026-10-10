---
name: "how-to-fix-checkov-failed-item-by-its-6e560e0763e07c63"
description: "You shouldn't use the wild card with resources, Right now it's opened widely for all the resources."
metadata:
  skill_id: "skl_7Vt_2A5EnuFsW-Pbm9uoMA"
  title: "How to fix checkov failed item by its rules?"
  version: "skv_UmbhOWi4CsMULoCG-9wPhw"
  updated: "2026-10-03T04:44:12.350108+00:00"
  canonical_url: "https://vectle.com/skills/skl_7Vt_2A5EnuFsW-Pbm9uoMA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix checkov failed item by its rules?

## TL;DR

[KayD (accepted answer)]: You shouldn't use the wild card with resources, Right now it's opened widely for all the resources. If you change the resource's wild card to the list of arns of the resources, which will use this policy then checkov will not show this error anymore. Context: Stack Overflow 67428658 (accepted answer, 3 votes, 1 answers): When run checkov for an Terraform resource scan, got this failed From official document, found its introduction page.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

There is a Fix - Buildtime on the page, but how to refer it to use for my case? From its Resource Exposure on the page, I didn't fi


---

Source: [Vectle](https://vectle.com/skills/skl_7Vt_2A5EnuFsW-Pbm9uoMA). Version: `skv_UmbhOWi4CsMULoCG-9wPhw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
