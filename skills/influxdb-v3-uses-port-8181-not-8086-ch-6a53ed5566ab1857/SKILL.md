---
name: "influxdb-v3-uses-port-8181-not-8086-ch-6a53ed5566ab1857"
description: "Point InfluxDB V3 clients at port 8181, not the V2 default 8086. Use this skill when the task matches the title above. Not for unrelated tools or errors; check the tool's own docs for those."
metadata:
  skill_id: "skl_XXPwe9TaXI4OG1r5GJTE_A"
  title: "InfluxDB V3 uses port 8181 not 8086, check before debugging refused connections"
  version: "skv_nyt6dZC8K0YydZUd1rJvEw"
  updated: "2026-10-03T05:11:14.535617+00:00"
  canonical_url: "https://vectle.com/skills/skl_XXPwe9TaXI4OG1r5GJTE_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Point InfluxDB V3 clients at port 8181, not the V2 default 8086. When you get connection refused, check the port against the server version before debugging credentials or network. Also confirm the security group allows the right port from the client.

## Fix

Point InfluxDB V3 clients at port 8181, not the V2 default 8086. When you get connection refused, check the port against the server version before debugging credentials or network. Also confirm the security group allows the right port from the client.

Context: Web skill doc (AWS agent toolkit, Timestream for InfluxDB): documents the gotcha that InfluxDB V3 listens on port 8181 while V2 uses 8086. The number one cause of connection refused on V3 is a client configured for 8086. Agents copying V2 connection snippets against a V3 cluster will fail to connect.

## Matched source
Source: Published skill
Original query: "InfluxDB V3 uses port 8181 not 8086, check before debugging refused connections"
Key terms: 8086, 8181, before, check, connections, debugging, influxdb, port, refused, uses

## When to use this

- Use this when your task, error, or question matches the title above and the setup in the Fix section.

## When not to use this

- Skip it when the error text, tool, or situation is different. Forcing a mismatched fix usually costs more time than searching again.

## Compatibility

The original write-up does not pin tool versions. Treat the commands and UI paths above as reflecting the author's setup, and check your tool's own docs if your version looks different.


---

Source: [Vectle](https://vectle.com/skills/skl_XXPwe9TaXI4OG1r5GJTE_A). Version: `skv_nyt6dZC8K0YydZUd1rJvEw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
