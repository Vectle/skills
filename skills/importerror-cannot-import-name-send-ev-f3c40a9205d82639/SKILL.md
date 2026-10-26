---
name: "importerror-cannot-import-name-send-ev-f3c40a9205d82639"
description: "Haystack: importError: cannot import name 'send_event' from 'haystack.telemetry'. The verified fix is Fix: uninstall both, then install only one (pip install farm-haystack OR pip install haystack-ai) in a clean venv. Use this when you hit the symptoms above in haystack; not for unrelated haystack errors or general setup questions."
metadata:
  skill_id: "skl_i6ikbqTRZGebSA1I0iGDaw"
  title: "ImportError: cannot import name 'send_event' from 'haystack.telemetry'"
  version: "skv_Wrejc5nU1nULk0sL-5RXYQ"
  updated: "2026-10-03T05:06:09.355208+00:00"
  canonical_url: "https://vectle.com/skills/skl_i6ikbqTRZGebSA1I0iGDaw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/deepset-ai/haystack/issues/6652\"]"
---

## TL;DR

Fix: uninstall both, then install only one (pip install farm-haystack OR pip install haystack-ai) in a clean venv.

## The error

```text
Issue deepset-ai/haystack#6652 (closed, 25 comments): **Describe the bug** When I try to import haystack from pipeline from haystack import Pipeline, I get this error. **Error message** ImportError: cannot import name 'send_event' from 'haystack.telemetry' ([HOME]/... **Expected behavior** Telemetry should run as expected. **To reproduce** Make a file with "from haystack import pipelines". Try to run it. ``` File "[HOME]/...", line 1, in [module] from haystack import pipelines File "[HOME]/...
```

## Fix

1. Fix: uninstall both, then install only one (pip install farm-haystack OR pip install haystack-ai) in a clean venv.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in haystack.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in haystack, even a similar-looking one.
- General haystack setup or credential questions.

## Compatibility

- Haystack (deepset-ai/haystack)

## Variant phrasings

- How to fix "importError: cannot import name 'send_event' from 'haystack.telemetry'" in haystack
- haystack: importError: cannot import name 'send_event' from 'haystack.telemetry'

## Source

- https://github.com/deepset-ai/haystack/issues/6652

---

Source: [Vectle](https://vectle.com/skills/skl_i6ikbqTRZGebSA1I0iGDaw). Version: `skv_Wrejc5nU1nULk0sL-5RXYQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
