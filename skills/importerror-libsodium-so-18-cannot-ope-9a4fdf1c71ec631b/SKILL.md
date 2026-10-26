---
name: "importerror-libsodium-so-18-cannot-ope-9a4fdf1c71ec631b"
description: "Third-person routing: this skill fixes ImportError: libsodium.so.18: cannot open shared object file when importing PyNaCl, which means the bundled libsodium cannot be found at runtime. Use when from nacl._sodium import ffi fails with a missing shared object. Not for undefined-symbol errors or _cffi_backend problems."
metadata:
  skill_id: "skl_mvK--aox7auIoCvHOvMmug"
  title: "ImportError: libsodium.so.18: cannot open shared object file: No such file or directory"
  version: "skv_avTC1nxglMa8T5w0voP13Q"
  updated: "2026-10-03T05:55:12.074146+00:00"
  canonical_url: "https://vectle.com/skills/skl_mvK--aox7auIoCvHOvMmug"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pyca/pynacl/issues/477\"]"
---

# ImportError: libsodium.so.18: cannot open shared object file: No such file or directory

TL;DR: your PyNaCl install linked against a system libsodium that is not there. Reinstall from the prebuilt wheel: `pip uninstall -y pynacl && pip install --no-cache-dir pynacl`.

```text
ImportError: libsodium.so.18: cannot open shared object file: No such file or directory
```

## The fix

1. Force a wheel reinstall (no local build, no cache):
```
python -m pip uninstall -y pynacl
python -m pip install --no-cache-dir pynacl
```

2. Verify:
```
python -c "import nacl.signing; print('ok')"
```
Success check: prints `ok`.

3. If it still fails, install the system library instead (Debian/Ubuntu): `sudo apt-get install libsodium23`, then reinstall pynacl.

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=pynacl+libsodium+cannot+open+shared+object'`

## When this applies
- `from nacl._sodium import ffi, lib` (directly or via nacl.signing) raises the missing .so error.
- You installed with `--no-binary` or on a platform without a wheel.

## When it does NOT apply
- `undefined symbol: crypto_pwhash_...`: version skew between bundled and system libsodium, different fix.
- `No module named '_cffi_backend'`: cffi itself is broken, different fix.

## Tool and version compatibility
PyNaCl 1.3+, Python 3.8+. The wheel bundles libsodium, so this mostly hits source installs and odd platforms.

## Why it happens
PyNaCl can build against the system libsodium instead of its bundled copy. If that build links `libsodium.so.18` and the library is later removed or was never properly installed, the dynamic loader fails at import time.

## Edge cases
- In Docker, a multi-stage build that compiles in one stage and runs in another drops the .so; install pynacl in the final stage.
- conda-forge's pynacl handles the library itself; mixing pip pynacl into a conda env is a common trigger.
- Setting SODIUM_INSTALL=system without actually having libsodium dev headers produces this on next import.

---

Source: [Vectle](https://vectle.com/skills/skl_mvK--aox7auIoCvHOvMmug). Version: `skv_avTC1nxglMa8T5w0voP13Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
