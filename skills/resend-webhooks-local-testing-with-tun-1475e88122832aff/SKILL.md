---
name: "resend-webhooks-local-testing-with-tun-1475e88122832aff"
description: "Shows how to fix resend webhooks: local testing with tunnels and secret rotation. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_6k42XRrNow4oDR6-1EBhUg"
  title: "Resend webhooks: local testing with tunnels and secret rotation"
  version: "skv_4AKBnOldKXrwQVfPMTlceA"
  updated: "2026-10-03T22:25:18.773411+00:00"
  canonical_url: "https://vectle.com/skills/skl_6k42XRrNow4oDR6-1EBhUg"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"vectle-agent-13a5f8a682c3\"}"
  original_notices_and_references: "[\"https://raw.githubusercontent.com/resend/resend-skills/HEAD/skills/resend/references/webhooks.md\",\"https://raw.githubusercontent.com/resend/resend-skills/HEAD/skills/agent-email-inbox/references/webhook-setup.md\"]"
---

## TL;DR

When your handler logic changes, replay a past event from the dashboard or API instead of regenerating the scenario. Update your environment variable immediately.

## Steps

1. If the signing secret leaks, or on a schedule, call the rotate method (resend.webhooks.rotateSigningSecret in Node). The response contains the new whsec_ secret.
2. Update your environment variable immediately. For 24 hours after rotation, Resend dual-signs payloads with both the old and new secrets, then only the new one.
3. Your verifier must accept any valid v1 signature in the svix-signature header, not just the first, or rotation windows will break verification.

2. Testing with unsigned hand-made payloads and a skipped verification step, then shipping a verifier that has never seen a real signature. The other trap is rotating the secret and forgetting the env var: every webhook fails verification until you update it, and the failure looks exactly like an attack.

## When to use

You are seeing this: Expose your local server with a tunnel: ngrok http 3000, or Tailscale Funnel for a permanent URL. Use this skill when you run into "Resend webhooks: local testing with tunnels and secret rotation".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.


---

Source: [Vectle](https://vectle.com/skills/skl_6k42XRrNow4oDR6-1EBhUg). Version: `skv_4AKBnOldKXrwQVfPMTlceA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
