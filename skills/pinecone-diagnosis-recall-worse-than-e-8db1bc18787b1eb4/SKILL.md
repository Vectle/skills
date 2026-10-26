---
name: "pinecone-diagnosis-recall-worse-than-e-8db1bc18787b1eb4"
description: "Symptom: queries miss results you expect. Separate model quality from index recall with a brute-force baseline over the same vectors, then act on whichever side fails. Not the full reference manual."
metadata:
  skill_id: "skl_ImWEujmSgZdJoBIVm6xlQw"
  title: "Pinecone diagnosis: recall worse than expected, isolate model vs index"
  version: "skv_24bBbF4vQLrjbUbnL5B1Hw"
  updated: "2026-10-03T14:46:23.802301+00:00"
  canonical_url: "https://vectle.com/skills/skl_ImWEujmSgZdJoBIVm6xlQw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.pinecone.io/troubleshooting/debug-model-vs-pinecone-recall-issues\"]"
---

**TL;DR:** Symptom: queries miss results you expect. Separate model quality from index recall with a brute-force baseline over the same vectors, then act on whichever side fails. Confirm it Follow the docs' recall-debug procedure: 1. Build an eval set: at least 10 queries over a 100k-vector source set, with labeled right answers.

## The error

```text
queries miss results you expect. Separate model quality from index recall with a brute-force baseline over the same vectors, then act on whichever side fails. Confirm it Follow the docs' recall-debug procedure: 1. Build an eval set: at least 10 queries over a 100k-vector source set, with labeled rig
```

## The fix

**TL;DR:** Symptom: queries miss results you expect. Separate model quality from index recall with a brute-force baseline over the same vectors, then act on whichever side fails. Confirm it Follow the docs' recall-debug procedure: 1. Build an eval set: at least 10 queries over a 100k-vector source set, with labeled right answers.

## The fix

1. Build an eval set: at least 10 queries over a 100k-vector source set, with labeled right answers.

2. Embed queries and corpus with your model; run brute-force search (FAISS or numpy) and score against the labels. If brute force scores badly, it is a model problem.

3. Upsert the same vectors to Pinecone, run the same queries, and compare Pinecone's returned ids to the brute-force ids. Pinecone recall near 0.99 on s1/p1 means the index is fine and the model is the issue.

4. Model problem: change the embedding model (and rebuild the index at the new dimension).

5. Index problem: check top_k (too small clips recall), filters (too strict), and pod size; escalate to support with the reproducible dataset if recall stays low.

## When to use this

- This covers exactly what the title says: Pinecone diagnosis.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Mentions 0.99 in the original; behavior may differ on much older or newer releases.

---

Source: [Vectle](https://vectle.com/skills/skl_ImWEujmSgZdJoBIVm6xlQw). Version: `skv_24bBbF4vQLrjbUbnL5B1Hw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
