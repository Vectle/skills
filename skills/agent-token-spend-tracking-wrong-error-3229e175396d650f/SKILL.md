---
name: "agent-token-spend-tracking-wrong-error-3229e175396d650f"
description: "agent token spend tracking wrong error costs double counted bug"
metadata:
  skill_id: "skl_OdWhFnqa0ecujojAdBOgXQ"
  title: "agent token spend tracking wrong error costs double counted bug"
  version: "skv_um3Bqz3wweMJ2ojai9YuSA"
  updated: "2026-11-17T01:56:16.375044+00:00"
  canonical_url: "https://vectle.com/skills/skl_OdWhFnqa0ecujojAdBOgXQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Pick one finished run and list every cost record your tracker holds for it.

Compare the request identifier, model, and token counts on each record for that run.

Decide which writer is the source of truth for a run, the live call logger or the later usage sync, and stop the other one from creating a second record for the same run.

Add or enforce a uniqueness check on the provider request identifier in the cost store.

Recount spend for a short period, such as one hour, from the deduped records and compare it with the provider usage report for the same hour.

Backfill the correction by removing duplicate records only where the request identifier matches exactly.

---

Source: [Vectle](https://vectle.com/skills/skl_OdWhFnqa0ecujojAdBOgXQ). Version: `skv_um3Bqz3wweMJ2ojai9YuSA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
