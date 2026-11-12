---
name: "set-output-deprecated-error-github-act-193334accdf5e8fb"
description: "set-output deprecated error GitHub Actions workflow fails"
metadata:
  skill_id: "skl_43-jBGoup8JivyvXdJJcPw"
  title: "set-output deprecated error GitHub Actions workflow fails"
  version: "skv_sN94f8elWMeQcrxmHGIpKA"
  updated: "2026-11-12T01:56:40.87221+00:00"
  canonical_url: "https://vectle.com/skills/skl_43-jBGoup8JivyvXdJJcPw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Search the workflow files and any local actions they use for the literal text set-output and list every occurrence with its step name.

For a single line value, replace the print with a shell line that appends the name and value to the file named by GITHUB_OUTPUT.

For a multiline value, use the delimiter form: write the name and a unique delimiter, then the value, then the delimiter again, all appended to the same output file.

Check composite and reusable actions called by the workflow for the same command inside their own steps.

Push the change and rerun the workflow, then read the step log and a downstream step that consumes the output.

---

Source: [Vectle](https://vectle.com/skills/skl_43-jBGoup8JivyvXdJJcPw). Version: `skv_sN94f8elWMeQcrxmHGIpKA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
