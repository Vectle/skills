---
name: "access-token-not-provided-supabase-cli-ca1808c3adfee334"
description: "Fixes Supabase CLI commands failing with Access token not provided. Use when remote commands like projects list, functions deploy, or db push fail because the CLI has no login session \u2014 common in CI, containers, and fresh machines. Authenticates with supabase login or the SUPABASE_ACCESS_TOKEN env var. Not for project-not-linked errors or local Docker issues."
metadata:
  skill_id: "skl_mYXDPkfv7zezzSDwW5WK1A"
  title: "Access token not provided (Supabase CLI)"
  version: "skv_VF76MEtOLEkGKc8-5Ho6hA"
  updated: "2026-10-03T04:47:25.766573+00:00"
  canonical_url: "https://vectle.com/skills/skl_mYXDPkfv7zezzSDwW5WK1A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/g-vega-cl/llm-market-bench/blob/HEAD/supabase/TYPE_GENERATION.md\"]"
---

# Access token not provided (Supabase CLI)

TL;DR: the CLI is not logged in. Run `supabase login` and approve in the browser, or on a headless box create a personal access token in the Supabase dashboard and set SUPABASE_ACCESS_TOKEN. Then `supabase projects list` should work.

```text
Access token not provided
```

## Steps

1. Confirm:

```bash
supabase projects list
```

Expected on success: your projects listed. `Access token not provided` means there is no session.

2. Interactive fix:

```bash
supabase login
```

Expected: browser opens; after you approve, the CLI prints success and stores the session.

3. Headless or CI fix: Supabase dashboard → Account → Access Tokens → Generate new token. Then make it available as SUPABASE_ACCESS_TOKEN in the environment (in CI, store it as a secret).

4. Verify:

```bash
supabase projects list
```

Expected: returns your projects.

## When this applies

- the exact error on remote commands like projects list, functions deploy, db push
- CI pipelines, containers, and fresh machines with no prior login
- after `supabase logout`

## When it doesnt

- `Cannot find project ref. Have you run supabase link?` — linking problem, auth is fine
- `supabase start` Docker failures — that is Docker, not auth

## Compatibility

Supabase CLI 1.x and 2.x.

## Why it happens

Remote CLI commands need a personal access token. `supabase login` stores one locally; without it (or the env var) the CLI refuses to guess and errors immediately instead of failing later with something cryptic.

## Edge cases

- the stored session lives under ~/.supabase — wiping home or running as another user logs you out
- some commands take a different auth path than others, so keep SUPABASE_ACCESS_TOKEN set in scripts rather than relying on the stored session alone

## Find this skill again

```bash
curl -s 'https://vectle.com/api/v1/search?q=supabase+access+token+not+provided+login'
```


---

Source: [Vectle](https://vectle.com/skills/skl_mYXDPkfv7zezzSDwW5WK1A). Version: `skv_VF76MEtOLEkGKc8-5Ho6hA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
