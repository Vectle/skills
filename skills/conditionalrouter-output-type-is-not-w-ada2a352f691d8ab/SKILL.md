---
name: "conditionalrouter-output-type-is-not-w-ada2a352f691d8ab"
description: "Haystack: conditionalRouter output type is not working anymore. The verified fix is Fix: Intentional breaking change in the 2.3.1 security patch: ConditionalRouter can now only return Python literal types (str, bytes, numbers, tuples, lists, dicts, sets, bools, None) because rendering arbitrary types via Jinja was a remote-code-execution risk. Use this when you hit the symptoms above in haystack; not for unrelated haystack errors or general setup questions."
metadata:
  skill_id: "skl_XIr4wp7fouIoLQcgLwen1Q"
  title: "ConditionalRouter output type is not working anymore"
  version: "skv_Mq5h48vFaAcd6uiYbJE_zQ"
  updated: "2026-10-03T05:01:15.70131+00:00"
  canonical_url: "https://vectle.com/skills/skl_XIr4wp7fouIoLQcgLwen1Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/deepset-ai/haystack/issues/8161\"]"
---

## TL;DR

Fix: Intentional breaking change in the 2.3.1 security patch: ConditionalRouter can now only return Python literal types (str, bytes, numbers, tuples, lists, dicts, sets, bools, None) because rendering arbitrary types via Jinja was a remote-code-execution risk. Contributor silvanocerza: to opt back into the old behavior, build ConditionalRouter/OutputAdapter with unsafe=True (shipped in 2.4.(0) - safe as long as you don't let end users write the Jinja templates themselves - or write a custom routing component; otherwise pin to 2.3.0.

## The error

```text
Issue deepset-ai/haystack#8161 (closed, 13 comments): **Describe the bug** We tried to update the Haystack version to 2.3.1 due to the [security update](https://github.com/deepset-ai/haystack/releases/tag/v2.3.1) and our code stopped working. We identified that the `ConditionalRouter` is returning a string instead of the type assigned in `output_type` **Error message** We are getting errors related to the fact that a string is now being returned. Here is an example of the error when running the provided code: `AttributeError: 'str' object has no attribute 'content'` **Expected behavior** We expected that the `output_type` provided in the route wo
```

## Fix

1. Intentional breaking change in the 2.3.1 security patch: ConditionalRouter can now only return Python literal types (str, bytes, numbers, tuples, lists, dicts, sets, bools, None) because rendering arbitrary types via Jinja was a remote-code-execution risk.
2. Contributor silvanocerza: to opt back into the old behavior, build ConditionalRouter/OutputAdapter with unsafe=True (shipped in 2.4.(0) - safe as long as you don't let end users write the Jinja templates themselves - or write a custom routing component; otherwise pin to 2.3.0.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in haystack.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in haystack, even a similar-looking one.
- General haystack setup or credential questions.

## Compatibility

- Haystack (deepset-ai/haystack)

## Variant phrasings

- How to fix "conditionalRouter output type is not working anymore" in haystack
- haystack: conditionalRouter output type is not working anymore

## Root cause

Intentional breaking change in the 2.3.1 security patch: ConditionalRouter can now only return Python literal types (str, bytes, numbers, tuples, lists, dicts, sets, bools, None) because rendering arbitrary types via Jinja was a remote-code-execution risk.

## Source

- https://github.com/deepset-ai/haystack/issues/8161

---

Source: [Vectle](https://vectle.com/skills/skl_XIr4wp7fouIoLQcgLwen1Q). Version: `skv_Mq5h48vFaAcd6uiYbJE_zQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
