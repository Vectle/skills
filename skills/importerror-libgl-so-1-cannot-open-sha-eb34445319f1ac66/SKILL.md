---
name: "importerror-libgl-so-1-cannot-open-sha-eb34445319f1ac66"
description: "Fixes ImportError: libGL.so.1: cannot open shared object file: No such file or directory Use when `import cv2` fails on libGL.so.1 (or libgthread) in Docker/CI/headless Linux Not for: you actually need cv2.imshow (then install the libs, do not go headless)"
metadata:
  skill_id: "skl_QNbndoq6D_ru5_WAdxnRkQ"
  title: "ImportError: libGL.so.1: cannot open shared object file: No such file or directory"
  version: "skv_8tFQ2PC_psaFlJ6pXPv0_A"
  updated: "2026-10-03T04:45:59.792955+00:00"
  canonical_url: "https://vectle.com/skills/skl_QNbndoq6D_ru5_WAdxnRkQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: libGL.so.1: cannot open shared object file: No such file or directory

You are on a headless box and opencv-python wants GUI system libs. Two fixes: install the lib (`sudo apt-get install libgl1`, often plus `libglib2.0-0`), or switch to the headless wheel: `pip install opencv-python-headless`. The headless wheel is the right call for servers and Docker; it has no GUI deps at all.

## The exact error

```text
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

## Fix it

1. Headless route (recommended): `pip uninstall -y opencv-python && pip install opencv-python-headless`.
   Expected: `import cv2` works

2. Or install system libs: `sudo apt-get install -y libgl1 libglib2.0-0`.
   Expected: `import cv2` works with the GUI wheel

3. Docker: add the apt line to your Dockerfile before pip install.
   Expected: container imports cv2 cleanly

## When this applies

`import cv2` fails on libGL.so.1 (or libgthread) in Docker/CI/headless Linux

## When this does NOT apply

you actually need cv2.imshow (then install the libs, do not go headless)

## Versions

Linux Docker / headless servers, opencv-python

## Why it happens

opencv-python links Qt/OpenGL system libraries that slim images do not ship.

## Edge cases

Never install both opencv-python and opencv-python-headless; they conflict.


---

Source: [Vectle](https://vectle.com/skills/skl_QNbndoq6D_ru5_WAdxnRkQ). Version: `skv_8tFQ2PC_psaFlJ6pXPv0_A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
