---
name: "playwright-mcp-browser-closed-after-id-b7016033002e624a"
description: "Fixes Playwright MCP closing the browser after an hour with no tool calls, so the next call fails. Use when long agent sessions hit browser-has-been-closed errors after idle periods. Not for the 0.0.73 launchApp regression."
metadata:
  skill_id: "skl_cyN2-E9vYtsmmYLa2SHhKw"
  title: "Playwright MCP: browser closed after idle timeout (set --idle-timeout)"
  version: "skv_HGv81x01rTxh8ecv9JEy2A"
  updated: "2026-10-03T06:11:44.266395+00:00"
  canonical_url: "https://vectle.com/skills/skl_cyN2-E9vYtsmmYLa2SHhKw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR
A headless browser launched by the server is closed after an hour without tool calls to save CPU; the next call then fails because there is no browser. Pass `--idle-timeout` (milliseconds) to raise it, or `0` to disable. Logins survive only if you also persist state, since `--isolated` memory state is lost on close.

## The error
```text
Target page, context or browser has been closed
```

## Fix it
1. **Add `--idle-timeout` to your MCP config args.** For a 5-minute window:
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "npx",
         "args": ["@playwright/mcp@latest", "--idle-timeout=300000"]
       }
     }
   }
   ```
   Use `0` to disable the timeout entirely.
   - Expected: valid JSON.
2. **Restart the client** and run a long session.
   - Expected: the browser stays up across idle gaps up to your timeout.
3. **If logins must survive**, also persist state: use a persistent profile or `--storage-state`, because with `--isolated` the in-memory cookies die with the browser anyway.
   - Expected: re-login not needed after idle closes.

## When to use
- Browser works, then after a long idle stretch the next tool call fails with browser-closed.
- Agent sessions span hours with gaps between browser actions.

## When NOT to use
- Browser dies between rapid successive calls on 0.0.73 - that is the launchApp regression, pin 0.0.72.
- Browser never launches - check the install.

## Compatibility
- @playwright/mcp with `--idle-timeout` support.

## Root cause
An animating page costs CPU as long as the browser is open, and agent sessions last hours. The server therefore reaps headless browsers after 60 minutes of no completed tool calls. Headed browsers and `--cdp-endpoint`/`--extension` attached browsers are never auto-closed; an explicit timeout on those only disconnects, leaving pages open.

## Edge cases
- The timer never fires mid-call; it only counts completed-call idle time.
- The next tool call after a close launches a fresh browser automatically, so the agent must navigate again.
- With `--shared-browser-context`, the timer spans all clients: the browser closes only once every client has been idle.


---

Source: [Vectle](https://vectle.com/skills/skl_cyN2-E9vYtsmmYLa2SHhKw). Version: `skv_HGv81x01rTxh8ecv9JEy2A`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
