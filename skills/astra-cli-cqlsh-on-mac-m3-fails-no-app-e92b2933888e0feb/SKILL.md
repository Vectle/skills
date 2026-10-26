---
name: "astra-cli-cqlsh-on-mac-m3-fails-no-app-e92b2933888e0feb"
description: "Fixes Astra CLI cqlsh failing on Mac M3 with 'No appropriate python interpreter found' or 'No module named six.moves'. Use this when the downloaded cqlsh bundle meets Python 3.12. Not for other cqlsh errors."
metadata:
  skill_id: "skl_BMxpnM3FZAiIdA7KHQ3tUQ"
  title: "Astra CLI cqlsh on Mac M3 fails: 'No appropriate python interpreter found' / No module named 'six.moves'"
  version: "skv_sEh_YdjSv0tFjL2_rENfHg"
  updated: "2026-10-03T05:31:04.305356+00:00"
  canonical_url: "https://vectle.com/skills/skl_BMxpnM3FZAiIdA7KHQ3tUQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_MBo_hIVcn9eTJY3bwKTiJQ\",\"https://github.com/datastax/astra-cli/issues/225\"]"
---

TL;DR: if `astra db cqlsh` on a Mac M3 fails with `No appropriate python interpreter found` (docker) or `ModuleNotFoundError: No module named 'six.moves'` (homebrew), the CLI downloads the cqlsh bundle into ~/.astra/ and runs it with the machine's Python, but the bundled cqlsh is not compatible with Python 3.12, the M3 default. Use an older Python: `brew install python@3.11` (after removing the 3.12 default if needed); the reporter also confirmed the macOS builtin python worked. In Astra CLI v1.x and later this is handled automatically: the CLI patches the cqlsh runner to try python3.11, python3.10, python3.9 before the default python3, so upgrading the CLI is the durable fix.

```text
No appropriate python interpreter found
ModuleNotFoundError: No module named 'six.moves'
```

## Steps

1. Upgrade the Astra CLI to v1.x+; or install python@3.11 via Homebrew.

2. Re-run `astra db cqlsh`.

   Expected: cqlsh starts. Success check: you get a cqlsh prompt.

## When to use this

- M3 Mac, Python 3.12 default, cqlsh bundle fails.

## When NOT to use this

- Other cqlsh errors; read the message.
- Non-M3 Macs with a compatible Python; it just works.

## Compatibility

- Astra CLI v1.x+ (auto-handles); manual python@3.11 for older CLIs.

## Variant phrasings

- "astra cqlsh M3 six.moves"
- "astra cli no appropriate python interpreter"

## Root cause

The bundled cqlsh predates Python 3.12 and breaks on its removed/renamed modules.

## Edge cases

- Do not break other tools by removing system Python; scope the older Python to cqlsh.

---

Source: [Vectle](https://vectle.com/skills/skl_BMxpnM3FZAiIdA7KHQ3tUQ). Version: `skv_sEh_YdjSv0tFjL2_rENfHg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
