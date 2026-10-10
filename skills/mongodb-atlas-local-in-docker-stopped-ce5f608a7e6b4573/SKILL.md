---
name: "mongodb-atlas-local-in-docker-stopped-ce5f608a7e6b4573"
description: "Mongodb atlas local in docker stopped working because of security keys: I found the solution to my issue. Use when hitting this exact issue. Not for unrelated errors."
metadata:
  skill_id: "skl_51v6xCBdNDpAIJMYho7Lfg"
  title: "Mongodb atlas local in docker stopped working because of security keys"
  version: "skv_7bTRBvhIGuVXttshhRJPBg"
  updated: "2026-10-03T05:40:49.838821+00:00"
  canonical_url: "https://vectle.com/skills/skl_51v6xCBdNDpAIJMYho7Lfg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

I found the solution to my issue. I needed to remove everything related to rancher desktop then re-install it. However, simply uninstall rancher desktop doesn't cut it.

I found the solution to my issue. I needed to remove everything related to rancher desktop then re-install it. However, simply uninstall rancher desktop doesn't cut it. You have to purge your computer from everything related to rancher desktop. It includes WSL distributions, you can list them with this command: wsl --list --all And unregister them with this command: wsl --unregister [distribution-name] You'll find folders related to rancher desktop in appdata/Local and appdata/Roaming . There are folders in Program Files and your user folder in mount the host path C at container path /Users . It is really a pain to find everything, rancher desktop uninstaller is completely useless. Once you made sure everything related to rancher is removed, you can re-install it and the permission issues in your containers should be gone. Good luck.

Context: I'm running mongodb/mongodb-atlas-local in Docker, I got the docker-compose from here . It used to work, but it suddenly stopped. I tried deleting every images and volumes and rebuild it but nothing work. Here is the error logs: {"t":{"$date":"2025-04-23T13:57:28.797Z"},"s":"I", "c":"CONTROL", "id":5760901, "ctx":"main","msg":"Applied --setParameter options","attr":{"serverParameters":{"mongotHost":{"default":"","value":"a local/non-public address:27027"},"searchIndexManagementHostAndPort":{"

## Matched source
Source: Source: https://stackoverflow.com/questions/79588809/mongodb-atlas-local-in-docker-stopped-working-because-of-security-keys
Original query: "Mongodb atlas local in docker stopped working because of security keys"
Key terms: atlas, because, docker, keys, local, mongodb, security, stopped, working

## When to use

- You hit this exact issue.
- The symptom matches: Mongodb atlas local in docker stopped working because of security keys.

## When NOT to use

- A different error or symptom; the cause here is specific to this one.

## Compatibility

Per the linked source.

## Edge cases

- If your error message differs even slightly, this is probably a different issue; search the exact text.
- If the fix does not help, capture the full error output and check the source link for updates.

## Source

https://stackoverflow.com/questions/79588809/mongodb-atlas-local-in-docker-stopped-working-because-of-security-keys

---

Source: [Vectle](https://vectle.com/skills/skl_51v6xCBdNDpAIJMYho7Lfg). Version: `skv_7bTRBvhIGuVXttshhRJPBg`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
