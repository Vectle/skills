---
name: "knock-feed-403-under-enhanced-security-99ffb4944249d688"
description: "The confirmed workaround was to downcase all user IDs before signing and identifying. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_L6Ajyf-eNQohDX8YkIr5XQ"
  title: "Knock feed 403 under enhanced security: the JWT parser downcases your user id"
  version: "skv_HDIiCrw8rw_IpHUCgh_d9g"
  updated: "2026-10-03T05:03:32.881089+00:00"
  canonical_url: "https://vectle.com/skills/skl_L6Ajyf-eNQohDX8YkIr5XQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

The confirmed workaround was to downcase all user IDs before signing and identifying.

## Fix

If Knock's enhanced security gives you a 403 on the feed while your signing code looks correct, compare the exact user_id casing on both sides. Knock's token parsing downcases the user_id inside the JWT, so a mixed-case id like a wallet address will never match the original. Sign and identify users with an already-lowercased id everywhere, and the feed auth will pass.

Context: GitHub issue knocklabs/knock-node#23 (closed): With enhanced security mode on, the notification feed returned 403 "You are not allowed to access that resource" even though the signing code looked right. A Knock contributor decoded the JWT and found the user_id had been downcased from 0xE7D9xxx to 0xe7d9xxx by the token parsing library, so the signed user no longer matched the user requesting the feed. The confirmed workaround was to downcase all user IDs before signing and identifying.

## Matched source
Source: Published skill
Original query: "Knock feed 403 under enhanced security: the JWT parser downcases your user id"
Key terms: downcases, enhanced, feed, knock, parser, security, under, user, your

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_L6Ajyf-eNQohDX8YkIr5XQ). Version: `skv_HDIiCrw8rw_IpHUCgh_d9g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
