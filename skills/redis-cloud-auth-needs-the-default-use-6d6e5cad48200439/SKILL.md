---
name: "redis-cloud-auth-needs-the-default-use-6d6e5cad48200439"
description: "On Redis Cloud, always send a username, usually default, plus the password from the Connect wizard; password-only legacy auth fails against RBAC-enabled databases."
metadata:
  skill_id: "skl_XhQqY5fdX9XknVXtB0bweQ"
  title: "Redis Cloud auth needs the default username plus password, not password alone"
  version: "skv__dj2q_PTAKwmJPCQv7zNpA"
  updated: "2026-10-03T05:33:52.26109+00:00"
  canonical_url: "https://vectle.com/skills/skl_XhQqY5fdX9XknVXtB0bweQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Redis Cloud auth needs the default username plus password, not password alone

## TL;DR

On Redis Cloud, always send a username, usually default, plus the password from the Connect wizard; password-only legacy auth fails against RBAC-enabled databases. Context: Web source (Redis Cloud connection skill notes): documents the auth-field gotcha. The username is often default unless RBAC custom users are used, and the password comes from the Connect wizard snippet.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

Tool: Redis. The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

Context: Web source (Redis Cloud connection skill notes): documents the auth-field gotcha. The username is often default unless RBAC custom users are used, and the password comes from the Connect wizard snippet. For redis-cli the TLS pattern is redis-cli -u rediss://[username]:[password]@[host]:[port], and non-TLS redis:// only when the database is explicitly configured without TLS.


---

Source: [Vectle](https://vectle.com/skills/skl_XhQqY5fdX9XknVXtB0bweQ). Version: `skv__dj2q_PTAKwmJPCQv7zNpA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
