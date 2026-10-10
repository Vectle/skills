---
name: "porter-porter-yaml-quote-env-values-pr-e45e639ae08e0afc"
description: "# Porter porter.yaml: env values must be strings, envGroups must pre-exist From Porter's official porter.yaml reference, the schema rules that fail deploys: - `env` values must be strings."
metadata:
  skill_id: "skl_rFwhAVHijQ9gaOBuvtnpnA"
  title: "Porter porter.yaml: quote env values, pre-create envGroups, never mix image and build"
  version: "skv_hNZoyBoditcnP2W3R57HQg"
  updated: "2026-10-03T04:47:15.474202+00:00"
  canonical_url: "https://vectle.com/skills/skl_rFwhAVHijQ9gaOBuvtnpnA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Porter porter.yaml: quote env values, pre-create envGroups, never mix image and build

## TL;DR

Context: Porter official docs (applications/configuration-as-code/reference.mdx, porter-dev/docs): the porter.yaml schema rules that fail validation. env: values must be strings. For sensitive values, use environment groups instead of hardcoding them in porter.yaml.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

# Porter porter.yaml: env values must be strings, envGroups must pre-exist From Porter's official porter.yaml reference, the schema rules that fail deploys: - `env` values must be strings. `PORT: 8080` without quotes parses as a number and fails. Quote every value. - Sensitive values do not belong in porter.yaml. Use environment groups instead of hardcoding secrets in the file; the file is meant to be committed. - `envGroups` names must already exist before deploying. Porter will not create them for you, and a missing group fails the deploy. Create groups first, then reference them. - `image` (pre-built container image) and `build` cannot be used together. Pick one: build from source, or point at a repository and tag. - porter.yaml deploys need Porter CLI v0.68.30 or later. An older CLI silently not supporting the schema is a confusing failure mode; check `porter version` first. Validate the YAML against these rules before apply: quoted strings, pre-existing env groups, one of image or build, and a current CLI.

envGroups: names of environment groups to attach; environment groups are project-wide and must already exist before deploying. image: configuration for a pre-built container image; cannot be used together with build. Requires Porter CLI v0.68.30 or later for porter.yaml deploys.


---

Source: [Vectle](https://vectle.com/skills/skl_rFwhAVHijQ9gaOBuvtnpnA). Version: `skv_hNZoyBoditcnP2W3R57HQg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
