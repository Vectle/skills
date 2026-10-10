---
name: "python-function-calling-error-when-usi-b49bd3ddbad7746f"
description: "Fixes 400 'unable to parse' errors on function calling through APIM-managed Azure OpenAI by setting estimate-prompt-tokens to false in the azure-openai-token-limit policy. Use when Python Semantic Kernel function calls fail behind Azure APIM. Not for direct-to-Azure OpenAI calls or non-APIM gateways."
metadata:
  skill_id: "skl_3z9pPakcR1-PTe9HotWAWQ"
  title: "Python: Function Calling Error when Using APIM Managed Azure OpenAI"
  version: "skv_84nnCGj7Y-Y_5k8yGF2FJg"
  updated: "2026-10-03T04:29:47.577544+00:00"
  canonical_url: "https://vectle.com/skills/skl_3z9pPakcR1-PTe9HotWAWQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: in your APIM instance, open the azure-openai-token-limit policy and set estimate-prompt-tokens to false. Two reporters confirmed function calling started working right after the change.

```text
400 unable to parse
```

1. Open the azure-openai-token-limit policy in Azure APIM.
2. Set estimate-prompt-tokens to false. When it is true, APIM estimates tokens from the prompt schema and throws the 400; when false, tokens are calculated from actual model usage.
3. Retry the function call. Expected: the call succeeds and returns tool calls with no 400.

When to use: function calling fails with a 400 through Azure APIM, in Python Semantic Kernel or similar setups.

When not to use: calls that go straight to Azure OpenAI without APIM, or 400s that come from somewhere other than the token-limit policy.

Compatibility: Semantic Kernel (Python), Azure API Management, Azure OpenAI.

Variants:
- "apim function calling 400 unable to parse"
- "azure-openai-token-limit policy function calling"
- "estimate-prompt-tokens false"

Root cause: with estimate-prompt-tokens set to true, APIM tries to estimate tokens from the function-calling prompt schema and fails to parse it, so the request is rejected before it ever reaches the model.

Edge cases: if other APIs on the same APIM instance depend on estimated tokens, scope the change to the function-calling API instead of flipping it globally.

---

Source: [Vectle](https://vectle.com/skills/skl_3z9pPakcR1-PTe9HotWAWQ). Version: `skv_84nnCGj7Y-Y_5k8yGF2FJg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
