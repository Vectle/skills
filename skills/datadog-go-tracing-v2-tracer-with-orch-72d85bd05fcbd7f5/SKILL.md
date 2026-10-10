---
name: "datadog-go-tracing-v2-tracer-with-orch-72d85bd05fcbd7f5"
description: "Go APM with dd-trace-go v2: Orchestrion compile-time instrumentation for zero code changes, or manual instrumentation with integration packages. Requires Go 1.18+ and Agent 5.21.1+. Not the full reference manual."
metadata:
  skill_id: "skl_gLEwZQ-j5XlOkHKkKNbaqQ"
  title: "Datadog Go tracing: v2 tracer with orchestrion compile-time or manual instrumentation"
  version: "skv_3glfzQa_14d9w46Wpe8EFQ"
  updated: "2026-10-03T13:50:24.019204+00:00"
  canonical_url: "https://vectle.com/skills/skl_gLEwZQ-j5XlOkHKkKNbaqQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Go APM with dd-trace-go v2: Orchestrion compile-time instrumentation for zero code changes, or manual instrumentation with integration packages. Requires Go 1.18+ and Agent 5.21.1+. Verify Run the service, generate traffic, check APM, Services.

## The fix

**TL;DR:** Go APM with dd-trace-go v2: Orchestrion compile-time instrumentation for zero code changes, or manual instrumentation with integration packages. Requires Go 1.18+ and Agent 5.21.1+. Verify Run the service, generate traffic, check APM, Services.

# Datadog Go tracing: v2 tracer, pick orchestrion or manual

The Go docs now recommend tracer v2 with two instrumentation paths. Agents still write v1-style manual code from memory, so check which version you are on first.

## Path A: Orchestrion (compile-time, no code changes)

```sh
go install github.com/DataDog/orchestrion@latest
orchestrion pin
```

Then build through orchestrion (or wire it into CI). It instruments your code and all dependencies, including the standard library, at compile time. Bonus: it unlocks the App and API Protection exploit prevention feature. Requirements: the two latest Go releases and go modules (vendoring is fine).

## Path B: manual instrumentation

Add dd-trace-go v2 to your module, import and start the tracer in `main` before anything else, then pull in the integration packages for your frameworks (net/http, gRPC, database/sql drivers, etc.). The docs point at the library configuration page for the full option list and pkg.go.dev for the API.

Either way, configure with the standard env vars: `DD_SERVICE`, `DD_ENV`, `DD_VERSION` for unified service tagging, `DD_AGENT_HOST` when the agent is not local, `DD_SITE` for non-US1.

## Requirements that bite

- Go 1.18+ and Datadog Agent >= 5.21.1. Older agents silently drop v2 payloads.
- On v1 still: read the v1-to-v2 migration guide in the docs before touching anything. The import paths changed (`gopkg.in/DataDog/dd-trace-go.v1` vs `github.com/DataDog/dd-trace-go/v2`).

## Verify

Run the service, generate traffic, check APM, Services. For manual instrumentation, a missing integration package means missing spans, not errors: if your HTTP handlers show up but DB calls do not, you forgot the database integration import.

## When to use this

- This covers exactly what the title says: Datadog Go tracing.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Datadog; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_gLEwZQ-j5XlOkHKkKNbaqQ). Version: `skv_3glfzQa_14d9w46Wpe8EFQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
