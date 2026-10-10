---
name: "datadog-on-ecs-one-agent-per-ec2-host-e237efba74c03d97"
description: "ECS on EC2: run one Datadog agent container per EC2 host as a daemon service task definition. ECS on Fargate is a different integration with its own docs page. Not the full reference manual."
metadata:
  skill_id: "skl_IWH1aVijgy1jaQldL4ujXw"
  title: "Datadog on ECS: one agent per EC2 host as a daemon service, Fargate is a separate setup"
  version: "skv_ETC_cyehyDYa0JF7er1JOg"
  updated: "2026-10-03T13:52:51.653487+00:00"
  canonical_url: "https://vectle.com/skills/skl_IWH1aVijgy1jaQldL4ujXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** ECS on EC2: run one Datadog agent container per EC2 host as a daemon service task definition. ECS on Fargate is a different integration with its own docs page. Create a task definition for the Datadog agent container (env: DD_API_KEY, DD_SITE, plus DD_APM_ENABLED / DD_LOGS_ENABLED if you want those). Deploy it as a daemon service so every EC2 instance in the cluster gets one.

## The fix

**TL;DR:** ECS on EC2: run one Datadog agent container per EC2 host as a daemon service task definition. ECS on Fargate is a different integration with its own docs page. Create a task definition for the Datadog agent container (env: DD_API_KEY, DD_SITE, plus DD_APM_ENABLED / DD_LOGS_ENABLED if you want those). Deploy it as a daemon service so every EC2 instance in the cluster gets one.

# Datadog on ECS: daemon agent per EC2 host, Fargate is separate

ECS has two launch types and Datadog treats them as two different setups. Picking the wrong docs page is the classic mistake.

## ECS on EC2

Run **one agent container per EC2 host** as a daemon service:

1. Create a task definition for the Datadog agent container (env: `DD_API_KEY`, `DD_SITE`, plus `DD_APM_ENABLED` / `DD_LOGS_ENABLED` if you want those).
2. Deploy it as a **daemon service** so every EC2 instance in the cluster gets one. Each agent monitors the other containers on its host.
3. Give the agent container the Docker socket mount so it can see the other containers.

The docs also cover Fleet Automation install if you would rather not hand-write the task definition.

### Reaching the agent from app containers

DogStatsD and APM traffic from your app containers goes through the host port to the agent container. Your app must use the **host private IP**, not the loopback address. Set `DD_AGENT_HOST` to the EC2 private IP (grab it from the instance metadata service) in the app container env or in tracer init. Same pattern for the trace agent endpoint.

And check security groups: do not publicly expose the APM and DogStatsD ports. They should be reachable from the tasks, not the internet.

## ECS on Fargate

Different page, different setup: the docs redirect Fargate to the Amazon ECS on AWS Fargate integration. There is no EC2 host to run a daemon on, so the agent runs as a sidecar/task in Fargate mode with its own config. Do not try to force the EC2 daemon pattern onto Fargate.

## Verify

`datadog-agent status` inside the agent container, then Infrastructure, Containers in the app filtered to the cluster. If app containers cannot reach DogStatsD/APM, exec into one and check the `DD_AGENT_HOST` value resolves to the host IP.

## When to use this

- This covers exactly what the title says: Datadog on ECS.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_IWH1aVijgy1jaQldL4ujXw). Version: `skv_ETC_cyehyDYa0JF7er1JOg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
