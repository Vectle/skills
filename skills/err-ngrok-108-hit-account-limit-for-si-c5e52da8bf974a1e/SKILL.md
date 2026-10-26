---
name: "err-ngrok-108-hit-account-limit-for-si-c5e52da8bf974a1e"
description: "Fixes ngrok failing with ERR_NGROK_108 when another agent session is already online on the account. Use when the free plan's single-session limit is hit by a stale agent on another machine. Covers finding and stopping the extra session. Not for invalid authtokens or tunnel-not-found errors."
metadata:
  skill_id: "skl_0zDuLDDV2TFOfDajxQlPAw"
  title: "ERR_NGROK_108: hit account limit for simultaneous ngrok agent sessions"
  version: "skv_4bWHPQNXHdzqhebXg7b6Iw"
  updated: "2026-10-03T06:11:55.633311+00:00"
  canonical_url: "https://vectle.com/skills/skl_0zDuLDDV2TFOfDajxQlPAw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://ngrok.com/docs/errors\"]"
---

# ERR_NGROK_108: hit account limit for simultaneous ngrok agent sessions

TL;DR: another ngrok agent is already online on this account, and the free plan allows one at a time. Stop the other agent — kill stray `ngrok` processes on your other machines, or end the session in the ngrok dashboard — then retry.

```text
ERR_NGROK_108
```

## Steps

1. Find the extra session. In the ngrok dashboard, open the agents page and look for sessions you do not recognize or no longer need.

2. Stop it there, or kill local strays on each machine:

```bash
pkill ngrok
```

Expected: `pgrep ngrok` returns nothing.

3. Start your tunnel again:

```bash
ngrok http 3000
```

Expected: the session panel shows online with no 108.

## When this applies

- the exact 108 error on agent start
- you recently ran ngrok on another machine, a CI job, or a Colab notebook
- a crashed agent left a session the edge still counts as online

## When it doesnt

- `ERR_NGROK_4018` — that is an invalid or unverified authtoken
- `ERR_NGROK_6022` — no authtoken installed at all
- `ERR_NGROK_3200` — tunnel not found, the agent side is fine

## Compatibility

ngrok v2 and v3 agent, all plans (the limit just differs by plan).

## Other phrasings

- `ngrok 108 simultaneous session limit`
- `You have hit your account limit for simultaneous ngrok agent sessions`

## Why it happens

ngrok counts online agent sessions per account. A second agent start is rejected at the edge before any tunnel is built, so nothing about your command is wrong — it is purely the concurrency cap.

## Edge cases

- Sessions can linger a few minutes after a crash; wait briefly before retrying.
- If this happens constantly, one persistent agent plus TCP multiplexing beats many agents.
- Upgrading the plan raises the cap instead of forcing you to hunt sessions.


---

Source: [Vectle](https://vectle.com/skills/skl_0zDuLDDV2TFOfDajxQlPAw). Version: `skv_4bWHPQNXHdzqhebXg7b6Iw`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
