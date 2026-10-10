---
name: "model-resilience-for-agents-retry-and-ddd241693cc3301d"
description: "Make agents survive provider blips with ModelRetryMiddleware (exponential backoff on retryable model errors) and ModelFallbackMiddleware (try the next model when the primary fails). Both are middleware, so they compose with the rest of the stack. Not the full reference manual."
metadata:
  skill_id: "skl_sE0paAJkAHEGW38fSemApw"
  title: "Model resilience for agents: retry and fallback middleware"
  version: "skv_CUFkL89-Za8OffgvxonsqA"
  updated: "2026-10-03T13:46:38.032271+00:00"
  canonical_url: "https://vectle.com/skills/skl_sE0paAJkAHEGW38fSemApw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Make agents survive provider blips with ModelRetryMiddleware (exponential backoff on retryable model errors) and ModelFallbackMiddleware (try the next model when the primary fails). Both are middleware, so they compose with the rest of the stack.

## The fix

1. Retry respects each exception's `is_retryable` attribute by default: rate limits, timeouts, connection errors, and server errors retry; auth errors, not-found, bad requests, and context overflow do not.

2. `on_failure` controls exhaustion: `continue` returns an AIMessage with the error details so the agent can handle it, `error` re-raises, or pass a callable for custom content.

3. Fallback tries the models in order when the primary fails. Model identifiers can be strings like `openai:gpt-5.4-mini` or model instances.

4. Retry handles transient failures; fallback handles outages. Use both for anything user-facing.

5. Backoff has jitter on by default; leave it on so a fleet of agents does not thundering-herd the provider.

6. Fallback models should be cheaper or more available than the primary, and they must support the features the agent uses (tool calling at minimum). A fallback that cannot call tools just fails differently.

## When to use this

- This covers exactly what the title says: Model resilience for agents.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Model; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.5, 2.0 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_sE0paAJkAHEGW38fSemApw). Version: `skv_CUFkL89-Za8OffgvxonsqA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
