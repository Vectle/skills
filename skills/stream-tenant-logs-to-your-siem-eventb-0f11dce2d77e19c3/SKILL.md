---
name: "stream-tenant-logs-to-your-siem-eventb-0f11dce2d77e19c3"
description: "Tenant logs have retention limits; log streams export events in near real time to your own systems. Pick the destination that matches your stack, set filters, and handle PII deliberately. Not the full reference manual."
metadata:
  skill_id: "skl_KReTzdLascJIyKRQVS3wNw"
  title: "Stream tenant logs to your SIEM: EventBridge, Datadog, Splunk, webhooks"
  version: "skv_LVQRUlK-TRv6j1nohQus1A"
  updated: "2026-10-03T04:49:14.382851+00:00"
  canonical_url: "https://vectle.com/skills/skl_KReTzdLascJIyKRQVS3wNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Tenant logs have retention limits; log streams export events in near real time to your own systems. Pick the destination that matches your stack, set filters, and handle PII deliberately. Log streams to SIEM 1. Create and configure - Webhook streams: give Auth0 your HTTPS endpoint; it POSTs JSON batches.

# Log streams to SIEM

## 1. Pick the destination

Dashboard > Monitoring > Streams > Create. Supported: Amazon EventBridge, Azure Event Grid, Datadog, Splunk, Sumo Logic, Segment, webhooks (custom HTTP), and Marketplace integrations (Elastic, Panther, Pangea, etc.). Auth0 ships dashboard templates for Datadog and a Splunk app.

## 2. Create and configure

- Webhook streams: give Auth0 your HTTPS endpoint; it POSTs JSON batches. Your endpoint must respond 2xx quickly; Auth0 retries with backoff on failure.
- EventBridge: Auth0 puts events on your event bus; attach your own rules/targets.
- Set filters: stream only the event types you need (auth events, admin events). Fewer events = lower cost and less PII surface.

## 3. PII

Streams can carry PII (emails, IPs). The stream settings include PII obfuscation options. Decide before enabling: hash or drop fields your SIEM does not need. You become the data controller for exported data.

## 4. Health

Monitor the stream health in the dashboard: failed deliveries, paused streams. A paused stream does not backfill everything; treat stream health as a production alert, not a nice-to-have.

## What streams are for

Security monitoring (failed logins, anomaly events), audit trails, and product analytics (signup funnels). They are not a backup of tenant logs for debugging old incidents; retention in your SIEM is your retention.

## Checklist

- Filters set, PII policy decided, health alerted.
- Do not use streams as your only incident tool; keep tenant-log search skills handy too.

## When to use this

- This covers exactly what the title says: Stream tenant logs to your SIEM.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Stream; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Stream behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_KReTzdLascJIyKRQVS3wNw). Version: `skv_LVQRUlK-TRv6j1nohQus1A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
