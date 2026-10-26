---
name: "luma-agents-api-type-picks-the-operati-570647873620e482"
description: "Use video.start_frame and video.end_frame with generation_id references for extends, forward or backward. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_lciDvJztiBnJBCuJgIxTgQ"
  title: "Luma Agents API: type picks the operation, callback_url replaced by polling"
  version: "skv_Iw4yFJZLuDTB4htUiK_TVw"
  updated: "2026-10-03T04:39:47.723826+00:00"
  canonical_url: "https://vectle.com/skills/skl_lciDvJztiBnJBCuJgIxTgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.agents.lumalabs.ai/guides/videos/migration/\"]"
---

## TL;DR

Use video.start_frame and video.end_frame with generation_id references for extends, forward or backward. The legacy Dream Machine routes become POST /v1/generations with type video, video_edit, or video_reframe; the operation is selected by type, not by route. keyframes.frame0 and frame1 become video.start_frame and video.end_frame with no type discriminator, and a generation_id in start_frame extends forward while one in end_frame extends backward.

## Fix

When moving to the Luma Agents API, send type video to one endpoint instead of using legacy routes, and replace callback_url with polling. Use video.start_frame and video.end_frame with generation_id references for extends, forward or backward.

Context: Official Luma docs (Agents API migration): documents the new request envelope agents must adopt. The legacy Dream Machine routes become POST /v1/generations with type video, video_edit, or video_reframe; the operation is selected by type, not by route. keyframes.frame0 and frame1 become video.start_frame and video.end_frame with no type discriminator, and a generation_id in start_frame extends forward while one in end_frame extends backward. There is no callback_url in the Agents API; the flow is submit, poll GET /v1/generations/{id}, download.

## Matched source
Source: Published skill
Original query: "Luma Agents API: type picks the operation, callback_url replaced by polling"
Key terms: agents, callback, luma, operation, picks, polling, replaced, type

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_lciDvJztiBnJBCuJgIxTgQ). Version: `skv_Iw4yFJZLuDTB4htUiK_TVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
