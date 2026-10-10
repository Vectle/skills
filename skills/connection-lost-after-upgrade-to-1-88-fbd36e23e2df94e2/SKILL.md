---
name: "connection-lost-after-upgrade-to-1-88-fbd36e23e2df94e2"
description: "N8n: connection lost after upgrade to 1.88.0. The verified fix is Fix: Reporter-confirmed fix (antman1p): add an explicit nginx location block for /rest/push with proxy_http_version 1.1, Upgrade/Connection headers and Origin/X-Forwarded headers, e.g. location /rest/push { proxy_pass http://n8n:5678; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection 'upgrade'; proxy_set_header Origin ...; }. Use this when you hit the symptoms above in n8n; not for unrelated n8n errors or general"
metadata:
  skill_id: "skl_ref_1gVm98FerTf8kOYbgQ"
  title: "Connection lost after upgrade to 1.88.0"
  version: "skv_RJjr0rlFLIFxJAcxffjPDQ"
  updated: "2026-10-03T04:40:30.421858+00:00"
  canonical_url: "https://vectle.com/skills/skl_ref_1gVm98FerTf8kOYbgQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Fix: Reporter-confirmed fix (antman1p): add an explicit nginx location block for /rest/push with proxy_http_version 1.1, Upgrade/Connection headers and Origin/X-Forwarded headers, e.g. location /rest/push { proxy_pass http://n8n:5678; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection 'upgrade'; proxy_set_header Origin ...; }. Member Joffcom closed the issue after the nginx-config guidance resolved it.

## The error

```text
Issue n8n-io/n8n#14653 (closed, 80 comments): ### Bug Description After the upgrade I started to get error index-D76xStxp.js:293035 [WebSocketClient] Connection lost, code=1008 onConnectionLost @ index-D76xStxp.js:29303 ### To Reproduce 1. Use nginx with reverse proxy 2. Upgrade to 1.88.0 3. WS failing to connect ### Expected behavior WS works as intended ### Operating System Ubuntu 22.04.5 LTS ### n8n Version 1.88.0 ### Node.js Version 21.7.3 ### Database PostgreSQL ### Execution mode main (default)
```

## Fix

1. Reporter-confirmed fix (antman1p): add an explicit nginx location block for /rest/push with proxy_http_version 1.1, Upgrade/Connection headers and Origin/X-Forwarded headers, e.g. location /rest/push { proxy_pass http://n8n:5678; proxy_set_header Upgrade $http_upgrade; proxy_set_header Connection 'upgrade'; proxy_set_header Origin ...; }.
2. Member Joffcom closed the issue after the nginx-config guidance resolved it.

Success check: the symptom above is gone and the original operation completes.

## When to use

- You hit this exact symptom in n8n.
- You want the verified fix without digging through the thread.

## When not to use

- A different error in n8n, even a similar-looking one.
- General n8n setup or credential questions.

## Compatibility

- N8n (n8n-io/n8n) Reported against version 1.88.0.

## Variant phrasings

- How to fix "connection lost after upgrade to 1.88.0" in n8n
- n8n: connection lost after upgrade to 1.88.0

## Edge cases

- After upgrading to 1.88.0, the editor websocket (/rest/push) failed with code 1008 behind nginx reverse proxies.

## Source

- https://github.com/n8n-io/n8n/issues/14653

---

Source: [Vectle](https://vectle.com/skills/skl_ref_1gVm98FerTf8kOYbgQ). Version: `skv_RJjr0rlFLIFxJAcxffjPDQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
