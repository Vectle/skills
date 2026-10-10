---
name: "groq-groq-ratelimiterror-groq-authenti-ea61ce4edce00ffa"
description: "Groq: groq.RateLimitError, groq.AuthenticationError, groq.NotFoundError fixes. For groq.NotFoundError: Model not found, Groq retires models, so check the live model list at console.groq.com/docs/models and update the model name in config. Use when hitting this exact issue with Groq. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_OrNuWzefH24Ot296gQCNbw"
  title: "Groq: groq.RateLimitError, groq.AuthenticationError, groq.NotFoundError fixes"
  version: "skv_g7WsZ8BPf8bWMTgrzFujig"
  updated: "2026-10-03T20:30:08.677991+00:00"
  canonical_url: "https://vectle.com/skills/skl_OrNuWzefH24Ot296gQCNbw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For groq.NotFoundError: Model not found, Groq retires models, so check the live model list at console.groq.com/docs/models and update the model name in config. For groq.RateLimitError, wait before retrying (check current limits at console.groq.com) or temporarily switch providers.

## The error

```text
groq.RateLimitError, groq.AuthenticationError, groq.NotFoundError fixes
```

## Fix

1. For groq.NotFoundError: Model not found, Groq retires models, so check the live model list at console.groq.com/docs/models and update the model name in config.
   Expected: You see the expected output instead of the problem.
2. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Groq.
- The symptom matches: groq.RateLimitError, groq.AuthenticationError, groq.NotFoundError fixes.

## When NOT to use

- A different error message from Groq; the cause here is specific to this error.
- Unrelated Groq issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Groq. Source: https://github.com/dotdev262/rag-nettwin/blob/HEAD/docs/TROUBLESHOOTING.md.

## Variant phrasings

### groq.RateLimitError, groq.AuthenticationError, groq.NotFoundError fixes

## Why it happens

Three Groq API errors keep recurring in integrations: groq.RateLimitError (Rate limit exceeded), groq.AuthenticationError (Invalid API key), and groq.NotFoundError (Model not found). Each has a distinct fix, and mixing them up wastes debugging time.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/dotdev262/rag-nettwin/blob/HEAD/docs/TROUBLESHOOTING.md

---

Source: [Vectle](https://vectle.com/skills/skl_OrNuWzefH24Ot296gQCNbw). Version: `skv_g7WsZ8BPf8bWMTgrzFujig`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
