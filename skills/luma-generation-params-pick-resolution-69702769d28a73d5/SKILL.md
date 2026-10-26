---
name: "luma-generation-params-pick-resolution-69702769d28a73d5"
description: "Set explicit resolution and duration on Luma generations instead of relying on defaults. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_Vdr_qVHzk2Bs7-KlHGi9kw"
  title: "Luma generation params: pick resolution, look up concepts, check keyframe conflicts"
  version: "skv_mh3E1pf1tQ_Pws_pToaKDA"
  updated: "2026-10-03T04:39:11.61476+00:00"
  canonical_url: "https://vectle.com/skills/skl_Vdr_qVHzk2Bs7-KlHGi9kw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.lumalabs.ai/docs/python-video-generation\"]"
---

## TL;DR

Set explicit resolution and duration on Luma generations instead of relying on defaults. Look up available style concepts via the concepts/list endpoint, and check parameter conflicts before combining keyframes with loop or other controls. Resolution options are 540p, 720p, 1080, and 4k; duration 5s is a common pick.

## Fix

Set explicit resolution and duration on Luma generations instead of relying on defaults. Look up available style concepts via the concepts/list endpoint, and check parameter conflicts before combining keyframes with loop or other controls.

Context: Official Luma docs (Python video generation): documents the generation parameters agents overlook. Resolution options are 540p, 720p, 1080, and 4k; duration 5s is a common pick. The concepts parameter accepts style keys, and the concepts/list endpoint returns what is available. loop can combine with an image keyframe in frame0, but keyframes collide with some other controls, so check the generation guide before stacking parameters.

## Matched source
Source: Published skill
Original query: "Luma generation params: pick resolution, look up concepts, check keyframe conflicts"
Key terms: check, concepts, conflicts, generation, keyframe, look, luma, params, pick, resolution

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_Vdr_qVHzk2Bs7-KlHGi9kw). Version: `skv_mh3E1pf1tQ_Pws_pToaKDA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
