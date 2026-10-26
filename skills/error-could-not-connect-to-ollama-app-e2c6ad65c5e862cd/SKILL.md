---
name: "error-could-not-connect-to-ollama-app-e2c6ad65c5e862cd"
description: "Fixes the Ollama CLI answering Error: could not connect to ollama app, is it running? Use when ollama list, ollama pull, or ollama run fail because the Ollama daemon is not running or the CLI points at the wrong host. Starts the server with ollama serve and checks OLLAMA_HOST. Not for model-not-found errors, which need ollama pull, or out-of-memory errors."
metadata:
  skill_id: "skl_1zo0UJTXEZQwlLhnAeFHTw"
  title: "Error: could not connect to ollama app, is it running?"
  version: "skv_bBpbm8WAOpZd0967WoKsZQ"
  updated: "2026-10-03T04:48:07.932096+00:00"
  canonical_url: "https://vectle.com/skills/skl_1zo0UJTXEZQwlLhnAeFHTw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/jvdbreemen/llmwiki-kennisbank/blob/HEAD/TROUBLESHOOTING.md\"]"
---

# Error: could not connect to ollama app, is it running?

TL;DR: the Ollama server is not running. Start it with `ollama serve` (in the background if you want your terminal back), then run `ollama list` — if it lists models instead of erroring, you are fixed. If the server runs on another machine or port, point the CLI at it with OLLAMA_HOST.

```text
Error: could not connect to ollama app, is it running?
```

## Steps

1. Check whether the daemon answers:

```bash
ollama list
```

If it errors, the server is down or unreachable.

2. Start it:

```bash
ollama serve
```

Expected: logs show it listening. Run it in the background or as a service so it survives the terminal.

3. Verify:

```bash
ollama list
```

Expected: your pulled models listed, no error.

4. Server on another machine or a custom port: set OLLAMA_HOST to the server address before running CLI commands, and bind the server to the all-interfaces address instead of loopback so other machines can reach it.

## When this applies

- the exact error on `ollama list`, `ollama pull`, or `ollama run`
- fresh installs where the app was installed but never launched
- after a reboot when the service didnt start

## When it doesnt

- `Error: model "..." not found` — run `ollama pull [model]`; the server is fine
- out-of-memory or CUDA errors — the server runs but the model doesnt fit
- connection refused from another machine while local works — bind address or firewall (see step 4)

## Compatibility

Ollama 0.x CLI and server, macOS, Linux, Windows.

## Why it happens

The `ollama` CLI is a thin client: every command is an HTTP call to the server. No server, no client — and the CLI does not auto-start the daemon.

## Edge cases

- on macOS the Ollama.app also starts the daemon; pick one launcher, not both
- only one server can own the port — a second `ollama serve` fails to bind
- containers reach a host server through the host gateway, not loopback

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=ollama+error+could+not+connect+is+it+running'
```


---

Source: [Vectle](https://vectle.com/skills/skl_1zo0UJTXEZQwlLhnAeFHTw). Version: `skv_bBpbm8WAOpZd0967WoKsZQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
