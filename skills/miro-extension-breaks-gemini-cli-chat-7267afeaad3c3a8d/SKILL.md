---
name: "miro-extension-breaks-gemini-cli-chat-7267afeaad3c3a8d"
description: "Miro extension breaks Gemini CLI chat with 400 INVALID_ARGUMENT. The extension tool and parameter names collided with something Gemini CLI rejected. Use when hitting this exact issue. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_QhasSBp3WkjDexFkU4Mnyw"
  title: "Miro extension breaks Gemini CLI chat with 400 INVALID_ARGUMENT"
  version: "skv_69yINsMCRd3Vt7VB-DbaOA"
  updated: "2026-10-03T22:26:59.433988+00:00"
  canonical_url: "https://vectle.com/skills/skl_QhasSBp3WkjDexFkU4Mnyw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/miroapp/miro-ai/issues/10\"]"
---

## TL;DR

The extension tool and parameter names collided with something Gemini CLI rejected. Miro updated their tool and parameter names to fix it: restart Gemini CLI so it re-fetches the tool list from the extension, and chat works again.

## Fix

1. The extension tool and parameter names collided with something Gemini CLI rejected.
   Expected: You get the expected result; the problem is gone.
2. Miro updated their tool and parameter names to fix it: restart Gemini CLI so it re-fetches the tool list from the extension, and chat works again.
   Expected: You get the expected result; the problem is gone.
3. If the 400 persists, make sure you are on the latest version of the miro-ai extension.
   Expected: You get the expected result; the problem is gone.

## When to use

- You are dealing with this situation.
- The symptom matches: Miro extension breaks Gemini CLI chat with 400 INVALID_ARGUMENT.

## When NOT to use

- Unrelated issues with a different cause.
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported per the linked source.

## Variant phrasings

### Miro extension breaks Gemini CLI chat with 400 INVALID_ARGUMENT

## Why it happens

GitHub issue on miroapp/miro-ai: after installing the miro-ai extension, every Gemini CLI chat attempt fails with a 400 INVALID_ARGUMENT API error until the extension is removed.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_QhasSBp3WkjDexFkU4Mnyw). Version: `skv_69yINsMCRd3Vt7VB-DbaOA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
