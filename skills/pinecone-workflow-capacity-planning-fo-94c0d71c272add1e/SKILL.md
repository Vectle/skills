---
name: "pinecone-workflow-capacity-planning-fo-94c0d71c272add1e"
description: "Pods bill per pod-hour whether queries run or not. Size from measured QPS and data volume: replicas for throughput, shards and pod type for data size."
metadata:
  skill_id: "skl_pk5sT9eg6LVcsACyA125eg"
  title: "Pinecone workflow: capacity planning for pod-based indexes"
  version: "skv_BDR11jWt6UJdfLbDzsNwpQ"
  updated: "2026-10-03T14:00:14.141552+00:00"
  canonical_url: "https://vectle.com/skills/skl_pk5sT9eg6LVcsACyA125eg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

**TL;DR:** Pods bill per pod-hour whether queries run or not. Size from measured QPS and data volume: replicas for throughput, shards and pod type for data size. Measure first. Index a representative slice and load-test: find the QPS where latency breaches your SLO on one replica.

## The fix

1. **Pod type** (p1, p2, s1...): memory and compute per pod. Bigger types hold more vectors and answer faster.

2. **Replicas**: copies of each shard. More replicas, more query throughput.

3. **Shards**: partitions of the data. More shards, more total capacity.

4. **Measure first.** Index a representative slice and load-test: find the QPS where latency breaches your SLO on one replica.

5. **Size replicas** from peak QPS divided by per-replica sustainable QPS, plus headroom (N+1 at least for production).

6. **Size shards and pod type** from total vector count and dimension: the data must fit in the pods' memory with room to grow.

7. **Start small, scale up.** It is cheaper to add replicas than to run oversized pods for a quarter. Serverless first for unknown traffic; pods when the traffic shape is known and steady.

8. **Revisit quarterly.** Data grows; QPS patterns change. A yearly-old sizing is a guess.

9. Sizing from marketing QPS instead of measured: the most expensive mistake in this list.

10. One giant pod instead of sharded smaller ones: worse failure blast radius and harder scaling.

11. Forgetting replicas do not help write-heavy bursts the way they help reads: size the write path separately.

12. Leaving a scaled-up pod fleet after the traffic spike: pod-hours accrue silently. Scale down deliberately.

## When to use this

- This covers exactly what the title says: Pinecone workflow.
- You are setting this up for the first time, or auditing an existing setup.
- You want the key gotchas in one place before you start.

## When not to use this

- You are doing a different workflow with Pinecone; these steps are specific to the title above.
- You need the full reference docs; this is the short path, not the manual.

## Compatibility

- Not pinned to a specific version; follows current Pinecone behavior.

---

Source: [Vectle](https://vectle.com/skills/skl_pk5sT9eg6LVcsACyA125eg). Version: `skv_BDR11jWt6UJdfLbDzsNwpQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
