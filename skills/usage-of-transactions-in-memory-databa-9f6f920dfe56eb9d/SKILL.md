---
name: "usage-of-transactions-in-memory-databa-9f6f920dfe56eb9d"
description: "Libsql Client Ts: usage of transactions in :memory: database was broken with #105. The verified fix is Workaround: use `file::memory:?cache=shared` as the URL (shared cache mode keeps one DB; introduced ~0.8/0.9 via PR #220). Use this when you hit the symptoms above in libsql-client-ts; not for unrelated libsql-client-ts errors or general setup questions."
metadata:
  skill_id: "skl_F9vhXJPkHsUhmwJ7-DctNQ"
  title: "Usage of transactions in `:memory:` database was broken with #105"
  version: "skv_GL96IFvtlZyvxrAWQKzlww"
  updated: "2026-10-03T04:46:34.83509+00:00"
  canonical_url: "https://vectle.com/skills/skl_F9vhXJPkHsUhmwJ7-DctNQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Workaround: use `file::memory:?cache=shared` as the URL (shared cache mode keeps one DB; introduced ~0.8/0.9 via PR #(220).

## The error

```text
Issue tursodatabase/libsql-client-ts#229 (closed, 11 comments): #105 regressed in memory databases when transactions are used. Once a transaction is created, the entire in memory database will be effectively discarded for subsequent db operations that the client makes.
From the regressing PR.
> 1. A single connection is created lazily whenever user executes a statement
> 2. When a transaction starts, the Transaction object takes ownership of the current transaction.
```

## Fix

1. Workaround: use `file::memory:?cache=shared` as the URL (shared cache mode keeps one DB; introduced ~0.8/0.9 via PR #(220).

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in libsql-client-ts.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in libsql-client-ts, even a similar-looking one.
- General libsql-client-ts setup or credential questions.

## Compatibility

- Libsql Client Ts (tursodatabase/libsql-client-ts)

## Variant phrasings

- How to fix "usage of transactions in :memory: database was broken with #105" in libsql-client-ts
- libsql-client-ts: usage of transactions in :memory: database was broken with #105

## Root cause

Root cause: PR #105 made transactions take ownership of a lazily-created connection, so on `:memory:` DBs the in-memory database is effectively discarded for subsequent operations after a transaction.

## Edge cases

- Caveat: closing connections behaves oddly in shared-cache mode.

## Source

- https://github.com/tursodatabase/libsql-client-ts/issues/229

---

Source: [Vectle](https://vectle.com/skills/skl_F9vhXJPkHsUhmwJ7-DctNQ). Version: `skv_GL96IFvtlZyvxrAWQKzlww`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
