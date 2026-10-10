---
name: "error-when-creating-new-prisma-migrati-51a39f8ecb8fefc4"
description: "Shows how to fix error when creating new Prisma migration. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_sbUqckKJ0MbZQR4ZVFJ44w"
  title: "Error when creating new Prisma migration"
  version: "skv_91ZUmvw5gaP1mHp_8BXg-g"
  updated: "2026-10-03T05:36:47.201104+00:00"
  canonical_url: "https://vectle.com/skills/skl_sbUqckKJ0MbZQR4ZVFJ44w"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Issue vercel/storage#114 (closed, 13 comments): When creating new migrations after having created the first one already, Prisma errors because the database schema isn't empty. This is because Prisma needs a separate database to be used as a shadow database.

## Steps

1. Issue vercel/storage#114 (closed, 13 comments): When creating new migrations after having created the first one already, Prisma errors because the database schema isn't empty. This is because Prisma needs a separate database to be used as a shadow database. While it's not a bug per se, it's still a limitation in Vercel since you can only connect one Postgres storage per project environment. To work around this you'd have to create another Postgres storage and manually set a new environment variable to be used as `shadowDatabaseUrl`. ``` Error: P3005 The database schema is not empty.

2. Prisma error P3005 ('database schema is not empty') on Vercel Postgres migrations was solved by Neon: the shadowDatabaseUrl workaround is no longer recommended and it should work by default now. If you're still carrying a manually created second Postgres storage just for the shadow database, you can remove that config. Note that migrations count toward your Written Data limits, which is a separate thing.

## When to use

You are seeing this: While it's not a bug per se, it's still a limitation in Vercel since you can only connect one Postgres storage per project environment. Use this skill when you run into "Error when creating new Prisma migration".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

Issue vercel/storage#114 (closed, 13 comments): When creating new migrations after having created the first one already, Prisma errors because the database schema isn't empty.

## Edge cases

- Note that migrations count toward your Written Data limits, which is a separate thing.


---

Source: [Vectle](https://vectle.com/skills/skl_sbUqckKJ0MbZQR4ZVFJ44w). Version: `skv_91ZUmvw5gaP1mHp_8BXg-g`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
