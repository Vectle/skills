---
name: "apm-trace-agent-connection-refused-poi-fdc4947cc3915f10"
description: "Tracers ship to the Datadog agent on the same host by default. Connection refused means the tracer cannot reach it: wrong DD_AGENT_HOST in containers, agent APM not enabled, or a firewall in between."
metadata:
  skill_id: "skl_z3oU0ZdrPY1LO_tYQMhp-g"
  title: "APM trace agent connection refused: point the tracer at the agent with DD_AGENT_HOST"
  version: "skv_bXEAkBLSbIO3ruCUlQsfgA"
  updated: "2026-10-03T05:02:13.87816+00:00"
  canonical_url: "https://vectle.com/skills/skl_z3oU0ZdrPY1LO_tYQMhp-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/containers/amazon_ecs/\",\"https://docs.datadoghq.com/tracing/setup/python/\"]"
---

**TL;DR:** Tracers ship to the Datadog agent on the same host by default. Connection refused means the tracer cannot reach it: wrong DD_AGENT_HOST in containers, agent APM not enabled, or a firewall in between. Connection refused is always hop one. Fix by environment - Same host: should just work.

## The error

```text
app runs, tracer initialized, zero traces in APM. The tracer log (or ddtrace-run --info, or the Node debug log) shows connection refused or timeouts to the trace agent endpoint.
```

# APM trace agent connection refused: the tracer cannot see the agent

Symptom: app runs, tracer initialized, zero traces in APM. The tracer log (or ddtrace-run --info, or the Node debug log) shows connection refused or timeouts to the trace agent endpoint.

## The mental model

Every tracer ships spans to the **Datadog agent** (its trace-agent component), defaulting to the same host. The agent then forwards to Datadog. So APM needs two hops working: app to agent, agent to Datadog. Connection refused is always hop one.

## Fix by environment

- **Same host**: should just work. If refused, the agent is not running or APM is disabled in its config. `datadog-agent status` first.
- **Docker / ECS / Kubernetes**: the loopback address inside your app container is NOT the agent. Set `DD_AGENT_HOST` to the agent container host: the EC2 private IP on ECS (from the instance metadata service), the node IP or a service DNS name on Kubernetes, the gateway IP or service name on plain Docker. The ECS docs show exactly this pattern for both DogStatsD and APM.
- **Full control**: `DD_TRACE_AGENT_URL` with the complete URL (scheme, host, port 8126). Useful for proxies and odd networks.
- **Lambda**: traces go through the Datadog extension, not a local agent. If you pointed the tracer at an agent host on Lambda, unset it.

## Confirm

From the app container/host, hit the trace agent port (default 8126) the way the tracer would. Then generate one request and watch the tracer debug log for a successful flush. In the app, APM Services should list the service within a minute or two.

## Traps

- Firewalls/security groups between app and agent subnets. The ECS docs warn about this: keep APM/DogStatsD ports off the public internet but open between your tasks.
- `DD_AGENT_HOST` set globally to a value that is right for one environment and wrong for another (staging vs prod). Per-environment config, not a shared default.
- Sampling confusion: connection works but no traces because the sample rate drops everything. That is a different skill (APM sampling), rule out connectivity first.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: APM trace agent connection refused.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Not pinned to a specific version; follows current APM behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_z3oU0ZdrPY1LO_tYQMhp-g). Version: `skv_bXEAkBLSbIO3ruCUlQsfgA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
