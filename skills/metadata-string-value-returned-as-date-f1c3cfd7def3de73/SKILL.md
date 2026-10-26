---
name: "metadata-string-value-returned-as-date-f1c3cfd7def3de73"
description: "Python SDK: metadata string value returned as datetime.date. The verified fix is Fixed in the non-GRPC client so date-like strings round-trip as strings (reporter confirmed). Use this when you hit the symptoms above in python-sdk; not for unrelated python-sdk errors or general setup questions."
metadata:
  skill_id: "skl_EdL8nZdnkivelAZ1bYnjuA"
  title: "Metadata string value returned as datetime.date"
  version: "skv_JFNMsw6IYtbrwtCdb1jzsA"
  updated: "2026-10-03T04:36:06.24601+00:00"
  canonical_url: "https://vectle.com/skills/skl_EdL8nZdnkivelAZ1bYnjuA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pinecone-io/python-sdk/issues/161\"]"
---

## TL;DR

Fixed in the non-GRPC client so date-like strings round-trip as strings (reporter confirmed). If you see datetime coercion in metadata, make sure you are on the fixed client version and using the non-GRPC path.

## The error

```text
Issue pinecone-io/python-sdk#161 (closed, 9 comments): ### Is this a new bug in the Pinecone Python client?
- [X] I believe this is a new bug in the Pinecone Python Client
- [X] I have searched the existing issues, and I could not find an existing issue for this bug
```

## Fix

1. Fixed in the non-GRPC client so date-like strings round-trip as strings (reporter confirmed).
2. If you see datetime coercion in metadata, make sure you are on the fixed client version and using the non-GRPC path.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in python-sdk.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in python-sdk, even a similar-looking one.
- General python-sdk setup or credential questions.

## Compatibility

- Python SDK (pinecone-io/python-sdk)

## Variant phrasings

- How to fix "metadata string value returned as datetime.date" in python-sdk
- python-sdk: metadata string value returned as datetime.date

## Source

- https://github.com/pinecone-io/python-sdk/issues/161

---

Source: [Vectle](https://vectle.com/skills/skl_EdL8nZdnkivelAZ1bYnjuA). Version: `skv_JFNMsw6IYtbrwtCdb1jzsA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
