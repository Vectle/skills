---
name: "pusher-js-connects-to-mt1-by-default-p-fc80c2c9830c508e"
description: "If your pusher-js client never connects while the app key is correct, check the cluster: const pusher = new Pusher(APP_KEY, { cluster: APP_CLUSTER, // e.g."
metadata:
  skill_id: "skl_WI6IloZ1stViwQR1D2PLkw"
  title: "pusher-js connects to mt1 by default: pass cluster for apps in any other region"
  version: "skv_GVfZ2KRFYi4sKZI-ksujow"
  updated: "2026-10-03T04:42:55.134144+00:00"
  canonical_url: "https://vectle.com/skills/skl_WI6IloZ1stViwQR1D2PLkw"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

# pusher-js connects to mt1 by default: pass cluster for apps in any other region

## TL;DR

If your pusher-js client never connects while the app key is correct, check the cluster: const pusher = new Pusher(APPKEY, { cluster: APPCLUSTER, // e.g. 'eu', 'us2', 'ap1' - from your dashboard }); pusher-js defaults to the mt1 (us-east-1) cluster. The cluster option is mandatory for any app created outside mt1; without it the client talks to the wrong region and the connection never establishes.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

This is the first thing to check on a fresh Pusher app whose dashboard says the app is in eu or us2: the default code snippet in old tutorials omits cluster entirely. Verify in the browser console with pusher.connection.state and confirm the cluster value in your dashboard matches what the client passes.

Context: Docs (pusher/docs, connection.md): pusher-js defaults to the mt1 (us-east-1) cluster when no cluster option is given, and the cluster parameter is mandatory for apps created in any other cluster. Symptom: the client never reaches connected state (or connects to the wrong app's region) while the key looks correct, because the app was created in eu/us2/ap1 etc. Fix: pass cluster from the dashboard: new Pusher(APP_KEY, { cluster: 'eu' }).


---

Source: [Vectle](https://vectle.com/skills/skl_WI6IloZ1stViwQR1D2PLkw). Version: `skv_GVfZ2KRFYi4sKZI-ksujow`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
