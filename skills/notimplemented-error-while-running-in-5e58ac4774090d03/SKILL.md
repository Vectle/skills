---
name: "notimplemented-error-while-running-in-5e58ac4774090d03"
description: "Fixes the NotImplementedError crash when running scrapegraphai (SmartScraperGraph, SearchGraph) on Windows by applying nest_asyncio before running. Use when a scraper dies with an asyncio error on Windows. Not for Linux or macOS asyncio issues, or for scrapers that dont use scrapegraphai."
metadata:
  skill_id: "skl_J0vhct48mT90kFp-G92sMw"
  title: "NotImplemented error while running in windows."
  version: "skv_QiWRf0EK7P_Aj4hrOQw1dg"
  updated: "2026-10-03T04:37:58.613092+00:00"
  canonical_url: "https://vectle.com/skills/skl_J0vhct48mT90kFp-G92sMw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

Fix first: apply nest_asyncio before you create the scraper graph. On Windows this is the fix; notebook users confirmed it.

```text
Uncaught app exception ... NotImplementedError
```

1. At the top of your notebook or script, before creating the graph, add:

```python
import nest_asyncio
nest_asyncio.apply()
```

Expected: the scraper runs instead of crashing with NotImplementedError.

When to use: SmartScraperGraph or SearchGraph crash with NotImplementedError on Windows.

When not to use: the same crash on Linux or macOS (different cause there), or scrapers that dont use scrapegraphai.

Compatibility: scrapegraphai, Windows, Python notebooks and scripts.

Variants:
- "scrapegraphai windows NotImplementedError"
- "SmartScraperGraph uncaught app exception windows"
- "nest_asyncio scrapegraphai"

Root cause: Windows defaults to the Proactor event loop, which scrapegraphai's asyncio usage does not handle.

Edge cases: nest_asyncio has to be applied before the graph is created. Applying it after the crash wont help.

---

Source: [Vectle](https://vectle.com/skills/skl_J0vhct48mT90kFp-G92sMw). Version: `skv_QiWRf0EK7P_Aj4hrOQw1dg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
