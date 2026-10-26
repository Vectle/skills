---
name: "elastic-observability-apm-node-js-apm-b0d1a2f856312f48"
description: "Elastic Observability APM Node.js: 'APM Server transport error ECONNREFUSED'. Also check for 'Elastic APM agent disabled (active is false)' which means the active flag is set to false. Use when hitting this exact issue with Elastic Observability APM Node.js. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_f0N9IES6fK3vImOT9VBzrw"
  title: "Elastic Observability APM Node.js: 'APM Server transport error ECONNREFUSED'"
  version: "skv_wmLEq7hcQbJdVqTSfrVZ5g"
  updated: "2026-10-03T14:05:07.729323+00:00"
  canonical_url: "https://vectle.com/skills/skl_f0N9IES6fK3vImOT9VBzrw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.elastic.co/docs/troubleshoot/observability/apm-agent-nodejs/apm-nodejs-agent\"]"
---

## TL;DR

Also check for 'Elastic APM agent disabled (active is false)' which means the active flag is set to false. ECONNREFUSED means the agent cannot reach the APM server: check serverUrl, secretToken or apiKey config, and that the server is up from the agent's host.

## The error

```text
ECONNREFUSED'
```

## Fix

1. Also check for 'Elastic APM agent disabled (active is false)' which means the active flag is set to false.
   Expected: You see the expected output instead of the problem.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Elastic Observability APM Node.js.
- The symptom matches: 'APM Server transport error ECONNREFUSED'.

## When NOT to use

- A different error message from Elastic Observability APM Node.js; the cause here is specific to this error.
- Unrelated Elastic Observability APM Node.js issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Elastic Observability APM Node.js. Source: https://www.elastic.co/docs/troubleshoot/observability/apm-agent-nodejs/apm-nodejs-agent.

## Variant phrasings

### 'APM Server transport error ECONNREFUSED'
### ECONNREFUSED'

## Why it happens

Agent logs show APM Server transport error (ECONNREFUSED) and no data appears in Kibana.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://www.elastic.co/docs/troubleshoot/observability/apm-agent-nodejs/apm-nodejs-agent

---

Source: [Vectle](https://vectle.com/skills/skl_f0N9IES6fK3vImOT9VBzrw). Version: `skv_wmLEq7hcQbJdVqTSfrVZ5g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
