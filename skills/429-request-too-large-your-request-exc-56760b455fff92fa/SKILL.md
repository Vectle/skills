---
name: "429-request-too-large-your-request-exc-56760b455fff92fa"
description: "Fixes the GitHub MCP server hitting a 429 context-window error when listing commits on a busy repo. Use when list_commits fails with request-too-large or rate_limit_exceeded and the diff is huge. Not for GitHub API rate limits or auth errors."
metadata:
  skill_id: "skl_jozLX-leOSjIRiWsM0TbDg"
  title: "429 Request too large: your request exceeds the model's context window on list_commits"
  version: "skv_orhEmhWRvhr3bFGlEQodrQ"
  updated: "2026-10-03T06:06:39.601038+00:00"
  canonical_url: "https://vectle.com/skills/skl_jozLX-leOSjIRiWsM0TbDg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# 429 Request too large: your request exceeds the model's context window on list_commits

**TL;DR:** Narrow the commit query: filter by path, author, or date range, and ask for fewer commits per call. The 429 here is not the GitHub API rate limit. The tool pulled more than 64k tokens of commits and blew past the model context. Page through results with several small calls instead of one giant list_commits.

## The error

```
429 Request too large: your request exceeds the model's context window of 200000 tokens. (rate_limit_exceeded)
```

## Fix it

1. Retry list_commits with a path filter for the directory you care about.
   Expected: The call returns a much smaller result set.
2. If you still need history, add a date range or author filter to split the query.
   Expected: Each call stays well under the context limit.
3. Ask for the newest N commits only and page backwards as needed.
   Expected: You get 429-free results across multiple small calls.

## When this applies

list_commits or a similar bulk GitHub MCP tool fails with a 429 that mentions the model's context window or request too large, especially on repos with long histories.

## When this does NOT apply

If the 429 mentions the GitHub API rate limit with a retry-after time, that is the API quota; wait it out instead. Auth errors are a different fix.

## Tool compatibility

GitHub MCP server (modelcontextprotocol/servers), recent versions

## Also seen as

- rate_limit_exceeded on GitHub MCP list_commits
- GitHub MCP server returns 429 listing commits
- request too large from GitHub MCP tools

## Why it happens

The MCP tool fetches the full commit list including diffs and hands it to the model as tool output. On an active repo that easily exceeds 64k tokens, and the model provider rejects the response with a 429. The fix is smaller queries, not a bigger quota.

## Edge cases

- Some clients retry 429s automatically, which just burns more tokens; narrow the query instead.
- Filtering by path is the biggest win because it drops unrelated diffs.
- If you need the whole history, script it outside the MCP call.

---

Source: [Vectle](https://vectle.com/skills/skl_jozLX-leOSjIRiWsM0TbDg). Version: `skv_orhEmhWRvhr3bFGlEQodrQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
