---
name: "hex-scheduled-runs-execute-the-publish-f0d7f18a4d28980a"
description: "Check the plan limits too: Professional allows only one scheduled run per project. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_0F9_Jm47irfWOVumtZQVPg"
  title: "Hex scheduled runs execute the published app, never the draft"
  version: "skv_-H9JSW5x-LP7Fq7FDIRO1w"
  updated: "2026-10-03T05:59:49.569086+00:00"
  canonical_url: "https://vectle.com/skills/skl_0F9_Jm47irfWOVumtZQVPg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://learn.hex.tech/docs/share-insights/scheduled-runs-and-notifications\"]"
---

## TL;DR

Check the plan limits too: Professional allows only one scheduled run per project. You must publish before the schedule will pick up your changes. Maximum frequency is hourly, and scheduling is gated by plan (Professional is limited to one scheduled run per project).

## Fix

When an agent sets up Hex automation, always publish the app first and verify the published version contains the intended cells: a scheduled run against an unpublished draft silently runs stale code. If you need the agent to answer fresh questions on a schedule, use Tasks, not scheduled app runs. Check the plan limits too: Professional allows only one scheduled run per project.

Context: Hex docs (scheduled runs): scheduled runs always execute the currently published version of the app, never the draft. You must publish before the schedule will pick up your changes. Maximum frequency is hourly, and scheduling is gated by plan (Professional is limited to one scheduled run per project). To schedule the Hex agent itself against a fresh prompt instead of re-running an app, use Tasks.

## Matched source
Source: Published skill
Original query: "Hex scheduled runs execute the published app, never the draft"
Key terms: draft, execute, never, published, runs, scheduled

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_0F9_Jm47irfWOVumtZQVPg). Version: `skv_-H9JSW5x-LP7Fq7FDIRO1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
