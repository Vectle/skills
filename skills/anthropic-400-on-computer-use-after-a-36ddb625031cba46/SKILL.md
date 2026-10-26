---
name: "anthropic-400-on-computer-use-after-a-36ddb625031cba46"
description: "Computer use calls that worked before return 400 invalid_request_error on Opus 5.5. Covers migrating from computer_20251124 to computer_toolset_20260801, dropping the beta header, and updating the agent loop. Not for 401 auth errors or other Anthropic tool types."
metadata:
  skill_id: "skl_yZGWVSKdeYGgfYd0GgJATg"
  title: "Anthropic 400 on computer use after a model upgrade: the tool type is now computer_toolset_20260801"
  version: "skv_sdVh9uaVDQ3juj1mwTA-Rw"
  updated: "2026-10-03T04:42:17.825096+00:00"
  canonical_url: "https://vectle.com/skills/skl_yZGWVSKdeYGgfYd0GgJATg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.anthropic.com/en/api/errors\"]"
---

TL;DR: Opus 5.5 supports computer use only as the `computer_toolset_20260801` toolset. Sending the older `computer_20251124` type returns 400 invalid_request_error, and the message names the rejected type and lists accepted types after "Did you mean one of". Declare `computer_toolset_20260801`, drop the beta header, and update the agent loop for the toolset. It is not a drop-in rename.

The error, verbatim:

```text
400 invalid_request_error ... Did you mean one of: computer_toolset_20260801 ...
```

Steps:

1. Change the tool declaration to type `computer_toolset_20260801` and drop the beta header. Success: the request no longer 400s.
2. Update the agent loop for the toolset as described in the migrate guide. The action format differs; a rename alone breaks the loop. Success: the tool loop handles the toolset's action format.
3. Keep the old type only for the models and platforms that still accept it (earlier models, and Opus 5.5 on Bedrock). Success: no regressions on other models.

When to use: computer use 400s after moving to Opus 5.5 on the Claude API or Google Cloud.

When not to use: 401s (bad key), 400s on other tool types (check what the model supports), or Bedrock Opus 5.5 (it still accepts the old type).

Compatibility: Anthropic Claude API, Google Cloud Vertex, AWS Bedrock (platform split noted above). Opus 5.5.

Variants:
- anthropic computer use 400 invalid_request_error
- computer_20251124 rejected
- computer_toolset_20260801 migration

Root cause: the model only accepts the toolset form now. The 400 message is unusually helpful: it names the rejected type and lists what it will accept, so the fix is read-the-error, not guess.

Edge cases:
- The same 400 pattern applies to any Anthropic-defined tool type the requested model does not support. Read the "Did you mean" list first.
- The platform split is the trap: code that branches per model needs the branch per platform too.

---

Source: [Vectle](https://vectle.com/skills/skl_yZGWVSKdeYGgfYd0GgJATg). Version: `skv_sdVh9uaVDQ3juj1mwTA-Rw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
