---
name: "modulenotfounderror-no-module-named-to-3fed6d034c386880"
description: "Resolves ModuleNotFoundError for torch by identifying the wrong-environment install and installing the right wheel. Use when `import torch` fails with No module named 'torch'. Not for DLL load failures, CUDA availability problems, or version conflicts between torch and torchvision."
metadata:
  skill_id: "skl_krFmo_t1Hh0CvznCEQtdIA"
  title: "ModuleNotFoundError: No module named 'torch'"
  version: "skv_eOQDVC_-j-CFVPghM4uVfQ"
  updated: "2026-10-03T06:07:53.36914+00:00"
  canonical_url: "https://vectle.com/skills/skl_krFmo_t1Hh0CvznCEQtdIA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/zju3dv/GVHMR/issues/49\"]"
---

TL;DR: Install PyTorch for your platform with pip. The most common cause is running the script in a different Python environment than the one torch was installed into, so first check which python you are using. If torch is already installed, you are almost certainly in the wrong venv or conda env.

The error:
```text
ModuleNotFoundError: No module named 'torch'
```

## Fix
1. Run `python -c "import sys; print(sys.executable)"` and `pip show torch`
   Expected: pip show torch reports a location; if it says not installed, torch is missing from this interpreter
2. Install the CPU build with `pip install torch --index-url https://download.pytorch.org/whl/cpu`
   Expected: pip reports Successfully installed torch
3. Re-run `python -c "import torch; print(torch.__version__)"`
   Expected: prints a version like 2.5.1 with no error

## When this applies
- you see No module named 'torch' on `import torch`
- pip list does not show torch in the active environment

## When this does not apply
- you get a DLL/shared-library error on import (different problem)
- torch imports but torch.cuda.is_available() is False (different problem)

## Version compatibility
Any PyTorch 2.x. Use the CUDA index URL instead of the cpu one if you need GPU builds: https://download.pytorch.org/whl/cu124 (match your CUDA).

## Why it happens
pip installed torch into one Python and you are running another. Conda envs, system python vs python3, and IDE interpreters are the usual mix-ups.

## Edge cases
- `pip` and `python` can point at different environments; prefer `python -m pip install`.
- On Apple Silicon, install the regular wheel, there is no separate MPS wheel.
- If you installed torch inside a notebook kernel, restart the kernel after install.

---

Source: [Vectle](https://vectle.com/skills/skl_krFmo_t1Hh0CvznCEQtdIA). Version: `skv_eOQDVC_-j-CFVPghM4uVfQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
