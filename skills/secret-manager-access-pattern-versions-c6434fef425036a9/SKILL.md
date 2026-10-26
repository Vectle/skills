---
name: "secret-manager-access-pattern-versions-c6434fef425036a9"
description: "Shows how to fix secret Manager access pattern: versions/latest and the secretAccessor role. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_t7ZNHViQSxJ93GtDTiNH5Q"
  title: "Secret Manager access pattern: versions/latest and the secretAccessor role"
  version: "skv_ohf4jSs9MuHgADSoyPaAeA"
  updated: "2026-10-03T13:56:52.355315+00:00"
  canonical_url: "https://vectle.com/skills/skl_t7ZNHViQSxJ93GtDTiNH5Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/secret-manager/docs/access-secret\",\"https://cloud.google.com/secret-manager/docs/iam\"]"
---

## TL;DR

Grant it on the specific secret, not the project, when you can: ` gcloud secrets add-iam-policy-binding [SECRET-ID] --member serviceAccount:[SA-EMAIL] --role roles/secretmanager.secretAccessor ` latest vs pinned: - latest` always resolves to the newest enabled version.

## Steps

1. ```python
from google.cloud import secretmanager
client = secretmanager.SecretManagerServiceClient()
name = "projects/[PROJECT]/secrets/[SECRET-ID]/versions/latest"
payload = client.access_secret_version(request={"name": name}).payload.data.decode("utf-8")
```

2. The resource name format is strict: projects/[PROJECT]/secrets/[SECRET-ID]/versions/[VERSION]. VERSION can be a number or `latest`. Get any segment wrong and you get NotFound, not a helpful hint.

3. IAM: the caller needs the secretmanager.versions.access permission, which roles/secretmanager.secretAccessor grants. Grant it on the specific secret, not the project, when you can:

```
gcloud secrets add-iam-policy-binding [SECRET-ID] --member serviceAccount:[SA-EMAIL] --role roles/secretmanager.secretAccessor
```

4. latest vs pinned:
- `latest` always resolves to the newest enabled version. Convenient, dangerous with rotation: a rotation can change the value under a running process.
- Production services should pin a version number and bump it deliberately, or handle rotation explicitly.
- Disabled and destroyed versions error on access. Destroyed is permanent; there is no undelete.

5. Do not:
- Log secret values. Not even at debug. The access call returns bytes; decode and use, never print.
- Store the secret in an env var baked into a container image. Mount it at runtime (Cloud Run --set-secrets) or fetch at startup.
- Grant secretmanager.admin to workloads. Accessor is enough.

6. Verify: access from the workload identity (not your user) and confirm the value shape without printing it, e.g. check length or a known prefix.

## When to use

You are seeing this: ``python from google.cloud import secretmanager client = secretmanager.SecretManagerServiceClient() name = "projects/[PROJECT]/secrets/[SECRET-ID]/versions/latest" payload = client.access\_secret\_version(request={"name":... Use this skill when you run into "Secret Manager access pattern: versions/latest and the secretAccessor role".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_t7ZNHViQSxJ93GtDTiNH5Q). Version: `skv_ohf4jSs9MuHgADSoyPaAeA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
