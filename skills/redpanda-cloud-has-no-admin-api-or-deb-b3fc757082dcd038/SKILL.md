---
name: "redpanda-cloud-has-no-admin-api-or-deb-b3fc757082dcd038"
description: "On a Cloud cluster, never reach for rpk debug bundle or the Admin API; they are unsupported."
metadata:
  skill_id: "skl_R5kO61l5TWQjdnvLvopiBw"
  title: "Redpanda Cloud has no Admin API or debug bundles; use support tickets plus Kafka-API triage"
  version: "skv_2RX0ntR1VE6PJ_NZJDyetw"
  updated: "2026-10-03T05:32:57.909301+00:00"
  canonical_url: "https://vectle.com/skills/skl_R5kO61l5TWQjdnvLvopiBw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Redpanda Cloud has no Admin API or debug bundles; use support tickets plus Kafka-API triage

## TL;DR

On a Cloud cluster, never reach for rpk debug bundle or the Admin API; they are unsupported. Keep the two playbooks separate so your agent does not waste turns on commands that cannot work. Context: Official docs (redpanda-data/skills, rpk-debug skill): documents the Cloud-vs-self-managed gotcha that trips agents used to on-prem Redpanda.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: Redpanda. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Keep the two playbooks separate so your agent does not waste turns on commands that cannot work.

Context: Official docs (redpanda-data/skills, rpk-debug skill): documents the Cloud-vs-self-managed gotcha that trips agents used to on-prem Redpanda. Redpanda Cloud clusters (Serverless, BYOC, Dedicated) do not support debug bundles, do not expose the Admin API, and do not expose broker hosts. The usual live-triage commands (rpk cluster health, rpk cluster license, rpk cluster maintenance, rpk cluster partitions, rpk cluster self-test) do not work against Cloud clusters.


---

Source: [Vectle](https://vectle.com/skills/skl_R5kO61l5TWQjdnvLvopiBw). Version: `skv_2RX0ntR1VE6PJ_NZJDyetw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
