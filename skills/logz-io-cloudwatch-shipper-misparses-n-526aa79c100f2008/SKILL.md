---
name: "logz-io-cloudwatch-shipper-misparses-n-526aa79c100f2008"
description: "Fixes the Logz.io CloudWatch logs shipper misparsing NodeJS Lambda log lines and failing to ignore START/END/REPORT lines. Use this when NodeJS function logs arrive mangled in Logz.io while Python functions are fine. Not for delivery failures or for non-Lambda log sources."
metadata:
  skill_id: "skl_-7qctqzI2e2B1ZIfMFAKxQ"
  title: "Logz.io CloudWatch shipper misparses NodeJS Lambda logs (no log level)"
  version: "skv_KFdUPpBuIquPOuY51RVlFg"
  updated: "2026-10-03T04:32:29.715799+00:00"
  canonical_url: "https://vectle.com/skills/skl_-7qctqzI2e2B1ZIfMFAKxQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://vectle.com/threads/thr_vL6FFCjhneY7dnAWek_6Ug\",\"https://github.com/logzio/logzio_aws_serverless/issues/40\"]"
---

TL;DR: if the Logz.io CloudWatch shipper mangles NodeJS Lambda logs, the parser assumed the 3-part Python format (timestamp, requestID, message) but NodeJS lines have 4 parts including the log level. Upgrade the shipper to a version containing the PR #42 fix; the maintainer confirmed AWS Lambda log formats differ per runtime.

## Steps

1. Upgrade the Logz.io CloudWatch logs shipper past PR #42.

   Expected: the parser handles the 4-part NodeJS format (timestamp, requestID, logLevel, message).

2. Send fresh NodeJS Lambda invocations and check Logz.io.

   Expected: log levels parse correctly and START/END/REPORT lines are ignored again. Success check: NodeJS logs look as clean as the Python ones.

## When to use this

- NodeJS Lambda logs arrive misparsed in Logz.io while Python function logs are fine.
- START/END/REPORT lines leak through instead of being filtered.

## When NOT to use this

- All runtimes misparse; check the shipper config instead.
- Logs never arrive at all; that is a delivery problem.

## Compatibility

- Logz.io CloudWatch logs shipper with the PR #42 fix; mixed-runtime (NodeJS + Python) setups.

## Variant phrasings

- "logzio lambda nodejs logs misparsed"
- "logz.io cloudwatch shipper log level missing"

## Root cause

AWS Lambda log formats differ per runtime, and the parser had only been tested against the Python 3-part format. On NodeJS functions the log level landed in the message slot and the real message shifted, while the START/END/REPORT filter missed.

## Edge cases

- The reporter-verified local workaround was changing the parse to 4 parts by hand, but upgrading is the real fix; do not fork the parser.

---

Source: [Vectle](https://vectle.com/skills/skl_-7qctqzI2e2B1ZIfMFAKxQ). Version: `skv_KFdUPpBuIquPOuY51RVlFg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
