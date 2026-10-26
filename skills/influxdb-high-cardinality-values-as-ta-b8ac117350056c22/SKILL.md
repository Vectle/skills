---
name: "influxdb-high-cardinality-values-as-ta-b8ac117350056c22"
description: "Store them as fields instead. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_g6LNanqACwXadUWe8oavTg"
  title: "InfluxDB: high-cardinality values as tags explode series and memory"
  version: "skv_0bXG9X8-Y-kYCOo0bZSIUw"
  updated: "2026-10-03T05:11:47.365004+00:00"
  canonical_url: "https://vectle.com/skills/skl_g6LNanqACwXadUWe8oavTg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/sanoy24/backend-performance-review/blob/HEAD/skills/backend-performance-review/technology/influxdb.md\"]"
---

## TL;DR

Store them as fields instead. When InfluxDB memory grows without bound, check series cardinality first and find the tag with exploding unique values. Agents that model per-request identifiers as tags will watch memory grow without bound; tags are for low-cardinality dimensions, fields are for the rest.

## Fix

Never put high-cardinality values like request IDs, user IDs, timestamps, or raw URLs into InfluxDB tags. Store them as fields instead. When InfluxDB memory grows without bound, check series cardinality first and find the tag with exploding unique values.

Context: Web skill doc (InfluxDB failure modes): documents the gotcha that a high-cardinality value written as a tag (request ID, user ID, raw URL) dominates memory, because every unique tag value creates a new series. Agents that model per-request identifiers as tags will watch memory grow without bound; tags are for low-cardinality dimensions, fields are for the rest.

## Matched source
Source: Published skill
Original query: "InfluxDB: high-cardinality values as tags explode series and memory"
Key terms: cardinality, explode, high, influxdb, memory, series, tags, values

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_g6LNanqACwXadUWe8oavTg). Version: `skv_0bXG9X8-Y-kYCOo0bZSIUw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
