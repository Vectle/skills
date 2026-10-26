---
name: "gladia-live-transcription-format-must-050629e1435b353a"
description: "Shows how to fix gladia live transcription: format must match exactly, stopRecording vs endSession, reconnect to same URL. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_LokIDb7kPZ_wVWVSffgHzw"
  title: "Gladia live transcription: format must match exactly, stopRecording vs endSession, reconnect to same URL"
  version: "skv_zKOZ7-p9WQClYYwEPZfOng"
  updated: "2026-10-03T14:07:10.199811+00:00"
  canonical_url: "https://vectle.com/skills/skl_LokIDb7kPZ_wVWVSffgHzw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/gladiaio/skills/blob/HEAD/plugins/gladia/skills/gladia-live-transcription/SKILL.md\"]"
---

## TL;DR

Set endpointing to 0.05-0.1 for voice agents, 0.2-0.4 for live subtitles. On a dropped socket, reuse the same WebSocket URL.

## Steps

1. When opening a Gladia live session, double check encoding, sample_rate, bit_depth, and channels against the real stream before sending audio. Always call stopRecording when done so post-processing runs, and wire cleanup into error handlers so a crashed stream does not hang until the 3-hour timeout. On a dropped socket, reuse the same WebSocket URL. Set endpointing to 0.05-0.1 for voice agents, 0.2-0.4 for live subtitles.

## When to use

You are seeing this: When opening a Gladia live session, double check encoding, sample_rate, bit_depth, and channels against the real stream before sending audio. Use this skill when you run into "Gladia live transcription: format must match exactly, stopRecording vs endSession, reconnect to same URL".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 0.05-0.1, agents 0.2-0.4. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_LokIDb7kPZ_wVWVSffgHzw). Version: `skv_zKOZ7-p9WQClYYwEPZfOng`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
