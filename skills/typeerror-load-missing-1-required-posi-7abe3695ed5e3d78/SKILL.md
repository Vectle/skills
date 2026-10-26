---
name: "typeerror-load-missing-1-required-posi-7abe3695ed5e3d78"
description: "Fixes TypeError: load() missing 1 required positional argument: 'Loader' from PyYAML 5.1+. Shows the safe_load replacement and when FullLoader is actually needed. Use when yaml.load with one argument blows up after a PyYAML upgrade. Not for missing-module errors or CLoader import errors."
metadata:
  skill_id: "skl_D1CLHezNZLx9q0E3TAM3sg"
  title: "TypeError: load() missing 1 required positional argument: 'Loader'"
  version: "skv_MyXJcJZ78kwmMNgc4GD-pQ"
  updated: "2026-10-03T05:59:48.50637+00:00"
  canonical_url: "https://vectle.com/skills/skl_D1CLHezNZLx9q0E3TAM3sg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/stanfordnqp/spins-b/issues/81\"]"
---

## TL;DR

Since PyYAML 5.1, yaml.load requires a Loader argument (it warns first, then 6.0 made it an error). In almost every case the fix is one word: call yaml.safe_load(stream) instead of yaml.load(stream). Only reach for Loader=yaml.FullLoader if you truly need non-safe constructs.

## The error

```text
TypeError: load() missing 1 required positional argument: 'Loader'
```

## Fix it

1. Replace `yaml.load(f)` with `yaml.safe_load(f)` and rerun.
   Expected: no TypeError; data loads exactly as before for plain dicts/lists/scalars

2. If safe_load rejects something you need (python objects, timestamps quirks), use `yaml.load(f, Loader=yaml.FullLoader)` instead.
   Expected: loads with the full (but still unsafe-construct-free) loader

3. Grep your repo for other bare `yaml.load(` calls and fix them all at once.
   Expected: grep returns no bare yaml.load( calls

## When this applies

- TypeError: load() missing 1 required positional argument: 'Loader'
- code written for PyYAML 4.x or older now running on 5.1+

## When it does NOT apply

- you actually want the unsafe Loader (rare; think twice, it can execute arbitrary objects)
- CLoader/SafeLoader import errors (different skill)

## Tool and version notes

PyYAML 5.1 through 6.x, all supported Pythons. Behavior change landed in 5.1 (warning) and became a hard error in 6.0.

## Other ways this shows up

### TypeError: load() missing 1 required positional argument: 'Loader' in Ansible or Salt

Same root cause: vendored or pinned old call sites. Fix the call site, dont downgrade PyYAML, since old versions have known deserialization CVEs.

## Why it happens

yaml.load without a Loader could construct arbitrary python objects from untrusted input, a real remote-code-execution vector. Upstream made the Loader mandatory so nobody gets the dangerous default by accident.

## Edge cases

- safe_load cant load custom python objects on purpose; thats the security boundary, not a bug.
- yaml.unsafe_load exists but you should basically never use it on input you didnt write yourself.

---

Source: [Vectle](https://vectle.com/skills/skl_D1CLHezNZLx9q0E3TAM3sg). Version: `skv_MyXJcJZ78kwmMNgc4GD-pQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
