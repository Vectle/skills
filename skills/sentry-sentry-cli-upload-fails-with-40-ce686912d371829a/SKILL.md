---
name: "sentry-sentry-cli-upload-fails-with-40-ce686912d371829a"
description: "Shows how to fix sentry: sentry-cli upload fails with 401. Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_KIHUYWkHVSNNI1v4fiaLTw"
  title: "Sentry: sentry-cli upload fails with 401"
  version: "skv_1By6EVymdLunoi_yCMWZ1w"
  updated: "2026-10-04T05:08:51.912495+00:00"
  canonical_url: "https://vectle.com/skills/skl_KIHUYWkHVSNNI1v4fiaLTw"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

## TL;DR

Keep one token per use case so the next rotation is surgical. If uploads broke months after setup with no config change, check whether the token owner is still in the org. Org tokens have a fixed limited permission set; if the command needs more (e.g. creating projects), use an internal integration token. `` sentry-cli info ` This prints the connected installation and auth state.

## When to use

You are seeing this: sentry-cli sourcemaps upload (or releases, or deploys) fails with error: API request failed and a 401 status. Use this skill when you run into "Sentry: sentry-cli upload fails with 401".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## The error

`sentry-cli sourcemaps upload` (or releases, or deploys) fails with `error: API request failed` and a 401 status. The CLI cannot authenticate.

## Causes, in order

1. **Token expired or revoked.** Org tokens are visible only once; if it was rotated or revoked after a security email, the CI secret is stale.
2. **Wrong token type for the job.** Personal tokens die when the user leaves the org. If uploads broke months after setup with no config change, check whether the token owner is still in the org. Prefer organization tokens for CI.
3. **Token pasted with whitespace or truncated.** CI secret values with a trailing newline are a classic. Re-copy carefully.
4. **Wrong Sentry host.** The CLI defaults to sentry.io; self-hosted needs `SENTRY_URL` set. A 401 against the wrong host is really a not-found wearing a 401 costume.
5. **Missing scope.** Org tokens have a fixed limited permission set; if the command needs more (e.g. creating projects), use an internal integration token.

## Confirmation

```
sentry-cli info
```

This prints the connected installation and auth state. If it 401s, the token or URL is wrong, full stop. Also verify scoping: `SENTRY_ORG` and `SENTRY_PROJECT` (or `--org`/`--project`) point at the org and project you intend.

## Fix and verify

Create a fresh organization token (Settings > Developer Settings > Organization Tokens), store it as the `SENTRY_AUTH_TOKEN` CI secret, and re-run `sentry-cli info` until it prints 200-level success. Then re-run the upload. Keep one token per use case so the next rotation is surgical.


---

Source: [Vectle](https://vectle.com/skills/skl_KIHUYWkHVSNNI1v4fiaLTw). Version: `skv_1By6EVymdLunoi_yCMWZ1w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
