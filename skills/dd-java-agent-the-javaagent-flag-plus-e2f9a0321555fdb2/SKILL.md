---
name: "dd-java-agent-the-javaagent-flag-plus-e2f9a0321555fdb2"
description: "Java APM with dd-java-agent: add -javaagent with the jar path, set service/env/version, and the tracer auto-instruments. Version of the agent jar matters. Not the full reference manual."
metadata:
  skill_id: "skl_E4X0UF46_Fng-IgThvtqGA"
  title: "dd-java-agent: the -javaagent flag plus service, env, version"
  version: "skv_mID1oe_ZNcjnGMwdErMafg"
  updated: "2026-10-03T13:46:04.818293+00:00"
  canonical_url: "https://vectle.com/skills/skl_E4X0UF46_Fng-IgThvtqGA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Java APM with dd-java-agent: add -javaagent with the jar path, set service/env/version, and the tracer auto-instruments. Version of the agent jar matters. The failure mode is always the flag placement or the jar version. After it they become app args and the agent never loads. dd-java-agent: the -javaagent flag and the three tags Java APM is a JVM flag, not a code change.

## The fix

**TL;DR:** Java APM with dd-java-agent: add -javaagent with the jar path, set service/env/version, and the tracer auto-instruments. Version of the agent jar matters. The failure mode is always the flag placement or the jar version. After it they become app args and the agent never loads.

# dd-java-agent: the -javaagent flag and the three tags

Java APM is a JVM flag, not a code change. The failure mode is always the flag placement or the jar version.

## Setup

Download dd-java-agent.jar (match it to your JVM and app; release candidates exist if you want the bleeding edge with GitHub release notifications). Then:

```sh
java -mount the host path javaagent at container path /path/to/dd-java-agent.jar \
  -Ddd.service=my-app -Ddd.env=prod -Ddd.version=1.2.3 \
  -jar /path/to/your/app.jar
```

Useful extras on the same command line: `-Ddd.profiling.enabled=true` for Continuous Profiler, `-Ddd.logs.injection=true` to inject trace IDs into logs (only useful if you ship logs to Datadog).

Works the same from Maven/Gradle exec plugins and IDE run configs: it is a JVM argument, wherever your launcher takes those.

## Traps

1. **Flag after -jar.** JVM args go before `-jar`. After it they become app args and the agent never loads. Silent, no traces.
2. **Stale jar.** Agents pin a jar from two years ago and miss profiler features or hit fixed bugs. Check the release notes when traces look wrong.
3. **Missing service/env/version.** `-Ddd.service`, `-Ddd.env`, `-Ddd.version` (or the `DD_` env equivalents). Without them you get default names and no deploy tracking.
4. **Agent connectivity.** Same story as every tracer: the agent must be reachable, `DD_AGENT_HOST` in containers, `DD_SITE` off US1.
5. **Fat jar shading.** If you shade the agent into your own jar or trim modules with jdeps, required modules can change between releases. Prefer the standalone jar unless image size forces your hand.

## Verify

Start the app and watch stdout: the agent logs its version and the endpoint it reports to on boot. Then APM, Services in the app. Profiler data shows up under Profiles only if you enabled it, it is not on by default.

## When to use this

- This covers exactly what the title says: dd-java-agent.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with dd-java-agent; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Edge cases

- Prefer the standalone jar unless image size forces your hand.

---

Source: [Vectle](https://vectle.com/skills/skl_E4X0UF46_Fng-IgThvtqGA). Version: `skv_mID1oe_ZNcjnGMwdErMafg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
