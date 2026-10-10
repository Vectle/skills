---
name: "in-asp-net-core-can-t-export-traces-fr-8f43675913228b14"
description: "In Asp.Net Core Can't export traces from OpenTelemetry exporter to elastic apm. After some search, reinstall and debug I found my fault. Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_XnOEMS3pPUDxU1r-cV0kfQ"
  title: "In Asp.Net Core Can't export traces from OpenTelemetry exporter to elastic apm"
  version: "skv_fAOKn3_QTIWo9CJ8EcullA"
  updated: "2026-10-03T14:00:55.503403+00:00"
  canonical_url: "https://vectle.com/skills/skl_XnOEMS3pPUDxU1r-cV0kfQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

After some search, reinstall and debug I found my fault. I Downloaded AspNetCore sample from OpenTelemetry .net samples and I found that I should add next line in my code: AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);

## The error

```text
In Asp.Net Core Can't export traces from OpenTelemetry exporter to elastic apm
```

## Fix

1. After some search, reinstall and debug I found my fault.
   Expected: You get the expected result; the problem is gone.
2. I Downloaded AspNetCore sample from OpenTelemetry .net samples and I found that I should add next line in my code: AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
   Expected: You get the expected result; the problem is gone.
3. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error.
- The symptom matches: In Asp.Net Core Can't export traces from OpenTelemetry exporter to elastic apm.

## When NOT to use

- A different error message; the cause here is specific to this error.
- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source. Source: https://stackoverflow.com/questions/71222918/in-asp-net-core-cant-export-traces-from-opentelemetry-exporter-to-elastic-a.

## Variant phrasings

### In Asp.Net Core Can't export traces from OpenTelemetry exporter to elastic apm

## Why it happens

Recently, I found OpenTelemetry, and I like to use it in my application. First, I created a new Asp.Net Core 5 web API and exported traces on the console. After that, I tried OpenTelemetry.Exporter.OpenTelemetryProtocol for export traces to Elastic APM, but I couldn't see log or traces at elastic. In 3rd step, I used Elastic.Apm.NetCoreAll, and I successfully sent traces to APM. So I think my Elastic APM configurations are correct, but some configurations at asp are wrong. Ca

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/71222918/in-asp-net-core-cant-export-traces-from-opentelemetry-exporter-to-elastic-apm

---

Source: [Vectle](https://vectle.com/skills/skl_XnOEMS3pPUDxU1r-cV0kfQ). Version: `skv_fAOKn3_QTIWo9CJ8EcullA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
