---
name: "importerror-cannot-import-name-keras-f-dc342c1ed5c17650"
description: "Resolves `from tensorflow import keras` failing on TF 2.16+ by switching to the standalone keras package. Use when the traceback says cannot import name 'keras' from 'tensorflow'. Not for plain tensorflow install failures."
metadata:
  skill_id: "skl_Ms7kztIREpSWHfVFnI9--w"
  title: "ImportError: cannot import name 'keras' from 'tensorflow'"
  version: "skv_3dN5y49IRo1oB47WOoeg1w"
  updated: "2026-10-03T06:09:22.035107+00:00"
  canonical_url: "https://vectle.com/skills/skl_Ms7kztIREpSWHfVFnI9--w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: Use `import keras` (the standalone Keras 3 package) instead, or `tf.keras` for the bundled API. In TF 2.16+, Keras 3 moved out of the tensorflow package, so `from tensorflow import keras` breaks. Install the standalone keras package and change the import.

The error:
```text
ImportError: cannot import name 'keras' from 'tensorflow' (.../tensorflow/__init__.py)
```

## Fix
1. Run `python -c "import tensorflow as tf; print(tf.__version__)"`
   Expected: prints 2.16 or newer, confirming Keras 3 split
2. Install it: `pip install keras`
   Expected: Successfully installed keras
3. Change `from tensorflow import keras` to `import keras` (or keep `tf.keras` if you want the bundled API)
   Expected: import works, no ImportError

## When this applies
- `from tensorflow import keras` fails on TF 2.16+
- you want the standalone Keras 3 API

## When this does not apply
- `import tensorflow` itself fails (different problem)
- you are on TF 2.15 or older, where `from tensorflow import keras` still works

## Version compatibility
TensorFlow 2.16+. Keras 3 lives in its own `keras` package; `tf.keras` remains as a compatibility shim.

## Why it happens
Starting with TF 2.16, Keras 3 became a separate package. `tensorflow/__init__.py` no longer exports the `keras` name the way older versions did, so the from-import fails while attribute-style `tf.keras` keeps working.

## Edge cases
- `tf.keras` and standalone `keras` can behave differently on saving/loading models; pick one and stay consistent.
- If a library does `from tensorflow import keras` internally, pin tensorflow<2.16 or patch the library.
- Check `pip show keras` vs `pip show tf-keras`; mixing them causes subtle bugs.

---

Source: [Vectle](https://vectle.com/skills/skl_Ms7kztIREpSWHfVFnI9--w). Version: `skv_3dN5y49IRo1oB47WOoeg1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
