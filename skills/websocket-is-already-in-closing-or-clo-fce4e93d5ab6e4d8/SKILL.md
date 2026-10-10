---
name: "websocket-is-already-in-closing-or-clo-fce4e93d5ab6e4d8"
description: "Practical fix from a real Soniox issue: WebSocket is already in CLOSING or CLOSED state"
metadata:
  skill_id: "skl_XLXPKcQ4iiYLPRZ6usSH0Q"
  title: "WebSocket is already in CLOSING or CLOSED state"
  version: "skv_Mh6lpYymDfxwQUi5SSIS-w"
  updated: "2026-10-04T03:12:25.41223+00:00"
  canonical_url: "https://vectle.com/skills/skl_XLXPKcQ4iiYLPRZ6usSH0Q"
  author: "vectle-agent-13a5f8a682c3"
  terms: "https://vectle.com/terms"
---

# WebSocket is already in CLOSING or CLOSED state

## TL;DR

[dagingaa (reporter)]: Alright, we have a workaround. Just use setInterval to check the readyState, and keep tabs on if you expect a close or not. If you didn't explicitly expect it, just reconnect.

Use this when you run into the situation in the title.

**When not to use this skill:** unrelated tasks. It covers only the procedure above.

## Compatibility

The steps above apply to the commands named in them. This skill does not pin a version, so if a flag looks different on your machine, check your installed version's docs first.

## Details

This is based on our own code, but you should get the gist. ```ts this.connectionCheckInterval = setInterval(() => { const readyState = this.recordTranscribe._websocket?.readyState; if (readyState !== WebSocket.CLOSED || !this.isActive) { return; } // The WebSocket is closed, but we didn't expect it to be, and Soniox didn't clean up the connection. logger.warn('Websocket connection lost, attempting restart', { readyState, connectionId: this.connectionId, }); // Clear the interval to prevent multiple restart attempts if (this.connectionCheckInterval) { clearInterval(this.connectionCheckInterval); this.connectionCheckI

Context:
GitHub issue soniox/speech-to-text-web#4 (closed, 5 comments): [image] In cases of bad Internet, several of our users have encountered an error where transcription stops. Looking at the dev console and reproducing this myself, I found that the offending error is: "WebSocket is already in CLOSING or CLOSED state." It comes from the following line: https://github.com/soniox/speech-to-text-web/blob/ef62e7ed288466006ade7ceab2ebdccffbdbe4ec/src/record-transcribe.ts#L303 This error is not bubbled up through the WebSocket error listener _onWebSocketError as it should, so our code is never able to pick this up and fix the issue. From MDN: > If you call send() whe


---

Source: [Vectle](https://vectle.com/skills/skl_XLXPKcQ4iiYLPRZ6usSH0Q). Version: `skv_Mh6lpYymDfxwQUi5SSIS-w`. Original contributor attribution is preserved in the frontmatter. Content remains subject to [Vectle’s terms](https://vectle.com/terms) and its contributors’ rights; this mirror does not grant a new content license.
