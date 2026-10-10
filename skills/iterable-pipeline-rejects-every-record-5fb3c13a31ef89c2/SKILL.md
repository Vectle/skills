---
name: "iterable-pipeline-rejects-every-record-5fb3c13a31ef89c2"
description: "When every Iterable record in a pipeline fails, check the toplevel email mapping first, not the field values. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_ZKxadNXrj7v1rPmSa7MB1w"
  title: "Iterable pipeline rejects every record: the missing toplevel email"
  version: "skv_Q0Yy66kkHTo89W9BRZXVlA"
  updated: "2026-10-03T05:08:58.90658+00:00"
  canonical_url: "https://vectle.com/skills/skl_ZKxadNXrj7v1rPmSa7MB1w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

When every Iterable record in a pipeline fails, check the toplevel email mapping first, not the field values. Email buried inside dataFields does not identify the contact; the toplevel email or userId must be mapped explicitly. Also trim custom email fields: a trailing space is rejected with an error that hides the real cause.

## The error, verbatim

```text
When every Iterable record in a pipeline fails, check the toplevel email mapping first, not the field values. Email buried inside dataFields does not identify the contact; the toplevel email or userId must be mapped explicitly. Also trim custom email fields: a trailing space is rejected with an error that hides the real cause.
```

## Fix

When every Iterable record in a pipeline fails, check the toplevel email mapping first, not the field values. Email buried inside dataFields does not identify the contact; the toplevel email or userId must be mapped explicitly. Also trim custom email fields: a trailing space is rejected with an error that hides the real cause.

Context: The Digioh help documentation for Iterable pipelines (updated June 2026) names the most common total-failure cause: Iterable identifies contacts with a toplevel email or userId that must be explicitly mapped. A pipeline that sends the email only inside dataFields, with a blank toplevel identifier, fails on every single submission. It also notes a trailing space in a custom email field gets rejected, and the log error does not make the cause obvious.

## Matched source
Source: Published skill
Original query: "Iterable pipeline rejects every record: the missing toplevel email"
Key terms: email, every, iterable, missing, pipeline, record, rejects, toplevel

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_ZKxadNXrj7v1rPmSa7MB1w). Version: `skv_Q0Yy66kkHTo89W9BRZXVlA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
