---
name: "harness-misleading-no-eligible-delegat-931db6afdaef13ba"
description: "Upgrade the delegate to get the clearer error. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_gKb1NcjsMUBuCMup5rjlRg"
  title: "Harness: misleading No eligible delegates when a secret fails to resolve"
  version: "skv_Fjm_F4fvAE48OsJ46SUd9w"
  updated: "2026-10-03T05:38:05.275989+00:00"
  canonical_url: "https://vectle.com/skills/skl_gKb1NcjsMUBuCMup5rjlRg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade the delegate to get the clearer error. A secret resolution failure from AWS Secrets Manager used to surface as There are no eligible delegates present, sending people down a delegate-connectivity rabbit hole when the actual problem was that a secret could not be fetched. Fixed in the noted release so the error now points at the real cause.

## Fix

If you hit There are no eligible delegates present on a Harness CI pipeline, check secrets before touching delegate networking: verify the AWS Secrets Manager secret exists, the delegate's IAM role can read it, and the secret reference in the pipeline is spelled right. On older delegate versions the misleading message still appears, so treat no-eligible-delegates as a possible secret-resolution failure, not only a connectivity problem. Upgrade the delegate to get the clearer error.

Context: Harness CI release notes (September 2026): documents a real misdiagnosis trap. A secret resolution failure from AWS Secrets Manager used to surface as There are no eligible delegates present, sending people down a delegate-connectivity rabbit hole when the actual problem was that a secret could not be fetched. Fixed in the noted release so the error now points at the real cause.

## Matched source
Source: Published skill
Original query: "Harness: misleading No eligible delegates when a secret fails to resolve"
Key terms: delegates, eligible, fails, harness, misleading, resolve, secret

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_gKb1NcjsMUBuCMup5rjlRg). Version: `skv_Fjm_F4fvAE48OsJ46SUd9w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
