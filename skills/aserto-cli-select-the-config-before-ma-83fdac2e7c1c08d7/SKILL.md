---
name: "aserto-cli-select-the-config-before-ma-83fdac2e7c1c08d7"
description: "Run aserto config use [policy-instance-name] after creating the config, or the CLI wont manage the authorizer."
metadata:
  skill_id: "skl_PyHQegVONAX4Mty7vVER5g"
  title: "Aserto CLI: select the config before managing the edge authorizer"
  version: "skv__aElycGlFstvyS7N_k-R5Q"
  updated: "2026-10-03T18:31:44.243609+00:00"
  canonical_url: "https://vectle.com/skills/skl_PyHQegVONAX4Mty7vVER5g"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# Aserto CLI: select the config before managing the edge authorizer

## TL;DR

Run aserto config use [policy-instance-name] after creating the config, or the CLI wont manage the authorizer. And create the edge authorizer connection in the console before referencing its id. Context: Official docs (Aserto CLI onebox): after you create the edge authorizer config with aserto config new, you still have to run aserto config use [policy-instance-name] before the CLI will actually manage that authorizer.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Skip it and commands like aserto start act on nothing useful. Also, the edge authorizer connection id you pass in has to come from a connection you created in the Aserto console first.


---

Source: [Vectle](https://vectle.com/skills/skl_PyHQegVONAX4Mty7vVER5g). Version: `skv__aElycGlFstvyS7N_k-R5Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
