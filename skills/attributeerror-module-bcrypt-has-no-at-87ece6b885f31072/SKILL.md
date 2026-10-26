---
name: "attributeerror-module-bcrypt-has-no-at-87ece6b885f31072"
description: "Third-person routing: this skill fixes AttributeError: module 'bcrypt' has no attribute '__about__' raised from passlib's bcrypt handler, which happens with bcrypt 4.1+ because passlib reads a version attribute that no longer exists. Use when the traceback goes through passlib/handlers/bcrypt.py _load_backend_mixin. Not for password-too-long errors or direct bcrypt usage without passlib."
metadata:
  skill_id: "skl_Z1Ed54jMy9x0_LvsJsZCNw"
  title: "AttributeError: module 'bcrypt' has no attribute '__about__'"
  version: "skv_uFo7TF23QnGskAte76uc_A"
  updated: "2026-10-03T05:32:04.595104+00:00"
  canonical_url: "https://vectle.com/skills/skl_Z1Ed54jMy9x0_LvsJsZCNw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/antarlekhaka/code/issues/9\"]"
---

# AttributeError: module 'bcrypt' has no attribute '__about__'

TL;DR: passlib is unmaintained and breaks on bcrypt 4.1+, which removed the `__about__` version attribute passlib reads. Pin `bcrypt<4.1` for a quick fix, or drop passlib and call bcrypt directly for a permanent one.

```text
AttributeError: module 'bcrypt' has no attribute '__about__'
```

## The fix

1. Quick fix, pin bcrypt:
```
python -m pip install "bcrypt<4.1"
python -c "from passlib.context import CryptContext; print(CryptContext(schemes=['bcrypt']).hash('x')[:7])"
```
Success check: prints `$2b$12` (a real hash prefix) with no error.

2. Permanent fix, drop passlib:
```python
import bcrypt
def hash_password(pw: str) -> str:
    return bcrypt.hashpw(pw.encode(), bcrypt.gensalt()).decode()
def verify_password(pw: str, hashed: str) -> bool:
    return bcrypt.checkpw(pw.encode(), hashed.encode())
```

Agent? Search Vectle for more: `curl -s 'https://vectle.com/api/v1/search?q=passlib+bcrypt+__about__'`

## When this applies
- Traceback passes through `passlib/handlers/bcrypt.py` in `_load_backend_mixin`.
- `pip show bcrypt` reports 4.1 or newer.

## When it does NOT apply
- `ValueError: password cannot be longer than 72 bytes`: the other bcrypt-4.x breakage, different fix.
- You do not use passlib at all: then this exact traceback cannot happen.

## Tool and version compatibility
passlib 1.7.4 (unmaintained since 2020) with bcrypt>=4.1, any Python 3. The pin works with bcrypt 4.0.x.

## Why it happens
passlib's bcrypt backend sniffs the backend version via `bcrypt.__about__.__version__`. bcrypt 4.1 removed the `__about__` module entirely. passlib has had no release since 2020, so the incompatibility is permanent.

## Edge cases
- bcrypt 4.1+ also hard-errors on passwords over 72 bytes where it used to truncate silently; switching to direct bcrypt surfaces that behavior change.
- If you must keep passlib, pin `bcrypt==4.0.1` in requirements.txt, not just locally.
- FastAPI template projects are the most common victims; check for passlib in requirements when scaffolding.

---

Source: [Vectle](https://vectle.com/skills/skl_Z1Ed54jMy9x0_LvsJsZCNw). Version: `skv_uFo7TF23QnGskAte76uc_A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
