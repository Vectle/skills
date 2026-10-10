---
name: "backend-eks-docdb-elastic-yields-mongo-41cf5402d24d1350"
description: "I guess both will work in mongoose await, its just error returned will be more detail for the `exec` one. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_ITUKfbci-80aJLq9J593Pw"
  title: "Backend: EKS + DocDB Elastic yields Mongoose distinct undefined error"
  version: "skv_APlj60oPm-s73t-ELkuVQQ"
  updated: "2026-10-03T05:12:56.503992+00:00"
  canonical_url: "https://vectle.com/skills/skl_ITUKfbci-80aJLq9J593Pw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

I guess both will work in mongoose await, its just error returned will be more detail for the `exec` one. Thus that's not an issue the call is getting executed. So i guess for someversions of mongo the distinct would be `undefined`.

## The error, verbatim

```text
[maintainer akhilmhdh]: Hey there. 1. I guess both will work in mongoose await, its just error returned will be more detail for the `exec` one. Thus that's not an issue the call is getting executed. 2. So i guess for someversions of mongo the distinct would be `undefined`. I guess we need to do an undefined check . so that it doesn't fail. This is my inference. @maidul98
```

## Fix

[maintainer akhilmhdh]: Hey there. 1. I guess both will work in mongoose await, its just error returned will be more detail for the `exec` one. Thus that's not an issue the call is getting executed. 2. So i guess for someversions of mongo the distinct would be `undefined`. I guess we need to do an undefined check . so that it doesn't fail. This is my inference. @maidul98

Context: Issue infisical/infisical#796 (closed, 14 comments): ### Describe the bug Hey! I'm executing a nuanced PoC for Infisical in EKS (AWS-hosted Kubernetes), and wanted to leverage a DocumentDB elastic cluster in lieu of an in-cluster `mongo` pod with persistence, to try and centralize DB management. The latest DocDB cluster specification is highly compatible with MongoDB 3, 4, and 5, so I figure it _should_ be okay. Maybe. This is in reference to the `v0.23.3` Docker images from yesterday as-of-writing. In the backend specifically, after wrestling with giving the app the correct `MONGO_URL` to get Mongoose to connect to the DocDB cluster succ

## Matched source
Source: Published skill
Original query: "Backend: EKS + DocDB Elastic yields Mongoose distinct undefined error"
Key terms: backend, distinct, docdb, elastic, error, mongoose, undefined, yields

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_ITUKfbci-80aJLq9J593Pw). Version: `skv_APlj60oPm-s73t-ELkuVQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
