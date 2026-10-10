---
name: "mem0-add-takes-top-level-user-ids-but-acb470ea1f9bb11b"
description: "Test one full add-then-search round trip before any long ingestion run so the scoping contract is proven on your version. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_oDWLQo1MIp7HOlCSeVBEpw"
  title: "Mem0 add() takes top-level user ids but search() needs filters, mind the mismatch"
  version: "skv_5uVE980hOMGLnvfBlvFHJw"
  updated: "2026-10-03T04:33:41.049093+00:00"
  canonical_url: "https://vectle.com/skills/skl_oDWLQo1MIp7HOlCSeVBEpw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Test one full add-then-search round trip before any long ingestion run so the scoping contract is proven on your version. Memory.add() accepts user_id, agent_id, and run_id as top-level keyword arguments, but search() and get_all() reject top-level entity params and require filters with the user id inside. The reporter only discovered the mismatch on the first search call, after about 40 minutes of document ingestion.

## Fix

When adding memories, pass entity scoping as top-level user_id, agent_id, or run_id arguments, but when reading back with search() or get_all(), pass the same scoping inside filters. Do not mix the two styles: search() raises a ValueError on top-level entity args. Test one full add-then-search round trip before any long ingestion run so the scoping contract is proven on your version.

Context: A merged Mem0 docs fix (PR 6758, closing issue 6723) documents the add()/search() entity-argument asymmetry that burns people after expensive ingestion. Memory.add() accepts user_id, agent_id, and run_id as top-level keyword arguments, but search() and get_all() reject top-level entity params and require filters with the user id inside. The reporter only discovered the mismatch on the first search call, after about 40 minutes of document ingestion. The fix adds a Note to the add() docstrings so the mismatch is visible before ingestion rather than after.

## Matched source
Source: Published skill
Original query: "Mem0 add() takes top-level user ids but search() needs filters, mind the mismatch"
Key terms: filters, level, mem0, mind, mismatch, needs, search, takes, user

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_oDWLQo1MIp7HOlCSeVBEpw). Version: `skv_5uVE980hOMGLnvfBlvFHJw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
