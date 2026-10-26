---
name: "jira-api-transitions-are-per-issue-lis-23955140efd63fa5"
description: "When you need the full set of Jira transitions, dont loop over issues calling the transitions endpoint per issue. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_ReHuU1vjaP6z2TklxgOkDQ"
  title: "Jira API: transitions are per issue, list them all via project statuses"
  version: "skv_Xp95-ViYWgKS-f287PniwA"
  updated: "2026-10-03T05:00:17.511354+00:00"
  canonical_url: "https://vectle.com/skills/skl_ReHuU1vjaP6z2TklxgOkDQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/31928540/listing-all-jira-transitions-via-api\"]"
---

## TL;DR

When you need the full set of Jira transitions, dont loop over issues calling the transitions endpoint per issue. Hit the project statuses endpoint once and walk the statuses arrays per issue type. Note the transitions endpoint is still what you use to actually move a specific issue, since available transitions depend on its current status.

## Fix

When you need the full set of Jira transitions, dont loop over issues calling the transitions endpoint per issue. Hit the project statuses endpoint once and walk the statuses arrays per issue type. Note the transitions endpoint is still what you use to actually move a specific issue, since available transitions depend on its current status.

Context: Stack Overflow #31928540 (accepted answer, 15 votes): the asker wanted a cheat sheet of all transition names but the API only lists transitions per issue. The accepted answer: call /rest/api/2/project/{projectIdOrKey}/statuses, which returns every issue type with its statuses array.

## Matched source
Source: Published skill
Original query: "Jira API: transitions are per issue, list them all via project statuses"
Key terms: issue, jira, list, project, statuses, them, transitions

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_ReHuU1vjaP6z2TklxgOkDQ). Version: `skv_Xp95-ViYWgKS-f287PniwA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
