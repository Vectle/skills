---
name: "diagnose-tracing-enabled-but-no-traces-747cce74168a6c5b"
description: "Shows how to fix diagnose: tracing enabled but no traces appear in LangSmith. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_CmhbPk9-0UxkaTUXOLcW7Q"
  title: "Diagnose: tracing enabled but no traces appear in LangSmith"
  version: "skv_LULosC3Gxaq7KqCnSMVE9Q"
  updated: "2026-10-03T13:45:24.912146+00:00"
  canonical_url: "https://vectle.com/skills/skl_CmhbPk9-0UxkaTUXOLcW7Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Run the smallest possible agent invoke and watch the project. Is LANGSMITH_TRACING=true actually set in the process that runs the agent?

## Steps

1. Is LANGSMITH_TRACING=true actually set in the process that runs the agent? Check from inside the process, not the shell you think launched it. Containers, schedulers, and notebooks routinely drop env vars.
2. Is LANGSMITH_PROJECT pointing where you are looking? The default project is literally named `default`. Check you are not staring at a custom project while traces land in `default`.
3. Is LANGSMITH_API_KEY valid (see the 401 diagnostic)?

2. The usual order: variable set after the process started, variable set in the wrong shell, or looking at the wrong project. No code changes are needed to trace; `create_agent` traces automatically once the env vars are right.

3. Export the variables before running:

4. - LANGSMITH_TRACING=true
- LANGSMITH_API_KEY holding your key
- LANGSMITH_PROJECT set to the project you want (optional)

5. Run the smallest possible agent invoke and watch the project. A trace appearing within a minute confirms the setup. If it appears in `default` instead of your project, the project variable is the problem.

## When to use

You are seeing this: No traces in the LangSmith project despite expecting them. Use this skill when you run into "Diagnose: tracing enabled but no traces appear in LangSmith".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The usual order: variable set after the process started, variable set in the wrong shell, or looking at the wrong project.


---

Source: [Vectle](https://vectle.com/skills/skl_CmhbPk9-0UxkaTUXOLcW7Q). Version: `skv_LULosC3Gxaq7KqCnSMVE9Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
