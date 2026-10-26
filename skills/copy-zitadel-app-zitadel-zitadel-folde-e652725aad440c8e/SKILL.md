---
name: "copy-zitadel-app-zitadel-zitadel-folde-e652725aad440c8e"
description: "Fixes 'Zitadel folder not available' when building Zitadel through build/dockerfile by building via make docker_image instead, which compiles the binary first. Use when the COPY zitadel step cant find the binary. Not for other Docker build failures."
metadata:
  skill_id: "skl_Dxr_ZxLVVuVtq8G_2JWUYw"
  title: "COPY zitadel /app/zitadel  Zitadel folder not available while building through build/dockerfile"
  version: "skv_IHyl_RzpEFD7bOmF8TYHrQ"
  updated: "2026-10-03T04:43:57.6078+00:00"
  canonical_url: "https://vectle.com/skills/skl_Dxr_ZxLVVuVtq8G_2JWUYw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/zitadel/zitadel/issues/6277\"]"
---

Fix first: dont build the Dockerfile directly. Run `make docker_image` from the repo root; it compiles the binary first as part of the flow. Maintainer-confirmed.

```text
COPY zitadel /app/zitadel -> Zitadel folder not available
```

1. From the repo root, run `make docker_image`.
2. Expected: the binary is compiled, the COPY step finds it, and the image builds.

When to use: building Zitadel through build/dockerfile fails because the COPY zitadel step cannot find the binary.

When not to use: other Docker build failures (missing base images, network issues); those are different problems.

Compatibility: zitadel repo, build/dockerfile. Reported in zitadel/zitadel#6277.

Variants:
- "zitadel folder not available docker build"
- "COPY zitadel /app/zitadel fails"
- "zitadel make docker_image"

Root cause: the Dockerfile expects a prebuilt zitadel binary in the build context. Building the Dockerfile directly skips the compile step, so there is nothing to copy.

Edge cases: if make docker_image itself fails, fix the compile error first. The Dockerfile was never meant to be built standalone.

---

Source: [Vectle](https://vectle.com/skills/skl_Dxr_ZxLVVuVtq8G_2JWUYw). Version: `skv_IHyl_RzpEFD7bOmF8TYHrQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
