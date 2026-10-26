---
name: "duplicate-key-value-violates-unique-co-7313317bbec803fa"
description: "Shows how to fix duplicate key value violates unique constraint \"unique_constraints_pkey\" on configuring step. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_FFE2MsXW6ZgJ5CTc62OEKw"
  title: "duplicate key value violates unique constraint \"unique_constraints_pkey\" on configuring step"
  version: "skv_lrCUh8DQO9tVOVVN3oxYxw"
  updated: "2026-10-03T14:01:07.970417+00:00"
  canonical_url: "https://vectle.com/skills/skl_FFE2MsXW6ZgJ5CTc62OEKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/zitadel/zitadel/issues/8910\"]"
---

## TL;DR

The fix The root cause is a UID/GID mismatch on the bind-mounted machinekey` folder: the container runs as UID 1000, but the host folder is often created owned by root, so setup cannot write its files and the migration fails. Fix it with: 3. chown 1000:1000 machinekey 4. then restart the stack. If the database migration state is already broken, delete the Postgres volume first so migrations start clean, then bring the stack up again.

## When to use

You are seeing this: Self-hosted ZITADEL deployed with Docker randomly throws migration exception on configuring step: msg="migration failed" caller="[HOME]/..." error="ID=V3-DKcYh Message=Errors.Instance.Domain.AlreadyExists... Use this skill when you run into "duplicate key value violates unique constraint "unique_constraints_pkey" on configuring step".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Steps

1. Self-hosted ZITADEL deployed with Docker randomly throws migration exception on configuring step:
`msg="migration failed" caller="[HOME]/..." error="ID=V3-DKcYh Message=Errors.Instance.Domain.AlreadyExists...

2. The fix
The root cause is a UID/GID mismatch on the bind-mounted `machinekey` folder: the container runs as UID 1000, but the host folder is often created owned by root, so setup cannot write its files and the migration fails. Fix it with:

3. chown 1000:1000 machinekey

4. then restart the stack. If the database migration state is already broken, delete the Postgres volume first so migrations start clean, then bring the stack up again. The maintainer independently reproduced the UID/GID mismatch, confirming this is the cause.

## Why this happens

The fix The root cause is a UID/GID mismatch on the bind-mounted machinekey` folder: the container runs as UID 1000, but the host folder is often created owned by root, so


---

Source: [Vectle](https://vectle.com/skills/skl_FFE2MsXW6ZgJ5CTc62OEKw). Version: `skv_lrCUh8DQO9tVOVVN3oxYxw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
