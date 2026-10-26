---
name: "bug-dalle-critic-not-working-2bbbfa8e0e12a05d"
description: "@whiskyboy `max_token` solved the cutoff problem! Are you using Azure Dalle? Because for Dalle I get the following error. Use when hitting this exact issue with Bug]. Not for unrelated errors."
metadata:
  skill_id: "skl_j2bC14AhtONOKD-WtD31bQ"
  title: "Bug]: Dalle-Critic not working"
  version: "skv_0MnVHsGmvRPjuHaE-CPMGg"
  updated: "2026-10-04T02:27:58.48887+00:00"
  canonical_url: "https://vectle.com/skills/skl_j2bC14AhtONOKD-WtD31bQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/microsoft/autogen/issues/2510\"]"
---

## TL;DR

Make sure the text is clear." [5](vscode-notebook-cell:?execution_count=11&line=5) # img_prompt = "Ask me how I'm doing" ----&gt; [7](vscode-notebook-cell:?execution_count=11&line=7) result = dalle.initiate_chat(critic, message=img_prompt) AuthenticationError: Error code: 401 - {'error': {'code': 'invalid_api_key', 'message': 'Incorrect API key provided: f***************************4e23. @whiskyboy `max_token` solved the cutoff problem!

[reporter nazkhan-8451]: @whiskyboy `max_token` solved the cutoff problem! Are you using Azure Dalle? Because for Dalle I get the following error. But the api key is fine because when I forced it to accept it (showed above comment) it works. `AuthenticationError Traceback (most recent call last) Cell In[11], [line 7](vscode-notebook-cell:?execution_count=11&line=7) [4](vscode-notebook-cell:?execution_count=11&line=4) img_prompt = "A happy dog wearing a shirt saying 'I Love AutoGen'. Make sure the text is clear." [5](vscode-notebook-cell:?execution_count=11&line=5) # img_prompt = "Ask me how I'm doing" ----&gt; [7](vscode-notebook-cell:?execution_count=11&line=7) result = dalle.initiate_chat(critic, message=img_prompt) AuthenticationError: Error code: 401 - {'error': {'code': 'invalid_api_key', 'message': 'Incorrect API key provided: f***************************4e23. You can find your API key at https://platform.openai.com/account/api-keys.', 'param': None, 'type': 'invalid_request_error'}}`

Context: Issue microsoft/autogen#2510 (closed, 29 comments): ### Describe the bug Followed the notebook [https://github.com/microsoft/autogen/blob/main/notebook/agentchat_image_generation_capability.ipynb](url), but getting the following response: [image] Code: ```python import autogen config_list_gpt4 = autogen.config_list_from_json( "OAI_CONFIG_LIST", filter_dict={ "model": ["wag-gpt4-128k"], }, ) config_list_gpt4_vision = autogen.config_list_from_json( "OAI_CONFIG_LIST", filter_dict={ "model": ["gpt4-

## When to use

- You hit this exact issue with Bug].
- The symptom matches: Dalle-Critic not working.

## When NOT to use

- A different error or symptom from Bug]; the cause here is specific to this one.

## Compatibility

Reported against Bug].

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_j2bC14AhtONOKD-WtD31bQ). Version: `skv_0MnVHsGmvRPjuHaE-CPMGg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
