---
name: "trying-to-generate-embeddings-using-in-d307ff6d61f993ed"
description: "Shows how to fix trying to generate embeddings using in-built. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_WvwPxsCl5HoRhKsZTIfvRg"
  title: "Trying to generate embeddings using in-built"
  version: "skv_FIpxL9vA3um4Gq0Gs79Gjg"
  updated: "2026-10-03T14:11:25.160515+00:00"
  canonical_url: "https://vectle.com/skills/skl_WvwPxsCl5HoRhKsZTIfvRg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Did an update collection to generate embeddings with ts/all-MiniLM-L12-v2 5. Next I did a restart on typesense-server.

## Steps

1. What was reported:
Issue typesense/typesense#1507 (closed, 17 comments): ## Description Trying some experiments (Round 1): 1. Started with a "fresh" server (clone of an existing production) 2. Upgraded TS to 0.25 3. Target is a collection with around 18K docs (post, articles etc) 4. Did an update collection to generate embeddings with `ts/all-MiniLM-L12-v2` 5. Server has been churning away since then for 18 hours 6. API calls to this collection dont complete (as expected) while calls to other collections do complete, also as expected 7. Which means that TS is working fine, and its not crashed 8. Next I did a restart on typesense-server.

2. What works:
The stall was memory pressure, not a crash: generating embeddings for an already-populated collection needs far more RAM than normal indexing. The reporter solved it by moving to a larger server class and succeeded with Typesense 0.26.0, about 20K documents, and the `gte-small` model, finishing in roughly 35 minutes. Practical steps: size the box up before altering a populated collection to add an embedding field, use a current Typesense release, and pick a small embedding model. Altering an empty collection is instant either way, so it is also fine to create the embedding field first and index documents after.

## When to use

You are seeing this: What was reported: Issue typesense/typesense#1507 (closed, 17 comments): ## Description Trying some experiments (Round 1): 1. Use this skill when you run into "Trying to generate embeddings using in-built".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

Versions mentioned in the source: Typesense 0.26.0. If you are on something much newer or older, the details may have shifted.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_WvwPxsCl5HoRhKsZTIfvRg). Version: `skv_FIpxL9vA3um4Gq0Gs79Gjg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
