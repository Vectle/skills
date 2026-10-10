---
name: "function-calling-broke-with-tool-call-a01adb959cde183d"
description: "Fixes function calling breaking on open-mixtral-8x22b and mistral-small-latest with 'Tool call id has to be defined' while mistral-large-latest keeps working. Use this when the same code fails only on those two models. Not for tool-call errors on all models."
metadata:
  skill_id: "skl_DSOW8mnxz3Jlw2S4xVzLhg"
  title: "Function calling broke with Tool call id has to be defined on open-mixtral-8x22b and mistral-small-latest"
  version: "skv_R-246hdtTZkfe5JAGaOysg"
  updated: "2026-10-03T04:48:47.694099+00:00"
  canonical_url: "https://vectle.com/skills/skl_DSOW8mnxz3Jlw2S4xVzLhg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if function calling on `open-mixtral-8x22b` or `mistral-small-latest` fails with `Tool call id has to be defined` while `mistral-large-latest` works with the same code, those models were updated to support multiple tool calls, so tool responses now need the tool call id the model provides. Mistral fixed this in client PR #93 and deployed an API-side fix, so update the package and rerun your existing code.

```text
Tool call id has to be defined
```

## Steps

1. Update the Mistral client package.

2. Re-run your function-calling code unchanged.

   Expected: tool calls resolve. Success check: the model completes the tool flow without the id error.

3. If you construct tool responses manually, pass through the id from the model's tool call instead of leaving it empty.

## When to use this

- The error appears only on open-mixtral-8x22b and mistral-small-latest; mistral-large-latest is fine.
- It started suddenly without a code change on your side.

## When NOT to use this

- All models fail the same way; check your tool-response construction.
- You never use function calling; this does not apply.

## Compatibility

- Mistral client with PR #93 plus the API-side fix.

## Variant phrasings

- "mistral Tool call id has to be defined"
- "open-mixtral-8x22b function calling broken"

## Root cause

Those models were updated to support multiple tool calls, which made the tool call id mandatory in tool responses; the client and API both needed updates to supply it.

## Edge cases

- Manual tool-response builders must thread the id through; the automatic path handles it after the update.

---

Source: [Vectle](https://vectle.com/skills/skl_DSOW8mnxz3Jlw2S4xVzLhg). Version: `skv_R-246hdtTZkfe5JAGaOysg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
