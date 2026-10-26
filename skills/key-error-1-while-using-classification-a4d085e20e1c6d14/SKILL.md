---
name: "key-error-1-while-using-classification-a4d085e20e1c6d14"
description: "Fixes the bare KeyError: 1 from Evidently's classification preset by upgrading evidently to 0.4.1 or newer, where the mlflow typing-annotation interaction is resolved. Use when a classification report that worked before suddenly raises KeyError: 1 from Evidently internals with no data changes. Not for KeyErrors from your own column names or data."
metadata:
  skill_id: "skl_CbMJg-Q4dryZ66EUuDTABQ"
  title: "KEY ERROR 1 while using classification preset in Evidently"
  version: "skv_9rb8rnq2BymsQLiDyzjW6g"
  updated: "2026-10-03T04:08:29.152963+00:00"
  canonical_url: "https://vectle.com/skills/skl_CbMJg-Q4dryZ66EUuDTABQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr__y0KPEJmDaONyiaL1WENHw\",\"https://github.com/evidentlyai/evidently/issues/701\"]"
---

## TL;DR

Upgrade Evidently to 0.4.1 or newer with `pip install -U evidently`. A bare `KeyError: 1` from inside the classification preset is caused by mlflow's typing annotations poisoning `typing.List`'s cache, which breaks Evidently's typed code paths. The fix landed in 0.4.1; downgrading does not help.

## The error

```text
KeyError: 1
```

Raised from inside Evidently's classification preset (e.g. running a classification report on a Spark/Databricks notebook). The traceback points into Evidently internals, not your code, and it appears suddenly with no data changes on your side.

## Fix it

1. Check your installed Evidently version:
   ```bash
   pip show evidently | grep Version
   ```
   Success check: the version is below 0.4.1, confirming you are affected.

2. Upgrade Evidently:
   ```bash
   pip install -U evidently
   ```
   Success check: the installed version is 0.4.1 or newer.

3. Re-run the classification report.
   Success check: the report completes with no KeyError.

4. Do not downgrade as a workaround: the reporter confirmed downgrading to 0.3.3 did not help.
   Success check: not applicable; skip downgrading entirely.

## When this applies

- Evidently classification preset raises a bare `KeyError: 1` from library internals.
- The same report worked recently with no data changes.
- mlflow is installed in the same environment (the confirmed trigger).

## When it does not apply

- The KeyError names one of your columns (e.g. `KeyError: 'prediction'`); that is a data/schema mismatch, not this bug.
- You are not using the classification preset, or Evidently is already at 0.4.1+.
- mlflow is not installed and the traceback points at your own code.

## Compatibility

- Evidently: affected below 0.4.1, fixed in 0.4.1 and newer (via PR #712).
- Trigger requires mlflow installed in the same Python environment.
- Spark/Databricks notebooks and plain Python both affected.

## Variant phrasings

- KeyError 1 evidently classification preset
- evidently classification report KeyError
- evidently KeyError 1 mlflow

## Why it happens

mlflow uses typing annotations that get cached incorrectly by `typing.List`'s internal cache. Evidently's classification preset relies on those typed code paths, so the poisoned cache makes a lookup fail with a bare `KeyError: 1`. The maintainers fixed the interaction in evidently 0.4.1. Source: https://github.com/evidentlyai/evidently/issues/701

## Edge cases

- If upgrading is blocked by dependency pins, isolate Evidently and mlflow in separate environments as a temporary measure.
- The error can appear intermittently depending on import order; a fresh kernel or container that imports mlflow first is more likely to trigger it.


---

Source: [Vectle](https://vectle.com/skills/skl_CbMJg-Q4dryZ66EUuDTABQ). Version: `skv_9rb8rnq2BymsQLiDyzjW6g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
