---
name: "1password-passkey-causes-illegal-invoc-7e2dcacf6eedbd18"
description: "Explains the 'Illegal invocation' error when registering a FIDO2 credential with a 1Password passkey - it is an upstream 1Password bug (their Chrome extension intercepts the WebAuthn call), exposed after Chrome 129 added PublicKeyCredential features. Use when the error appears only with 1Password passkeys. Not for other WebAuthn errors."
metadata:
  skill_id: "skl_UATszmGCJs3fg3x2A_GFuw"
  title: "1Password passkey causes Illegal Invocation error"
  version: "skv_A0EubVRz8iV7GzBsHaaRQQ"
  updated: "2026-10-03T04:23:59.730963+00:00"
  canonical_url: "https://vectle.com/skills/skl_UATszmGCJs3fg3x2A_GFuw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/aws-samples/amazon-cognito-passwordless-auth/issues/94\"]"
---

## TL;DR

This is an upstream 1Password bug, not your library: the 1Password Chrome extension intercepts the WebAuthn call and replaces it with its own implementation, which throws `Illegal invocation`. Chrome 129 added PublicKeyCredential features that exposed the incompatibility. Track the 1Password fix; as a workaround, register the passkey without the 1Password extension intercepting.

## The error

```text
Uncaught TypeError: Illegal invocation
```

Shown in the UI when registering a FIDO2 credential with a 1Password passkey, at the `navigator.credentials.create` / WebAuthn call in the client code.

## Fix it

1. Confirm the scope: the error happens only when the 1Password passkey flow is used, not with platform authenticators.
   Success check: other passkey providers register fine.

2. Workaround: disable the 1Password extension's passkey interception (or use a different browser/profile) and retry registration.
   Success check: registration completes with no Illegal invocation.

3. Track the upstream 1Password fix for full resolution.
   Success check: re-enable the extension after the fix and registration works.

## When this applies

- `Illegal invocation` on FIDO2 credential registration with 1Password passkeys.
- Chrome 129+.

## When it does not apply

- Other authenticators fail too; that is a problem in your WebAuthn code.
- Different WebAuthn errors (NotAllowedError, InvalidStateError).
- The error occurs outside credential registration.

## Compatibility

- Chrome 129+ (PublicKeyCredential additions exposed the bug). 1Password Chrome extension passkey implementation.
- Library: amazon-cognito-passwordless-auth client (fido2.ts).

## Variant phrasings

- 1Password passkey Illegal invocation
- Uncaught TypeError Illegal invocation webauthn
- fido2 register Illegal invocation 1password

## Why it happens

The 1Password extension replaces the native WebAuthn implementation with its own. Its replacement does not handle the newer PublicKeyCredential surface Chrome 129 added, so the call throws `Illegal invocation` instead of completing.

## Edge cases

- Users on older Chrome may not hit it; the incompatibility is version-specific.
- Source: https://github.com/aws-samples/amazon-cognito-passwordless-auth/issues/94


---

Source: [Vectle](https://vectle.com/skills/skl_UATszmGCJs3fg3x2A_GFuw). Version: `skv_A0EubVRz8iV7GzBsHaaRQQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
