---
name: "agent-evals-in-ci-langsmith-evaluate-p-7d0be3cbbc7dcf64"
description: "Run agent evals two ways: the evaluate function for ad-hoc and notebook runs, and the LangSmith pytest integration for CI. Both read from versioned datasets so results are comparable across runs. Not the full reference manual."
metadata:
  skill_id: "skl_6h0QgJHUnmEHHaIeBI-HVA"
  title: "Agent evals in CI: LangSmith evaluate plus pytest integration"
  version: "skv_6aalLgB6Kg6AxB3PWxx0gA"
  updated: "2026-10-03T13:57:06.948414+00:00"
  canonical_url: "https://vectle.com/skills/skl_6h0QgJHUnmEHHaIeBI-HVA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/test/evals\"]"
---

**TL;DR:** Run agent evals two ways: the evaluate function for ad-hoc and notebook runs, and the LangSmith pytest integration for CI. Both read from versioned datasets so results are comparable across runs. Pin the judge model and record its version with the experiment. - Start with a small, high-signal dataset (20 to 50 cases covering your real failure modes) rather than a thousand generic questions.

## The fix

1. Datasets: versioned collections of inputs (and reference outputs or trajectories) in LangSmith. Every production failure becomes a new case.

2. `evaluate`: the function that runs your agent (or chain) over a dataset and records an experiment.

3. Evaluators: `agentevals` prebuilt evaluators. Trajectory match for deterministic comparison against a reference trajectory; `create_trajectory_llm_as_judge` for qualitative grading without a reference.

4. pytest integration: run the same evals as tests in CI.

5. Gate merges on the eval suite the way you gate on unit tests. An agent change that drops trajectory-match scores is a regression, full stop.

6. Keep eval inputs fixed and versioned. Changing the dataset and the agent in the same commit makes the comparison meaningless.

7. LLM-judge scores drift with the judge model. Pin the judge model and record its version with the experiment.

8. Start with a small, high-signal dataset (20 to 50 cases covering your real failure modes) rather than a thousand generic questions. Grow it from production incidents.

## When to use this

- This covers exactly what the title says: Agent evals in CI.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Agent; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

---

Source: [Vectle](https://vectle.com/skills/skl_6h0QgJHUnmEHHaIeBI-HVA). Version: `skv_6aalLgB6Kg6AxB3PWxx0gA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
