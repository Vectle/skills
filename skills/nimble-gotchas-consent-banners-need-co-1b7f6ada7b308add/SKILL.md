---
name: "nimble-gotchas-consent-banners-need-co-1b7f6ada7b308add"
description: "Nimble gotchas: consent banners need --consent-header, sign-in pages are not render problems, crawl is HTML-only: Three Nimble landmines worth knowing before you script. Use when hitting this exact issue with Nimble gotchas. Not for unrelated errors."
metadata:
  skill_id: "skl_SBifUBl50RVg_1q8W2By4w"
  title: "Nimble gotchas: consent banners need --consent-header, sign-in pages are not render problems, crawl is HTML-only"
  version: "skv_D5FEk-PhVv1iIa39JtXYOg"
  updated: "2026-10-03T20:05:09.938699+00:00"
  canonical_url: "https://vectle.com/skills/skl_SBifUBl50RVg_1q8W2By4w"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

One: cookie consent banners block first-load content - pass --consent-header to auto-handle them instead of extracting a banner. Two: if extract returns a sign-in page, the site needs a login - do not escalate the render tier at an access barrier, use public search results instead (and for LinkedIn/X profiles specifically, --focus social is the supported route; extract just gives status 999). Three Nimble landmines worth knowing before you script.

Three Nimble landmines worth knowing before you script. One: cookie consent banners block first-load content - pass --consent-header to auto-handle them instead of extracting a banner. Two: if extract returns a sign-in page, the site needs a login - do not escalate the render tier at an access barrier, use public search results instead (and for LinkedIn/X profiles specifically, --focus social is the supported route; extract just gives status 999). Three: crawl output is raw HTML with no markdown option - pipe it through map plus extract --format markdown to get something an LLM can actually use.

Context: Nimble's own error-handling reference: known site limitations that trip agents. Cookie consent banners block content on first load - add --consent-header to auto-handle consent dialogs. Sites requiring a sign-in: extract returns the site's own sign-in page, not the target - report it and use public search results instead; never escalate the render tier at an access barrier. LinkedIn and X profile pages are not available to extract (status 999) - use --focus social search instead. Crawl results return raw HTML (60-115KB per page) with no markdown option - use map plus extract --format markdown for LLM-friendly output.

## Matched source
Source: Source: https://github.com/nimbleway/agent-skills/blob/HEAD/skills/nimble-web-expert/references/error-handling.md
Original query: "Nimble gotchas: consent banners need --consent-header, sign-in pages are not render problems, crawl is HTML-only"
Key terms: banners, consent, crawl, gotchas, header, html, need, nimble, only, pages, problems, render

## When to use

- You hit this exact issue with Nimble gotchas.
- The symptom matches: consent banners need --consent-header, sign-in pages are not render problems, crawl is HTML-only.

## When NOT to use

- A different error or symptom from Nimble gotchas; the cause here is specific to this one.

## Compatibility

Reported against Nimble gotchas.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://github.com/nimbleway/agent-skills/blob/HEAD/skills/nimble-web-expert/references/error-handling.md

---

Source: [Vectle](https://vectle.com/skills/skl_SBifUBl50RVg_1q8W2By4w). Version: `skv_D5FEk-PhVv1iIa39JtXYOg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
