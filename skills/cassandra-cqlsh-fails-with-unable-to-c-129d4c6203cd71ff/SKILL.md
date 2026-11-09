---
name: "cassandra-cqlsh-fails-with-unable-to-c-129d4c6203cd71ff"
description: "cassandra cqlsh fails with unable to connect to any servers error"
metadata:
  skill_id: "skl_9zAfKDjbjG0uTOQk7gU2ew"
  title: "cassandra cqlsh fails with unable to connect to any servers error"
  version: "skv_CszSU-y05Q9imp9TKhcRcg"
  updated: "2026-11-09T13:52:33.001509+00:00"
  canonical_url: "https://vectle.com/skills/skl_9zAfKDjbjG0uTOQk7gU2ew"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Note the exact host and port cqlsh is trying, from your command or cqlshrc file, and confirm that host is a live node in the cluster.

Test TCP reachability to port 9042 on that node from the client machine with a port check tool.

On the node, check the Cassandra service status and the system log tail for listen and startup lines, and confirm the process finished starting.

Check the listen and rpc addresses in cassandra.yaml. The native transport must listen on an address the client can reach, not only on a private internal address.

Retry cqlsh against a second node in the cluster.

---

Source: [Vectle](https://vectle.com/skills/skl_9zAfKDjbjG0uTOQk7gU2ew). Version: `skv_CszSU-y05Q9imp9TKhcRcg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
