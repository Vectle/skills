---
name: "apps-script-bigquery-calls-fail-when-t-aaefc227436ba712"
description: "The accepted fix: the new copy was bound to a different Cloud project, and the BigQuery API had to be enabled on that project via Advanced Google Services and the Cloud console. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_zf-aRKMZZxcLQcsnUzz5gQ"
  title: "Apps Script BigQuery calls fail when the API isnt enabled on the project"
  version: "skv_FJB6zKegUsNyIUD4Q8TipA"
  updated: "2026-10-03T05:42:03.695369+00:00"
  canonical_url: "https://vectle.com/skills/skl_zf-aRKMZZxcLQcsnUzz5gQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/43234769/project-project-id-is-not-found-and-cannot-be-used-for-api-calls\"]"
---

## TL;DR

The accepted fix: the new copy was bound to a different Cloud project, and the BigQuery API had to be enabled on that project via Advanced Google Services and the Cloud console.

## Fix

When Apps Script throws 'project not found and cannot be used for API calls', open Resources, Advanced Google Services and follow the link to the Cloud console for the bound project, then enable the API there. Duplicated scripts bind to new projects silently, so the API enablement doesnt carry over.

Context: Stack Overflow #43234769 (accepted answer, 14 votes): duplicating a sheet that called the BigQuery API produced 'Project not found and cannot be used for API calls'. The accepted fix: the new copy was bound to a different Cloud project, and the BigQuery API had to be enabled on that project via Advanced Google Services and the Cloud console.

## Matched source
Source: Published skill
Original query: "Apps Script BigQuery calls fail when the API isnt enabled on the project"
Key terms: apps, bigquery, calls, enabled, fail, isnt, project, script

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_zf-aRKMZZxcLQcsnUzz5gQ). Version: `skv_FJB6zKegUsNyIUD4Q8TipA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
