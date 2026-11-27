---
name: "ffmpeg-chapter-metadata-error-fails-to-7d92493767a41f4b"
description: "ffmpeg chapter metadata error fails to embed chapters in mp4"
metadata:
  skill_id: "skl_tHw69GKrq5UeAZhr-eYDMA"
  title: "ffmpeg chapter metadata error fails to embed chapters in mp4"
  version: "skv_kwhqOEgIdlfZJuRIbnutvA"
  updated: "2026-11-27T13:52:04.200169+00:00"
  canonical_url: "https://vectle.com/skills/skl_tHw69GKrq5UeAZhr-eYDMA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Check your metadata file format. It must start with the ffmetadata header line and contain CHAPTER blocks each with a timebase, start, end, and title.

Run ffprobe on the output file and look for a chapters section.

Re-run ffmpeg with the metadata file as the second input and add the option that maps chapters from that input, keeping the video and audio mappings explicit.

Avoid a second re-encode afterwards. If you must trim or remux, include the chapter copy option so chapters are carried over.

Open the final mp4 in a player that shows a chapter menu and jump between chapters.

---

Source: [Vectle](https://vectle.com/skills/skl_tHw69GKrq5UeAZhr-eYDMA). Version: `skv_kwhqOEgIdlfZJuRIbnutvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
