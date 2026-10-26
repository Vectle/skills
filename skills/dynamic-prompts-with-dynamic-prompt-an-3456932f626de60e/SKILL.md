---
name: "dynamic-prompts-with-dynamic-prompt-an-3456932f626de60e"
description: "v1 replaced callable prompts with the @dynamic_prompt middleware decorator. Static context arrives via context= on invoke with a context_schema; the prompt function reads it from runtime.context. Not the full reference manual."
metadata:
  skill_id: "skl_cA-vVXK_OCd8h-Ot_JcPZQ"
  title: "Dynamic prompts with @dynamic_prompt and runtime context"
  version: "skv_LyWXXdMF9WrGIpTQ6P3KAw"
  updated: "2026-10-03T13:58:25.13207+00:00"
  canonical_url: "https://vectle.com/skills/skl_cA-vVXK_OCd8h-Ot_JcPZQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/migrate/langchain-v1\"]"
---

**TL;DR:** v1 replaced callable prompts with the @dynamic_prompt middleware decorator. Static context arrives via context= on invoke with a context_schema; the prompt function reads it from runtime.context.

## The fix

# Dynamic prompts

```python
from dataclasses import dataclass
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

@dataclass
class Context:
    user_role: str = "user"

@dynamic_prompt
def my_prompt(request: ModelRequest) -> str:
    base = "You are a helpful assistant."
    if request.runtime.context.user_role == "expert":
        return base + " Provide detailed technical responses."
    return base + " Explain concepts simply and avoid jargon."

agent = create_agent(
    model="gpt-5.5",
    tools=tools,
    middleware=[my_prompt],
    context_schema=Context,
)

agent.invoke(
    {"messages": [{"role": "user", "content": "Explain async programming"}]},
    context=Context(user_role="expert"),
)
```

## Rules

- Do not pass a function as `system_prompt`. The v1 API takes a string there; dynamic behavior lives in middleware.
- `context_schema` types the context; `context=` on invoke/stream supplies it. This replaces stuffing values into `config["configurable"]`.
- Keep the prompt function pure and fast: it runs before every model call. Expensive lookups belong in before_agent middleware or in tools.

## When to use this

- This covers exactly what the title says: Dynamic prompts with @dynamic_prompt and runtime context.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Dynamic; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_cA-vVXK_OCd8h-Ot_JcPZQ). Version: `skv_LyWXXdMF9WrGIpTQ6P3KAw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
