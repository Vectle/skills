---
name: "feature-add-azure-application-insights-6319b163726a0b7f"
description: "Shows how to fix \ud83d\ude80 Feature: Add Azure Application Insights as an open telemetry destination. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_ZKXDCDUGJdKA6ZQvlfaM-A"
  title: "\ud83d\ude80 Feature: Add Azure Application Insights as an open telemetry destination"
  version: "skv_VUghGNh1sYr-mAU4n1ertQ"
  updated: "2026-10-03T14:14:21.089413+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZKXDCDUGJdKA6ZQvlfaM-A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/traceloop/openllmetry/issues/93\"]"
---

## TL;DR

I was going to add links to Azure documentation for OTEL + App Insights...

## Steps

1. What was reported:
Issue traceloop/openllmetry#93 (closed, 12 comments): ### Which component is this feature for? OpenAI Instrumentation ### 🔖 Feature description In addition to the [destinations currently supported](https://www.traceloop.com/docs/python-sdk/exporting) to catch traces, it would be great to extend and include Azure Application Insights. OpenTelemetry is a key recommendation for almost any solution deployed on Azure as they should be tracking traces and metrics, and it would be great to have native support. I was going to add links to Azure documentation for OTEL + App Insights...

2. What works:
[drewby (commenter)]: To export Traceloop traces to Azure Application Insights, set the APPLICATIONINSIGHTS_CONNECTION_STRING env var and pass AzureMonitorTraceExporter() to Traceloop.init; you can then omit the connection string from the constructor. The reporter documented this in the docs repo and closed the issue.

## When to use

You are seeing this: What was reported: Issue traceloop/openllmetry#93 (closed, 12 comments): ### Which component is this feature for? Use this skill when you run into "🚀 Feature: Add Azure Application Insights as an open telemetry destination".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://www.traceloop.com/docs/python-sdk/exporting


---

Source: [Vectle](https://vectle.com/skills/skl_ZKXDCDUGJdKA6ZQvlfaM-A). Version: `skv_VUghGNh1sYr-mAU4n1ertQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
