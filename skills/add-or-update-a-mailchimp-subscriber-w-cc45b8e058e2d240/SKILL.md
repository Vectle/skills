---
name: "add-or-update-a-mailchimp-subscriber-w-cc45b8e058e2d240"
description: "Shows how to fix add or update a Mailchimp subscriber with API v3: PUT upsert keyed by MD5 of the email. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_5fMqEfsEytSFFW4PnFu5_Q"
  title: "Add or update a Mailchimp subscriber with API v3: PUT upsert keyed by MD5 of the email"
  version: "skv_VxMUhzUipuBXDBPi9sBbnw"
  updated: "2026-10-03T14:00:34.319541+00:00"
  canonical_url: "https://vectle.com/skills/skl_5fMqEfsEytSFFW4PnFu5_Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Use PUT on /3.0/lists/{list_id}/members/{member_id} where member_id is the MD5 of the lowercase email address. PUT either adds the member or updates them if they already exist, so it doubles as your upsert. Authenticate with HTTP basic auth where the username can be any string and the password is your API key, and build the host from the datacenter suffix of the key - {dc}.api.mailchimp.com.

## Fix

Use PUT on /3.0/lists/{list_id}/members/{member_id} where member_id is the MD5 of the lowercase email address. PUT either adds the member or updates them if they already exist, so it doubles as your upsert. Authenticate with HTTP basic auth where the username can be any string and the password is your API key, and build the host from the datacenter suffix of the key - {dc}.api.mailchimp.com. Do not put the API key inside the JSON body, it is not part of the schema and the request will fail validation.

Context: Stack Overflow #30481979 (accepted answer, 139 votes): The reporter could not find working examples for adding subscribers with the Mailchimp API v3 after v2 was deprecated, and kept tripping over auth and endpoint shape. The accepted answer gives the canonical pattern: a PUT to the member endpoint that upserts.

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_5fMqEfsEytSFFW4PnFu5_Q). Version: `skv_VxMUhzUipuBXDBPi9sBbnw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
