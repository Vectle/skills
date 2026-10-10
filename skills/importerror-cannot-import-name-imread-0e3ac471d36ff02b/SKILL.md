---
name: "importerror-cannot-import-name-imread-0e3ac471d36ff02b"
description: "Fixes ImportError: cannot import name 'imread' from 'scipy.misc' Use when old code/tutorials doing `from scipy.misc import imread` on scipy>=1.3 Not for: you just need any image reader (use imageio or PIL directly)"
metadata:
  skill_id: "skl_ZdtyBQgPnCuHQQUtH5KR2w"
  title: "ImportError: cannot import name 'imread' from 'scipy.misc'"
  version: "skv_EhT92k3j2_9YeR6YLUARBg"
  updated: "2026-10-03T04:48:34.793228+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZdtyBQgPnCuHQQUtH5KR2w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: cannot import name 'imread' from 'scipy.misc'

scipy removed imread/imresize/imsave in 1.3. Replace `from scipy.misc import imread` with imageio (`from imageio import imread`) or PIL (`Image.open(path)`). imageio is scipy's own recommended replacement and returns the same numpy array.

## The exact error

```text
ImportError: cannot import name 'imread' from 'scipy.misc'
```

## Fix it

1. `python -m pip install imageio`
   Expected: installed

2. Replace `from scipy.misc import imread` with `from imageio import imread`.
   Expected: same numpy array back

3. For imresize: use `Image.fromarray(arr).resize((w, h))` from PIL.
   Expected: equivalent resize

## When this applies

old code/tutorials doing `from scipy.misc import imread` on scipy>=1.3

## When this does NOT apply

you just need any image reader (use imageio or PIL directly)

## Versions

scipy >= 1.3

## Why it happens

scipy dropped its PIL wrappers; imageio became the blessed replacement.

## Edge cases

imageio v3 changed the API slightly; `imageio.v2.imread` keeps the old behavior.


---

Source: [Vectle](https://vectle.com/skills/skl_ZdtyBQgPnCuHQQUtH5KR2w). Version: `skv_EhT92k3j2_9YeR6YLUARBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
