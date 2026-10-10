---
name: "supabase-cli-cannot-find-project-ref-h-c0c178abe6c2fa7e"
description: "Fixes Supabase CLI commands failing with Cannot find project ref. Have you run supabase link? Use when db push, db pull, or functions commands fail because the project was never linked or the link config was lost. Runs supabase link (or re-links) to restore the project ref. Not for auth token errors during linking itself."
metadata:
  skill_id: "skl_h4srGc8JesYbYUIVn3Hu_A"
  title: "Supabase CLI: Cannot find project ref. Have you run supabase link?"
  version: "skv_xr57y375vRBcKIO677TJcQ"
  updated: "2026-10-03T05:42:03.599148+00:00"
  canonical_url: "https://vectle.com/skills/skl_h4srGc8JesYbYUIVn3Hu_A"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Supabase CLI: Cannot find project ref. Have you run supabase link?

TL;DR: the CLI does not know which remote project you mean. Link it once with `supabase link --project-ref [ref]` (find the ref in the dashboard URL), entering the database password when prompted. If it used to work, the link config was deleted or you are in a different directory: re-link. Unlink and re-link if the stored ref points at the wrong project.

```text
Cannot find project ref. Have you run supabase link?
```

## Steps

1. Run `supabase link --project-ref [ref]` using the ref from the project's dashboard URL. Enter the database password when prompted.

2. Confirm the link: check that the project config now records the ref, then rerun the failing command. Expected: it targets the linked project instead of erroring.

3. If it worked before, check you are in the same project directory — the link is per-directory. Re-link in the right directory if needed.

4. Wrong project linked: run `supabase unlink`, then link again with the correct ref.

## When this applies

- the exact `Cannot find project ref. Have you run supabase link?` message
- a fresh clone where nobody ran supabase link yet
- commands run from a different directory than the linked one

## When it doesn't

- `Authorization failed for the access token and project ref pair` — linking itself is failing, fix that
- database password rejections after a successful link
- dashboard-side project deletion (linking to a deleted ref fails differently)

## Compatibility

Supabase CLI supabase link/unlink; per-directory link config. Verified against the themehackers CLI unlink side-effects notes.

## Variant phrasings

- supabase cannot find project ref have you run supabase link
- supabase link project ref fix
- supabase cli not linked error

## Root cause

Most supabase commands resolve the remote project from local link state, not from arguments. With no link state there is no project ref to send, so the CLI aborts before doing anything.

## Edge cases

- the link is per working directory; monorepos need a link in each package that calls the CLI
- unlinking does not delete remote resources, it only clears local state
- CI should link once during setup, not on every command

---

Source: [Vectle](https://vectle.com/skills/skl_h4srGc8JesYbYUIVn3Hu_A). Version: `skv_xr57y375vRBcKIO677TJcQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
