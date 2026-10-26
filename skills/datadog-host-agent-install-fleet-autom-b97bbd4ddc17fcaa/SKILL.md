---
name: "datadog-host-agent-install-fleet-autom-b97bbd4ddc17fcaa"
description: "Get the Datadog agent onto a Linux host the supported way: Fleet Automation or the one-line installer with DD_API_KEY and DD_SITE set, then confirm with agent status before you touch anything else. Not the full reference manual."
metadata:
  skill_id: "skl_kAAIonvlhK57hv05xXoyXw"
  title: "Datadog host agent install: fleet automation first, one-line installer second, verify with agent status"
  version: "skv_Vftre3MBf11p6T1BDAnFoA"
  updated: "2026-10-03T13:48:01.785835+00:00"
  canonical_url: "https://vectle.com/skills/skl_kAAIonvlhK57hv05xXoyXw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.datadoghq.com/getting_started/agent/\"]"
---

**TL;DR:** Get the Datadog agent onto a Linux host the supported way: Fleet Automation or the one-line installer with DD_API_KEY and DD_SITE set, then confirm with agent status before you touch anything else. Not the full reference manual. Copy it from the Agent docs page for your platform (the Agent documentation page has per-platform tabs: Host-based, Docker, Kubernetes). Set both in the environment before running the installer.

## The fix

**TL;DR:** Get the Datadog agent onto a Linux host the supported way: Fleet Automation or the one-line installer with DD_API_KEY and DD_SITE set, then confirm with agent status before you touch anything else. Copy it from the Agent docs page for your platform (the Agent documentation page has per-platform tabs: Host-based, Docker, Kubernetes). Set both in the environment before running the installer.

# Datadog host agent install, done right

The fastest way to waste an afternoon is installing the agent three times with three different methods. Pick one.

## The supported paths

1. **Fleet Automation** (docs: getting started with the agent). This is Datadogs in-app workflow to install, upgrade, configure, and troubleshoot the agent on one host or a thousand. If you have console access, start here.
2. **The one-line installer** for Linux. Copy it from the Agent docs page for your platform (the Agent documentation page has per-platform tabs: Host-based, Docker, Kubernetes). It takes your API key and site as environment variables. Do not retype it from memory, the script URL and flags change.

## What the installer needs

Two values, nothing else is required:

- `DD_API_KEY` : your org API key. Grab it from the Datadog app under Organization Settings, API Keys. This is the key the agent uses to submit data. It is NOT the application key.
- `DD_SITE` : the site parameter for where your org lives, e.g. `datadoghq.com` for US1, `datadoghq.eu` for EU. Get this wrong and the agent happily reports into the void. See the site parameter skill for the full table.

Set both in the environment before running the installer. On a host, the installer writes them into `datadog.yaml` so you only do this once.

## Verify before you walk away

Run `datadog-agent status` (or `sudo datadog-agent status`). You want:

- The `datadog.agent.up` service check OK, meaning the agent connected to Datadog.
- Forwarder section showing payloads accepted, not 403s or timeouts.

Then open Infrastructure, Hosts in the app and look for the hostname. If it is not there within a couple minutes, you have a key or site problem, not an install problem. Do not reinstall. Fix the config, restart the agent.

## Traps

- Installing the agent as root vs a package manager mix: pick the package (deb/rpm) OR the script, not both. Two installs fight over ports and config.
- The agent is open source (DataDog/datadog-agent on GitHub). If the installer misbehaves on an odd distro, the example `datadog.yaml` files in that repo show every option for your OS.
- macOS and Windows have their own installers on the same docs page. The Linux one-liner does not apply.

## When to use this

- This covers exactly what the title says: Datadog host agent install.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Datadog behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_kAAIonvlhK57hv05xXoyXw). Version: `skv_Vftre3MBf11p6T1BDAnFoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
