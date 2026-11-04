---
name: "dependabot-exclude-paths-not-working-u-541eb8108ec5b2fc"
description: "dependabot exclude paths not working: updates still open for excluded directory"
metadata:
  skill_id: "skl_k-uZnbBkCSnD9mgKNXzWZA"
  title: "dependabot exclude paths not working: updates still open for excluded directory"
  version: "skv_DGss2J_boQ2225d0ec_DVw"
  updated: "2026-11-04T14:05:45.949335+00:00"
  canonical_url: "https://vectle.com/skills/skl_k-uZnbBkCSnD9mgKNXzWZA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Identify whether the unwanted PRs are version updates or security updates by reading the PR label and branch name in the repository.

Open the dependabot configuration and find the update entry whose package ecosystem and directory match the PR exactly, including a leading slash on the directory.

Check the ignore rule inside that entry: the dependency name must match the manifest name exactly, and a version rule must use the supported condition syntax for ignoring all versions or a range.

Validate the whole file with a YAML parser and the Dependabot configuration checker, since a silent syntax error makes the whole file ignored.

Close the already open unwanted PRs with a comment noting the exclusion; Dependabot does not auto-close version PRs when a new ignore rule lands.

Trigger a fresh Dependabot check from the insights dependency graph page or wait for the next scheduled run.

---

Source: [Vectle](https://vectle.com/skills/skl_k-uZnbBkCSnD9mgKNXzWZA). Version: `skv_DGss2J_boQ2225d0ec_DVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
