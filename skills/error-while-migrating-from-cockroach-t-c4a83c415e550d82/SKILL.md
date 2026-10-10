---
name: "error-while-migrating-from-cockroach-t-c4a83c415e550d82"
description: "Shows how to fix error while migrating from Cockroach to Postgres. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_7v1nItwnLgTsDVLy077Ttw"
  title: "Error while migrating from Cockroach to Postgres"
  version: "skv_QKhIRKbdrBdZJyCUQhqcUQ"
  updated: "2026-10-03T14:42:54.475142+00:00"
  canonical_url: "https://vectle.com/skills/skl_7v1nItwnLgTsDVLy077Ttw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

[adsehgal (commenter)]: To migrate a Zitadel instance from CockroachDB to PostgreSQL, run the init command first, then the setup command, then mirror with the --replace flag. 23.2.16, migrating to Postgres 16/17

## Steps

1. [adsehgal (commenter)]: To migrate a Zitadel instance from CockroachDB to PostgreSQL, run the init command first, then the setup command, then mirror with the --replace flag. Two reporters confirmed the migration worked with no issues.

## When to use

You are seeing this: Issue zitadel/zitadel#9042 (closed, 26 comments): ### Preflight Checklist - [x] I could not find a solution in the documentation, the existing issues or discussions - [ ] I have joined the ZITADEL chat Use this skill when you run into "Error while migrating from Cockroach to Postgres".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: 2.65.1, 23.2.16. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://zitadel.com/chat

- https://zitadel.com/docs/self-hosting/manage/cli/mirror

- https://github.com/zitadel/zitadel/issues/9042


---

Source: [Vectle](https://vectle.com/skills/skl_7v1nItwnLgTsDVLy077Ttw). Version: `skv_QKhIRKbdrBdZJyCUQhqcUQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
