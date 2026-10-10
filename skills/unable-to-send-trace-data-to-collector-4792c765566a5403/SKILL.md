---
name: "unable-to-send-trace-data-to-collector-4792c765566a5403"
description: "Fixes 'Unable to send trace data to collector' with ReadUint64 errors in the opentelemetry-web OTLP HTTP exporter by upgrading past the 0.44 regression (64-bit timestamps serialized as objects instead of strings). Use when the web example cant ship traces to the collector. Not for gRPC exporter issues or collector-side misconfigurations."
metadata:
  skill_id: "skl_EjgKo1dBeJhRaYQi2AAMNQ"
  title: "Unable to send trace data to collector using 'examples/opentelemetry-web'"
  version: "skv_xkXvS1RkNCjZwH3uJiHWuA"
  updated: "2026-10-03T04:42:23.038653+00:00"
  canonical_url: "https://vectle.com/skills/skl_EjgKo1dBeJhRaYQi2AAMNQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: upgrade to the latest 0.44.x or newer. Version 0.44 broke the OTLP HTTP exporter by serializing 64-bit timestamps as objects instead of strings, so the collector threw ReadUint64 errors. The fix uses BigInt serialization (PR #4220); the contributor tested the latest version and confirmed it works.

```text
Unable to send trace data to collector using 'examples/opentelemetry-web'
... ReadUint64 errors
```

1. Upgrade your OpenTelemetry JS packages to the latest 0.44.x or newer.
2. Re-run the opentelemetry-web example and send traces. Expected: traces arrive at the collector with no ReadUint64 errors.

When to use: the opentelemetry-web example cant send trace data to the collector and you see ReadUint64 errors.

When not to use: gRPC exporter problems, or a collector that was never configured to receive OTLP HTTP in the first place.

Compatibility: @opentelemetry/exporter-trace-otlp-http 0.44.x+, opentelemetry-web example.

Variants:
- "opentelemetry web ReadUint64"
- "otlp http exporter 64-bit timestamp"
- "unable to send trace data to collector opentelemetry"

Root cause: a regression in 0.44 serialized 64-bit timestamps as objects instead of strings, which the collector could not parse.

Edge cases: if you pinned 0.44.0 exactly, any 0.44.x patch with the BigInt serialization fix works; latest is fine.

---

Source: [Vectle](https://vectle.com/skills/skl_EjgKo1dBeJhRaYQi2AAMNQ). Version: `skv_xkXvS1RkNCjZwH3uJiHWuA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
