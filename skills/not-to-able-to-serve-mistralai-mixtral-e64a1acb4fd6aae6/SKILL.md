---
name: "not-to-able-to-serve-mistralai-mixtral-e64a1acb4fd6aae6"
description: "Fixes multi-GPU serving of mistralai/Mixtral-8x7B-Instruct-v0.1 on LoRAX by pulling the latest image (a stale image was the cause) and setting NCCL_P2P_LEVEL=NVL on NVLink boxes. Use when LoRAX wont serve across multiple GPUs. Not for single-GPU problems or non-NVIDIA hardware."
metadata:
  skill_id: "skl_snTpGO07Le1I2LqG-zEg_Q"
  title: "Not to able to serve mistralai/Mixtral-8x7B-Instruct-v0.1 on loraX with multiple GPU's"
  version: "skv_gVf8qlDatUEN3ALDfk0_EA"
  updated: "2026-10-03T04:37:21.783092+00:00"
  canonical_url: "https://vectle.com/skills/skl_snTpGO07Le1I2LqG-zEg_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/predibase/lorax/issues/191\"]"
---

Fix first: pull the latest LoRAX image and redeploy. The maintainer suspected a stale image, and the reporter confirmed multi-GPU serving worked after updating.

```text
docker pull ghcr.io/predibase/lorax:latest
```

1. Pull the latest image with `docker pull ghcr.io/predibase/lorax:latest` and redeploy. Expected: LoRAX starts and serves the model across your GPUs.
2. On NVLink setups, also set `NCCL_P2P_LEVEL=NVL`. The reporter confirmed that combination worked too. Expected: no NCCL or P2P errors in the logs.

When to use: LoRAX refuses to serve a model when you give it multiple GPUs.

When not to use: single-GPU serving issues, or hardware that isnt NVIDIA.

Compatibility: LoRAX (Predibase), mistralai/Mixtral-8x7B-Instruct-v0.1, NVIDIA GPUs (the env var applies to NVLink setups). Reported in predibase/lorax#191.

Variants:
- "lorax multi gpu not working"
- "serve mixtral 8x7b lorax multiple gpus"
- "NCCL_P2P_LEVEL NVL lorax"

Root cause: a stale LoRAX image; the multi-GPU path was fixed in a newer build.

Edge cases: the env var was only confirmed on NVLink boxes. If you are not on NVLink, try the image update on its own first.

---

Source: [Vectle](https://vectle.com/skills/skl_snTpGO07Le1I2LqG-zEg_Q). Version: `skv_gVf8qlDatUEN3ALDfk0_EA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
