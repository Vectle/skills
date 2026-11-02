---
name: "depth-zero-self-signed-cert-18a42bad0e3e76d4"
description: "depth_zero_self_signed_cert"
metadata:
  skill_id: "skl_9ov2u8zknUjhNiufHkSJlQ"
  title: "depth_zero_self_signed_cert"
  version: "skv_RZ4_qtghhM1c_RixFngBIQ"
  updated: "2026-11-02T16:10:27.340909+00:00"
  canonical_url: "https://vectle.com/skills/skl_9ov2u8zknUjhNiufHkSJlQ"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Confirm what the server is really presenting with `openssl s_client -connect HOST:PORT -servername HOST` and read the issuer and subject lines. Expected: issuer and subject are the same name, which proves the certificate is self-signed and this is a trust problem, not an expiry or hostname problem.

Save the certificate (or the private CA certificate that issued your dev servers) as a PEM file, meaning it contains a BEGIN CERTIFICATE block, and start Node with the NODE_EXTRA_CA_CERTS variable pointing at that file. Expected: the same request now succeeds with verification still on. Note the variable is read once at startup, so restart the process after setting it.

For a single call site, pass the certificate in code instead: give the https or fetch client the ca option with the PEM contents for that host. Expected: only that connection trusts the extra certificate and the rest of the app is unchanged.

On current Node versions (22.15 and later), `node --use-system-ca` can use a certificate your OS already trusts, which covers the case where IT installed the company CA in the system store but Node kept using its bundled store. Expected: the error clears without an extra file.

Development-only last resort: set the NODE_TLS_REJECT_UNAUTHORIZED variable to 0. This disables certificate verification for the whole process and removes the protection TLS exists for, so never ship it, never set it in CI that touches real services, and remove it as soon as step 2 works. Expected: connections succeed with no verification at all, which is exactly why it is dangerous.

---

Source: [Vectle](https://vectle.com/skills/skl_9ov2u8zknUjhNiufHkSJlQ). Version: `skv_RZ4_qtghhM1c_RixFngBIQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
