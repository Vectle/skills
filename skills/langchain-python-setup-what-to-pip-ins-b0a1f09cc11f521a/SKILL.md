---
name: "langchain-python-setup-what-to-pip-ins-b0a1f09cc11f521a"
description: "pip install langchain gets you the core agent building blocks on Python 3.10 plus. Model providers like OpenAI and Anthropic ship in their own packages that you install separately, and most agent code only needs the core package plus one provider package. Not the full reference manual."
metadata:
  skill_id: "skl_V7j6Hmn3jV83sQudWPcf0w"
  title: "LangChain Python setup: what to pip install and what lives in provider packages"
  version: "skv_Ae8p0p27q4RKTdAKPsFjXw"
  updated: "2026-10-03T14:09:46.985861+00:00"
  canonical_url: "https://vectle.com/skills/skl_V7j6Hmn3jV83sQudWPcf0w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/install\",\"https://docs.langchain.com/oss/python/langchain/models\"]"
---

**TL;DR:** pip install langchain gets you the core agent building blocks on Python 3.10 plus. Model providers like OpenAI and Anthropic ship in their own packages that you install separately, and most agent code only needs the core package plus one provider package. Install the ones you use: Or pull a provider in as an extra of the core package: Rules - Do not expect pip install langchain to include OpenAI or Anthropic support. Keep the key in the environment (OPENAI_API_KEY, ANTHROPIC_API_KEY).

## The fix

**TL;DR:** pip install langchain gets you the core agent building blocks on Python 3.10 plus. Model providers like OpenAI and Anthropic ship in their own packages that you install separately, and most agent code only needs the core package plus one provider package. Install the ones you use: Or pull a provider in as an extra of the core package: Rules - Do not expect pip install langchain to include OpenAI or Anthropic support.

## The fix

1. Do not expect `pip install langchain` to include OpenAI or Anthropic support. If the import of `langchain_openai` fails, the fix is installing the provider package, not reinstalling langchain.

2. Keep the key in the environment (OPENAI_API_KEY, ANTHROPIC_API_KEY). The model classes read it from there by default; do not hardcode it in the script.

3. Use `uv add langchain` / `uv add langchain-openai` if the project is uv-managed. Mixing pip and uv in one project is how you get two copies of langchain-core fighting each other.

## When to use this

- This covers exactly what the title says: LangChain Python setup.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with LangChain; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 3.10 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_V7j6Hmn3jV83sQudWPcf0w). Version: `skv_Ae8p0p27q4RKTdAKPsFjXw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
