---
name: "ggshield-valueerror-invalid-literal-fo-c26287af14473d2e"
description: "Fixes ggshield 1.51.0 crashing at startup on macOS with ValueError: invalid literal for int() with base 10: ''. Use this when every ggshield run dies before scanning after a Homebrew install. Not for scan failures or for non-macOS installs."
metadata:
  skill_id: "skl_9PXmxBrwzuy0y9BqqDtHkg"
  title: "ggshield ValueError: invalid literal for int() with base 10: '' on macOS"
  version: "skv_HwUs24dDJR1SQStXxXxjEA"
  updated: "2026-10-03T04:44:40.121086+00:00"
  canonical_url: "https://vectle.com/skills/skl_9PXmxBrwzuy0y9BqqDtHkg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_erskcdfVrI-Jc03fyJmzQw\",\"https://github.com/GitGuardian/ggshield/issues/1265\"]"
---

TL;DR: if ggshield 1.51.0 installed via Homebrew crashes on every run with `ValueError: invalid literal for int() with base 10: ''`, the `setup_truststore()` step failed to parse the macOS version string. Run `brew upgrade ggshield` to get 1.52.1, where it falls back to the bundled certifi certificates instead of crashing.

```text
ValueError: invalid literal for int() with base 10: ''
```

## Steps

1. Upgrade:

```sh
brew upgrade ggshield
```

   Expected: ggshield 1.52.1+.

2. Re-run your scan.

   Expected: no more startup crash. Success check: the scan completes normally.

## When to use this

- ggshield 1.51.0 via Homebrew on macOS, every run crashes at startup before scanning.

## When NOT to use this

- Scans fail after starting; that is a different problem.
- Non-macOS installs; the version-string parsing is macOS-specific.

## Compatibility

- ggshield 1.52.1+.

## Variant phrasings

- "ggshield macOS ValueError int base 10"
- "ggshield crashes startup homebrew"

## Root cause

`setup_truststore()` tried to parse the macOS version string and died on an empty value; the fix falls back to bundled certifi certificates when parsing fails.

## Edge cases

- None; the fallback covers unparseable version strings generally.

---

Source: [Vectle](https://vectle.com/skills/skl_9PXmxBrwzuy0y9BqqDtHkg). Version: `skv_HwUs24dDJR1SQStXxXxjEA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
