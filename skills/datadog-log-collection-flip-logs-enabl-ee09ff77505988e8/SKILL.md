---
name: "datadog-log-collection-flip-logs-enabl-ee09ff77505988e8"
description: "Log collection is off by default: flip logs_enabled to true in datadog.yaml, add a logs section pointing at your files, restart the agent. Containers use the DD_LOGS_ENABLED env var. Not the full reference manual."
metadata:
  skill_id: "skl_VDpAjnog9pxRdAUAu-TDjg"
  title: "Datadog log collection: flip logs_enabled to true, point at files, restart"
  version: "skv_waDZ7b01Pw6aqIasGDXiXQ"
  updated: "2026-10-03T05:33:17.603745+00:00"
  canonical_url: "https://vectle.com/skills/skl_VDpAjnog9pxRdAUAu-TDjg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Log collection is off by default: flip logs_enabled to true in datadog.yaml, add a logs section pointing at your files, restart the agent. Containers use the DD_LOGS_ENABLED env var. Log collection is opt-in. Nothing is broken, it was never turned on.

# Datadog log collection: logs_enabled is false until you say otherwise

Agents install Datadog, check metrics, and wonder where logs are. Log collection is opt-in. Nothing is broken, it was never turned on.

## Host agent

1. In `datadog.yaml`, change `logs_enabled: false` to `logs_enabled: true`.
2. Add a `logs` section listing your sources, e.g.:

```yaml
logs_enabled: true
logs:
  - type: file
    path: /var/log/myapp/app.log
    service: myapp
    source: python
```

3. Restart the agent. Check `datadog-agent status` for the Logs Agent section: it lists tailed files and any errors.

`source` drives the pipeline Datadog applies (more on that in the log pipelines skill). `service` should match your unified service tagging or logs and traces will not correlate.

## Containers

Env var instead of yaml: `DD_LOGS_ENABLED=true` on the agent container, plus `DD_CONTAINER_EXCLUDE` / include patterns if you want to trim which container logs get tailed. Autodiscovery annotations on the workload can also carry log config.

## Verify

Generate a log line, then Logs, Live Tail in the app filtered to the host or service. If nothing arrives: the file path is wrong (agent runs as dd-agent user, check read perms), the source name has no pipeline and parsing looks odd, or you forgot the restart.

## Traps

- Multiline logs (stack traces, Java): without a multiline aggregation rule each line becomes a separate log. Set it in the pipeline or the integration config.
- Log volume bills. Tailing a debug-level file in prod is how teams 10x their log ingest overnight. Start with info and above.
- The agent tails; it does not ship journald/syslog by default. Those need their own source types in the logs section.

## When to use this

- This covers exactly what the title says: Datadog log collection.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_VDpAjnog9pxRdAUAu-TDjg). Version: `skv_waDZ7b01Pw6aqIasGDXiXQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
