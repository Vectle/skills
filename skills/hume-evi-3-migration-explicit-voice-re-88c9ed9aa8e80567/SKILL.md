---
name: "hume-evi-3-migration-explicit-voice-re-88c9ed9aa8e80567"
description: "Update your WebSocket message handling to read prosody scores from assistant_prosody messages and join them to assistant_message on id. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_eqvAwfpKIpq1KQsOhm38gg"
  title: "Hume EVI 3 migration: explicit voice required, prosody moved to its own message"
  version: "skv_ncgRmNp9_h1EXU1bfZJ1Rg"
  updated: "2026-10-03T05:30:38.309093+00:00"
  canonical_url: "https://vectle.com/skills/skl_eqvAwfpKIpq1KQsOhm38gg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://dev.hume.ai/changelog\"]"
---

## TL;DR

Update your WebSocket message handling to read prosody scores from assistant_prosody messages and join them to assistant_message on id. Do not rely on EVI 1 or 2 endpoints; they are deprecated. EVI 1 and 2 were deprecated on August 30, 2025; EVI 3 is enabled with evi_version 3 in the config.

## Fix

When migrating to EVI 3, set evi_version 3, pick an explicit voice from the Voice Library, and drop any legacy EVI 2 voice references. Update your WebSocket message handling to read prosody scores from assistant_prosody messages and join them to assistant_message on id. Do not rely on EVI 1 or 2 endpoints; they are deprecated.

Context: Official Hume changelog (July 18, 2025 entry): documents the EVI 3 breaking changes agents hit when upgrading. EVI 1 and 2 were deprecated on August 30, 2025; EVI 3 is enabled with evi_version 3 in the config. A voice must now be explicitly specified in every EVI 3 config, default voices are gone, and legacy EVI 2 Base Voices and Custom Voices are not supported, only Voice Library voices and ones you design or clone. Assistant prosody scores moved out of the assistant_message into a dedicated assistant_prosody message, linked back via the id field, so parsers reading prosody from assistant_message silently get nothing.

## Matched source
Source: Published skill
Original query: "Hume EVI 3 migration: explicit voice required, prosody moved to its own message"
Key terms: explicit, hume, message, migration, moved, prosody, required, voice

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_eqvAwfpKIpq1KQsOhm38gg). Version: `skv_ncgRmNp9_h1EXU1bfZJ1Rg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
