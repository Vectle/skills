---
name: "calendly-embed-events-not-firing-in-re-4621fb10703ad6cc"
description: "Shows how to fix calendly embed events not firing in React Native WebView (only page_height works). Use it when you hit this exact problem. Skip it when your error message or symptom looks different."
metadata:
  skill_id: "skl_xOXVxVgR-QACyzX_uix-eg"
  title: "Calendly embed events not firing in React Native WebView (only page_height works)"
  version: "skv_Dhb43O6lQ6shs1yl_a3MOQ"
  updated: "2026-10-03T14:02:54.337886+00:00"
  canonical_url: "https://vectle.com/skills/skl_xOXVxVgR-QACyzX_uix-eg"
  author: "issueatlas"
  terms: "https://vectle.com/terms"
---

## TL;DR

Add a message-forwarding script in the HTML (window.addEventListener('message', e => window.ReactNativeWebView.postMessage(JSON.stringify(e.data)))) so the events reach the React Native onMessage handler.

## Steps

1. What was going on
Embedding a Calendly inline widget inside a react-native-webview with source={{ uri: calendlyUrl }} only delivered the calendly.page_height event; calendly.event_scheduled, calendly.date_and_time_selected and the other events never arrived. Calendly posts the non-height events only when window.parent !== window, and with a direct URI load the webview has no parent frame, so those messages are skipped. Switching the WebView source to an HTML string containing an iframe (with embed_domain and embed_type=Inline on the URL) restored all events.

2. What fixed it
Load the widget through an HTML string containing an iframe instead of a bare URI: source={{ html: '[iframe src="https://calendly.com/your-event?embed_domain=1&embed_type=Inline" width="100%" height="100%"][/iframe]' }}. Add a message-forwarding script in the HTML (window.addEventListener('message', e => window.ReactNativeWebView.postMessage(JSON.stringify(e.data)))) so the events reach the React Native onMessage handler. The iframe restores the parent/child window relationship Calendly needs to post its events, and the reporter confirmed all events fired after the switch. Source: https://github.com/tcampb/react-calendly/issues/190

## When to use

You are seeing this: Calendly posts the non-height events only when window.parent !== window, and with a direct URI load the webview has no parent frame, so those messages are skipped. Use this skill when you run into "Calendly embed events not firing in React Native WebView (only page_height works)".

## When not to use

If your error message or symptom does not match what is described above, this is probably not your fix. Search for your exact error text instead of forcing this one to fit.

## Versions

No specific versions are mentioned in the source material, so treat the fix as generally applicable and check the examples against whatever you have installed.

## Why this happens

The original report does not dig into a root cause. It documents the symptom and the fix that resolved it.

## Sources

- https://calendly.com/your-event?embed_domain=1&embed_type=Inline"

- https://github.com/tcampb/react-calendly/issues/190


---

Source: [Vectle](https://vectle.com/skills/skl_xOXVxVgR-QACyzX_uix-eg). Version: `skv_Dhb43O6lQ6shs1yl_a3MOQ`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
