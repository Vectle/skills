---
name: "bigquery-table-must-be-qualified-with-8961bf473a0a9896"
description: "bigquery table must be qualified with a dataset"
metadata:
  skill_id: "skl_VLBOoN45a9I8sg2BsXqKcQ"
  title: "bigquery table must be qualified with a dataset"
  version: "skv_DxbFXckDdWHxRylpC0EJPQ"
  updated: "2026-11-02T16:09:38.20992+00:00"
  canonical_url: "https://vectle.com/skills/skl_VLBOoN45a9I8sg2BsXqKcQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Qualify the reference in the query itself: write the table as dataset_name.table_name, and for another project as `project_id.dataset_name.table_name` in backticks. Expected: the error disappears and the query validates.

Or set a default dataset for the run: with bq, pass the dataset on the query command (the --dataset_id flag on bq mk is for creating; for queries use the project and dataset defaults in your client config or job config defaultDataset). In the Python client, set the default dataset on the QueryJobConfig. Expected: unqualified names resolve against that dataset.

Inside EXECUTE IMMEDIATE, qualify anyway or set the session variable first: run SET @@dataset_id to your dataset before the dynamic statement. A configured default schema or default dataset does not carry into the separate execution context of EXECUTE IMMEDIATE, which is the most common way this error surprises people in scripting and in Dataform. Expected: the dynamic statement resolves the table.

In BI and connector tools (Looker Studio, Oracle Analytics, JDBC or ODBC drivers), turn on the fully qualified names option or set the default dataset in the connection, because generated SQL often emits bare table names. Expected: the generated SQL shows dataset.table in the query log.

---

Source: [Vectle](https://vectle.com/skills/skl_VLBOoN45a9I8sg2BsXqKcQ). Version: `skv_DxbFXckDdWHxRylpC0EJPQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
