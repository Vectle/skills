---
name: "apify-mcp-actor-run-failed-read-the-st-c8c0d6ca85772a02"
description: "Fixes confusion when Apify Actor runs report FAILED with no obvious cause in the MCP client. Covers where the real error lives (the run's statusMessage), the common causes it names (input validation, proxy blocks, timeouts), and how to fetch it. Not for auth or Actor-resolution errors."
metadata:
  skill_id: "skl_AbhRD_calo24PLnRZf2s-g"
  title: "Apify MCP: Actor run FAILED (read the statusMessage for the real reason)"
  version: "skv_dTU3NjRjjbl3r2xTUF6ltw"
  updated: "2026-10-03T06:09:00.36534+00:00"
  canonical_url: "https://vectle.com/skills/skl_AbhRD_calo24PLnRZf2s-g"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://docs.apify.com/api/v2#/reference/actors/run-collection\"]"
---

Read the run's statusMessage. The MCP client shows FAILED but not why; the Apify run object carries a statusMessage field with the actual reason (bad input, proxy failure, out of memory, timeout). Open the run in the Console or fetch it via API and the message tells you what to fix.

```text
Run FAILED
```

## The fix

1. Find the run ID from the failed tool call output.
2. Open it: `https://console.apify.com/actors/runs/[run ID]` or fetch the run via API.
   Expected: the run detail page loads.
3. Read statusMessage (and the run log tail).
   Expected: a concrete reason, e.g. input failed validation, proxy blocked, memory limit.
4. Fix what it names: correct the input JSON, enable better proxies, raise memory, then re-run.
   Expected: the next run succeeds.

## When this applies

- The Actor resolves and starts, then the run ends FAILED.
- Retrying the identical call fails identically (deterministic, not flaky infra).

## When it does NOT apply

- The Actor never starts: resolution/auth problem, different skill.
- Run stays RUNNING forever: it is stuck, not failed; check timeouts.

## Tool and version compatibility

- All Apify Actors via the MCP server or API; statusMessage is platform-wide.

## Variant phrasings

### Apify run failed with no error message
The message exists, just not in the MCP output. Look at the run object.

### Actor run keeps failing
Read one statusMessage fully before retrying; blind retries of the same input fail the same way.

## Why it happens

The MCP tool surfaces the run's terminal status, not its diagnostics. Apify records the failure reason on the run for the Console, so the two views disagree in detail level by design.

## Edge cases

- Input validation failures name the exact field; fix the JSON you pass, not the Actor.
- Proxy-blocked runs suggest residential proxies or the Actor's built-in proxy settings.
- Out-of-memory FAILED: raise the run's memory in the input or Actor configuration and retry.


---

Source: [Vectle](https://vectle.com/skills/skl_AbhRD_calo24PLnRZf2s-g). Version: `skv_dTU3NjRjjbl3r2xTUF6ltw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
