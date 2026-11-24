---
name: "mongodb-write-fails-with-not-primary-e-8c086df9e1bc6700"
description: "mongodb write fails with not primary error after replica set election"
metadata:
  skill_id: "skl_6gSuSybmc03RZmk4bItJOA"
  title: "mongodb write fails with not primary error after replica set election"
  version: "skv_oqKp8hgisMa_XAl_4C709Q"
  updated: "2026-11-24T01:53:05.185045+00:00"
  canonical_url: "https://vectle.com/skills/skl_6gSuSybmc03RZmk4bItJOA"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm a primary actually exists now

Check how the client connects

Look for writes pinned to a secondary

Enable retryable writes and a sane server selection timeout

Restart clients that hold a stale topology

Stop repeat elections if they keep happening

---

Source: [Vectle](https://vectle.com/skills/skl_6gSuSybmc03RZmk4bItJOA). Version: `skv_oqKp8hgisMa_XAl_4C709Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
