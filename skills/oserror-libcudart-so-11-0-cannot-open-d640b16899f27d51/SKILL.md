---
name: "oserror-libcudart-so-11-0-cannot-open-d640b16899f27d51"
description: "Fixes OSError: libcudart.so.11.0: cannot open shared object file: No such file or directory Use when `import torch` (or torchvision/torch_geometric) fails with `libcudart.so.X` / `libcudnn` / `libtorch_cuda` not found on Linux Not for: Windows DLL errors or `No module named 'torch'`"
metadata:
  skill_id: "skl_prg4VnnSQkpfpWoEOGRo9A"
  title: "OSError: libcudart.so.11.0: cannot open shared object file: No such file or directory"
  version: "skv_X0s9Y9PMlIkVkANDtMx_cg"
  updated: "2026-10-03T04:34:45.725862+00:00"
  canonical_url: "https://vectle.com/skills/skl_prg4VnnSQkpfpWoEOGRo9A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://www.iopenv.com/36E4IQF8I/Program-Error-Torch-Torch-Geometric-Torch-Dependency-issues-with-versions-such-as-sparse\"]"
---

# How to fix OSError: libcudart.so.11.0: cannot open shared object file: No such file or directory

Your torch build wants CUDA 11.0 but the loader cannot find its libraries. Either install the matching CUDA toolkit (or set LD_LIBRARY_PATH to its lib64 dir), or switch to the CPU-only torch wheel if you do not need the GPU. The version in the filename must match the CUDA your torch was built against.

## The exact error

```text
OSError: libcudart.so.11.0: cannot open shared object file: No such file or directory
```

## Fix it

1. Check what CUDA your torch expects: look at the +cuXX tag in `python -m pip show torch`.
   Expected: e.g. cu110, cu118, cu121

2. Option A (keep GPU): install that CUDA toolkit, or point the loader at it: `export LD_LIBRARY_PATH=/usr/local/cuda-11.0/lib64:$LD_LIBRARY_PATH`.
   Expected: `import torch` no longer raises the OSError

3. Option B (no GPU needed): `pip install torch --index-url https://download.pytorch.org/whl/cpu`.
   Expected: torch imports and runs on CPU

## When this applies

`import torch` (or torchvision/torch_geometric) fails with `libcudart.so.X` / `libcudnn` / `libtorch_cuda` not found on Linux

## When this does NOT apply

Windows DLL errors or `No module named 'torch'`

## Versions

Linux, CUDA builds of torch

## Why it happens

CUDA torch wheels still resolve some CUDA libs from the system; a version mismatch or missing toolkit breaks the load.

## Edge cases

nvidia-smi showing CUDA 12.x does not mean the toolkit is installed; the driver version and toolkit version are different things.


---

Source: [Vectle](https://vectle.com/skills/skl_prg4VnnSQkpfpWoEOGRo9A). Version: `skv_X0s9Y9PMlIkVkANDtMx_cg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
