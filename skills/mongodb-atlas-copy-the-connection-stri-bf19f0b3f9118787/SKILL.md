---
name: "mongodb-atlas-copy-the-connection-stri-bf19f0b3f9118787"
description: "Shows how to fix mongoDB Atlas: copy the connection string without breaking it. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_nH_TVXRLsLqgJ0bc7wNIeQ"
  title: "MongoDB Atlas: copy the connection string without breaking it"
  version: "skv_SRXNCZpatm0q62Ne1dvpog"
  updated: "2026-10-03T14:04:42.503546+00:00"
  canonical_url: "https://vectle.com/skills/skl_nH_TVXRLsLqgJ0bc7wNIeQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Replace ONLY the placeholder with the database user's password. URL-encode the password before substituting: ``js const uri = template.replace('[password]', encodeURIComponent(rawPassword)); ` @ becomes %40, / becomes %2F`, and so on.

## Steps

1. Atlas UI: Database, Connect, Drivers. Pick your driver and version.
2. Copy the string. It contains a `[password]` placeholder (sometimes shown as `[password]` or similar bracketed text).
3. Replace ONLY the placeholder with the database user's password. Touch nothing else.
4. Store the result in an environment variable or secret manager. Never in code, never in a chat log, never in a ticket.

2. If the password contains `@ / : ? # [ ]` or `%`, the URI parser misreads the string and auth fails with a misleading error. URL-encode the password before substituting:

```js
const uri = template.replace('[password]', encodeURIComponent(rawPassword));
```

3. `@` becomes `%40`, `/` becomes `%2F`, and so on. Encode only the password, not the whole URI.

4. - Generate passwords without URI-special characters when you control creation. It removes the whole class of bug.
- The username goes in the URI as-is unless it also has special characters; same encoding rule applies.
- After substituting, the string must still start with `mongodb+srv://` (or `mongodb://` for the standard form) and contain no literal brackets.
- Rotate: if a connection string ever lands somewhere it should not (logs, screenshots, chat), rotate the database user password immediately and update the secret.

## When to use

You are seeing this: Atlas UI: Database, Connect, Drivers. Use this skill when you run into "MongoDB Atlas: copy the connection string without breaking it".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_nH_TVXRLsLqgJ0bc7wNIeQ). Version: `skv_SRXNCZpatm0q62Ne1dvpog`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
