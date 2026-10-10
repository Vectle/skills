---
name: "datadog-lambda-monitoring-for-python-a-9c4b888b2d5d491e"
description: "For Lambda, Datadog wants the Lambda Extension layer on your function (metrics, traces, logs) with DD_API_KEY and DD_SITE set. The forwarder is for log shipping from CloudWatch, not a substitute for the extension."
metadata:
  skill_id: "skl_WkKKG20kr0YvjrLPlG3xyg"
  title: "Datadog Lambda monitoring for Python: attach the extension layer, not just the forwarder"
  version: "skv_A4IVRBdBMjm3ETIMJ4uplw"
  updated: "2026-10-03T05:54:52.812136+00:00"
  canonical_url: "https://vectle.com/skills/skl_WkKKG20kr0YvjrLPlG3xyg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** For Lambda, Datadog wants the Lambda Extension layer on your function (metrics, traces, logs) with DD_API_KEY and DD_SITE set. The forwarder is for log shipping from CloudWatch, not a substitute for the extension. Attach the Datadog Extension layer to your function. Use the latest version from the docs, not a version you remember.

# Datadog on Lambda (Python): the extension layer is the setup

Two Datadog pieces exist for Lambda and agents mix them up: the **Lambda Extension** (runs alongside your function, ships telemetry directly) and the **Forwarder** (a separate Lambda that tails CloudWatch log groups). For metrics, traces, and enhanced Lambda metrics, you want the extension.

## Setup

1. Attach the Datadog Extension layer to your function. The layer ARN pattern is `arn:aws:lambda:[region]:464622532012:layer:Datadog-Extension:[version]` plus the runtime layer for your language. Use the latest version from the docs, not a version you remember.
2. Set function env vars: `DD_API_KEY` (use Secrets Manager or KMS in prod; plaintext key in the template is flagged in the docs as quick-testing only) and `DD_SITE` matching your org region.
3. Enable the pieces you want: `DD_TRACE_ENABLED=true` for APM, `DD_LOGS_ENABLED` / log forwarding for logs, `DD_ENHANCED_METRICS` for the enhanced Lambda metrics.

The docs show the CloudFormation macro and SAM transform that do all of this for you if you are in CloudFormation/SAM land. One macro install per region, then annotate functions.

## Extension vs forwarder, concretely

- Extension: in-account, no log-group subscription needed, ships metrics/traces/logs straight to Datadog. Cold start cost is small but real; keep the layer version current.
- Forwarder: needed when you want CloudWatch Logs (from any source, not just Lambda) shipped to Datadog, or when you cannot touch the function. It subscribes to log groups, which has account-level subscription filter limits worth knowing about.

You can run both: extension for telemetry, forwarder for the log groups the extension does not cover.

## Verify

Invoke the function, then check Serverless, Functions in the app. You want invocations, duration, and cold starts charting. If the function shows nothing: check the layer actually attached (wrong region in the ARN is common), then the env vars, then the site. APM traces need the tracer library in your code too, the extension alone does not instrument Python.

## When to use this

- This covers exactly what the title says: Datadog Lambda monitoring for Python.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_WkKKG20kr0YvjrLPlG3xyg). Version: `skv_A4IVRBdBMjm3ETIMJ4uplw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
