---
name: "agent-not-reporting-host-down-agent-de-2977f2a53d398d40"
description: "The host disappears from Infrastructure and datadog.agent.up stops reporting. The agent died, the host died, or something between them broke. Not the full reference manual."
metadata:
  skill_id: "skl_yTrstKTxjBAJh0zt4r4lcA"
  title: "Agent not reporting: host down, agent dead, or the network path broke"
  version: "skv_fwme1s7EpdjwxAxkt7oQEg"
  updated: "2026-10-03T04:39:36.05219+00:00"
  canonical_url: "https://vectle.com/skills/skl_yTrstKTxjBAJh0zt4r4lcA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/getting_started/agent/\"]"
---

**TL;DR:** The host disappears from Infrastructure and datadog.agent.up stops reporting. The agent died, the host died, or something between them broke. Proxy changes and egress firewall rules are the usual silent killers. Check the agent uptime in status: if it is always a few minutes old, it is crash-looping.

# Agent not reporting: the host vanished from Infrastructure

What you see: the host was there, now it is gone or stale. `datadog.agent.up` is missing or not OK.

## Triage order

1. **Is the host alive?** SSH in. If the box is down, this is not a Datadog problem.
2. **Is the agent running?** `systemctl status datadog-agent` (or the platform equivalent). If dead, check why: OOM killer, disk full (the agent buffers to disk), a bad config push that fails validation on restart.
3. **Did the config change?** A recent `datadog.yaml` edit with bad indentation prevents startup. The agent logs the parse error; read them before reinstalling.
4. **Network path to Datadog.** From the host, reach the intake endpoints for your site. Proxy changes and egress firewall rules are the usual silent killers.
5. **Clock skew.** TLS to the intake fails with a wildly wrong system clock. NTP issues are in the troubleshooting index for a reason.

## The flapping variant

Host appears and disappears every few minutes: usually **duplicate hostnames** (two machines reporting as one, each overwriting the other) or the agent restarting in a loop (config error plus a supervisor restarting it). Check the agent uptime in status: if it is always a few minutes old, it is crash-looping.

## Fix and confirm

Fix the underlying cause, restart, then `datadog-agent status` should show the forwarder accepting payloads and the host reappears in Infrastructure within a couple minutes. Set a monitor on `datadog.agent.up` per host so the next one pages you instead of being discovered in a dashboard.

## When to use this

- This covers exactly what the title says: Agent not reporting.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Agent; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Agent behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_yTrstKTxjBAJh0zt4r4lcA). Version: `skv_fwme1s7EpdjwxAxkt7oQEg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
