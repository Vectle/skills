---
name: "harness-ff-returns-your-default-when-e-7fcc49cb43621aa6"
description: "In tests, mock at the evaluation boundary rather than racing real init. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_bw2S4gk5DGvyWF7Jsp_-Qg"
  title: "Harness FF returns your default when evaluated before init completes"
  version: "skv_TCsZfkIHWZuek1ZRM_JOTQ"
  updated: "2026-10-03T05:38:54.67752+00:00"
  canonical_url: "https://vectle.com/skills/skl_bw2S4gk5DGvyWF7Jsp_-Qg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"http://developer.harness.io/docs/feature-flags/use-ff/ff-sdks/server-sdks/python-sdk-reference/\"]"
---

## TL;DR

In tests, mock at the evaluation boundary rather than racing real init. The Android guide shows the same pattern with waitForInitialization. Agents that evaluate flags immediately at startup, before the SDK has fetched flag definitions, silently get defaults for every flag and read that as the flags being off.

## Fix

Always wait for SDK initialization to complete before the first evaluation, and treat a run of all-defaults as a possible init failure, not as flag state. Log or alert on initialization errors separately so they are visible. In tests, mock at the evaluation boundary rather than racing real init.

Context: Official docs (Harness Python SDK reference): if you evaluate a feature flag when initialization fails, the default variation you provided is returned as the evaluation result, and an error is logged. The Android guide shows the same pattern with waitForInitialization. Agents that evaluate flags immediately at startup, before the SDK has fetched flag definitions, silently get defaults for every flag and read that as the flags being off.

## Matched source
Source: Published skill
Original query: "Harness FF returns your default when evaluated before init completes"
Key terms: before, completes, default, evaluated, harness, init, returns, your

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_bw2S4gk5DGvyWF7Jsp_-Qg). Version: `skv_TCsZfkIHWZuek1ZRM_JOTQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
