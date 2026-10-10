---
name: "logz-io-node-js-tracing-use-the-right-69cc076c722293aa"
description: "If no traces appear, set the OTLP endpoint explicitly to your collector host with port 4317 for gRPC or 4318 plus the v1 traces path for HTTP, and make sure the exporter protocol matches. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_PJnQJhuwUS-tZngY8rxQMQ"
  title: "Logz.io Node.js tracing: use the right OTLP endpoint and protocol or get zero spans"
  version: "skv_5nfoWqj_tI5RaYad3iQ7-g"
  updated: "2026-10-03T04:41:00.717564+00:00"
  canonical_url: "https://vectle.com/skills/skl_PJnQJhuwUS-tZngY8rxQMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

If no traces appear, set the OTLP endpoint explicitly to your collector host with port 4317 for gRPC or 4318 plus the v1 traces path for HTTP, and make sure the exporter protocol matches. Turn on debug logging in the collector to see whether exports return 200 or fail, and compare spans received against spans sent on the collector metrics endpoint to find where the pipeline drops them.

## Fix

If no traces appear, set the OTLP endpoint explicitly to your collector host with port 4317 for gRPC or 4318 plus the v1 traces path for HTTP, and make sure the exporter protocol matches. Turn on debug logging in the collector to see whether exports return 200 or fail, and compare spans received against spans sent on the collector metrics endpoint to find where the pipeline drops them.

Context: Official Logz.io Node.js tracing docs document the exporter misconfiguration that produces zero traces. The OTLP receiver needs the right protocol and endpoint: gRPC on port 4317 or HTTP on port 4318 with the v1 traces path. A wrong exporter, protocol, or endpoint silently yields no spans. The docs recommend enabling debug logs in the collector config to see the HTTP status of each export attempt, and checking the collector metrics endpoint for spans received versus sent.

## Matched source
Source: Published skill
Original query: "Logz.io Node.js tracing: use the right OTLP endpoint and protocol or get zero spans"
Key terms: endpoint, logz, node, otlp, protocol, right, spans, tracing, zero

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_PJnQJhuwUS-tZngY8rxQMQ). Version: `skv_5nfoWqj_tI5RaYad3iQ7-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
