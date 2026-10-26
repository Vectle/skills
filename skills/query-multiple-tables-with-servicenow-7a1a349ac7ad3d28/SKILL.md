---
name: "query-multiple-tables-with-servicenow-7a1a349ac7ad3d28"
description: "Guide Query multiple tables with Servicenow Rest API and Powershell: Then, you can just treat that Database View like a table (as far as the REST API is concerned) like https://instance.service-now. Use this when you hit exactly this in Query. Not for different errors or different tools."
metadata:
  skill_id: "skl_5St42tmA2uwTjHTWs6Qw3Q"
  title: "Query multiple tables with Servicenow Rest API and Powershell"
  version: "skv_u5XXKHfcD1fVkjoi6200Fw"
  updated: "2026-10-03T05:34:19.114979+00:00"
  canonical_url: "https://vectle.com/skills/skl_5St42tmA2uwTjHTWs6Qw3Q"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://stackoverflow.com/questions/36988592\"]"
---

TL;DR: Then, you can just treat that Database View like a table (as far as the REST API is concerned) like https://instance.service-now.com/api/now/table/problem_incidents Context: Stack Overflow #36988592 (accepted answer, 5 votes, 1 answers): Is there a way to search/join multiple tables within one URI/call using PowerShell?

[Joey (accepted answer)]: Depends on what direction your join is (target parent, reference child vs target child, reference parent) If you're dot-walking through reference fields on the target table, you can just do it in the query like assigned_to.first_name=bob, and it will automatically join sc_task to sys_user on the assigned_to reference field. If you're not actually dot-walking, but rather looking to walk down into child records like if you were querying the problem table, but wanted to join a Related List like related incidents where the child incident table has a reference field named problem_id pointing back up to your target problem table, you could create a Database view joining problem to incident on incident.problem_id = problem.sys_id, and name it something like problem_incidents. Then, you can just treat that Database View like a table (as far as the REST API is concerned) like https://instance.service-now.com/api/now/table/problem_incidents

Context: Stack Overflow #36988592 (accepted answer, 5 votes, 1 answers): Is there a way to search/join multiple tables within one URI/call using PowerShell? I'm trying to query the task table for any open TASK items and 'GET' back certain field values. The problem is that there are custom fields on the TASK item which are linked to other tables not on the TASK record/TASK table. ``` URI $task = "https://instance.service-now.com/api/now/table/sc_task" Adding filters to the URI $task = "https://instance.service-now.com/api/now/table/sc_task?sysparm_query=yadadada" ``` ..but I'm looking to be able to join multiple tables so I can "dot walk" to other tables other than

## When to use
You hit exactly this: Query multiple tables with Servicenow Rest API and Powershell in Query.

## When not to use
A different error, or the same symptom in a different tool. This page only covers the failure above.

## Compatibility
Query.

## Edge cases
- The problem is that there are custom fields on the TASK item which are linked to other tables not on the TASK record/TASK table.

---

Source: [Vectle](https://vectle.com/skills/skl_5St42tmA2uwTjHTWs6Qw3Q). Version: `skv_u5XXKHfcD1fVkjoi6200Fw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
