---
name: "importerror-dll-load-failed-while-impo-07eb3fc793edeaca"
description: "Fixes ImportError: DLL load failed while importing torch: The specified module could not be found. Use when Windows `import torch` raises 'DLL load failed' with 'The specified module could not be found' Not for: `No module named 'torch'` (torch is not installed) or Linux/macOS .so errors"
metadata:
  skill_id: "skl_FAucZzcadWDYZu4N6f5DLA"
  title: "ImportError: DLL load failed while importing torch: The specified module could not be found."
  version: "skv_U-CnjmDeKfwqK5Kmq5zQgw"
  updated: "2026-10-03T04:33:33.867613+00:00"
  canonical_url: "https://vectle.com/skills/skl_FAucZzcadWDYZu4N6f5DLA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# How to fix ImportError: DLL load failed while importing torch: The specified module could not be found.

On Windows this almost always means the CUDA DLLs or the MSVC runtime are not visible to Python 3.8+, which no longer searches PATH for extension DLLs. Easiest fix: install the CPU-only torch build, or register the torch/lib directory with os.add_dll_directory before importing. Also make sure the Visual C++ redistributable matching your torch build is installed.

## The exact error

```text
ImportError: DLL load failed while importing torch: The specified module could not be found.
```

## Fix it

1. Confirm it is a DLL-visibility issue, not a missing torch: `python -m pip show torch` should list torch.
   Expected: torch is installed; only the import fails

2. For plain `import torch` failures, reinstall the CPU wheel: `pip install torch --index-url https://download.pytorch.org/whl/cpu`.
   Expected: `import torch` succeeds

3. For CUDA builds: install the matching CUDA toolkit + cuDNN and the MSVC redistributable, with their bin dirs on PATH.
   Expected: `torch.cuda.is_available()` reflects your GPU

## When this applies

Windows `import torch` raises 'DLL load failed' with 'The specified module could not be found'

## When this does NOT apply

`No module named 'torch'` (torch is not installed) or Linux/macOS .so errors

## Versions

Windows, torch with CUDA builds, Python 3.8+

## Why it happens

Python 3.8+ on Windows stopped loading extension DLLs from PATH; torch's native libs need their directory registered.

## Edge cases

Mixing pip torch with conda cudatoolkit is the most common trigger; use one channel for GPU builds, not both.


---

Source: [Vectle](https://vectle.com/skills/skl_FAucZzcadWDYZu4N6f5DLA). Version: `skv_U-CnjmDeKfwqK5Kmq5zQgw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
