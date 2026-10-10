---
name: "middleware-docker-agent-mount-the-sock-cbd2e72d2fd2aa47"
description: "Guide Middleware Docker agent: mount the socket, run only one per host: If the Middleware Docker agent does not report data, check two things first. Mount /var/run/docker.sock into the container; without the socket the agent cannot collect container metrics and may exit. Use this when you hit exactly this in Middleware Docker agent. Not for different errors or different tools."
metadata:
  skill_id: "skl_RzK7IiAmrU_9gYLy4gljBg"
  title: "Middleware Docker agent: mount the socket, run only one per host"
  version: "skv_LUP9Y-HBpRHq1NWMx6hA5A"
  updated: "2026-10-03T04:43:04.823202+00:00"
  canonical_url: "https://vectle.com/skills/skl_RzK7IiAmrU_9gYLy4gljBg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: If the Middleware Docker agent does not report data, check two things first. Mount /var/run/docker.sock into the container; without the socket the agent cannot collect container metrics and may exit. Then confirm only one agent runs on the host: two agents with the same hostname fight each other and one silently wins.

If the Middleware Docker agent does not report data, check two things first. Mount /var/run/docker.sock into the container; without the socket the agent cannot collect container metrics and may exit. Then confirm only one agent runs on the host: two agents with the same hostname fight each other and one silently wins. If the container exits immediately, run docker logs on it instead of restarting blind; the log line names the cause (bad key, no socket, no network). The agent needs outbound HTTPS on port 443 to its target, so also confirm the firewall allows it.

Context: Official docs (docs.middleware.io, Docker agent installation): documents the two install killers: the Docker socket must be mounted into the agent container, and only one agent may run per host. A container that starts and exits silently needs its logs inspected.

## When to use
You hit exactly this: Middleware Docker agent: mount the socket, run only one per host in Middleware Docker agent.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Middleware Docker agent.

## Edge cases
- Then confirm only one agent runs on the host: two agents with the same hostname fight each other and one silently wins.
- A container that starts and exits silently needs its logs inspected.

---

Source: [Vectle](https://vectle.com/skills/skl_RzK7IiAmrU_9gYLy4gljBg). Version: `skv_LUP9Y-HBpRHq1NWMx6hA5A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
