---
name: "err-ngrok-4018-ngrok-authentication-fa-6db8db6a6229a919"
description: "Fixes ngrok failing to start with ERR_NGROK_4018 authentication failed: Usage of ngrok requires a verified account and authtoken. Use when the authtoken is missing, wrong, or the account email is not verified. Installs the token with ngrok config add-authtoken. Not for session limit errors or tunnel-not-found errors."
metadata:
  skill_id: "skl_x5OR_4E51s14O7-Xqad_Dw"
  title: "ERR_NGROK_4018: ngrok authentication failed"
  version: "skv_v-BPoTJBzOWV3nrXHStInA"
  updated: "2026-10-03T04:46:43.385151+00:00"
  canonical_url: "https://vectle.com/skills/skl_x5OR_4E51s14O7-Xqad_Dw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# ERR_NGROK_4018: ngrok authentication failed

TL;DR: ngrok has no idea who you are. Grab your authtoken from the ngrok dashboard and run `ngrok config add-authtoken [your token]`. If it still 4018s after that, your account email is not verified — verify it, then retry.

```text
ERROR:  authentication failed: Usage of ngrok requires a verified account and authtoken.

ERROR:  Sign up for an account: https://dashboard.ngrok.com/signup
ERROR:  Install your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken

ERROR:  ERR_NGROK_4018
```

## Steps

1. Find your authtoken at the top of the ngrok dashboard setup page.

2. Install it:

```bash
ngrok config add-authtoken [your authtoken]
```

Expected: `Authtoken saved to configuration file: [path]/ngrok.yml`.

3. Start the tunnel:

```bash
ngrok http 3000
```

Expected: the session panel shows `account` with your email and no 4018.

4. Headless or CI alternative: set NGROK_AUTHTOKEN in the environment instead of writing the config file — ngrok picks it up natively.

## When this applies

- the exact 4018 error on startup
- first run on a new machine, or CI where the config file wasnt carried over
- authtoken rotated in the dashboard and the saved one is stale

## When it doesnt

- `ERR_NGROK_322` — the free tier allows one simultaneous session; stop the other one
- tunnels that start then die — that is the app behind the tunnel, not auth

## Compatibility

ngrok v2 and v3 CLI.

## Why it happens

ngrok ended anonymous tunnels: every agent session must present an authtoken bound to a verified account. The CLI reads it from ngrok.yml or the NGROK_AUTHTOKEN env var — if both are absent, wrong, or the account is unverified, the edge rejects the session with 4018.

## Edge cases

- config file location differs per OS (~/.config/ngrok/ngrok.yml on Linux)
- rotating the token in the dashboard invalidates the saved one — re-run add-authtoken afterwards
- in Docker, bake NGROK_AUTHTOKEN into the container env, not into the image

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=ngrok+ERR_NGROK_4018+authentication+failed'
```


---

Source: [Vectle](https://vectle.com/skills/skl_x5OR_4E51s14O7-Xqad_Dw). Version: `skv_v-BPoTJBzOWV3nrXHStInA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
