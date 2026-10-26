---
name: "attributeerror-nonrecordingspan-object-41edf91c80caffdf"
description: "Fixes AttributeError: 'NonRecordingSpan' object has no attribute 'attributes' in Logfire by calling logfire.configure() before creating any spans. Use when spans behave as no-op placeholders. Not for Logfire setups that are already configured and recording normally."
metadata:
  skill_id: "skl_Z3FjX-p5cnhRT-pVfrMqVw"
  title: "AttributeError: 'NonRecordingSpan' object has no attribute 'attributes'. Did you mean: 'set_attributes'?"
  version: "skv_BZOUHFvj1suvHFkTV5ImkA"
  updated: "2026-10-03T04:36:20.202083+00:00"
  canonical_url: "https://vectle.com/skills/skl_Z3FjX-p5cnhRT-pVfrMqVw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pydantic/logfire/issues/1484\"]"
---

Fix first: call `logfire.configure()` before you create any spans. The error means Logfire was never configured, so every span is a no-op NonRecordingSpan placeholder.

```text
AttributeError: 'NonRecordingSpan' object has no attribute 'attributes'. Did you mean: 'set_attributes'?
```

1. Call `logfire.configure()` at startup, before any span is created.
2. Then use `span.set_attributes(...)` as normal. Expected: no AttributeError, and attributes land on the span.

When to use: you see NonRecordingSpan errors, typically in tests where configuration never ran.

When not to use: Logfire is already configured and spans record fine (something else is wrong then).

Compatibility: Logfire (Python). Maintainer-identified.

Variants:
- "logfire NonRecordingSpan attributes"
- "logfire span no-op placeholder"
- "Did you mean set_attributes logfire"

Root cause: without configure(), Logfire hands out NonRecordingSpan no-ops, which dont implement the attributes accessor.

Edge cases: in tests, make sure configure() runs before the code under test creates spans. The original report surfaced confusingly because a mock was raising inside a span context manager.

---

Source: [Vectle](https://vectle.com/skills/skl_Z3FjX-p5cnhRT-pVfrMqVw). Version: `skv_BZOUHFvj1suvHFkTV5ImkA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
