---
name: "dogstatsd-udp-port-8125-10-second-flus-c2073a0587490d99"
description: "DogStatsD ships custom metrics over UDP 8125 to the agent, which aggregates on a 10 second flush. The server is bundled with Agent v6+ and on by default; point clients at the agent host in containers. Not the full reference manual."
metadata:
  skill_id: "skl_Fw15-db6wCSBdn6dHtozqQ"
  title: "DogStatsD: UDP port 8125, 10 second flush, bundled with the agent"
  version: "skv_z5o0F2Nu-5_SgMYJQ4QdWw"
  updated: "2026-10-03T13:54:37.86744+00:00"
  canonical_url: "https://vectle.com/skills/skl_Fw15-db6wCSBdn6dHtozqQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** DogStatsD ships custom metrics over UDP 8125 to the agent, which aggregates on a 10 second flush. The server is bundled with Agent v6+ and on by default; point clients at the agent host in containers. Two processes, one port, and the failure is always the network path between them. Change it with dogstatsd_port in the agent config if you must.

## The fix

**TL;DR:** DogStatsD ships custom metrics over UDP 8125 to the agent, which aggregates on a 10 second flush. The server is bundled with Agent v6+ and on by default; point clients at the agent host in containers. Two processes, one port, and the failure is always the network path between them. Change it with dogstatsd_port in the agent config if you must.

# DogStatsD: UDP 8125, 10s flush, agent-bundled

DogStatsD is the fire-and-forget metrics protocol. Client library in your app, UDP packets to the agent, agent aggregates and forwards. Two processes, one port, and the failure is always the network path between them.

## Setup

1. The server is **bundled with the Datadog Agent and enabled by default** over UDP port 8125 (Agent v6+). No separate install. Change it with `dogstatsd_port` in the agent config if you must.
2. Add the client library for your language and point it at the agent:
   - Same host: default (the loopback address, port 8125) just works.
   - Containers: point the client at the agent container/pod (env var for the agent host, e.g. `DD_AGENT_HOST`). UDP to the loopback address inside your app container hits nothing.
3. Emit: counters, gauges, histograms, sets, distributions. Distributions give you server-side percentiles; histograms aggregate client-side.

## The 10 second flush

DogStatsD aggregates multiple points per unique metric into a single point per flush interval (10 seconds). Your 1000 increments/sec become one point per 10s with count, rate, etc. This is why a counter that fires twice in testing shows odd rates: you are seeing flush math, not packet loss.

## Traps

- **UDP is lossy by design.** On a busy host with a full socket buffer, packets drop silently. If metrics are spotty under load, it is the buffer, not Datadog. The agent exposes DogStatsD drop metrics; alert on them if custom metrics matter.
- **Non-local traffic.** The agent only listens on the loopback address by default for some endpoints; DogStatsD binds more broadly, but verify with a test packet from the app container before assuming.
- **Tag cardinality.** Every unique tag combo is a separate metric series and it bills. `user_id` as a DogStatsD tag is how teams get a surprise invoice. See the custom metrics cost skill.
- **Naming.** Metric names have rules (lowercase, dots, underscores). Invalid names get rejected at intake with no client-side error because UDP.

## When to use this

- This covers exactly what the title says: DogStatsD.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with DogStatsD; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current DogStatsD behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_Fw15-db6wCSBdn6dHtozqQ). Version: `skv_z5o0F2Nu-5_SgMYJQ4QdWw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
