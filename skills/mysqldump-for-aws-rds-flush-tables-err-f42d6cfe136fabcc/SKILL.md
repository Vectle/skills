---
name: "mysqldump-for-aws-rds-flush-tables-err-f42d6cfe136fabcc"
description: "Shows how to fix mysqldump for AWS RDS `flush tables` error on linux only. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_4qpvM6xFMTgOvSHMho0dIQ"
  title: "mysqldump for AWS RDS `flush tables` error on linux only"
  version: "skv_r8SD00aVyQyLC26q4uGAHQ"
  updated: "2026-10-04T03:06:31.1971+00:00"
  canonical_url: "https://vectle.com/skills/skl_4qpvM6xFMTgOvSHMho0dIQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/75183032/mysqldump-for-aws-rds-flush-tables-error-on-linux-only\"]"
---

## TL;DR

For "Access denied; you need (at least one of) the RELOAD privilege(s) for this operation": it's interesting that 5.7.41 changelog doesn't list anything close to the FLUSH TABLES WITH READ LOCK or to default values.

```text
Access denied; you need (at least one of) the RELOAD privilege(s) for this operation
```

## When to use

You are seeing this: I faced the same issue couple of days ago. Use this skill when you run into "mysqldump for AWS RDS `flush tables` error on linux only".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: recent 5.7.41, 5.7.40. If you are on something much newer or older, the details may have shifted.

I faced the same issue couple of days ago. My mysqldump script had been working for years just fine until it started to give me the `Access denied; you need (at least one of) the RELOAD privilege(s) for this operation` error. My first instinct was to grant this privilege. But after that I started to get `Access denied for user 'user'@'%' (using password - YES) (1045)` error, which is documented in AWS docs. After couple hours of investigation it turned out to be a bug of the most recent 5.7.41 version of mysql (It was released 17th of January, exactly when we started to get errors). Downgrading to 5.7.40 solved the problem. It's interesting that 5.7.41 changelog doesn't list anything close to the FLUSH TABLES WITH READ LOCK or to default values.

Context: Stack Overflow #75183032 (accepted answer, 23 votes): I have a process that exports the data from an AWS RDS MariaDB using mysqldump which has been running succesfully in a docker-image on Concourse for years. Since two nights ago the process has started failing with the error: `mysqldump: Couldn't execute 'FLUSH TABLES WITH READ LOCK': Access denied for user 'admin'@'%' (using password - YES) (1045) ` The official AWS explanation seems to be that because they do not allow super privileges to the master user or GLOBAL READ LOCK the mysqldump fails if the --master-data option is set. I do not have that option set. I'm running with these flags:...


---

Source: [Vectle](https://vectle.com/skills/skl_4qpvM6xFMTgOvSHMho0dIQ). Version: `skv_r8SD00aVyQyLC26q4uGAHQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
