---
name: "modulenotfounderror-no-module-named-te-1ca75d286195f076"
description: "Resolves ModuleNotFoundError for tensorflow via interpreter-matched install. Use when `import tensorflow` fails with No module named 'tensorflow'. Not for DLL/.so load failures or CUDA setup problems."
metadata:
  skill_id: "skl_b9rbjNu_ywwP65h4t1G8VQ"
  title: "ModuleNotFoundError: No module named 'tensorflow'"
  version: "skv_kna7d7-RLdSO98m8Q8hWUQ"
  updated: "2026-10-03T06:11:07.255133+00:00"
  canonical_url: "https://vectle.com/skills/skl_b9rbjNu_ywwP65h4t1G8VQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/qurator-spk/eynollah/issues/191\"]"
---

TL;DR: Install tensorflow in the Python you are actually running: `pip install tensorflow`. If pip says it is already installed, you have an interpreter mismatch, check `python -c "import sys; print(sys.executable)"` against where pip installed it. On Apple Silicon use `tensorflow-macos`, not `tensorflow`.

The error:
```text
ModuleNotFoundError: No module named 'tensorflow'
```

## Fix
1. Run `python -c "import sys; print(sys.executable)"` then `python -m pip show tensorflow`
   Expected: either shows tensorflow info or confirms it is missing from this interpreter
2. Install: `python -m pip install tensorflow` (or `tensorflow-macos` on Apple Silicon)
   Expected: Successfully installed tensorflow
3. Verify: `python -c "import tensorflow as tf; print(tf.__version__)"`
   Expected: prints the version, no error

## When this applies
- No module named 'tensorflow' on import
- pip list shows tensorflow but the script still fails (interpreter mismatch)

## When this does not apply
- import fails with a DLL or .so error (installed but broken)
- you need GPU support, that is a separate install decision

## Version compatibility
tensorflow 2.x CPU. For GPU on Linux use the CUDA-enabled build per the TF install docs; Apple Silicon uses tensorflow-macos + tensorflow-metal.

## Why it happens
TensorFlow is a large package that people often install with one pip/python and run with another (system python, venv, conda, notebook kernel). The module simply is not on sys.path of the running interpreter.

## Edge cases
- Always use `python -m pip` so the installer targets the interpreter you run.
- In notebooks, restart the kernel after installing.
- tensorflow does not publish an official Windows GPU wheel for 2.11+; CPU wheel or WSL2 instead.

---

Source: [Vectle](https://vectle.com/skills/skl_b9rbjNu_ywwP65h4t1G8VQ). Version: `skv_kna7d7-RLdSO98m8Q8hWUQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
