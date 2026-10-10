---
name: "inconsistent-errorresponse-contents-er-727b1f9b05ba910c"
description: "Shows how to fix inconsistent `ErrorResponse` contents: `.error` vs `.message`. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_wwbISpquF7PTvq_9FJwNdA"
  title: "Inconsistent `ErrorResponse` contents: `.error` vs `.message`"
  version: "skv_QtVtkxnsIxEp_5m0V-pEUQ"
  updated: "2026-10-04T15:31:18.694248+00:00"
  canonical_url: "https://vectle.com/skills/skl_wwbISpquF7PTvq_9FJwNdA"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

For "ErrorResponse": to send emails to other recipients, please verify a domain at resend.com/domains, and change the from address to an email using this domain.', name: 'validation\_error' } ` Unexpected ErrorResponse: ``ts { statusCode: 403, er

```text
ErrorResponse
```

## Steps

1. [gabrielmfern (maintainer)]: This seems to've been a regression on the API itself, which we just fixed. If anyone still experiences this, please let me know and I'll reopen.

## When to use

You are seeing this: Issue resend/resend-node#538 (closed, 9 comments): Sometimes the ErrorResponse contains an.error property, sometimes a.message property, as a response to resend.emails.send. Use this skill when you run into "Inconsistent `ErrorResponse` contents: `.error` vs `.message`".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Variants

Other phrasings of the same problem that show up in reports:

### {

```text
{
    statusCode: 403,
    message: 'You can only send testing emails to your own email address ([email redacted]). To send emails to other recipients, please verify a domain at resend.com/domains, and change the `from` address to an email using this domain.',
    name: 'validation_error'
  }
```

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_wwbISpquF7PTvq_9FJwNdA). Version: `skv_QtVtkxnsIxEp_5m0V-pEUQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
