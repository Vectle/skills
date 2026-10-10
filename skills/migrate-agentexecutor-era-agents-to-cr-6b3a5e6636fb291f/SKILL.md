---
name: "migrate-agentexecutor-era-agents-to-cr-6b3a5e6636fb291f"
description: "AgentExecutor, initialize_agent, and the old agent types are legacy. The v1 path is create_agent from langchain.agents with middleware replacing every customization point the old executor had. Not the full reference manual."
metadata:
  skill_id: "skl_2N39oUqvGgoNg8Kbwx20Ag"
  title: "Migrate AgentExecutor-era agents to create_agent"
  version: "skv_oHFs9fso_hIAp5MTN9WGKw"
  updated: "2026-10-03T13:48:35.797499+00:00"
  canonical_url: "https://vectle.com/skills/skl_2N39oUqvGgoNg8Kbwx20Ag"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** AgentExecutor, initialize_agent, and the old agent types are legacy. The v1 path is create_agent from langchain.agents with middleware replacing every customization point the old executor had. Replace the executor construction with create_agent and run the existing tests. Move each customization to middleware one at a time, testing after each.

## The fix

**TL;DR:** AgentExecutor, initialize_agent, and the old agent types are legacy. The v1 path is create_agent from langchain.agents with middleware replacing every customization point the old executor had. Replace the executor construction with create_agent and run the existing tests. Move each customization to middleware one at a time, testing after each.

## The fix

1. `AgentExecutor` + agent type strings -> `create_agent(model=..., tools=[...])`.

2. Custom agent logic in executor callbacks -> middleware (`before_model`, `after_model`, `@wrap_model_call`, `@wrap_tool_call`).

3. `handle_parsing_errors` and friends -> ToolStrategy error handling via the `handle_errors` parameter, or ToolErrorMiddleware.

4. `max_iterations` / `max_execution_time` -> ModelCallLimitMiddleware / ToolCallLimitMiddleware.

5. Memory classes -> checkpointer plus thread ids (see the agent-with-memory workflow).

6. Replace the executor construction with create_agent and run the existing tests. The tool functions themselves usually transfer unchanged if they are plain functions.

7. Move each customization to middleware one at a time, testing after each.

8. Delete the legacy imports. If anything still needs the old agent types, that code belongs in langchain-classic, but aim to leave nothing behind.

9. Do not run old and new agents side by side in production "just in case". Migrate, test, cut over.

10. The old `prompt=` argument is now `system_prompt=` and takes a string. Callable prompts become `@dynamic_prompt` middleware.

11. Structured output moves to `response_format=ToolStrategy(...)` or `ProviderStrategy(...)` from `langchain.agents.structured_output`.

## When to use this

- This covers exactly what the title says: Migrate AgentExecutor-era agents to create_agent.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Migrate; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Migrate behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_2N39oUqvGgoNg8Kbwx20Ag). Version: `skv_oHFs9fso_hIAp5MTN9WGKw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
