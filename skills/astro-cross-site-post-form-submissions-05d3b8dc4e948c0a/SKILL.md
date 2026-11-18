---
name: "astro-cross-site-post-form-submissions-05d3b8dc4e948c0a"
description: "astro cross site post form submissions forbidden after deploy error"
metadata:
  skill_id: "skl_f2h0saN-8zUIUeH2Qljkdw"
  title: "astro cross site post form submissions forbidden after deploy error"
  version: "skv_xQIuFEiy5V7CsvvAoZKoHQ"
  updated: "2026-11-18T01:53:23.122896+00:00"
  canonical_url: "https://vectle.com/skills/skl_f2h0saN-8zUIUeH2Qljkdw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Reproduce the form post on the deployed site, not on a local dev server, and note the exact page URL and form action URL.

Check the configured site URL in the Astro config and compare it with the live deployed domain, including www versus bare domain.

If the app sits behind a proxy or a platform router, check whether the original host and protocol are forwarded to the server.

Redeploy after fixing the config or the proxy forwarding, then submit the form again in a fresh browser session.

Only if the form must accept posts from another origin, disable the built-in origin check in the server config and add your own CSRF token check in the handler.

---

Source: [Vectle](https://vectle.com/skills/skl_f2h0saN-8zUIUeH2Qljkdw). Version: `skv_xQIuFEiy5V7CsvvAoZKoHQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
