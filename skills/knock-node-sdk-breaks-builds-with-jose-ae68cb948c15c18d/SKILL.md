---
name: "knock-node-sdk-breaks-builds-with-jose-ae68cb948c15c18d"
description: "The thread's resolution is that the 1.x SDK release dropped the jose dependency entirely, and edge-runtime import issues were fixed via PR #101; on the latest version, importing signUserToken from the tokenSigner module path produces no errors or warnings. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_3F0jpSobhIJt17N48sgywQ"
  title: "Knock Node SDK breaks builds with jose conflicts: upgrade to 1.x"
  version: "skv_Uw1jVjLXHYOYoqv0BFTO5A"
  updated: "2026-10-03T05:02:57.245465+00:00"
  canonical_url: "https://vectle.com/skills/skl_3F0jpSobhIJt17N48sgywQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The thread's resolution is that the 1.x SDK release dropped the jose dependency entirely, and edge-runtime import issues were fixed via PR #101; on the latest version, importing signUserToken from the tokenSigner module path produces no errors or warnings.

## Fix

If importing @knocklabs/node breaks your build with jose-related errors, upgrade to the 1.x SDK: it removed the jose dependency that conflicted with newer jose versions in the same bundle. On 1.x, import signing helpers from the tokenSigner module path. Do not pin an old SDK to work around the conflict; the dependency that caused it is gone in the current release.

Context: GitHub issue knocklabs/knock-node#80 (resolved): Merely importing @knocklabs/node broke builds wherever the app also used jose at 5.9.6, because Knock pinned jose at 5.2.0 and its compiled output confused ESM bundlers. The thread's resolution is that the 1.x SDK release dropped the jose dependency entirely, and edge-runtime import issues were fixed via PR #101; on the latest version, importing signUserToken from the tokenSigner module path produces no errors or warnings.

## Matched source
Source: Published skill
Original query: "Knock Node SDK breaks builds with jose conflicts: upgrade to 1.x"
Key terms: breaks, builds, conflicts, jose, knock, node, upgrade

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_3F0jpSobhIJt17N48sgywQ). Version: `skv_Uw1jVjLXHYOYoqv0BFTO5A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
