---
name: "importerror-cannot-import-name-modelme-d94aab388e96ec7b"
description: "Fixes ImportError: cannot import name 'ModelMetaclass' from 'pydantic.main' Use when v2 code importing ModelMetaclass from pydantic.main Not for: normal BaseModel subclassing (you never need the metaclass)"
metadata:
  skill_id: "skl_ahE58EiFPGitSuTu6xJqiw"
  title: "ImportError: cannot import name 'ModelMetaclass' from 'pydantic.main'"
  version: "skv_zYcJMBLXDQbdLjSdqoLykg"
  updated: "2026-10-03T04:43:44.263286+00:00"
  canonical_url: "https://vectle.com/skills/skl_ahE58EiFPGitSuTu6xJqiw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'ModelMetaclass' from 'pydantic.main'

`ModelMetaclass` is not public API in v2. If you just need a model's metaclass, use `type(YourModel)` instead of importing it. If a library does this (motor-odm did), upgrade the library. The class does exist at `pydantic._internal._model_construction`, but that is private and can move between releases.

## The exact error

```text
ImportError: cannot import name 'ModelMetaclass' from 'pydantic.main'
```

## Fix it

1. Replace `from pydantic.main import ModelMetaclass` usage: `type(MyModel)` gives you the metaclass.
   Expected: no import needed

2. If a library does this (motor-odm did), upgrade the library.
   Expected: fixed upstream

3. Last resort: import from `pydantic._internal._model_construction`.
   Expected: works but pinned to internals

## When this applies

v2 code importing ModelMetaclass from pydantic.main

## When this does NOT apply

normal BaseModel subclassing (you never need the metaclass)

## Versions

pydantic v2

## Why it happens

v2 rebuilt the internals; ModelMetaclass left the public namespace.

## Edge cases

Depending on _internal ties you to exact pydantic versions; avoid in libraries.


---

Source: [Vectle](https://vectle.com/skills/skl_ahE58EiFPGitSuTu6xJqiw). Version: `skv_zYcJMBLXDQbdLjSdqoLykg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
