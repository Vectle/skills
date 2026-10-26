---
name: "importerror-cannot-import-name-asn1-fr-c6ffea1907df2901"
description: "Third-person routing: this skill fixes the cryptography error cannot import name 'asn1' from 'cryptography.hazmat.bindings._rust', which means the installed package mixes stub .pyi files with a missing or broken native _rust extension. Use when the traceback ends in cryptography.hazmat.bindings._rust. Not for default_backend removal, OpenSSL symbol errors, or pure-Python usage."
metadata:
  skill_id: "skl_TRaQuhUXQgd83uDl9rIcmQ"
  title: "ImportError: cannot import name 'asn1' from 'cryptography.hazmat.bindings._rust'"
  version: "skv_QXT5bqXng-XYFfN2yk5m7g"
  updated: "2026-10-03T05:59:51.370128+00:00"
  canonical_url: "https://vectle.com/skills/skl_TRaQuhUXQgd83uDl9rIcmQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pyca/cryptography/issues/8433\"]"
---

# ImportError: cannot import name 'asn1' from 'cryptography.hazmat.bindings._rust'

TL;DR: your cryptography install is half-broken. The pure-Python stubs (.pyi files) are there but the compiled native extension (_rust.abi3.so) is missing or mismatched. Fix it with a clean reinstall: `pip uninstall cryptography -y` then `pip install --no-cache-dir cryptography`.

```text
ImportError: cannot import name 'asn1' from 'cryptography.hazmat.bindings._rust'
```

## The fix

1. Confirm the native extension is missing:
```
python -c "import cryptography.hazmat.bindings._rust, os; print(os.path.dirname(cryptography.hazmat.bindings._rust.__file__))"
ls [that-dir] | grep -i "rust.*\.so"
```
Success check: you see only `.pyi` stub files and no `_rust.abi3.so`. That confirms the diagnosis.

2. Clean reinstall:
```
pip uninstall -y cryptography
pip install --no-cache-dir cryptography
```

3. Verify:
```
python -c "from cryptography.hazmat.bindings._rust import asn1; print('ok')"
```
Expected output: `ok`.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=cryptography+asn1+_rust'`

## When this applies
- Traceback goes through `cryptography/hazmat/primitives/...` down to `from cryptography.hazmat.bindings._rust import asn1`.
- The failing import is triggered by paramiko, pyOpenSSL, or anything importing cryptography.

## When it does NOT apply
- `cannot import name 'default_backend'`: version-removal issue, different fix.
- `undefined symbol: SSL_...` or `dlopen` failures: OpenSSL mismatch, different fix.

## Tool and version compatibility
cryptography 37+ (rust-backed), Python 3.7+, any OS. Most common on Linux systems with mixed distro/pip installs.

## Why it happens
Since 37.0 cryptography ships Rust code compiled into _rust.abi3.so. A partial upgrade, a copied site-packages, or an interrupted pip install can leave the Python stubs without the compiled half. The .pyi files satisfy nothing at runtime, so the first real import fails.

## Edge cases
- If the reinstall still fails, check for a second cryptography copy on sys.path (distro package vs pip): `python -c "import cryptography; print(cryptography.__file__)"`.
- Conda users: prefer `conda install -c conda-forge cryptography` over mixing pip and conda.
- Never copy site-packages between machines; always reinstall.

---

Source: [Vectle](https://vectle.com/skills/skl_TRaQuhUXQgd83uDl9rIcmQ). Version: `skv_QXT5bqXng-XYFfN2yk5m7g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
