---
name: "pinecone-core-exceptions-pineconeexcep-806025a646029a28"
description: "Python SDK: pinecone.core.exceptions.PineconeException with simple examples. The verified fix is Fix: Reporter's workaround when inference went wrong: pass `project_name` explicitly to `pinecone.init()`. Use this when you hit the symptoms above in python-sdk; not for unrelated python-sdk errors or general setup questions."
metadata:
  skill_id: "skl_15Rt99NRE90dJYB1Opphgw"
  title: "pinecone.core.exceptions.PineconeException with simple examples"
  version: "skv_x6cW3Yqk3BABnZjYMDDH3Q"
  updated: "2026-10-03T04:36:46.825116+00:00"
  canonical_url: "https://vectle.com/skills/skl_15Rt99NRE90dJYB1Opphgw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pinecone-io/python-sdk/issues/154\"]"
---

## TL;DR

Fix: Reporter's workaround when inference went wrong: pass `project_name` explicitly to `pinecone.init()`.

## The error

```text
Issue pinecone-io/python-sdk#154 (closed, 14 comments): I have created a simple script from readme to demonstrate that almost simple example is not working on my end for unknown reasons. I have tested several examples with the same result. However, I tested a JavaScript version that worked perfectly on my end. But I need to work with Python.
Using `Python 3.10.10` with `poetry` on a `Windows` machine. I have spent two days trying to figure out what happened, but I have had no luck.
```python
import logging
```

## Fix

1. Reporter's workaround when inference went wrong: pass `project_name` explicitly to `pinecone.init()`.

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

- How to fix "pinecone.core.exceptions.PineconeException with simple examples" in python-sdk
- python-sdk: pinecone.core.exceptions.PineconeException with simple examples

## Source

- https://github.com/pinecone-io/python-sdk/issues/154

---

Source: [Vectle](https://vectle.com/skills/skl_15Rt99NRE90dJYB1Opphgw). Version: `skv_x6cW3Yqk3BABnZjYMDDH3Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
