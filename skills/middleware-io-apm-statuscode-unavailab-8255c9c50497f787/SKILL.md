---
name: "middleware-io-apm-statuscode-unavailab-8255c9c50497f787"
description: "Middleware.io APM: StatusCode.UNAVAILABLE exporting to the loopback address. If you run host-based, install and run the Middleware Agent. Use when hitting this exact issue with Middleware.io APM. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_-cbNTxn3wXd9htLCjBOvdw"
  title: "Middleware.io APM: StatusCode.UNAVAILABLE exporting to the loopback address"
  version: "skv_1pQIkP_xAzHpqXQUZzCwvA"
  updated: "2026-10-03T13:59:32.754837+00:00"
  canonical_url: "https://vectle.com/skills/skl_-cbNTxn3wXd9htLCjBOvdw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.middleware.io/apm-configuration/troubleshooting\"]"
---

## TL;DR

If you run host-based, install and run the Middleware Agent. If you are on serverless or containers, configure the APM SDK to send data directly to Middleware servers instead of the loopback address. The SDK is configured for a host-based setup but there is no Middleware agent listening locally.

## Fix

1. If you run host-based, install and run the Middleware Agent.
   Expected: You get the expected result; the problem is gone.
2. If you are on serverless or containers, configure the APM SDK to send data directly to Middleware servers instead of the loopback address.
   Expected: You get the expected result; the problem is gone.
3. In Docker, host-level metrics should go through the mw-host-agent sidecar image rather than embedding the agent install in the app container.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are setting up or using this Middleware.io APM feature.
- The symptom matches: StatusCode.UNAVAILABLE exporting to the loopback address.

## When NOT to use

- Unrelated Middleware.io APM issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Middleware.io APM. Source: https://docs.middleware.io/apm-configuration/troubleshooting.

## Variant phrasings

### StatusCode.UNAVAILABLE exporting to the loopback address

## Why it happens

The OTel exporter logs 'Transient error StatusCode.UNAVAILABLE encountered while exporting logs to the loopback address, retrying' and no telemetry appears.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://docs.middleware.io/apm-configuration/troubleshooting

---

Source: [Vectle](https://vectle.com/skills/skl_-cbNTxn3wXd9htLCjBOvdw). Version: `skv_1pQIkP_xAzHpqXQUZzCwvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
