---
name: "error-while-loading-shared-libraries-l-a79f34f98ac0108c"
description: "error while loading shared libraries: libcudart.so.13: cannot open shared object file: no such file or directory"
metadata:
  skill_id: "skl_vzEMdwHeWZlYGj6M7M8dfQ"
  title: "error while loading shared libraries: libcudart.so.13: cannot open shared object file: no such file or directory"
  version: "skv_19yBftWfxqfF28D0ZPCLfg"
  updated: "2026-11-13T03:20:10.941132+00:00"
  canonical_url: "https://vectle.com/skills/skl_vzEMdwHeWZlYGj6M7M8dfQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Run ldd on the failing binary and confirm the libcudart line reads not found.

Search the filesystem for an existing libcudart.so.13 under a CUDA install directory.

If none is present, install the CUDA 13 runtime package that matches your distribution, or use a base container image that already carries the CUDA 13 runtime.

Register the library directory with the loader by adding it to the loader configuration and running ldconfig, or set the library path for the service process to include that directory.

Check that you did not resolve to the stub library that ships for linking only. The stub lives in a stubs subdirectory and lets a binary link on a machine without a GPU, but CUDA calls then fail at runtime.

Start the binary again and run a small GPU smoke check.

---

Source: [Vectle](https://vectle.com/skills/skl_vzEMdwHeWZlYGj6M7M8dfQ). Version: `skv_19yBftWfxqfF28D0ZPCLfg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
