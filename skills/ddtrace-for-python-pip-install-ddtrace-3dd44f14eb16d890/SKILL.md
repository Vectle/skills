---
name: "ddtrace-for-python-pip-install-ddtrace-3dd44f14eb16d890"
description: "Python APM with ddtrace: pip install ddtrace, prefix the entry point with ddtrace-run, and check config with ddtrace-run --info. No code changes needed for the basics. Not the full reference manual."
metadata:
  skill_id: "skl_V2GEq7nL8WO5CjCLjwfNGQ"
  title: "ddtrace for Python: pip install ddtrace, prefix the entry point with ddtrace-run"
  version: "skv_4y70-h6kjBt1I__zllevXA"
  updated: "2026-10-03T05:10:24.912452+00:00"
  canonical_url: "https://vectle.com/skills/skl_V2GEq7nL8WO5CjCLjwfNGQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Python APM with ddtrace: pip install ddtrace, prefix the entry point with ddtrace-run, and check config with ddtrace-run --info. No code changes needed for the basics. Set it or the tracer guesses from the module name and your APM becomes a mess of wrong names. - DD_ENV : e.g. prod, staging. Verify This prints the effective tracer configuration.

# ddtrace for Python: wrap the entry point, dont rewrite the app

The Python tracer needs zero code changes for basic APM. Agents overcomplicate this by editing source files first.

## Setup

```sh
pip install ddtrace
```

Then start the app with the wrapper:

```sh
ddtrace-run python app.py
```

That is it for traces. The wrapper auto-instruments supported frameworks (Django, Flask, FastAPI, Celery, requests, and friends) and ships spans to the agent.

## Config via environment

The tracer reads the usual suspects:

- `DD_SERVICE` : your service name. Set it or the tracer guesses from the module name and your APM becomes a mess of wrong names.
- `DD_ENV` : e.g. prod, staging. Part of unified service tagging.
- `DD_VERSION` : your deploy version. Makes deploy tracking work.
- `DD_AGENT_HOST` / `DD_TRACE_AGENT_URL` : where the trace agent lives. Default assumes the Datadog agent on the same host. In Docker/K8s, point it at the agent.
- `DD_SITE` : set for non-US1 orgs, same trap as the agent.

## Verify

```sh
ddtrace-run --info
```

This prints the effective tracer configuration. The docs warn it does not reflect config changed at runtime in code, so treat it as the startup truth. Then generate traffic and check APM, Services in the app. No service after a minute: the tracer cannot reach the agent (see the trace-agent connection skill) or the site is wrong.

## Traps

- Running the app without the wrapper and wondering why there are no traces. `python app.py` vs `ddtrace-run python app.py` is the whole difference.
- Forgetting `DD_SERVICE` in a repo with many entry points: each gets a guessed name and your service list fills with junk.
- Version pinning: `ddtrace` moves fast. Pin it in requirements like any other dependency or a minor bump changes sampling behavior under you.

## When to use this

- This covers exactly what the title says: ddtrace for Python.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with ddtrace; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_V2GEq7nL8WO5CjCLjwfNGQ). Version: `skv_4y70-h6kjBt1I__zllevXA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
