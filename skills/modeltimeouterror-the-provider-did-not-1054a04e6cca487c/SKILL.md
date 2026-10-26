---
name: "modeltimeouterror-the-provider-did-not-1054a04e6cca487c"
description: "The request exceeded the timeout. It is retryable, but if it keeps happening the timeout is wrong for the workload, not the network. Raise it, and for slow models raise it a lot."
metadata:
  skill_id: "skl_mp2oaTskNGM6EQt7Bmuk4g"
  title: "ModelTimeoutError: the provider did not answer in time"
  version: "skv_CqvxAqthdMmgMjC_j9nwOA"
  updated: "2026-10-03T15:22:16.816011+00:00"
  canonical_url: "https://vectle.com/skills/skl_mp2oaTskNGM6EQt7Bmuk4g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.langchain.com/oss/python/langchain/models\"]"
---

**TL;DR:** The request exceeded the timeout. It is retryable, but if it keeps happening the timeout is wrong for the workload, not the network.

## The error

```text
python
model = init_chat_model("openai:gpt-5.5", timeout=120)
```

## The fix

1. Reasoning models and long generations need generous timeouts. A timeout tuned for a chat reply will constantly fire on a thinking model.

2. The error is retryable, so the default retry loop will re-fire the same too-short timeout. Fix the timeout value, not the retry count.

3. If timeouts cluster on one provider or region, check the provider status before blaming your code.

4. For agents, set the timeout on the model instance you pass to create_agent; the agent uses that instance for every model call.

## When to use this

- You are seeing this exact error message; match the block above, not just part of it.
- The failing call matches the scenario in the title: ModelTimeoutError.
- You want the fastest verified fix before digging through logs.

## When not to use this

- Your error text differs from the block above; close cousins often have different causes.
- The stack trace points at a different component than the one in the title.
- You already applied this fix and the error persists; look for a second cause instead of reapplying.

## Compatibility

- Mentions 5.5 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_mp2oaTskNGM6EQt7Bmuk4g). Version: `skv_CqvxAqthdMmgMjC_j9nwOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
