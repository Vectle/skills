---
name: "modulenotfounderror-no-module-named-cr-9f110c5bcfee816d"
description: "Third-person routing: this skill fixes ModuleNotFoundError: No module named 'Crypto' after installing PyCryptodome or pycrypto. It covers the pip-name vs import-name mismatch, the Windows crypto-vs-Crypto namespace collision, and cleaning out conflicting installs. Use when code does from Crypto.Cipher import AES and the import fails. Not for Cryptodome namespace (pycryptodomex) or old pycrypto-specific errors."
metadata:
  skill_id: "skl_yYUlQSrr4W6sVcUbM3piAQ"
  title: "ModuleNotFoundError: No module named 'Crypto'"
  version: "skv_U2oy1DZu9cyw1nQj9i0fjw"
  updated: "2026-10-03T05:53:55.295027+00:00"
  canonical_url: "https://vectle.com/skills/skl_yYUlQSrr4W6sVcUbM3piAQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ModuleNotFoundError: No module named 'Crypto'

TL;DR: the import is `Crypto` but the pip package is `pycryptodome`. Run `pip install pycryptodome`. If it is already installed and still fails, you have a namespace collision: `pip uninstall -y crypto pycrypto pycryptodome` then `pip install pycryptodome`.

```text
ModuleNotFoundError: No module named 'Crypto'
```

## The fix

1. Install the right package:
```
python -m pip install pycryptodome
python -c "from Crypto.Cipher import AES; print('ok')"
```
Success check: prints `ok`.

2. If it is already installed but still fails, check for squatters:
```
python -m pip list 2>/dev/null | grep -i -E "crypto"
```
If you see `crypto` or `pycrypto` alongside `pycryptodome`, nuke all three and reinstall only pycryptodome:
```
python -m pip uninstall -y crypto pycrypto pycryptodome
python -m pip install --no-cache-dir pycryptodome
```

3. On Windows, check site-packages for a lowercase `crypto` folder and delete it by hand if the uninstall left it behind.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=pycryptodome+No+module+named+Crypto'`

## When this applies
- `from Crypto.Cipher import AES` (or any `Crypto.*` import) fails.
- You ran `pip install crypto` and expected the Crypto namespace; that is a different, unrelated package.

## When it does NOT apply
- Your code imports `Cryptodome` (with an o): that needs the `pycryptodomex` package instead.
- `ImportError: cannot import name 'AES' from 'Crypto.Cipher'`: the namespace exists but something else is off; see the AES variant skill.

## Tool and version compatibility
pycryptodome 3.x, Python 3.6+, Windows/Linux/macOS. pycrypto is dead; do not install it.

## Why it happens
PyCryptodome installs under the `Crypto` namespace but is published as `pycryptodome` on PyPI. The unrelated `crypto` package claims the same namespace, and on Windows the filesystem is case-insensitive so `crypto` and `Crypto` collide. pip then installs PyCryptodome's files into the squatter's directory.

## Edge cases
- Multiple interpreters: always use `python -m pip` so pip and python are the same environment.
- A file named `Crypto.py` in your project shadows the package; rename it.
- `pycryptodomex` is the conflict-free alternative (`from Cryptodome.Cipher import AES`) if you must coexist with old pycrypto.

---

Source: [Vectle](https://vectle.com/skills/skl_yYUlQSrr4W6sVcUbM3piAQ). Version: `skv_U2oy1DZu9cyw1nQj9i0fjw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
