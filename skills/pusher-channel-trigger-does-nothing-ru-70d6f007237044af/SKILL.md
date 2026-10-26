---
name: "pusher-channel-trigger-does-nothing-ru-70d6f007237044af"
description: "Client events via channel.trigger('client-...', data) fail silently unless every rule holds: 1."
metadata:
  skill_id: "skl_zDFVlx0vO59QK7unMiqXCQ"
  title: "Pusher channel.trigger does nothing: run the client-event checklist (dashboard toggle first)"
  version: "skv_NCO4jZRygWv7iR_pB_JmHA"
  updated: "2026-10-03T05:39:16.531103+00:00"
  canonical_url: "https://vectle.com/skills/skl_zDFVlx0vO59QK7unMiqXCQ"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"issueatlas\"}"
  original_notices_and_references: "[\"https://github.com/pusher/docs/blob/HEAD/docs/channels/using_channels/events.md\"]"
---

# Pusher channel.trigger does nothing: run the client-event checklist (dashboard toggle first)

## TL;DR

Client events via channel.trigger('client-...', data) fail silently unless every rule holds: 1. Any one of these violated and the trigger silently does nothing.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

2. Event names must start with client-. Any other prefix is rejected by the server. 3. Only on private- and presence- channels. Public channels reject client triggers. 4. Trigger only after pusher:subscription_succeeded fires on that channel; earlier triggers are rejected. 5. Max 10 messages per second per client connection; over that the API rejects the excess. 6. The originator does not receive its own client event, so do not use the echo to confirm delivery. Also remember client events originate from other users' browsers, so treat the payload as untrusted input. When a trigger "does nothing", walk this checklist in order before blaming the connection.

Context: Docs (pusher/docs events.md): client events (channel.trigger from the browser) have enforced restrictions: they must be enabled in the app Settings tab in the dashboard; they can only fire on private and presence channels; the event name must be prefixed client- (anything else is rejected); you must be subscribed and the subscription must have succeeded (wait for pusher:subscription_succeeded); client events are not delivered back to the originator; and there is a rate limit of 10 messages per second per client, above which events are rejected. Any one of these violated and the trigger silently does nothing.


---

Source: [Vectle](https://vectle.com/skills/skl_zDFVlx0vO59QK7unMiqXCQ). Version: `skv_NCO4jZRygWv7iR_pB_JmHA`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
