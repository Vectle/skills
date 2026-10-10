---
name: "unable-to-import-module-main-no-module-6ff37b2c5182132a"
description: "Fixes Unable to import module 'main': No module named 'boto3' Use when Lambda invocation fails with Unable to import module ... No module named 'boto3' (or requests, etc.) Not for: the error names your own handler file (that is a packaging path problem, not boto3)"
metadata:
  skill_id: "skl_evmyrWS8QeYRAe2y5mVmAw"
  title: "Unable to import module 'main': No module named 'boto3'"
  version: "skv_UX4qLDrIX8WwQmJeePwQBQ"
  updated: "2026-10-03T04:40:47.336589+00:00"
  canonical_url: "https://vectle.com/skills/skl_evmyrWS8QeYRAe2y5mVmAw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix Unable to import module 'main': No module named 'boto3'

Lambda's Python runtime does not put boto3 on your function's import path the way local dev does. Package boto3 with your deployment zip (`pip install boto3 -t .`) or attach a Lambda layer containing boto3. Also double-check the handler string is `file.function` format.

## The exact error

```text
Unable to import module 'main': No module named 'boto3'
```

## Fix it

1. Bundle it: `pip install boto3 -t ./package`, copy your handler in, zip the package dir, upload.
   Expected: boto3 inside the zip

2. Or publish a layer: `mkdir python && pip install boto3 -t python/` then zip the python dir and attach the layer.
   Expected: function imports boto3 from the layer

3. Verify the handler setting is `main.lambda_handler` (file.function).
   Expected: Runtime.ImportModuleError gone

## When this applies

Lambda invocation fails with Unable to import module ... No module named 'boto3' (or requests, etc.)

## When this does NOT apply

the error names your own handler file (that is a packaging path problem, not boto3)

## Versions

AWS Lambda Python runtimes

## Why it happens

Lambda only guarantees the runtime plus stdlib; third-party deps must ship in the zip or a layer.

## Edge cases

Watch the 250MB unzipped deployment limit when bundling heavy deps.


---

Source: [Vectle](https://vectle.com/skills/skl_evmyrWS8QeYRAe2y5mVmAw). Version: `skv_UX4qLDrIX8WwQmJeePwQBQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
