---
name: "groq-429-read-the-rpm-tpm-rpd-dimensio-3c8e59e0bd5f2ec1"
description: "Groq 429: read the RPM/TPM/RPD dimension and honor retry-after. 'Rate limit reached for model llama-3.3-70b-versatile on tokens per minute (TPM): Limit 6000, Used 5800, Requested 500' tells you the dimension. Use when hitting this exact issue with Groq 429. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_XkuC3CCNkhL6oqOlX4g7AA"
  title: "Groq 429: read the RPM/TPM/RPD dimension and honor retry-after"
  version: "skv_xZULcZfZkJuDtZ5tRywCyQ"
  updated: "2026-10-03T20:28:45.67546+00:00"
  canonical_url: "https://vectle.com/skills/skl_XkuC3CCNkhL6oqOlX4g7AA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://github.com/funxgao/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/groq-pack/skills/groq-common-errors/SKILL.md\"]"
---

## TL;DR

'Rate limit reached for model llama-3.3-70b-versatile on tokens per minute (TPM): Limit 6000, Used 5800, Requested 500' tells you the dimension.

## Fix

1. 'Rate limit reached for model llama-3.3-70b-versatile on tokens per minute (TPM): Limit 6000, Used 5800, Requested 500' tells you the dimension.
   Expected: you can confirm this matches your situation.

## When to use

- You are setting up or using this Groq 429 feature.
- The symptom matches: read the RPM/TPM/RPD dimension and honor retry-after.

## When NOT to use

- Unrelated Groq 429 issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Groq 429 (mentions 3.3). Source: https://github.com/funxgao/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/groq-pack/skills/groq-common-err.

## Variant phrasings

### read the RPM/TPM/RPD dimension and honor retry-after

## Why it happens

Groq's 429 names the exact dimension you hit. The fix depends on which one.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- Behavior can change between releases; the linked source reflects the versions above.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/funxgao/claude-code-plugins-plus-skills/blob/HEAD/plugins/saas-packs/groq-pack/skills/groq-common-errors/SKILL.md

---

Source: [Vectle](https://vectle.com/skills/skl_XkuC3CCNkhL6oqOlX4g7AA). Version: `skv_xZULcZfZkJuDtZ5tRywCyQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
