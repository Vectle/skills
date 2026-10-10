---
name: "servicenow-table-api-returning-duplica-e1f5852acedd5d4c"
description: "So this is almost certainly a bug in their API related to service account access. Here is what I have done, and what I believe to be occuring (and my work around!) After playing around with some different logic, I encountered the following: ``` {0}/api/now/table/cmdb_ci_vm_instance?sysparm_offset=0&sysparm_limit=750&sysparm_exclude_reference_link=true&sysparm_query=ORDERBYsys_id 2016-08-19 12:46:15,277 [INFO ] Returned Records Count: 750 {0}/api/now/table/cmdb_ci_vm_instance? Use when hitting th"
metadata:
  skill_id: "skl_zQlFHCc_3pvhmfeSPyL9oQ"
  title: "ServiceNow Table API returning duplicates / not returning all records"
  version: "skv_f2KRYTvgXQOHsEHtjhQv4Q"
  updated: "2026-10-04T00:17:25.213252+00:00"
  canonical_url: "https://vectle.com/skills/skl_zQlFHCc_3pvhmfeSPyL9oQ"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

So this is almost certainly a bug in their API related to service account access.

So this is almost certainly a bug in their API related to service account access. Here is what I have done, and what I believe to be occuring (and my work around!) After playing around with some different logic, I encountered the following: ``` {0}/api/now/table/cmdb_ci_vm_instance?sysparm_offset=0&sysparm_limit=750&sysparm_exclude_reference_link=true&sysparm_query=ORDERBYsys_id 2016-08-19 12:46:15,277 [INFO ] Returned Records Count: 750 {0}/api/now/table/cmdb_ci_vm_instance?sysparm_offset=750&sysparm_limit=750&sysparm_exclude_reference_link=true&sysparm_query=ORDERBYsys_id 2016-08-19 12:46:28,243 [INFO ] Returned Records Count: 746 ``` Notice on the second pass I asked for 750 records, but only got 746 (A difference of 4.) The other batches continued to return 750 as normal, and in the end I wound up with exactly 4 duplicates out of 5200+ total records retrieved. Because the second pass was returning less than the 750 I asked for, my code was breaking since it thought the data was complete... In order to get around this (initially) I did the following to the code above: ``` if (virtualmachineRo.result.Count == 0) { //AddRange(virtualmachineRo.result); break; } ``` I no longer trust that just because the number of records returned was less than the sysparm_limit that I have retrieved all records. It looks like when the data is pulled from the database, a separate process filters the data based on your permissions. Therefore, the second batch removes 4 records - but the database doesn't know any better... so on the next pass when I incremented my offse

Context: Stack Overflow question (score 4, has accepted answer): I am attempting to pull ALL data out of the ServiceNow CMDB data tables into my own SQL database. I plan on using this for automated updates when data is being maintained in a customer legacy system which needs to be sync'd with the new SN implementation. Our SN environment has many domains, many customers, etc. Which translates to a huge amount of data. Attempting to pull ALL records in a single API call naturally results in a timeout exception as the data is too large. The Web API suggests batching data, which is what I have implemented: ``` ... var offset = 0; while (true) { var requestUrl = string.Format("{0}/api/now/table/cmdb_ci_vm_instance?sysparm_offset={1}&sysparm_limit={2}&sysparm_exclude_reference_link=true", url, offset, batc

## When to use

- You hit this exact issue.
- The symptom matches: ServiceNow Table API returning duplicates / not returning all records.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

---

Source: [Vectle](https://vectle.com/skills/skl_zQlFHCc_3pvhmfeSPyL9oQ). Version: `skv_f2KRYTvgXQOHsEHtjhQv4Q`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
