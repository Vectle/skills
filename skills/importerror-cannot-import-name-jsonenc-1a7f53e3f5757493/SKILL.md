---
name: "importerror-cannot-import-name-jsonenc-1a7f53e3f5757493"
description: "Fixes `ImportError: cannot import name 'JSONEncoder' from 'flask.json'` in flask. Use when a Flask 2.2/2.3 upgrade breaks a custom JSON encoder imported from flask.json. Not for 'Object of type X is not JSON serializable' at runtime; that means the provider is fine but a type lacks a handler."
metadata:
  skill_id: "skl_gnYAZD-iJt2-tUwdSU2RMQ"
  title: "ImportError: cannot import name 'JSONEncoder' from 'flask.json'"
  version: "skv_s5TfP5ELmpFPwfLq0yI_HQ"
  updated: "2026-10-03T05:59:48.831655+00:00"
  canonical_url: "https://vectle.com/skills/skl_gnYAZD-iJt2-tUwdSU2RMQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ImportError: cannot import name 'JSONEncoder' from 'flask.json'

## TL;DR
Flask 2.2 deprecated and 2.3 removed flask.json.JSONEncoder. Subclass flask.json.provider.DefaultJSONProvider and override default() instead, then set it as app.json_provider_class. That is the supported way to customize JSON output now.

## The error
```text
ImportError: cannot import name 'JSONEncoder' from 'flask.json'
```

## Fix it
1. Locate the custom encoder: grep -rn "JSONEncoder" --include=*.py .
   Expected: Usually one class subclassing flask.json.JSONEncoder.
2. Rewrite it as a provider: class MyProvider(DefaultJSONProvider): def default(self, obj): ... and set app.json_provider_class = MyProvider (or pass it via app.json).
   Expected: Custom types serialize exactly as before.
3. Delete the old import from flask.json. The provider import is from flask.json.provider import DefaultJSONProvider.
   Expected: No ImportError on startup.
4. Hit your JSON endpoints and confirm the output matches the old format.
   Expected: Responses are byte-identical to before the upgrade.

## When to use this
Use when a Flask 2.2/2.3 upgrade breaks a custom JSON encoder imported from flask.json.

## When NOT to use this
Not for 'Object of type X is not JSON serializable' at runtime; that means the provider is fine but a type lacks a handler.

## Version notes
JSONEncoder deprecated in Flask 2.2, removed in 2.3. DefaultJSONProvider is the replacement across 2.2+ and 3.x.

## Why it happens
Flask replaced its encoder-class customization point with a provider class. The old JSONEncoder name was deleted, so any subclass import fails immediately on Flask 2.3+.

## Edge cases
app.json_encoder assignments are also ignored on 2.2+; the provider class is the only hook that still works.


---

Source: [Vectle](https://vectle.com/skills/skl_gnYAZD-iJt2-tUwdSU2RMQ). Version: `skv_s5TfP5ELmpFPwfLq0yI_HQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
