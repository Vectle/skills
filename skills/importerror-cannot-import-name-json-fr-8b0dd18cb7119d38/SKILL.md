---
name: "importerror-cannot-import-name-json-fr-8b0dd18cb7119d38"
description: "Third-person routing: this skill fixes ImportError: cannot import name 'json' from 'itsdangerous', which hits Flask apps when itsdangerous 2.1+ removed the json shim that old Flask 1.x/2.0 imports. Use when the traceback shows from itsdangerous import json as _json. Not for TimedJSONWebSignatureSerializer removal or general Flask version conflicts."
metadata:
  skill_id: "skl_0tSx69mWFPhzmXQwrDcz2g"
  title: "ImportError: cannot import name 'json' from 'itsdangerous'"
  version: "skv_fIl9G7u87UlewElMglB-pg"
  updated: "2026-10-03T05:30:46.435095+00:00"
  canonical_url: "https://vectle.com/skills/skl_0tSx69mWFPhzmXQwrDcz2g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/71189819/importerror-cannot-import-name-json-from-itsdangerous\"]"
---

# ImportError: cannot import name 'json' from 'itsdangerous'

TL;DR: itsdangerous 2.1+ removed the `json` shim that old Flask imports. Quick fix: `pip install itsdangerous==2.0.1`. Better fix: upgrade Flask to 2.0.1 or newer, which no longer needs it.

```text
ImportError: cannot import name 'json' from 'itsdangerous'
```

## The fix

1. Pin itsdangerous (fastest, no Flask upgrade):
```
pip install itsdangerous==2.0.1
python -c "from flask import Flask; print('ok')"
```
Success check: prints `ok` and your app starts.

2. Or upgrade Flask instead (cleaner long term):
```
pip install -U "Flask>=2.0.1"
```
Then remove the itsdangerous pin from requirements.txt.

3. Rebuild your Docker image from scratch after either change; a cached layer can keep the old itsdangerous.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=itsdangerous+cannot+import+json'`

## When this applies
- Flask 1.1.x or 2.0.0 with itsdangerous 2.1+ installed.
- Traceback line reads `from itsdangerous import json as _json`.
- Docker builds that suddenly broke when a fresh `pip install` pulled a newer itsdangerous.

## When it does NOT apply
- `cannot import name 'TimedJSONWebSignatureSerializer'`: also a 2.0 removal, different name and fix.
- `cannot import name 'soft_unicode' from 'markupsafe'`: the sibling Flask-era error; fix with markupsafe==2.0.1.

## Tool and version compatibility
Flask 1.1.x/2.0.0 with itsdangerous>=2.1. Fixed pair: Flask>=2.0.1 with any itsdangerous>=2.0, or Flask 1.1.x with itsdangerous==2.0.1.

## Why it happens
Flask used to do `from itsdangerous import json as _json` because itsdangerous bundled a json helper. itsdangerous 2.1 deleted it. Flask fixed their import in 2.0.1, so the error only bites old Flask + new itsdangerous combos, which is exactly what an unpinned `pip install` produces.

## Edge cases
- `pip install Flask==1.1.4` alone can trade this for the markupsafe soft_unicode error; pin markupsafe==2.0.1 with it.
- Check requirements.txt for bare `itsdangerous` with no pin and add the pin there, not just in the container.
- Itsdangerous 2.0.1 still gets security fixes contextually; upgrading Flask is the supported path.

---

Source: [Vectle](https://vectle.com/skills/skl_0tSx69mWFPhzmXQwrDcz2g). Version: `skv_fIl9G7u87UlewElMglB-pg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
