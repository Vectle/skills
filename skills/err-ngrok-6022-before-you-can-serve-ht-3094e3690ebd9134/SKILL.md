---
name: "err-ngrok-6022-before-you-can-serve-ht-3094e3690ebd9134"
description: "Fixes ngrok showing ERR_NGROK_6022 when serving browser pages without an account and authtoken. Use on first runs and fresh machines where no authtoken was ever installed. Covers signing up and installing the token with ngrok config add-authtoken. Not for expired tokens or session limits."
metadata:
  skill_id: "skl_PW3QdTJbZHvlEC_PogW7BA"
  title: "ERR_NGROK_6022: before you can serve HTML content"
  version: "skv_v02ypYKqW9gr-Yep_9bLnQ"
  updated: "2026-10-03T06:12:55.198831+00:00"
  canonical_url: "https://vectle.com/skills/skl_PW3QdTJbZHvlEC_PogW7BA"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://ngrok.com/docs/errors/err_ngrok_6022/\"]"
---

# ERR_NGROK_6022: before you can serve HTML content

TL;DR: ngrok will not serve browser pages until you sign up for a free account and install your authtoken. Grab the token from the ngrok dashboard, run `ngrok config add-authtoken [your token]`, then restart the tunnel.

```text
Before you can serve HTML content, you must sign up for an ngrok account and install your authtoken.

ERR_NGROK_6022
```

## Steps

1. Sign up at the ngrok dashboard and open the authtoken page.

Expected: a page showing your personal authtoken.

2. Install it:

```bash
ngrok config add-authtoken [your token]
```

Expected: `Authtoken saved to configuration file`.

3. Restart the tunnel:

```bash
ngrok http 3000
```

Expected: the forwarding URL loads your app in the browser instead of the 6022 page.

## When this applies

- first run on a new machine or container
- CI images that install ngrok but never configure it
- the 6022 interstitial page in the browser when opening the forwarding URL

## When it doesnt

- `ERR_NGROK_4018` — a token is installed but invalid or the account is unverified
- `ERR_NGROK_108` — session limit, unrelated to tokens
- 6022 persisting after the token is installed — see the follow-up skill on that

## Compatibility

ngrok v2 and v3 agent.

## Other phrasings

- `ngrok error 6022`
- `must sign up for an ngrok account and install your authtoken`

## Why it happens

ngrok ended anonymous browser-facing tunnels. Serving HTML now requires an authtoken bound to an account, so the edge shows 6022 instead of your page until one is installed.

## Edge cases

- Headless setups can set NGROK_AUTHTOKEN in the environment instead of writing the config file.
- After installing the token you must restart the agent; the running session keeps the old state.
- The first browser visit still shows a warning interstitial on free plans; click through it.


---

Source: [Vectle](https://vectle.com/skills/skl_PW3QdTJbZHvlEC_PogW7BA). Version: `skv_v02ypYKqW9gr-Yep_9bLnQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
