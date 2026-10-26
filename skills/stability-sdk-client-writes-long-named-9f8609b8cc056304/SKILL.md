---
name: "stability-sdk-client-writes-long-named-9f8609b8cc056304"
description: "Fixes stability-sdk's client.py writing super-long filenames with no extension and empty files instead of .json and .png outputs. Use this when generation runs but the output files are wrong. Not for API errors or for empty results from the API itself."
metadata:
  skill_id: "skl_D5dZXtbg2NDi8eW9UJAEHQ"
  title: "stability-sdk client writes long-named empty files instead of PNG output"
  version: "skv_zEX3ckL4ZxItZvW_E0R8Sg"
  updated: "2026-10-03T04:47:34.235151+00:00"
  canonical_url: "https://vectle.com/skills/skl_D5dZXtbg2NDi8eW9UJAEHQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_G4Hb526H9Q9Oyg1oCxSCMw\",\"https://github.com/Stability-AI/stability-sdk/issues/57\"]"
---

TL;DR: if `client.py` from stability-sdk produces super-long filenames with no extension and empty files instead of `.json` and `.png`, your installed package is behind the fix. Run `pip install --upgrade stability-sdk`; the filename bug was fixed in PR #67.

## Steps

1. Upgrade the package:

```sh
pip install --upgrade stability-sdk
```

   Expected: installed version includes the PR #67 fix.

2. Re-run `client.py`.

   Expected: outputs land as proper `.json` and `.png` files with normal names. Success check: the PNGs open and have non-zero size.

## When to use this

- client.py writes long-named extensionless empty files instead of PNG/JSON output.
- The pip-installed version is older than the PR #67 fix.

## When NOT to use this

- The API itself errors or returns empty results; check your key and request first.
- You already run the latest package and still see it; file a fresh issue.

## Compatibility

- stability-sdk pip package, versions before the PR #67 fix. Showed up most on Windows, where the long generated names caused the most trouble.

## Variant phrasings

- "stability-sdk client.py empty files"
- "stability sdk long filename no extension"

## Root cause

A filename handling bug in the older package generated over-long artifact names that the filesystem could not write properly. PR #67 fixed the naming.

## Edge cases

- One user worked around it by shortening the artifact filename in client.py, but upgrading is the real fix; do not patch the script.

---

Source: [Vectle](https://vectle.com/skills/skl_D5dZXtbg2NDi8eW9UJAEHQ). Version: `skv_zEX3ckL4ZxItZvW_E0R8Sg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
