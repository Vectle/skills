---
name: "strands-agent-can-t-support-litellm-mo-2f26bbc669c9a2f6"
description: "Shows how to fix strands agent can't support LiteLLM model with Groq and Cerebras. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_1V2gDN4g-so9o5CrrMxg5Q"
  title: "Strands agent can't support LiteLLM model with Groq and Cerebras"
  version: "skv_nAiVXGZEmSjUdEVJPXYMhg"
  updated: "2026-10-03T05:03:29.262085+00:00"
  canonical_url: "https://vectle.com/skills/skl_1V2gDN4g-so9o5CrrMxg5Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/strands-agents/harness-sdk/issues/729\"]"
---

## TL;DR

For "Strands agent can't support LiteLLM model with Groq and Cerebras": issue strands-agents/harness-sdk#729 (closed, 11 comments): ### Checks - [x] I have updated to the lastest minor and patch version of Strands - [x] I have checked the documentation and this is not expected behavior - [x] I have searched./issues and there are no duplicates of my issue ### Strands Version 1.5.0 ### Python Version 3.12.11 ### Operating System Colab notebook ### Installation Method pip ### Steps to Reproduce # Problem Statement Currently, LiteLLM model supports Cerebras and Groq provider, but i cannot use them

```text
Strands agent can't support LiteLLM model with Groq and Cerebras
```

## When to use

You are seeing this: When debugging similar provider errors in Strands, check how message content is shaped for the target provider before assuming the provider key or model is the problem. Use this skill when you run into "Strands agent can't support LiteLLM model with Groq and Cerebras".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 1.5.0, 3.12.11. If you are on something much newer or older, the details may have shifted.

## Steps

1. Issue strands-agents/harness-sdk#729 (closed, 11 comments): ### Checks - [x] I have updated to the lastest minor and patch version of Strands - [x] I have checked the documentation and this is not expected behavior - [x] I have searched [./issues](./issues?q=) and there are no duplicates of my issue ### Strands Version 1.5.0 ### Python Version 3.12.11 ### Operating System Colab notebook ### Installation Method pip ### Steps to Reproduce # Problem Statement Currently, LiteLLM model supports Cerebras and Groq provider, but i cannot use them in strands agent - It appears strands_agents wrapper of litellm did not passed the input correctly, which result...

2. If a Strands agent can't use LiteLLM with Groq or Cerebras, especially when tools are involved, the root cause is LiteLLM's inconsistent content format across providers: OpenAI expects content as a list of parts ([{type: text, text: ...}]) while Cerebras and Groq expect a plain string. A community fix addresses this by overriding message formatting in LiteLLMModel (_format_request_message_contents / _format_request_messages) so tool messages get provider-compatible formatting too. When debugging similar provider errors in Strands, check how message content is shaped for the target provider before assuming the provider key or model is the problem.


---

Source: [Vectle](https://vectle.com/skills/skl_1V2gDN4g-so9o5CrrMxg5Q). Version: `skv_nAiVXGZEmSjUdEVJPXYMhg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
