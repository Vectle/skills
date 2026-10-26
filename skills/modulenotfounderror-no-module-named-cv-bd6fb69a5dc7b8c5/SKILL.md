---
name: "modulenotfounderror-no-module-named-cv-bd6fb69a5dc7b8c5"
description: "Fixes ModuleNotFoundError: No module named 'cv2' Use when `import cv2` -> No module named 'cv2' Not for: cv2 imports but crashes on libGL (different error, different fix)"
metadata:
  skill_id: "skl_edWkoudUCSSY-Hh6ZOhFGw"
  title: "ModuleNotFoundError: No module named 'cv2'"
  version: "skv_2AvROklxQSAFWhwYZBwltQ"
  updated: "2026-10-03T04:46:47.110017+00:00"
  canonical_url: "https://vectle.com/skills/skl_edWkoudUCSSY-Hh6ZOhFGw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/madboy2026/vcamera/blob/HEAD/tests/SETUP.md\"]"
---

# How to fix ModuleNotFoundError: No module named 'cv2'

The pip name is `opencv-python`, the import name is `cv2`; install with `python -m pip install opencv-python`. If it is 'already installed', you are in the wrong environment: check that `python` and `pip` point at the same env, or you named a file cv2.py that is shadowing the real one.

## The exact error

```text
ModuleNotFoundError: No module named 'cv2'
```

## Fix it

1. `python -m pip install opencv-python`
   Expected: Successfully installed

2. `python -c "import cv2; print(cv2.__version__)"`
   Expected: prints a version

3. Still failing? `python -m pip show opencv-python` vs `which python`: make pip and python match; rename any cv2.py in your project.
   Expected: consistent env, no shadowing

## When this applies

`import cv2` -> No module named 'cv2'

## When this does NOT apply

cv2 imports but crashes on libGL (different error, different fix)

## Versions

any

## Why it happens

pip name vs import name mismatch, or interpreter/env mismatch.

## Edge cases

Jupyter: restart the kernel after installing; notebook pip can target a different env.


---

Source: [Vectle](https://vectle.com/skills/skl_edWkoudUCSSY-Hh6ZOhFGw). Version: `skv_2AvROklxQSAFWhwYZBwltQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
