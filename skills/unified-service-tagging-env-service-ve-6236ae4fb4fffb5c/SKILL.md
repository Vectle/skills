---
name: "unified-service-tagging-env-service-ve-6236ae4fb4fffb5c"
description: "Set env, service, and version on everything (agent, tracers, logs) so metrics, traces, and logs join up. The Java tracer docs show the canonical three: dd.service, dd.env, dd.version. Not the full reference manual."
metadata:
  skill_id: "skl_mcRvWUd0Sr9rQp76wlLTWw"
  title: "Unified service tagging: env, service, version everywhere or APM stays a mess"
  version: "skv_9NmRTOOPCnTp9yCt1SwKKg"
  updated: "2026-10-03T04:47:23.524091+00:00"
  canonical_url: "https://vectle.com/skills/skl_mcRvWUd0Sr9rQp76wlLTWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Set env, service, and version on everything (agent, tracers, logs) so metrics, traces, and logs join up. The Java tracer docs show the canonical three: dd.service, dd.env, dd.version. Set them everywhere or you get three views of your system that refuse to join: the service catalog shows dupes, trace-to-log jumps 404, deploy tracking is empty. Host-level tags apply to every metric the agent emits. - Logs: the service field in your log config should equal the tracer service name.

# Unified service tagging: env, service, version on everything

Datadog correlates metrics, traces, and logs by three tags: `env`, `service`, `version`. Set them everywhere or you get three views of your system that refuse to join: the service catalog shows dupes, trace-to-log jumps 404, deploy tracking is empty.

## The triple

- `service`: the logical service name. Same string in every language, every host, every container for that service.
- `env`: prod, staging, dev. Keeps staging traces out of your prod monitors.
- `version`: the deploy version (git sha, semver). Powers deploy tracking and version-scoped monitors.

## Where to set them

- **Tracers**: `DD_SERVICE`, `DD_ENV`, `DD_VERSION` env vars, or the tracer-specific flags (`-Ddd.service` etc. for Java, init options for Node). The Java docs show all three on one command line.
- **Agent**: `tags:` in datadog.yaml, or `DD_TAGS` / `DD_ENV` env vars in containers. Host-level tags apply to every metric the agent emits.
- **Logs**: the `service` field in your log config should equal the tracer service name. Trace IDs get injected into logs (dd.logs.injection for Java, equivalents elsewhere) and the app joins them on service + trace id.
- **Lambda**: function env vars, same names.

## The discipline

1. Pick the service names once, write them down, enforce in code review. `checkout-api` vs `checkout_api` vs `CheckoutAPI` across three teams is three services in Datadog.
2. `env` values are a closed list: prod, staging, dev. Not `production`, `prod-us`, `Prod`.
3. `version` comes from CI, never hand-typed. A wrong version is worse than none because deploy markers lie.

## Verify

In APM, group services by env and version. One service, one row per env. In Logs, click a trace id and confirm it jumps to the trace. If either breaks, diff the tags: the mismatch is always a typo or a missing env var in one deploy path.

## When to use this

- This covers exactly what the title says: Unified service tagging.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Unified; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_mcRvWUd0Sr9rQp76wlLTWw). Version: `skv_9NmRTOOPCnTp9yCt1SwKKg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
