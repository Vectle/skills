---
name: "moov-io-ach-allowmissingfileheader-has-260d772dbace74fa"
description: "Fixes moov-io/ach POST /files/create 500ing on raw NACHA text bodies while JSON works. Use this when allowMissingFileHeader/allowMissingFileControl flags have no effect on text/plain posts. Not for JSON-body creation issues."
metadata:
  skill_id: "skl_9kzZLdBOKkQtKoUDcRvqWw"
  title: "moov-io/ach: allowMissingFileHeader has no effect, POST /files/create 500s on text body"
  version: "skv_Og6NIMUSfjpM_jNh-Q5UWA"
  updated: "2026-10-03T05:30:11.31609+00:00"
  canonical_url: "https://vectle.com/skills/skl_9kzZLdBOKkQtKoUDcRvqWw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

TL;DR: if `POST /files/create` with an ACH text body (`Content-Type: text/plain`) 500s on moov-io/ach v1.34.2 for both valid and invalid files while the same file as JSON works, it is a bug in the text body handling, not your file or flags. Upgrade to v1.34.4 or later; the fix shipped in PR #1379 and the reporter confirmed it works. No request change needed, just the version bump.

## Steps

1. Upgrade moov-io/ach to v1.34.4+.

2. Re-submit the text file with the bypass flags as before.

   Expected: the file is accepted. Success check: no more 500 on the text path.

## When to use this

- v1.34.2, text/plain 500s, JSON works, flags ignored.

## When NOT to use this

- JSON creation fails too; that is a different problem.
- You are on v1.34.4+ and still see it; report it.

## Compatibility

- moov-io/ach v1.34.4+ (PR #1379).

## Variant phrasings

- "moov ach files/create 500 text"
- "moov-io allowMissingFileHeader no effect"

## Root cause

The text-body code path mishandled the request independent of the bypass flags.

## Edge cases

- General lesson: when one content type works and another 500s on the same data, the bug is in the failing content-type's code path; check the project's issues for that path before re-encoding files.

---

Source: [Vectle](https://vectle.com/skills/skl_9kzZLdBOKkQtKoUDcRvqWw). Version: `skv_Og6NIMUSfjpM_jNh-Q5UWA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
