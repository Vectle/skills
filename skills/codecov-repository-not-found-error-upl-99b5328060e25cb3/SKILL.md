---
name: "codecov-repository-not-found-error-upl-99b5328060e25cb3"
description: "codecov repository not found error upload fails"
metadata:
  skill_id: "skl_hKIdxfhwmW_7TQxlGYGj2g"
  title: "codecov repository not found error upload fails"
  version: "skv_kYpsoGC7IZMOv5CX03zfuA"
  updated: "2026-11-10T01:55:42.2388+00:00"
  canonical_url: "https://vectle.com/skills/skl_hKIdxfhwmW_7TQxlGYGj2g"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

From the failing CI log, find the repository slug the uploader detected (owner and repository name) and how it detected it (git remote or CI environment).

Compare that slug with the repository URL on the code host, character for character, including the owner.

Open Codecov for that owner and confirm the repository is listed and activated.

Check that the upload credential configured in CI belongs to this repository (repository upload credential from this repo settings in Codecov, or the global credential of the owning organisation).

Validate the Codecov config file if the repo has one, using the config validation endpoint or the uploader dry run offered by your uploader version.

Re-run the upload step on the same commit.

---

Source: [Vectle](https://vectle.com/skills/skl_hKIdxfhwmW_7TQxlGYGj2g). Version: `skv_kYpsoGC7IZMOv5CX03zfuA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
