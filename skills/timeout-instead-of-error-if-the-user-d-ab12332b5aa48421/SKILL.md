---
name: "timeout-instead-of-error-if-the-user-d-ab12332b5aa48421"
description: "Serverless: timeout instead of error if the user did not configure the database URL. The verified fix is Fix: Anyone who genuinely wants the defaults can explicitly set `host`, `connectionString`, or `PGHOST`. Use this when you hit the symptoms above in serverless; not for unrelated serverless errors or general setup questions."
metadata:
  skill_id: "skl_D7dy9KArDaWdu6ZgNNKvmA"
  title: "Timeout instead of error if the user did not configure the database URL"
  version: "skv_LFZsTiuG8-6lxftctU7NHA"
  updated: "2026-10-03T05:07:21.639571+00:00"
  canonical_url: "https://vectle.com/skills/skl_D7dy9KArDaWdu6ZgNNKvmA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/neondatabase/serverless/issues/30\"]"
---

## TL;DR

Fix: Anyone who genuinely wants the defaults can explicitly set `host`, `connectionString`, or `PGHOST`.

## The error

```text
Issue neondatabase/serverless#30 (closed, 10 comments): @skyzh's report:
The serverless driver will timeout instead of reporting any error if the user did not configure the database URL. It seems that the driver will try connecting to YOUR_HOST:5432 if the database URL is not configured, and it will timeout. This looks like the default behavior for pg library but I don’t think it makes sense if people are using the serverless driver as they are always connecting to an external provider? I feel it would be better to give a warning / throw an error in the serverless driver in case that the database endpoint is not configured?
```

## Fix

1. Anyone who genuinely wants the defaults can explicitly set `host`, `connectionString`, or `PGHOST`.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in serverless.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in serverless, even a similar-looking one.
- General serverless setup or credential questions.

## Compatibility

- Serverless (neondatabase/serverless)

## Variant phrasings

- How to fix "timeout instead of error if the user did not configure the database URL" in serverless
- serverless: timeout instead of error if the user did not configure the database URL
- timeout instead of problem if the user did not configure the database URL

## Edge cases

- [jawj (maintainer)]: As of driver 0.5.2, the driver throws an error when it detects default connection parameters (missing DATABASE_URL / host), instead of hanging until the edge function times out (EDGE_FUNCTION_INVOCATION_TIMEOUT with no useful logs).

## Source

- https://github.com/neondatabase/serverless/issues/30

---

Source: [Vectle](https://vectle.com/skills/skl_D7dy9KArDaWdu6ZgNNKvmA). Version: `skv_LFZsTiuG8-6lxftctU7NHA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
