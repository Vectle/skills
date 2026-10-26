---
name: "importerror-cannot-import-name-request-1376bc6a60606998"
description: "Fixes old boto3/botocore-era code that imports requests from botocore.vendored, which botocore removed. Use when upgrading boto3 breaks an import of botocore.vendored.requests. Not for general requests-library problems."
metadata:
  skill_id: "skl_ikzqiGKSjhwvZPm1r87NOg"
  title: "ImportError: cannot import name 'requests' from 'botocore.vendored'"
  version: "skv_IU-4K1Js7PvF2cgwsG46Xw"
  updated: "2026-10-03T06:12:38.144474+00:00"
  canonical_url: "https://vectle.com/skills/skl_ikzqiGKSjhwvZPm1r87NOg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/boto/botocore/issues/2217\"]"
---

TL;DR: botocore used to ship a private copy of the requests library at botocore.vendored.requests, and it was removed. Replace `from botocore.vendored import requests` with a plain `import requests` (pip install requests if needed). Never import from botocore.vendored; it is private API.

```text
ImportError: cannot import name 'requests' from 'botocore.vendored'
```

## Fix it

1. Find the offending import: grep -rn "botocore.vendored" your codebase. Expected: one or more lines importing requests (or six, etc.) from botocore.vendored.
2. Replace `from botocore.vendored import requests` with `import requests`. Expected: the file no longer references botocore.vendored.
3. Make sure requests is installed: pip install requests. Expected: pip show requests prints a version.
4. Rerun your code. Expected: the import succeeds.

## When this applies
- The traceback points at an import from botocore.vendored.
- The code worked with old boto3 (pre-2019 era) and broke after an upgrade.

## When it doesn't
- Your code imports plain `requests` and that fails: you just need pip install requests.
- The failing import is from some other vendored path: same principle, stop importing privates.

## Compatibility
- boto3/botocore >= 1.13 (when the vendored copy was dropped). requests >= 2.20.

## Why it happens
botocore once vendored third-party libraries so installs were self-contained. Vendoring was dropped to reduce security and maintenance burden, which broke anyone importing those private copies directly.

## Edge cases
- botocore.vendored also used to carry six and python-dateutil shims; same fix: install the real package.
- If a dependency (not your code) does this import, upgrade that dependency to a version that no longer uses botocore.vendored.


---

Source: [Vectle](https://vectle.com/skills/skl_ikzqiGKSjhwvZPm1r87NOg). Version: `skv_IU-4K1Js7PvF2cgwsG46Xw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
