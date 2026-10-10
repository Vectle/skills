---
name: "can-t-instantiate-abstract-class-basen-cc62977e81fa93de"
description: "Llama Index: can't instantiate abstract class BaseNode with abstract methods. The verified fix is Fix: create a fresh virtualenv and install only what you need (python -m venv venv; pip install llama-index; pip install [integration packages]), or pip uninstall llama-index then pip install llama-index --upgrade. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_gFbv4CjNMMfXKHISJsBHUA"
  title: "Can't instantiate abstract class BaseNode with abstract methods"
  version: "skv_uYdOdGZcW6r4eac1I8ur4A"
  updated: "2026-10-03T05:55:41.07265+00:00"
  canonical_url: "https://vectle.com/skills/skl_gFbv4CjNMMfXKHISJsBHUA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: create a fresh virtualenv and install only what you need (python -m venv venv; pip install llama-index; pip install [integration packages]), or pip uninstall llama-index then pip install llama-index --upgrade. Reporter gingerwizard confirmed: 'Resolved for me when i completely cleaned the env.'.

## The error

```text
Issue run-llama/llama_index#10697 (closed, 42 comments): ### Bug Description Any vector store which returns a TextNode to the query method, i get the following error ` File "pydantic/main.py", line 341, in pydantic.main.BaseModel.__init__ pydantic.error_wrappers.ValidationError: 1 validation error for NodeWithScore node Can't instantiate abstract class BaseNode with abstract methods get_content, get_metadata_str, get_type, hash, set_content (type=type_error)` ### Version v0.10.3 ### Steps to Reproduce ``` VectorStoreIndex.from_vector_store(vector_store) engine = clickhouse_vector_store().as_query_engine( similarity_top_k=10) response = engine.query(
```

## Fix

1. Fix: create a fresh virtualenv and install only what you need (python -m venv venv; pip install llama-index; pip install [integration packages]), or pip uninstall llama-index then pip install llama-index --upgrade.
2. Reporter gingerwizard confirmed: 'Resolved for me when i completely cleaned the env.'

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in llama_index.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in llama_index, even a similar-looking one.
- General llama_index setup or credential questions.

## Compatibility

- Llama Index (run-llama/llama_index) Reported against version v0.10.3.

## Variant phrasings

- How to fix "can't instantiate abstract class BaseNode with abstract methods" in llama_index
- llama_index: can't instantiate abstract class BaseNode with abstract methods

## Root cause

Maintainer nerdai confirmed the root cause is a polluted environment: legacy llama-index (0.9.x, llama_index.legacy) installed alongside the v0.10 namespaced packages breaks isinstance checks and class resolution ('Any legacy llama-index lingering in the virtual envs will certainly cause some issues').

## Source

- https://github.com/run-llama/llama_index/issues/10697

---

Source: [Vectle](https://vectle.com/skills/skl_gFbv4CjNMMfXKHISJsBHUA). Version: `skv_uYdOdGZcW6r4eac1I8ur4A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
