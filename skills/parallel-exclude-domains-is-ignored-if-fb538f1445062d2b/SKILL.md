---
name: "parallel-exclude-domains-is-ignored-if-fb538f1445062d2b"
description: "Shows how to fix parallel: exclude_domains is ignored if include_domains is set; path matching is case sensitive. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_h7VPO3kg50AaZDt5Cw3Rsg"
  title: "Parallel: exclude_domains is ignored if include_domains is set; path matching is case sensitive"
  version: "skv_T0TM9L-Knp4tlG_ugxTf3w"
  updated: "2026-10-03T05:11:23.903325+00:00"
  canonical_url: "https://vectle.com/skills/skl_h7VPO3kg50AaZDt5Cw3Rsg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

An apex domain like example.com automatically includes all subdomains; domain/path prefixes like example.com/blog match that path and descendants on the domain and subdomains; paths are case-sensitive and match at segment boundaries (example.com/blog matches /blog and /blog/post but not /blogroll); trailing slashes ignored. There is a source filter limit (combined limit 200 per official agent-skill reference).

## When to use

You are seeing this: There is a source filter limit (combined limit 200 per official agent-skill reference). Use this skill when you run into "Parallel: exclude_domains is ignored if include_domains is set; path matching is case sensitive".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Parallel source policy: exclude_domains is ignored when include_domains is set From Parallel's official Source Policy docs, the interaction rules that break filtering: - `include_domains` is an allow list. Only matching domains or path prefixes can appear; the rest of the web is not searched. Never use it as a soft preference. - `exclude_domains` is applied ONLY when `include_domains` is empty. Send both and your block list is silently ignored. - `after_date` (Search API) is an inclusive RFC 3339 (`YYYY-MM-DD`) lower bound on publication date. Publish metadata is imperfect, so treat it as approximate. - Apex domain `example.com` automatically includes all subdomains (www, blog, api). A path prefix like `example.com/blog` matches that path and its descendants, but matching is case-sensitive and at segment boundaries: `/blog` and `/blog/post` match, `/blogroll` does not. - Combined filter limit is 200 entries. The practical rule: one domain-list type per request. Need a hard corpus boundary for compliance? Use include_domains. Need to block a few bad sites while searching the open web? Use exclude_domains alone. And to steer sources without nuking coverage, put the preference in the objective ("prefer official documentation") instead of a filter.

Context: Parallel official Source Policy docs (docs.parallel.ai/resources/source-policy): source policies work across Task, Search, and Monitor APIs. include_domains is an allow list: only matching sources are returned. exclude_domains is a block list applied only when include_domains is empty. after_date (Search API) is an RFC 3339 date lower bound. An apex domain like example.com automatically includes all subdomains; domain/path prefixes like example.com/blog match that path and descendants on the domain and subdomains; paths are case-sensitive and match at segment boundaries (example.com/blog matches /blog and /blog/post but not /blogroll); trailing slashes ignored. There is a source filter limit (combined limit 200 per official agent-skill reference).


---

Source: [Vectle](https://vectle.com/skills/skl_h7VPO3kg50AaZDt5Cw3Rsg). Version: `skv_T0TM9L-Knp4tlG_ugxTf3w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
