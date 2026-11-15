---
name: "transaction-numbers-are-only-allowed-o-d636f8ace86665f0"
description: "transaction numbers are only allowed on a replica set member or mongos mongodb error"
metadata:
  skill_id: "skl_zTe0to06980lt7gjmAEO-A"
  title: "transaction numbers are only allowed on a replica set member or mongos mongodb error"
  version: "skv_yYlPxcRHz_dU8xOxp8FgVg"
  updated: "2026-11-14T01:53:42.759417+00:00"
  canonical_url: "https://vectle.com/skills/skl_zTe0to06980lt7gjmAEO-A"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm the deployment type by running db.serverStatus in mongosh and checking whether the repl field is present.

Stop the standalone mongod cleanly and back up the data directory before changing its mode.

Restart mongod with replication enabled, using the replSet option and a set name such as rs0, keeping the same data directory and port.

Run rs.initiate in mongosh once to create the single node replica set.

Update the application connection string to name the replica set, for example by adding the replicaSet parameter with the set name.

Retry the transaction in the application or in a short mongosh session using startSession and withTransaction.

For production, expand to at least three members before relying on transactions under load.

---

Source: [Vectle](https://vectle.com/skills/skl_zTe0to06980lt7gjmAEO-A). Version: `skv_yYlPxcRHz_dU8xOxp8FgVg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
