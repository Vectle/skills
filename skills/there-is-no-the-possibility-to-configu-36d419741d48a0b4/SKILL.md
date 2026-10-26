---
name: "there-is-no-the-possibility-to-configu-36d419741d48a0b4"
description: "Qdrant: there is no the possibility to configure the initial cluster topology from the qdrant/config/config.yaml file. The verified fix is Implemented by maintainer timvisee: cluster bootstrap/topology configuration in the config file shipped first in the qdrant/qdrant:dev image and then in stable Qdrant 1.13.3. Use this when you hit the symptoms above in qdrant; not for unrelated qdrant errors or general setup questions."
metadata:
  skill_id: "skl_roktq_5Y8clK-8UiTW82iw"
  title: "There is no the possibility to configure the initial cluster topology from the qdrant/config/config.yaml file"
  version: "skv_RiTnFODc0uQzmD2U8XxRoA"
  updated: "2026-10-03T04:37:25.070579+00:00"
  canonical_url: "https://vectle.com/skills/skl_roktq_5Y8clK-8UiTW82iw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/qdrant/qdrant/issues/5880\"]"
---

## TL;DR

Implemented by maintainer timvisee: cluster bootstrap/topology configuration in the config file shipped first in the qdrant/qdrant:dev image and then in stable Qdrant 1.13.3. Reporter confirmed 'it works like a charm'.

## The error

```text
When deploying a multi-node Qdrant cluster with docker-compose / swarm / kubernetes, the initial cluster topology (bootstrap, peer URIs) could only be passed as CLI flags (--bootstrap, --uri), not configured in config.yaml, making containerized scaling awkward.
```

## Fix

1. Implemented by maintainer timvisee: cluster bootstrap/topology configuration in the config file shipped first in the qdrant/qdrant:dev image and then in stable Qdrant 1.13.3.
2. Reporter confirmed 'it works like a charm'.
3. Closed as completed.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in qdrant.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in qdrant, even a similar-looking one.
- General qdrant setup or credential questions.

## Compatibility

- Qdrant (qdrant/qdrant)

## Variant phrasings

- How to fix "there is no the possibility to configure the initial cluster topology from the qdrant/config/config.yaml file" in qdrant
- qdrant: there is no the possibility to configure the initial cluster topology from the qdrant/config/config.yaml file

## Source

- https://github.com/qdrant/qdrant/issues/5880

---

Source: [Vectle](https://vectle.com/skills/skl_roktq_5Y8clK-8UiTW82iw). Version: `skv_RiTnFODc0uQzmD2U8XxRoA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
