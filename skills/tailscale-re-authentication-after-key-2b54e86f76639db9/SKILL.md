---
name: "tailscale-re-authentication-after-key-2b54e86f76639db9"
description: "Fixes Tailscale devices losing their ACL tags after the node key expires and the device is re-authenticated. Use when a tagged machine stops matching tag-based ACL rules right after you re-logged it in. Covers re-authenticating with a tagged auth key or the --tags flag so the tags survive. Not for tags missing on first enrollment or ACL rules that never matched."
metadata:
  skill_id: "skl_dhmI-x3h8cTn1qkSkaqxeQ"
  title: "Tailscale re-authentication after key expiry removes all tags (keep them)"
  version: "skv_4Z9mmKi0CIDXSF2UdfO-XA"
  updated: "2026-10-03T04:42:33.033588+00:00"
  canonical_url: "https://vectle.com/skills/skl_dhmI-x3h8cTn1qkSkaqxeQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# Fix Tailscale tags disappearing after key expiry re-authentication

**TL;DR:** Logging back in as a user makes the node user-owned, which drops its tags. Re-authenticate with a tagged auth key or `tailscale up --tags=tag:example` instead, and the tags survive.

## The error

```text
After key expiration, reauthentication removes all tags from the machine
```

Symptom level: the device was `tag:server`, you re-logged it in after expiry, and now ACL rules for `tag:server` no longer match it.

## Fix it

### 1. Confirm the tags are actually gone

Check the machine in the admin console. If the tags column is empty where it used to list tags, this is your bug.

### 2. Re-authenticate with tags attached

Option A, auth key with tags baked in (best for servers): generate an auth key that carries the tags, then pass it as the flag value:

```
sudo tailscale up --auth-key YOUR_KEY_HERE
```

Replace YOUR_KEY_HERE with the real key value.

Option B, pass tags directly:

```
sudo tailscale up --tags=tag:server
```

Expected: the machine reappears in the admin console WITH its tags.

### 3. Verify ACLs match again

Test the access the tags are supposed to grant (SSH, subnet, port).

Expected: tag-based rules work as before.

## When this applies

- Tags vanished right after re-authenticating an expired node
- You logged in interactively as a user (browser flow)
- macOS/iOS forced re-auth is a common trigger

## When it does not apply

- Tags were never assigned (first-enrollment problem)
- ACL rules never matched even with tags present (rule problem)
- You want user-owned nodes (then tag loss is expected behavior)

## Tool compatibility

All Tailscale clients. Tagged auth keys need an admin/owner to create them.

## Variant phrasings

### iOS forced re-authentication, then could not connect to anything

Same cause: the re-auth dropped the tags, so tag-scoped ACLs stopped matching. Re-tag and re-auth with the key.

## Why it happens

Tags live on the node identity created at auth time. Interactive user login creates a user-owned node with no tags. Only key-based auth (tagged key or `--tags`) stamps tags onto the new identity.

## Edge cases

- **Expiry is the trigger, not the bug:** with 24h key expiry policies this bites constantly. Automate re-auth with tagged keys instead of clicking through logins.
- **Disable expiry as a stopgap:** several reporters just disabled key expiry on affected devices to stop the cycle. That trades security for convenience; tagged-key automation is the better fix.
- **Key reuse:** make the auth key reusable if many machines share the tag set, or one-use per machine for tighter control.

---

Source: [Vectle](https://vectle.com/skills/skl_dhmI-x3h8cTn1qkSkaqxeQ). Version: `skv_4Z9mmKi0CIDXSF2UdfO-XA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
