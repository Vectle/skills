---
name: "issue-function-call-not-working-with-n-c7797c3edc3c0f3a"
description: "What Microsoft AutoGen users hit in practice, with the verified fix: Issue] Function call not working with Non-OpenAI models + LiteLLM proxy."
metadata:
  skill_id: "skl_TEb7XgQ_UCyQJ4o9C6-L0A"
  title: "Issue] Function call not working with Non-OpenAI models + LiteLLM proxy."
  version: "skv_DVwB3ac8mwzvsSCJQwKbvA"
  updated: "2026-10-04T03:15:33.399228+00:00"
  canonical_url: "https://vectle.com/skills/skl_TEb7XgQ_UCyQJ4o9C6-L0A"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# Issue] Function call not working with Non-OpenAI models + LiteLLM proxy.

## TL;DR

[ragesh2000 (reporter)]: Adding api_style="function" helped me to get rid of that error message. But now also the problem is my assistant agent is aware of the function to use but not the user proxy. Is that the issue with the model iam using ?

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: OpenAI. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Context: GitHub issue microsoft/autogen#1150 (closed, 32 comments): I was following exactly as the notebook for function calling [https://github.com/microsoft/autogen/blob/main/notebook/agentchat_function_call_currency_calculator.ipynb](url) but instead of the output shown there Iam keep on getting an error [image] The only change i made is instead of open ai model i used open source model using litellm. Can anybody tell me why it is happening ?


---

Source: [Vectle](https://vectle.com/skills/skl_TEb7XgQ_UCyQJ4o9C6-L0A). Version: `skv_DVwB3ac8mwzvsSCJQwKbvA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
