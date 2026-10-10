---
name: "mcp-server-only-has-two-entry-points-n-739a04684189829b"
description: "Restores missing exa-mcp-server tools (linkedin search, deep researcher, crawling, company research) by upgrading to 3.0.8/3.0.9 and using the new single-dash tools= flag syntax. Use when only web_search_exa and get_code_context_exa appear despite passing all tool names. Not for tools missing for other reasons."
metadata:
  skill_id: "skl_lGnvgClj9Pf_eCC2Tn8IWQ"
  title: "Mcp server only has two entry points now missing linkedin, deepresearch etc"
  version: "skv_Q_kw5cQfkFznTQQyNqq-ZA"
  updated: "2026-10-03T04:12:47.030188+00:00"
  canonical_url: "https://vectle.com/skills/skl_lGnvgClj9Pf_eCC2Tn8IWQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Upgrade exa-mcp-server to 3.0.8 or 3.0.9 and change the flag syntax: drop the double dash and use a single `tools=` argument. The old `--tools` syntax silently exposes only two tools.

## The problem

exa-mcp-server only exposes `web_search_exa` and `get_code_context_exa` even when all 7 tool names are passed. Linkedin search, deep researcher, crawling, and company research tools are gone.

## Fix it

1. Upgrade the package:
   ```bash
   npm i -g exa-mcp-server@3.0.9
   ```
   Success check: the installed version is 3.0.8 or newer.

2. Change the flag syntax from `--tools` to `tools=`:
   ```json
   "args": ["-y", "exa-mcp-server", "tools=web_search_exa,get_code_context_exa,crawling_exa,company_research_exa,linkedin_search_exa,deep_researcher_start,deep_researcher_check"]
   ```
   Success check: all 7 tools appear in the MCP tool list.

3. For remote MCP servers, pass `?tools=[comma-list]` on the URL instead.
   Success check: the remote tool list shows all requested tools.

4. Temporary workaround before the fix: pin `exa-mcp-server@2.0.5`.
   Success check: tools reappear, but upgrade when you can.

## When this applies

- exa-mcp-server 3.0.x showing only 2 tools despite `--tools` with all names.
- Missing linkedin_search_exa, deep_researcher_*, crawling_exa, company_research_exa.

## When it does not apply

- Tools missing on 2.x versions; that is a different configuration problem.
- The MCP client itself cannot list tools at all.

## Compatibility

- exa-mcp-server npm package 3.0.8/3.0.9 (fixed). Affected: early 3.0.x.
- Workaround: pin 2.0.5.

## Variant phrasings

- exa-mcp-server only two tools
- exa mcp missing linkedin deepresearch
- exa-mcp-server tools flag not working

## Why it happens

Version 3.0 changed the CLI flag parsing: the double-dash `--tools` form stopped being recognized, so the server fell back to its default two tools. The single `tools=` form is parsed correctly in 3.0.8+.

## Edge cases

- Quote the comma list if your MCP client config splits on commas.
- Remote URL form needs URL-encoded commas in some clients.


---

Source: [Vectle](https://vectle.com/skills/skl_lGnvgClj9Pf_eCC2Tn8IWQ). Version: `skv_Q_kw5cQfkFznTQQyNqq-ZA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
