---
name: "wire-cloud-run-to-cloud-sql-over-priva-fc6e2f4d6472baa4"
description: "Shows how to fix wire Cloud Run to Cloud SQL over private IP: VPC egress and connectors. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_Y1L5BcmtLwHAGZWUMMsuyA"
  title: "Wire Cloud Run to Cloud SQL over private IP: VPC egress and connectors"
  version: "skv_OmMTMRFP_S2pjsVr-jAQMQ"
  updated: "2026-10-03T14:02:00.389509+00:00"
  canonical_url: "https://vectle.com/skills/skl_Y1L5BcmtLwHAGZWUMMsuyA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/sql/docs/mysql/connect-run\",\"https://cloud.google.com/run/docs/configuring/vpc-direct-vpc\"]"
---

## TL;DR

Check IAM before debugging VPC. - Connection pooling: use the language connectors with pooling; opening a fresh connection per request exhausts the instance. Goal: a Cloud Run service talking to Cloud SQL without exposing the database to the public internet more than necessary.

## When to use

You are seeing this: The --add-cloudsql-instances flag wires the Cloud SQL Auth Proxy sidecar for you. Use this skill when you run into "Wire Cloud Run to Cloud SQL over private IP: VPC egress and connectors".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

Goal: a Cloud Run service talking to Cloud SQL without exposing the database to the public internet more than necessary.

Path A - public IP instance (simplest):

```
gcloud run deploy [SERVICE] --image [IMAGE] --region [REGION]   --add-cloudsql-instances [PROJECT]:[REGION]:[INSTANCE]
```

Your code connects via the Cloud SQL Python/Node connectors or a unix socket at /cloudsql/[CONNECTION-NAME]. The --add-cloudsql-instances flag wires the Cloud SQL Auth Proxy sidecar for you.

Path B - private IP instance (recommended for prod):
- Route egress through Direct VPC egress or a Serverless VPC Access connector, and use the instance's private IP.
- Direct VPC egress is the newer path; the Serverless VPC Access connector is the older one. Compare them in the docs before choosing; both are documented.
- The Cloud Run service account needs cloudsql.client (roles/cloudsql.client) on the instance.

Ordering:
1. Create the Cloud SQL instance first, note the connection name.
2. Create the SA for the service, grant cloudsql.client.
3. Deploy with --add-cloudsql-instances (public) or VPC egress config (private).
4. Test connectivity from the deployed revision, not just locally. Local tests use your credentials; prod uses the SA.

Traps:
- Mixing paths: --add-cloudsql-instances with a private-IP-only instance fails. Match the method to the IP type.
- Forgetting the SA grant gives connection errors that look like network issues. Check IAM before debugging VPC.
- Connection pooling: use the language connectors with pooling; opening a fresh connection per request exhausts the instance.

Verify: hit an endpoint that queries the DB, check query latency in Cloud SQL insights, and confirm no public-IP connections if you intended private-only.


---

Source: [Vectle](https://vectle.com/skills/skl_Y1L5BcmtLwHAGZWUMMsuyA). Version: `skv_OmMTMRFP_S2pjsVr-jAQMQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
