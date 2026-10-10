---
name: "importerror-cannot-import-name-default-b55f7ff494591c53"
description: "Third-person routing: this skill fixes the cryptography upgrade error where code written for cryptography 41 or older calls from cryptography.hazmat.backends import default_backend and dies with ImportError after upgrading to 42+. Use when the traceback names default_backend from cryptography.hazmat.backends. Not for missing rust bindings, OpenSSL symbol errors, or code that never imported default_backend."
metadata:
  skill_id: "skl_QQhAcm16kLNNGOzyFa5JCw"
  title: "ImportError: cannot import name 'default_backend' from 'cryptography.hazmat.backends'"
  version: "skv_8PERANgtPc5hISWCkI3I5A"
  updated: "2026-10-03T05:58:05.529942+00:00"
  canonical_url: "https://vectle.com/skills/skl_QQhAcm16kLNNGOzyFa5JCw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ImportError: cannot import name 'default_backend' from 'cryptography.hazmat.backends'

TL;DR: cryptography 42.0 deleted default_backend. Delete the import line `from cryptography.hazmat.backends import default_backend` and drop any `backend=default_backend()` arguments. Your code works the same because backend arguments have been ignored since version 36.0.

```text
ImportError: cannot import name 'default_backend' from 'cryptography.hazmat.backends'
```

## The fix

1. Remove the import. Delete this line wherever it appears:
```python
from cryptography.hazmat.backends import default_backend
```
Success check: no file in your project mentions default_backend. Search with `grep -rn "default_backend" .` and expect zero hits.

2. Remove backend= arguments from calls. Change:
```python
key [your value] key_size=2048, backend=default_backend())
```
to:
```python
key [your value] key_size=2048)
```

3. Confirm the environment actually upgraded:
```
python -c "import cryptography; print(cryptography.__version__)"
```
Expected output: a version number of 42.0.0 or higher.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=cryptography+default_backend'`

## When this applies
- You upgraded cryptography to 42+ and an old import broke.
- You are fixing a third-party script like RsaCtfTool that still imports default_backend.

## When it does NOT apply
- The error names `cryptography.hazmat.bindings._rust` or `_openssl`: that is a broken native install, not this.
- `ImportError: cannot import name 'asn1'` or similar rust-binding names: different failure.

## Tool and version compatibility
Python 3.8+, cryptography 42.0+ (removed) vs 36.0-41.x (deprecated but present). Any OS.

## Why it happens
cryptography stopped needing backend arguments in 3.1, deprecated them in 36.0, and finally removed `default_backend` in 42.0. Old tutorials and tools still ship the import, so a fresh `pip install -U cryptography` turns working code into an ImportError overnight.

## Edge cases
- Pinning cryptography<42 keeps the import working but leaves you on an old version; better to fix the import.
- If you maintain a library, guard with a try/except import so you work on both old and new versions.
- Some vendored copies of paramiko or old fabric versions import default_backend indirectly; upgrade those packages too.

---

Source: [Vectle](https://vectle.com/skills/skl_QQhAcm16kLNNGOzyFa5JCw). Version: `skv_8PERANgtPc5hISWCkI3I5A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
