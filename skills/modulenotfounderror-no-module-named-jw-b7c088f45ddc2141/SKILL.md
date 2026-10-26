---
name: "modulenotfounderror-no-module-named-jw-b7c088f45ddc2141"
description: "Third-person routing: this skill fixes ModuleNotFoundError: No module named 'jwt' after installing the wrong package or installing PyJWT into the wrong interpreter. It covers the pip-name vs import-name mismatch (PyJWT provides jwt). Use when import jwt fails. Not for PyJWT API changes, decode algorithm errors, or python-jose confusion."
metadata:
  skill_id: "skl_xlSmzgPDYh_ERSmqcvsU-Q"
  title: "ModuleNotFoundError: No module named 'jwt'"
  version: "skv_fLhEXQO1bAG9sk6xzing2Q"
  updated: "2026-10-03T05:29:29.322142+00:00"
  canonical_url: "https://vectle.com/skills/skl_xlSmzgPDYh_ERSmqcvsU-Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pocheang/payguard-crew/blob/HEAD/docs/guides/TROUBLESHOOTING.md\"]"
---

# ModuleNotFoundError: No module named 'jwt'

TL;DR: the import is `jwt` but the pip package is `PyJWT`. Run `python -m pip install PyJWT`. If it is already installed, your pip and python are different interpreters; `python -m pip` fixes that too.

```text
ModuleNotFoundError: No module named 'jwt'
```

## The fix

1. Install with the same interpreter that runs your code:
```
python -m pip install PyJWT
python -c "import jwt; print(jwt.__version__)"
```
Success check: prints a version like `2.8.0`.

2. If it says already satisfied but the import still fails, you have two Pythons:
```
python -c "import sys; print(sys.executable)"
python -m pip show PyJWT | grep Location
```
The Location must sit under the same prefix as sys.executable. If not, reinstall into the right one with `python -m pip`.

3. If you need RSA/ECDSA support, install the crypto extra: `python -m pip install "PyJWT[crypto]"`.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=pyjwt+No+module+named+jwt'`

## When this applies
- `import jwt` fails right after a fresh clone or in a new venv/CI container.
- A tutorial told you to `pip install jwt`, which installs an unrelated dead package.

## When it does NOT apply
- `ImportError: cannot import name 'PyJWT' from 'jwt'`: you have a shadowing file or ancient version; different fix.
- `jwt.exceptions.ExpiredSignatureError` or decode errors: the import works, your token or call is wrong.
- python-jose users: that package imports as `jose`, not `jwt`.

## Tool and version compatibility
PyJWT 2.x, Python 3.7+. PyJWT 1.x is ancient; upgrade.

## Why it happens
PyPI name and import name differ: `pip install PyJWT` gives you `import jwt`. There is also a squatter package literally named `jwt` that does nothing useful. Installing the wrong one, or installing into a different interpreter than the one running the code, produces exactly this error.

## Edge cases
- A file named `jwt.py` in your project shadows the package; rename it.
- If both `jwt` and `PyJWT` show in pip list, uninstall `jwt`.
- In Docker, make sure the pip install happens in the same layer/stage that runs the app.

---

Source: [Vectle](https://vectle.com/skills/skl_xlSmzgPDYh_ERSmqcvsU-Q). Version: `skv_fLhEXQO1bAG9sk6xzing2Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
