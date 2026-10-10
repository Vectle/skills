---
name: "api-not-enabled-error-the-exact-gcloud-201745f94e16b1fd"
description: "Google Cloud APIs fail with the API-has-not-been-used-in-this-project error. Covers the exact enable command, common API names, propagation wait, and the IAM permission the enable call needs. Not for quota, billing, or permission errors on the API call itself."
metadata:
  skill_id: "skl_GModwW7BE0xJv4OL0JnvYg"
  title: "API not enabled error: the exact gcloud services enable fix"
  version: "skv_Up3zIinc9Cg4UCUg8K2P0A"
  updated: "2026-10-03T04:34:08.487168+00:00"
  canonical_url: "https://vectle.com/skills/skl_GModwW7BE0xJv4OL0JnvYg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: The API is not enabled on that project. Copy the API name exactly from the error, run `gcloud services enable [API] --project [PROJECT]`, wait a minute or two for propagation, and retry. If the enable call 403s, your identity lacks serviceusage.services.use. Thats an IAM grant, not a wrong API name.

The error, verbatim:

```text
[API] has not been used in project [P] before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/[API]/overview?project=[P] then retry.
```

Steps:

1. Copy the API name from the error exactly. Success: you have the dotted name, and you did not substitute a lookalike (storage-component.googleapis.com is not storage.googleapis.com).
2. Run `gcloud services enable [API] --project [PROJECT]`. Success: no 403.
3. Wait 1-2 minutes, then rerun the original call. Success: it works.

Common API names: storage.googleapis.com, bigquery.googleapis.com, run.googleapis.com, pubsub.googleapis.com, secretmanager.googleapis.com, sqladmin.googleapis.com, cloudfunctions.googleapis.com.

When to use: any Google Cloud API call fails with the not-been-used/disabled error.

When not to use: quota exceeded, billing not enabled, or permission denied on the API call itself (different errors, different fixes).

Compatibility: gcloud CLI, every Google Cloud API, Terraform google_project_service.

Variants:
- gcloud api not enabled before use
- enable google cloud api
- API has not been used in project before

Root cause: every Google Cloud API must be enabled per project before use, and new projects have almost nothing enabled. Agents often enable the API on the wrong project, so the error persists and looks like a deeper problem.

Edge cases:
- Enabling can take a minute or two to propagate. If the next call still fails, wait and retry rather than enabling twice.
- You need serviceusage.services.use permission on the project to enable APIs. A 403 on the enable call means your identity lacks that, not that the API name is wrong.
- Terraform: use google_project_service resources so enablement is in state. The provider fails the same way if the API is off.

---

Source: [Vectle](https://vectle.com/skills/skl_GModwW7BE0xJv4OL0JnvYg). Version: `skv_Up3zIinc9Cg4UCUg8K2P0A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
