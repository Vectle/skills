---
name: "highlight-redact-sensitive-network-bod-cdcc06409cb19e51"
description: "Keep network recording on for debuggability and redact the sensitive keys instead: configure redaction for fields like auth tokens and PII in request and response bodies while leaving the rest of the traffic recorded. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_UMBgwgRhimEyIDwziyY5lA"
  title: "Highlight: redact sensitive network body keys instead of disabling network recording"
  version: "skv_5POutBOR4Q96HKCU3l2fNQ"
  updated: "2026-10-03T05:34:24.458145+00:00"
  canonical_url: "https://vectle.com/skills/skl_UMBgwgRhimEyIDwziyY5lA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Keep network recording on for debuggability and redact the sensitive keys instead: configure redaction for fields like auth tokens and PII in request and response bodies while leaving the rest of the traffic recorded. If replays crash or feel sluggish, remember request body sizes are capped automatically, so look at response sizes and DOM complexity before blaming the SDK. Version 6.3.0 added support for redacting specific request and response body keys while recording everything else, and 6.2.

## Fix

Keep network recording on for debuggability and redact the sensitive keys instead: configure redaction for fields like auth tokens and PII in request and response bodies while leaving the rest of the traffic recorded. If replays crash or feel sluggish, remember request body sizes are capped automatically, so look at response sizes and DOM complexity before blaming the SDK.

Context: Highlight firstload SDK changelog documents the network-recording privacy option teams miss. Version 6.3.0 added support for redacting specific request and response body keys while recording everything else, and 6.2.0 limited the size of recorded network request bodies to prevent replay-time crashes. Teams that disable network recording entirely for privacy lose API debugging context they could have kept with key-level redaction.

## Matched source
Source: Published skill
Original query: "Highlight: redact sensitive network body keys instead of disabling network recording"
Key terms: body, disabling, highlight, instead, keys, network, recording, redact, sensitive

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_UMBgwgRhimEyIDwziyY5lA). Version: `skv_5POutBOR4Q96HKCU3l2fNQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
