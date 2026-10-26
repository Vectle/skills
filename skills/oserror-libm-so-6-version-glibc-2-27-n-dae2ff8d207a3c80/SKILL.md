---
name: "oserror-libm-so-6-version-glibc-2-27-n-dae2ff8d207a3c80"
description: "Resolves torch GLIBC version failures via OS/container/pin options. Use when the error names GLIBC_X.XX not found under torch libs. Not for a missing torch install."
metadata:
  skill_id: "skl_q_2IRnST4PWEfhU1K3FTKg"
  title: "OSError: libm.so.6: version `GLIBC_2.27' not found"
  version: "skv_a9NtFR33NJa6RID7eJWdPA"
  updated: "2026-10-03T06:05:42.076576+00:00"
  canonical_url: "https://vectle.com/skills/skl_q_2IRnST4PWEfhU1K3FTKg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/dmlc/dgl/issues/7046\"]"
---

TL;DR: Upgrade your OS/glibc or use an older torch. New torch wheels need a newer glibc than old distros (CentOS 7, Ubuntu 18.04) ship. Your options: upgrade the OS, use a container with a newer base image, or pin torch to a version built for your glibc (torch 1.13 works on manylinux2014-era systems).

The error:
```text
OSError: /lib64/libm.so.6: version `GLIBC_2.27' not found (required by /.../torch/lib/libtorch_cpu.so)
```

## Fix
1. Check: `ldd --version`
   Expected: shows your glibc; 2.27+ needed for current torch
2. Easiest: run in a container, e.g. `docker run --gpus all -it pytorch/pytorch:2.5.1-cuda12.4-cudnn9-runtime`
   Expected: import torch works inside
3. Or pin older torch: `python -m pip install 'torch==1.13.1' --index-url https://download.pytorch.org/whl/cpu`
   Expected: imports on old glibc

## When this applies
- GLIBC_X.XX not found required by torch libs
- import torch failing on old Linux distros

## When this does not apply
- No module named 'torch' (not installed)
- other missing .so errors (different libs)

## Version compatibility
torch 2.x needs glibc >= 2.28 or so (manylinux_2_28 wheels); torch 1.13 targets manylinux2014.

## Why it happens
PyTorch's wheels are built against recent manylinux standards. Old distros ship older glibc, and the dynamic loader refuses to load libtorch when the required symbol versions are absent.

## Edge cases
- Upgrading the OS is the durable fix; pinning old torch accrues tech debt.
- Conda's torch sometimes bundles more compat; worth a try before downgrading.
- Do not replace system libm; you will break the OS.

---

Source: [Vectle](https://vectle.com/skills/skl_q_2IRnST4PWEfhU1K3FTKg). Version: `skv_a9NtFR33NJa6RID7eJWdPA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
