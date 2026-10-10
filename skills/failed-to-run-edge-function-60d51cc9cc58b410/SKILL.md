---
name: "failed-to-run-edge-function-60d51cc9cc58b410"
description: "Failed to run Edge Function: My bad, it was my mistake. Use when hitting this exact issue. Not for unrelated errors."
metadata:
  skill_id: "skl_V-fc3ptkk-Y7ypo5O6O61Q"
  title: "Failed to run Edge Function"
  version: "skv_ZAvFMDzdzg7bEhA8onSQeA"
  updated: "2026-10-03T18:22:43.791401+00:00"
  canonical_url: "https://vectle.com/skills/skl_V-fc3ptkk-Y7ypo5O6O61Q"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

E.g ```json { "imports": { "xata": "./src/xata.ts" } } ``` Then add the import_map path to `netlify.toml`. E.g ```diff + import { XataClient } from 'xata'; - import { XataClient } from '../../src/xata'; const xata = new XataClient({ apiKey - Netlify.env.get('XATA_API_KEY'), branch: Netlify.env.get('XATA_BRANCH'), }); export default async function handler() { try { const { records } = await xata.sql`SELECT * FROM users`; return new Response(JSON.stringify({ message: 'A-Ok!', data records }, null, 2), { status: 200, headers: { 'content-type': 'application/json' }, }); } catch (error) { return new Response({ status: 500, headers: { 'content-type': 'application/json' }, }); } } export const config = { path: '/get-all-users' }; ``` Works like a charm! My bad, it was my mistake.

## The error

```text
Failed to run Edge Function
```

[reporter PaulieScanlon]: My bad, it was my mistake. Here's how i solved it [edge-functions/api/#import-maps](https://docs.netlify.com/edge-functions/api/#import-maps) At the root of my project i created a `deno.json`. E.g ```json { "imports": { "xata": "./src/xata.ts" } } ``` Then add the import_map path to `netlify.toml`. E.g ```toml [functions] deno_import_map = "deno.json" ``` Then i changed the import in my edge function. E.g ```diff + import { XataClient } from 'xata'; - import { XataClient } from '../../src/xata'; const xata = new XataClient({ apiKey - Netlify.env.get('XATA_API_KEY'), branch: Netlify.env.get('XATA_BRANCH'), }); export default async function handler() { try { const { records } = await xata.sql`SELECT * FROM users`; return new Response(JSON.stringify({ message: 'A-Ok!', data records }, null, 2), { status: 200, headers: { 'content-type': 'application/json' }, }); } catch (error) { return new Response({ status: 500, headers: { 'content-type': 'application/json' }, }); } } export const config = { path: '/get-all-users' }; ``` Works like a charm!

Context: Issue xataio/client-ts#1437 (closed, 8 comments): **Describe the bug** Hi all, not sure if this is a Xata thing, or a Netlify thing but, i'm trying to use Xata with Netlify Edge Functions. E.g ```typescript import { XataClient } from '../../src/xata'; const xata = new XataClient({ apiKey - Netlify.env.get('XATA_API_KEY'), branch: Netlify.env.get('XATA_BRANCH'), }); export default async function handler() { try { const { records } = await xata.sql`SELECT * FROM users`; return new Response(JSON.stringify({ message: 'A-Ok!', data records }, null, 2), { status: 200, headers: { 'content-type': 'ap

## Matched source
Source: GitHub issue: https://github.com/xataio/client-ts/issues/1437
Original query: "Failed to run Edge Function"
Key terms: edge, failed, function

## When to use

- You hit this exact issue.
- The symptom matches: Failed to run Edge Function.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

GitHub issue: https://github.com/xataio/client-ts/issues/1437

---

Source: [Vectle](https://vectle.com/skills/skl_V-fc3ptkk-Y7ypo5O6O61Q). Version: `skv_ZAvFMDzdzg7bEhA8onSQeA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
