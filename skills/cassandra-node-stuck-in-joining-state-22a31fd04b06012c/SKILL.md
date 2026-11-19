---
name: "cassandra-node-stuck-in-joining-state-22a31fd04b06012c"
description: "cassandra node stuck in joining state after bootstrap, streaming failed"
metadata:
  skill_id: "skl_SAS-weG0gB0cswuPbL_zAw"
  title: "cassandra node stuck in joining state after bootstrap, streaming failed"
  version: "skv_mEuD9S2x8kto_EKaOGoqEA"
  updated: "2026-11-19T01:52:55.50772+00:00"
  canonical_url: "https://vectle.com/skills/skl_SAS-weG0gB0cswuPbL_zAw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Run nodetool status and nodetool netstats on the joining node.

Check system and debug logs on the joining node and on one source node for stream session failures around the bootstrap start time.

Check free disk space on the joining node and confirm it can hold the data being streamed.

Verify the storage port is open between the joining node and every source node, with no idle timeout cutting long streams.

If bootstrap keeps failing on retry, stop the node, clear its data, commitlog and saved caches directories, and start it again as a fresh bootstrap, or use the replace address flow for a failed join.

---

Source: [Vectle](https://vectle.com/skills/skl_SAS-weG0gB0cswuPbL_zAw). Version: `skv_mEuD9S2x8kto_EKaOGoqEA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
