---
name: "loops-custom-contact-property-rejected-d8e46ccae155a153"
description: "Loops: custom contact property rejected - add it in the Loops dashboard first. Add custom properties at loops.so/docs/contacts/properties in your Loops account first, then reference them in API calls. Use when hitting this exact issue with Loops. Not for unrelated errors or different features."
metadata:
  skill_id: "skl_qLMIS2GYEuq7Y2UBC6jHUA"
  title: "Loops: custom contact property rejected - add it in the Loops dashboard first"
  version: "skv_q34kRGYd4V6IPayZIy062w"
  updated: "2026-10-03T15:16:38.420015+00:00"
  canonical_url: "https://vectle.com/skills/skl_qLMIS2GYEuq7Y2UBC6jHUA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Add custom properties at loops.so/docs/contacts/properties in your Loops account first, then reference them in API calls. The default properties (id, email, firstName, lastName, source, subscribed, userGroup, userId, optInStatus) always work.

## The error

```text
custom contact property rejected - add it in the Loops dashboard first
```

## Fix

1. Add custom properties at loops.so/docs/contacts/properties in your Loops account first, then reference them in API calls.
   Expected: You get the expected result; the problem is gone.
2. The default properties (id, email, firstName, lastName, source, subscribed, userGroup, userId, optInStatus) always work.
   Expected: You get the expected result; the problem is gone.
3. When a call fails, the SDK throws APIError with the API JSON in error.json and the HTTP code in error.statusCode (rawBody holds the raw text when the response was not valid JSON), so log both instead of guessing.
   Expected: You get the expected result; the problem is gone.
4. Re-run the original operation and confirm the error is gone.
   Expected: no error, normal output.

## When to use

- You hit this exact error with Loops.
- The symptom matches: custom contact property rejected - add it in the Loops dashboard first.

## When NOT to use

- A different error message from Loops; the cause here is specific to this error.
- Unrelated Loops issues (different feature, different failure).
- You need general documentation for the tool; check the official docs instead.

## Compatibility

Reported against Loops. Source: https://github.com/loops-so/loops-js/blob/HEAD/README.md.

## Variant phrasings

### custom contact property rejected - add it in the Loops dashboard first

## Why it happens

A Loops API call using a custom contact property fails. Custom contact properties must be created in the Loops account before the API will accept them.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/loops-so/loops-js/blob/HEAD/README.md

---

Source: [Vectle](https://vectle.com/skills/skl_qLMIS2GYEuq7Y2UBC6jHUA). Version: `skv_q34kRGYd4V6IPayZIy062w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
