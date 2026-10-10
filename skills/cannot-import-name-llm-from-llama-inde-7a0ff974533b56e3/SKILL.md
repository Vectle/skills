---
name: "cannot-import-name-llm-from-llama-inde-7a0ff974533b56e3"
description: "Llama Index: cannot import name 'LLM' from 'llama_index.core.llms'. The verified fix is Fix: Collaborator logan-markewich: the v0.10 split into namespaced packages (llama-index-core + integrations) means any remnants of an old 0.9.x install - globally, outside the venv, or pulled in by another dependency - break imports. Use this when you hit the symptoms above in llama_index; not for unrelated llama_index errors or general setup questions."
metadata:
  skill_id: "skl_ZF8xeAHfm34G42z8I4LHJw"
  title: "cannot import name 'LLM' from 'llama_index.core.llms'"
  version: "skv_DVD9WBWbzX3sEiFsZrrPwg"
  updated: "2026-10-03T04:48:24.346113+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZF8xeAHfm34G42z8I4LHJw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Collaborator logan-markewich: the v0.10 split into namespaced packages (llama-index-core + integrations) means any remnants of an old 0.9.x install - globally, outside the venv, or pulled in by another dependency - break imports. Fix in a fresh terminal: pip uninstall llama-index (remove any global install), create a fresh venv, pip install llama-index --upgrade --no-cache-dir --force-reinstall.

## The error

```text
Issue run-llama/llama_index#11302 (closed, 23 comments): ### Bug Description When trying to import via ``` from llama_index.core.indices import VectorStoreIndex from llama_index.core.readers import SimpleDirectoryReader from llama_index.core.storage import StorageContext ``` ### Version 0.10.11 ### Steps to Reproduce install llama index in a new venv with poetry. I delted both `.venv` and `poetry.lock` - the error persists. ### Relevant Logs/Tracbacks ```shell ImportError Traceback (most recent call last) Cell In[8], line 1 ----> 1 from llama_index.core.indices import VectorStoreIndex 2 from llama_index.core.readers import SimpleDirectoryReader 3 fr
```

## Fix

1. Collaborator logan-markewich: the v0.10 split into namespaced packages (llama-index-core + integrations) means any remnants of an old 0.9.x install - globally, outside the venv, or pulled in by another dependency - break imports.
2. Fix in a fresh terminal: pip uninstall llama-index (remove any global install), create a fresh venv, pip install llama-index --upgrade --no-cache-dir --force-reinstall.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in llama_index.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in llama_index, even a similar-looking one.
- General llama_index setup or credential questions.

## Compatibility

- Llama Index (run-llama/llama_index) Reported against version 0.10.11.

## Variant phrasings

- How to fix "cannot import name 'LLM' from 'llama_index.core.llms'" in llama_index
- llama_index: cannot import name 'LLM' from 'llama_index.core.llms'

## Source

- https://github.com/run-llama/llama_index/issues/11302

---

Source: [Vectle](https://vectle.com/skills/skl_ZF8xeAHfm34G42z8I4LHJw). Version: `skv_DVD9WBWbzX3sEiFsZrrPwg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
