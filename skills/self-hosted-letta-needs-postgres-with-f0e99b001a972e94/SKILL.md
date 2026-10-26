---
name: "self-hosted-letta-needs-postgres-with-f0e99b001a972e94"
description: "Test archival_memory_insert followed by archival_memory_search right after deploy: if search returns nothing while core memory works, the vector store is the suspect. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_NZY6bf0hbQUj4dH1kfefWg"
  title: "Self-hosted Letta needs Postgres with pgvector or archival memory search breaks"
  version: "skv_7cRlQfMW86_v8pT5gNhpgQ"
  updated: "2026-10-03T04:43:58.201015+00:00"
  canonical_url: "https://vectle.com/skills/skl_NZY6bf0hbQUj4dH1kfefWg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/dbrowneup/linus/blob/HEAD/docs/repo-notes/Letta.md\"]"
---

## TL;DR

Test archival_memory_insert followed by archival_memory_search right after deploy: if search returns nothing while core memory works, the vector store is the suspect. Archival memory is backed by an embedding index that requires pgvector in production, and Postgres plus the pgvector extension is a hard requirement of the default compose file.

## Fix

When self-hosting Letta, provision Postgres with the pgvector extension before creating agents that use archival memory, do not treat it as optional. If you want the lightweight path, install the sqlite extra so sqlite-vec backs the embedding index. Test archival_memory_insert followed by archival_memory_search right after deploy: if search returns nothing while core memory works, the vector store is the suspect.

Context: Repo research notes on Letta document the archival memory storage requirement that breaks self-hosted setups. Archival memory is backed by an embedding index that requires pgvector in production, and Postgres plus the pgvector extension is a hard requirement of the default compose file. Running the server without it, or with plain SQLite and no sqlite-vec optional dependency, leaves archival search non-functional while everything else looks healthy.

## Matched source
Source: Published skill
Original query: "Self-hosted Letta needs Postgres with pgvector or archival memory search breaks"
Key terms: archival, breaks, hosted, letta, memory, needs, pgvector, postgres, search, self

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_NZY6bf0hbQUj4dH1kfefWg). Version: `skv_7cRlQfMW86_v8pT5gNhpgQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
