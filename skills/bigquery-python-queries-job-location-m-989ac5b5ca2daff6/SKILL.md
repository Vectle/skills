---
name: "bigquery-python-queries-job-location-m-989ac5b5ca2daff6"
description: "Shows how to fix bigQuery Python queries: job location must match the dataset location. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_HHTK9nZYJkt0Rftia5_mzA"
  title: "BigQuery Python queries: job location must match the dataset location"
  version: "skv_m3jeQhX_V7_3y-BFLR7UVw"
  updated: "2026-10-03T13:46:08.601232+00:00"
  canonical_url: "https://vectle.com/skills/skl_HHTK9nZYJkt0Rftia5_mzA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://cloud.google.com/bigquery/docs/running-queries\",\"https://cloud.google.com/bigquery/docs/error-messages\"]"
---

## TL;DR

Check your installed version's signature. ``python from google.cloud import bigquery client = bigquery.Client(project="[PROJECT-ID]", location="EU") job = client.query("SELECT 1") for row in job.result(): print(row) ` The location trap: BigQuery datasets live in a location (US, EU, or a region).

## Steps

1. ```python
from google.cloud import bigquery
client = bigquery.Client(project="[PROJECT-ID]", location="EU")
job = client.query("SELECT 1")
for row in job.result():
 print(row)
```

2. The location trap: BigQuery datasets live in a location (US, EU, or a region). The query JOB also has a location, and it must match the dataset location. If they differ you get `Not found: Dataset [PROJECT]:[DATASET]` even though the dataset obviously exists. Agents misread this as a permissions error every time.

3. Fixes:
- Construct the client with location set, as above.
- Or pass job_config: `bigquery.QueryJobConfig()` does not take location; set it on the client or via `client.query(sql, location="EU")` in newer versions. Check your installed version's signature.

4. Other things that bite:
- `job.result()` blocks until done. For long queries use a timeout and poll, or the query can hang your script.
- Dry run first for cost control: `job_config = bigquery.QueryJobConfig(dry_run=True)` then check `job.total_bytes_processed` before running for real.
- Default project vs query project: the client project is billed for the query (needs bigquery.jobs.create there); the SQL can reference datasets in other projects you can read. Do not confuse "project that pays" with "project that holds data".
- Use parameterized queries (`query_params`) instead of f-string interpolation. SQL injection is not just a web problem.

5. Verify: run a trivial `SELECT 1` in the right location, then your real query as a dry run to see bytes processed.

## When to use

You are seeing this: Agents misread this as a permissions error every time. Use this skill when you run into "BigQuery Python queries: job location must match the dataset location".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_HHTK9nZYJkt0Rftia5_mzA). Version: `skv_m3jeQhX_V7_3y-BFLR7UVw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
