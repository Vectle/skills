---
name: "wix-app-setup-incomplete-badge-never-s-f5d39792c06ca644"
description: "Wix app \"Setup incomplete\" badge never shows after sending APP_FINISHED_CONFIGURATION"
metadata:
  skill_id: "skl_lVp5TVvE8BmKUbSjNTHorw"
  title: "Wix app \"Setup incomplete\" badge never shows after sending APP_FINISHED_CONFIGURATION"
  version: "skv_EaKj7-GB9kZER6xpByxrDQ"
  updated: "2026-11-14T12:07:02.353496+00:00"
  canonical_url: "https://vectle.com/skills/skl_lVp5TVvE8BmKUbSjNTHorw"
  author: "Fin"
  terms: "https://vectle.com/terms"
  artifact_format_revision: "2"
  public_attribution: "{\"client\":null,\"label\":\"Fin\"}"
  original_notices_and_references: "[]"
---

Separate the two installs in your notes. Write down which site each event was sent for, with the timestamp. Success check: the 200 response you already have belongs to the first site only, so it cannot explain or fix the badge state of the second site.

On the second site, send the event for that site specifically. Use the documented setup-finished event name from the sample flows, APP_FINISHED_CONFIGURATION, exactly once, authorised as that install (its own instance credentials, not the first site's). Success check: a 200 response tied to the second site's install, recorded with its timestamp. Note that a 200 with an empty body confirms the endpoint received the event; by itself it is not proof the badge state changed.

Do not send the second event name as a substitute. APP_SETUP_FINISHED appears as a separate name, and sending both names in the first test muddies which one the badge logic keys on. Success check: the clean retest in step 2 used only APP_FINISHED_CONFIGURATION.

Check the app definition in the app dashboard. The badge points a site owner at an unfinished setup step, so the app needs a dashboard page or setup step configured in its installation/dashboard settings for there to be anything to flag as incomplete. If a recent version removed the app's only site widget or dashboard surface, restore or re-add a setup surface and publish a new version. Success check: the app definition shows a dashboard page or setup step that a new install has not completed yet.

Reinstall fresh after steps 2 to 4 and wait. Uninstall, install again from the dashboard App Market, do not send the event for this new install, and check the dashboard again after allowing propagation time rather than immediately. Success check: either the badge now shows (the earlier test was polluted by the per-install mix-up or the missing setup surface), or it still does not show on a clean install, which rules out your event call as the cause.

If a clean install still shows no badge, treat it as platform-side and escalate to Wix developer support. Include the app ID, both site instance IDs, the exact event timestamps, the event name sent for each, and the 200 responses. Success check: a support ticket that lets Wix check review status and event routing, the two remaining suspects, since test installs made before App Market review can be treated as developer installs that never surface the badge.

---

Source: [Vectle](https://vectle.com/skills/skl_lVp5TVvE8BmKUbSjNTHorw). Version: `skv_EaKj7-GB9kZER6xpByxrDQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
